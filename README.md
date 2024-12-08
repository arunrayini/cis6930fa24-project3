# cis6930fa24 -- Project 3

 ## Name: Arun Kumar Reddy Rayini

 # Project Description:

 ---

 This project represents the culmination of efforts in building a comprehensive data pipeline, where we transition from raw data collection to creating an interactive interface designed for end-users. The data used in this project was originally collected and processed in Project 0 from incident reports provided by the Norman Police Department (NormanPD). These incident reports contain structured information about various police-related activities and events, and this project focuses on leveraging that data to offer meaningful insights and enhanced usability.

The primary objective of this project is to process incident data from multiple NormanPD-style PDFs, either uploaded by users or accessed via URLs, and transform this data into an accessible, interactive format. By doing so, the project aims to bridge the gap between raw data and actionable insights. This involves parsing, organizing, and analyzing the data for visualization and interpretation.

To achieve this, the system incorporates three distinct types of visualizations, each designed to provide a unique perspective on the data:

Clustering Visualization: A scatter plot that categorizes and clusters incidents based on their nature, helping users quickly identify patterns or trends within the dataset.

Bar Graph: A representation of the top 10 most frequently occurring incident types, offering users a clear comparison of incident prevalence.

Line Graph: A temporal analysis that plots the distribution of incidents by the hour of the day, providing insights into when incidents are most likely to occur.

By presenting the data through these interactive visualizations, the project ensures that users, regardless of technical expertise, can derive valuable insights from the incident data. Additionally, the platform includes a feedback mechanism, where users can upload new data in the form of PDFs or URLs, ensuring that the system remains dynamic and up-to-date.

This project not only demonstrates the practical applications of data pipelines but also highlights the importance of user-centered design in data visualization. By combining data processing capabilities with an intuitive interface, the system transforms raw data into actionable insights, empowering end-users to make informed decisions based on the presented information.

---

# Project Objectives:

---
The project focuses on achieving several key objectives essential for its success. First, it aims to extract crucial details, such as incident time, type, and location, from PDFs and URLs. This involves employing robust parsing techniques to handle inconsistencies and varying formats within the data, ensuring that the extracted information is structured, reliable, and ready for analysis.

A significant part of the project involves presenting the extracted data through compelling visualizations. The visualizations include clustering to reveal patterns and relationships among incidents, frequency distribution to highlight the most common incident types, and time-based analysis to identify trends across different hours of the day. These visualizations are designed to be both informative and easy to interpret, helping users gain actionable insights from the data.

The system is built with a modular architecture to ensure scalability and maintainability. Each component—data extraction, processing, and visualization—operates independently, making it easy to extend or modify the system without disrupting its overall functionality. This design allows for seamless future enhancements and ensures long-term adaptability.

The user interface is designed with a strong emphasis on usability and aesthetics, ensuring a seamless experience for all users, regardless of technical expertise. The interface provides an intuitive platform for uploading files, entering URLs, and interacting with visualizations. Features like tooltips, clear labels, and responsive design enhance accessibility and usability, making the system approachable for a wide audience.

# Data Directory
This directory holds the necessary files and assets generated or used during the execution of the project.

### Uploads:

Purpose: Stores all PDF files uploaded by the user either through the file upload option or fetched via URLs.
Description: Every uploaded file is saved in this directory temporarily for processing. It ensures that the system can easily access files during the data extraction stage. Uploaded PDFs are processed by the application to extract relevant incident data.

### Static:

Purpose: Contains all generated visualizations and static assets.
Description: After processing the data, visualizations such as clustering plots, bar graphs, and line graphs are saved in this directory. These images are then rendered dynamically in the web application. Additionally, this folder houses static assets like the custom CSS file (style.css), which defines the layout and appearance of the application.


### main.py:

Purpose: The main script orchestrating the entire workflow of the application.
Description: This Python script is the core of the project. It includes:
Flask routes for handling web requests and rendering templates.
Functions to extract data from uploaded files or URLs.
Logic to generate visualizations such as clustering, bar graphs, and line graphs.
Error handling and debugging tools for smooth operation.

### Templates:

Purpose: Contains the HTML files used to build the web interface.
Description: This directory ensures a clean separation of front-end and back-end functionality, following Flask's templating conventions.

