# Project
Python

## Table of Contents

1.	Presentation of the Theme - Argument
2.	Application Functionality
3.	Software Used
4.	Application Implementation
5.	Bibliography
6.	Appendix

## 1. Presentation of the Theme
The Body Mass Index (BMI) is an essential metric for monitoring body weight and is an important tool in efforts to maintain optimal health. By evaluating the ratio between weight and height, BMI provides a general perspective on body composition and potential health risks.
Using a dedicated application for calculating and monitoring BMI offers numerous benefits. Through such an application, users can quickly and easily access information about their health status, enabling them to make informed decisions regarding their diet and physical activity levels.
With the increased accessibility provided by applications, users can benefit from constant monitoring of their BMI, which can help prevent health issues associated with extreme weight fluctuations. Ultimately, integrating technology into personal health management through BMI applications can play a significant role in promoting a balanced lifestyle and sustainable health.

## 2. Application Functionality
The application was designed to have a simple and interactive interface. When launched, the first page loads where the user can enter the necessary data for calculating BMI.

Once the user completes the required form and clicks on the "Calculate BMI" button, the application displays the result of the calculation, the user's weight category based on the BMI value, and feedback:

The form remains active for new data entry if a reassessment is desired. It can be filled out again, and for recalculating, the "Calculate BMI" button remains active. Additionally, immediately after displaying the category, a new link becomes available, which the user can access to be directed to a page dedicated to describing the different weight categories:

If the user wishes to return to the main application page, they can access the link at the end of the descriptions.

## 3. Software Used
For implementing the application, the Flask library was used for rendering pages, along with HTML and CSS formats for their design. Flask also includes the Jinja framework, which allows for modifying the content of various pages based on the parameters entered by the user. For portability reasons, a Virtual Environment (VENV) was used to run the application on any station without needing to install any of the other applications listed above. Installing the Python interpreter is thus the only prerequisite to running the program that starts the application on a specific server or a local test server.

## 4. Application Implementation
As mentioned at the end of the chapter dedicated to the software used in the implementation, the application runs on a local server (in the testing phase, it can later be replaced with a rented one) that loads web pages with content adapted to the requests made by the client/user to the server.
Flask uses a standardized working directory format for running applications. The HTML pages to be displayed must be placed in a "templates" directory, and the CSS files responsible for the design and format of the content are found in the "static" directory.
I have attached the code implementation at the end of the documentation. I will go through the logic of the code along with the changes it makes to the content of the loaded pages.
At the beginning of the program, line 1 imports the base constructor of a Flask application from the Flask library, the render_template function that formats HTML pages with parameters passed using the Jinja library, and the request function that handles HTTP requests (POST requests) made by the user to the server.
Line 3 calls the Flask constructor to create the application, and it needs to be passed the parameter `__name__` (a convention established by developers, primarily to check that the application is initialized in a running source code and not in a library to be included in another).
Lines 5-19 define the two basic functions of the application, `calculate_bmi` and `get_weight_category`, which first allow the calculation of BMI and then categorize the user into a specific weight category (the first returns the BMI value based on the height and weight entered, and the next one takes this result and returns the weight category as a string).
Next, lines 20-37 define the routes where the application will display content and handle requests made by the user to the server after processing the data sent by them.
The first route (line 20) models the content of the first page (located at the base address "/"), accepting two types of requests: "GET" and "POST". The first is used for initially loading the main page (when the user has not entered any data), and the second for updating the page and displaying results based on the parameters sent by the client through the form.
In the first situation, for the "GET" request, the parameters are set to the neutral value `None` used in Python to declare an uninitialized variable. After checking `request.method == 'POST'`, the execution block is skipped, and `render_template` generates a page displaying only the initial form (see the content of `index.html`, where the body `{%if bmi %}` checks if the `bmi` value has been initialized, so in this initial case it skips displaying the lines reserved for the result that does not exist at this initial point).
In the second situation, for the "POST" request, the condition `request.method == 'POST'` is met, and the `bmi` and `category` variables are overwritten by the results returned by the dedicated functions that receive the values from the form fields on the initial page from which the request was made as parameters. This time, the `render_template` constructor receives parameters other than the neutral value `None`, and when the page is reloaded, the Jinja syntax condition `{%if bmi %}` will be met (the `bmi` variable has recorded a value at this request), and the content of the main page will be modified, now including lines 24-25 from `index.html` that receive the `bmi` and `category` values through the `render_template` constructor returned by the `index()` function.
At the first "POST" request, preceded by the initial "GET" request, the form will be cleared and available to launch a new "POST" request for a new calculation, displaying the new result, and so on.
Additionally, in the HTML code of the main page (`index.html`), the same checks (for variable initialization and value retrieval, if affirmative) are made for displaying interactive feedback based on the obtained weight category.
The source code also includes a second route, (@app.route('/weight_categories')), which allows rendering a page dedicated to additional information about different weight categories. The page contains a link to return to the main page. Accessing the main page is done through a "GET" request, as mentioned above (only displays the page with uninitialized data and content according to the uninitialized data).
Finally, in the last two lines, the created Flask application is run, first checking that the application object creation is done from the running source code and not an imported one, as mentioned earlier.
Regarding the design of the project, I will not go into details; I attach the CSS file at the end. I mention that it was a challenge to create a dynamic background that loops a video.

## 5. Bibliography
- Our Documentation | Python.org
- Welcome to Flask — Flask Documentation (3.0.x) (palletsprojects.com)
- CS50x 2023 - Lecture 9 - Flask (youtube.com)
- HTML: HyperText Markup Language | MDN (mozilla.org)
- ChatGPT (openai.com)
