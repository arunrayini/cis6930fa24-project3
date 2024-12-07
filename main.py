import matplotlib
matplotlib.use('Agg')  
from flask import Flask, render_template, request, jsonify
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time
from PyPDF2 import PdfReader
import requests
import re

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
STATIC_FOLDER = os.path.join(os.getcwd(), 'static')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(STATIC_FOLDER, exist_ok=True)

# Extracting incidents from PDF
def extract_from_pdf(file_path):
    incidents = []
    try:
        reader = PdfReader(file_path)
        for page in reader.pages:
            text = page.extract_text()
            if text:
                lines = text.split("\n")
                for line in lines[3:]:  # Skiping the header rows
                    fields = re.split(r'\s{2,}', line.strip())
                    if len(fields) == 5:  # Ensuring valid data
                        incidents.append(tuple(fields))
    except Exception as e:
        print(f"Error extracting PDF {file_path}: {e}")
    return incidents

def process_pdf(file_path):
    """
    Processing a PDF file to extract incident data using regex for structured data extraction.

    :param file_path: Path to the PDF file.
    :return: A list of tuples containing extracted incident data.
    """
    incidents = []
    try:
        pdf = PdfReader(file_path)
        for page_number, page in enumerate(pdf.pages, start=1):
            raw_text = page.extract_text()
            print(f"Page {page_number} Text:\n{raw_text}\n{'=' * 50}\n") 

            lines = raw_text.split("\n")
            for line in lines:
               
                match = re.match(r"(\d{1,2}/\d{1,2}/\d{4} \d{1,2}:\d{2})\s+(\d{4}-\d+)\s+(.*?)\s+([\w/ ]+)\s+(\w+)", line)
                if match:
                    incident_time = match.group(1)
                    incident_number = match.group(2)
                    incident_location = match.group(3)
                    nature = match.group(4)
                    incident_ori = match.group(5)
                    incidents.append((incident_time, incident_number, incident_location, nature, incident_ori))
                else:
                    print(f"Skipping unmatched line: {line}") 
    except Exception as e:
        print(f"Error processing PDF {file_path}: {e}")

    if incidents:
        print(f"Extracted {len(incidents)} incidents from {file_path}.")
    else:
        print(f"No data extracted from {file_path}.")
    return incidents


# Processing a URL
def process_url(url):
    """
    Downloading a PDF from a URL and process it.
    
    :param url: URL of the PDF file.
    :return: A list of tuples containing extracted incident data.
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            file_name = os.path.basename(url)
            file_path = os.path.join(UPLOAD_FOLDER, file_name)
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded and saved PDF: {file_path}")
            return process_pdf(file_path)
        else:
            print(f"Failed to fetch URL {url}: HTTP {response.status_code}")
    except Exception as e:
        print(f"Error processing URL {url}: {e}")
    return []


# Generating visualizations
def create_visualizations(incidents):
    if not incidents:
        return None, None, None

    df = pd.DataFrame(incidents, columns=['incident_time', 'incident_number', 'incident_location', 'nature', 'incident_ori'])

    # Simplify "nature" for clustering
    top_natures = df['nature'].value_counts().head(15).index 
    df['simplified_nature'] = df['nature'].apply(lambda x: x if x in top_natures else 'Other')

    # Clustering scatter plot
    plt.figure(figsize=(12, 8))
    sns.scatterplot(
        y=df['simplified_nature'],  # Using simplified nature for y-axis
        x=range(len(df)),
        hue=df['simplified_nature'],  # Hue by simplified nature
        palette="viridis",
        s=20,  # Adjusted size for clarity
        legend=False
    )
    plt.title("Clustering of Incidents by Nature")
    plt.xlabel("Index")
    plt.ylabel("Simplified Nature")
    plt.tight_layout()
    clustering_filename = f"clustering_{int(time.time())}.png"
    plt.savefig(os.path.join(STATIC_FOLDER, clustering_filename))
    plt.close()

    # Bar graph
    # Bar graph
    plt.figure(figsize=(14, 8))  # Adjusted size for better visualization
    bars = df['nature'].value_counts().head(10)
    bars.plot(kind='bar', color='cornflowerblue', edgecolor='black', width=0.6)

    # Adding data labels
    for i, value in enumerate(bars):
        plt.text(i, value + 1, str(value), ha='center', va='bottom', fontsize=10, fontweight='bold')

    plt.title("Top 10 Incident Types", fontsize=16, fontweight='bold')
    plt.xlabel("Incident Type", fontsize=14, fontweight='bold')
    plt.ylabel("Frequency", fontsize=14, fontweight='bold')
    plt.xticks(rotation=45, ha='right', fontsize=12)  # Rotating x-axis labels for better readability
    plt.yticks(fontsize=12)
    plt.grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)
    plt.tight_layout()

    bar_filename = f"bar_{int(time.time())}.png"
    plt.savefig(os.path.join(STATIC_FOLDER, bar_filename))
    plt.close()


    # Line graph for incidents by hour
    df['hour'] = pd.to_datetime(df['incident_time'], errors='coerce').dt.hour
    if df['hour'].dropna().empty:
        line_filename = None
    else:
        hourly_counts = df['hour'].value_counts().sort_index()
        plt.figure(figsize=(12, 8))  # Adjusted size for better visualization
        sns.lineplot(x=hourly_counts.index, y=hourly_counts.values, marker="o", linestyle='-', color="blue")
        plt.title("Incidents by Hour")
        plt.xlabel("Hour of the Day")
        plt.ylabel("Number of Incidents")
        plt.xticks(range(24))  # Ensuring all 24 hours are labeled
        plt.tight_layout()
        line_filename = f"line_{int(time.time())}.png"
        plt.savefig(os.path.join(STATIC_FOLDER, line_filename))
        plt.close()

    return clustering_filename, bar_filename, line_filename


@app.route('/')
def index():
    return render_template('multi_file_url_upload.html')

@app.route('/upload', methods=['POST'])
def upload_files_and_urls():
    files = request.files.getlist('files')
    urls = request.form.get('urls', '').split('\n')
    all_incidents = []

    # Processing uploaded files
    for file in files:
        if file and file.filename:
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)
            incidents = process_pdf(file_path)  # Using process_pdf() here
            all_incidents.extend(incidents)

    # Processing URLs
    for url in urls:
        if url.strip():
            incidents = process_url(url.strip())
            all_incidents.extend(incidents)

    # Generating visualizations
    clustering_plot, bar_graph, heatmap = create_visualizations(all_incidents)

    return render_template(
        'visualizations.html',
        clustering_plot=clustering_plot,
        bar_graph=bar_graph,
        heatmap=heatmap,
        incident_count=len(all_incidents)
    )


if __name__ == '__main__':
    app.run(debug=True)