### multi_file_url_upload.html:

This file represents the homepage of the web application.
It provides an interface for users to upload PDF files and enter URLs.
Includes form elements for selecting files, adding URLs, and a submit button for processing.

### visualizations.html:

This file is responsible for displaying the generated visualizations to the user.
Includes sections for each type of visualization (clustering, bar graph, and line graph) and allows users to view the results interactively.
The layout ensures the visualizations are well-organized and user-friendly, with tooltips and lightbox functionality for larger image previews.

### Static:

Purpose: Hosts static files required by the application, such as CSS and JavaScript.
Description: This directory is critical for defining the design and layout of the web application.

### style.css:

This CSS file provides the styling for the entire web application.
It includes styles for the background, fonts, buttons, tooltips, and responsive design.
Enhances the visual appeal and ensures a consistent layout across different devices and screen sizes.
Functionality of the Directory Structure
The Uploads and Static directories work together to handle user-provided data and generated assets, ensuring smooth data flow from input to visualization.

main.py manages back-end logic.

Templates handles the front-end interface.

Static ensures a polished and professional appearance for users.

This clear separation ensures the application is modular, scalable, and easy to understand for future enhancements or debugging.

# Setup Instructions:

Install Python: Ensure Python 3.7 or later is installed.
Install Dependencies: pip install flask matplotlib seaborn pandas PyPDF2 requests

# How to run:

Once the setup is complete, you can run the Flask application to start the web interface:

1.Run the Flask application: pipenv run python main.py

2.The Flask server will start, and you should see output like this: Running on http://127.0.0.1:5000

3.Open your web browser and navigate to the address displayed in the terminal: http://127.0.0.1:5000



https://github.com/user-attachments/assets/d2cd9ee5-32ee-4df2-a95c-405b7942a1d5


For High video clarity Refer below:
## video Demonstration Link:  https://youtu.be/_8mX_zo_wdo


4.Interacting with the Application

Homepage:

Upload PDFs or enter URLs of NormanPD-style incident reports.
Click the Submit button to process the data.

Visualizations:

Once the data is processed, the page will display three visualizations:

Clustering Graph: Displays incidents grouped by their nature.
Bar Graph: Shows the top 10 most common incident types.
Line Graph: Illustrates incidents by the hour.

Interactive Features:
Hover over visualizations to see tooltips.
Click on any graph to view it in a larger lightbox view.

5. Exiting the Application
To stop the Flask server, press CTRL+C in the terminal where the application is running.

# Code Explanation:

## main.py

1.extract_from_pdf(file_path):

Purpose:
This function reads a PDF file, extracts the text from its pages, and processes it to extract rows of incident data.

Detailed Explanation:

The PdfReader object from the PyPDF2 library reads the PDF file. Each page is processed sequentially.
The extract_text() method extracts raw text from the page.
The extracted text is split into lines. The first three lines (usually containing headers) are skipped.
Each line is split into fields using a regular expression that identifies multiple spaces as delimiters (\s{2,}).
Only rows containing exactly five fields are considered valid. These fields represent:
Incident Time
Incident Number
Incident Location
Nature of the Incident
Incident ORI Code
Valid rows are appended to the incidents list as tuples.

Output:
A list of tuples, where each tuple represents a single incident.

2.process_pdf(file_path):

Purpose:
To extract structured data from a PDF file using regex patterns to identify specific fields of interest.

Detailed Explanation:

Similar to extract_from_pdf(), this function processes the PDF file page by page.
Each line of text is matched against a regex pattern designed to capture specific fields:
Incident Time: A date and time format.
Incident Number: A unique identifier.
Incident Location: A descriptive string indicating the location.
Nature of the Incident: A short description.
ORI Code: An alphanumeric identifier.

Output:
A list of tuples, each containing the above five fields.

3.process_url(url)

Purpose:
To download a PDF file from a given URL, save it locally, and process it for data extraction.

Detailed Explanation:

The requests.get() function is used to fetch the file from the URL. The response is checked for a successful HTTP status.
The file is saved in the UPLOAD_FOLDER directory with its original name.
Once saved, the file is passed to process_pdf() for data extraction.
Handles exceptions that may occur during file processing.

Output:
Returns the same type of structured data (list of tuples) as process_pdf().

4.create_visualizations(incidents):

Purpose:
To generate three visualizations—clustering scatter plot, bar graph, and line graph—based on the extracted data.

Detailed Explanation:

Input Validation:

If no incidents are passed, the function returns None values for all visualizations.

Data Preparation:

Converts the incidents list into a pandas DataFrame with the following columns:
Incident Time
Incident Number
Incident Location
Nature
Incident ORI Code

Clustering Scatter Plot:

Simplifies the "Nature" column by grouping less frequent categories into an "Other" category.
Uses seaborn.scatterplot() to create a scatter plot, where:
The x-axis represents the index of the incident.
The y-axis represents the simplified nature of the incident.
Saves the plot as an image file in the STATIC_FOLDER.

Bar Graph:

Counts the occurrences of each "Nature" and selects the top 10.
Creates a bar graph with:
Incident types on the x-axis.
Frequency on the y-axis.
Annotates each bar with its corresponding frequency.
Saves the graph as an image.

Line Graph:

Extracts the hour from the "Incident Time" column.
Counts the number of incidents per hour and plots a line graph.
Ensures all 24 hours are labeled on the x-axis.
Saves the graph as an image.

Output:

Returns the filenames of the three generated images.

5.index():

Purpose:
To render the homepage (multi_file_url_upload.html) for uploading files and entering URLs.

Detailed Explanation:

Uses Flask’s render_template() function to load the HTML template.
The homepage provides:

File upload functionality.
A text box for entering multiple URLs.

6.upload_files_and_urls():

Purpose:
To handle the form submission, process uploaded files and URLs, and generate visualizations.

Detailed Explanation:

File Processing:

Iterates over the uploaded files.
Saves each file to the UPLOAD_FOLDER directory.
Calls process_pdf() to extract data and appends it to a master list (all_incidents).
URL Processing:

Iterates over the entered URLs.
Calls process_url() for each URL and appends the extracted data to all_incidents.
Visualization Generation:

Calls create_visualizations() with the consolidated data.
Receives the filenames of the generated plots.
Rendering Results:

Passes the filenames and incident count to the visualizations.html template for display.

7.if __name__ == '__main__': app.run(debug=True):

Purpose:
To run the Flask application in debug mode for development purposes.

Detailed Explanation:

Starts the web server and listens for incoming requests.

Debug mode provides:
Automatic reloading on code changes.
Detailed error messages in the browser.

## Templates:

The two templates, multi_file_url_upload.html and visualizations.html, are integral to the user interface of your project. Each plays a specific role in enhancing user interaction and presenting data effectively. Below is a detailed explanation of their structure and functionality:

1.multi_file_url_upload.html:

Purpose:

This template serves as the homepage for the application, where users can upload PDF files or enter URLs to fetch incident data. It provides a clean and intuitive interface for inputting data into the pipeline.

Structure and Functionality:
HTML Head Section:

Meta Tags:
<meta charset="UTF-8">: Ensures the webpage supports UTF-8 character encoding.
<meta name="viewport" content="width=device-width, initial-scale=1.0">: Makes the page responsive on all devices.

Title: The title tag sets the page title as "Upload PDF Files and/or Enter URLs."

Styles and Fonts:
Includes the Roboto font from Google Fonts for modern typography.
Links to Font Awesome for adding icons, enhancing usability and aesthetics.
Loads style.css for custom styling.

Body Section:

Header:
Displays a prominent heading: "Upload PDF Files and/or Enter URLs."

Form:
Uses the <form> element to enable file and URL uploads:
action="/upload": Specifies the route to handle form submission.
method="post": Ensures data is sent securely to the server.
enctype="multipart/form-data": Allows file uploads.

File Upload Input:

<input type="file" name="files" id="files" multiple>:

Lets users select multiple PDF files.
Includes a label with the Font Awesome file upload icon (<i class="fas fa-file-upload"></i>), improving accessibility and user experience.

URL Input Textarea:
<textarea name="urls" id="urls" rows="5">: Allows users to input multiple URLs, one per line.
Placeholder text guides users: "Enter URLs here."

Submit Button:
<button type="submit">: Submits the form.

Decorated with the Font Awesome paper plane icon (<i class="fas fa-paper-plane"></i>).

Styling and Usability:

Icons and Labels:
Icons (e.g., upload and link) make the form visually appealing and intuitive.

CSS Integration:
style.css ensures consistent spacing, colors, and layout.
The use of responsive styles adapts the interface for various screen sizes.

2.visualizations.html:

Purpose:
This template displays the visualizations generated from the uploaded or fetched data. Users can view clustering scatter plots, bar graphs, and line graphs interactively.

Structure and Functionality:
HTML Head Section:

Similar to multi_file_url_upload.html, includes meta tags, fonts, icons, and CSS for consistency in design.

Body Section:

Header:
Displays the page title: "Incident Visualizations."
Incident Count:
Shows the total number of incidents processed using the template variable: {{ incident_count }}.

Visualization Cards:

The visualizations are displayed dynamically using the following blocks:
Clustering Scatter Plot:

Includes a heading: "Clustering of Incidents by Nature."
The plot image ({{ clustering_plot }}) is displayed within an interactive tooltip.
Clicking the image enlarges it using the lightbox feature.

Bar Graph:
Includes a heading: "Top 10 Incident Types."
Displays the bar graph ({{ bar_graph }}) similarly with a tooltip.

Line Graph:
Includes a heading: "Incidents by Hour (Line Graph)."
Displays the line graph  with identical interactivity.

Footer:

A footer at the bottom states: "© 2024 Incident Analysis."
Lightbox Feature:

Purpose:
Enhances usability by allowing users to enlarge images for better visibility.
Implementation:

HTML:
A hidden div (id="lightbox") contains an enlarged image and a close button.

JavaScript:
openLightbox(src): Sets the source of the enlarged image and makes the lightbox visible.
closeLightbox(): Hides the lightbox.

Styling:

Tooltip:
Each image is wrapped in a tooltip (<div class="tooltip">), which provides additional context ("Click to view larger").

Visual Containers:
Uses .visualization-container to organize visualization cards flexibly.
Consistency:
Fonts and colors match the overall theme of the application.

## styles.css:

The styles.css file is crafted to provide a visually appealing and user-friendly interface while maintaining responsiveness across devices. The body styling uses a linear gradient background (#74ebd5 to #acb6e5) for a modern aesthetic and centers the content using flexbox, ensuring a clean and balanced layout. The form and visualization container styles ensure content is centered and well-structured, with a white background, rounded corners, and a subtle shadow to create a card-like appearance. The headings (h1, h2) are styled with bold fonts, shadow effects, and distinct sizes to establish a clear hierarchy.

The input fields and buttons are designed with smooth hover and focus transitions, enhancing user interaction. Input fields have a clean design with soft background colors, and buttons are styled with a bright green theme (#28a745) that changes on hover and click for an interactive feel. The visualization cards are styled for clarity and consistency, with a fixed width, centralized content, and image tooltips for a professional presentation.

Finally, the footer and tooltips add subtle enhancements, with concise text styling and padding for visual balance. The file prioritizes modern design principles, using shadows, gradients, and responsive properties to ensure the application is visually engaging and easy to use.

# Assumptions
1.Data Structure:It is assumed that the PDF files contain structured text with consistent fields, such as incident time, location, nature of the incident, and other relevant details.
The URLs provided by users are expected to link directly to valid and accessible PDF files containing the required data.

2.Features:Clustering graphs are generated based on simplified incident categories derived from the nature of the incident. The assumption is that this categorization effectively represents meaningful clusters.Time-based analysis assumes that all time-related data in the input is formatted correctly and is consistent with standard time formats, enabling accurate extraction and visualization.

# Known Bugs and Limitations
1.PDF Parsing:PDFs with irregular formatting or inconsistent structures may lead to skipped rows or incomplete data extraction. The program relies on structured and predictable text formatting to parse incident details effectively.

2.URL Processing:Non-functional URLs or inaccessible files are skipped during processing, and a warning is displayed. However, there is no retry mechanism for transient network issues or temporarily unavailable files.

3.Visualization:Sparse or insufficient data can result in suboptimal clustering plots that lack meaningful insights. Similarly, line graphs may appear empty or fail to provide a clear pattern if the input data lacks diversity or completeness.





































