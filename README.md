# Project_costumerchurn

Welcome to the Customer Churn Prediction App! 👋

Have you ever wondered if a customer is about to leave your service? This simple app helps you figure that out. You just enter a few details about the customer, and the app will tell you if they are likely to stay or churn.

What is this about?
--------------------
This is a fun and useful project built using Streamlit (for the web interface) and a logistic regression machine learning model (for predictions). It’s designed to be user-friendly so that even someone with no technical background can use it.

How does it help?
--------------------
Businesses often lose customers without knowing why. With this app, you can predict if a customer is likely to stop using the service. This helps businesses take action before it's too late.

What does the app ask you for?
--------------------
- Gender (Male or Female)
- Senior Citizen (Yes or No)
- Has Partner (Yes or No)
- Has Dependents (Yes or No)
- Tenure (how long the customer has stayed, in months)
- Monthly Charges (the monthly bill amount)
- Total Charges (total billed so far)
- Paperless Billing (Yes or No)
- Contract Type (Month-to-month, One year, Two year)

What happens after entering the details?
--------------------
The app processes the inputs and sends them to a trained model. Then it tells you:
- If the customer is likely to stay, or
- If the customer is at risk of leaving

How to run it on your system?
--------------------
1. Make sure Python is installed.
2. Clone or download this project folder.
3. Open your terminal or command prompt.
4. Run this command:
   streamlit run app.py

It will open the app in your browser. You’re ready to predict churn!

What's inside this project?
--------------------
- app.py: The main app file
- logistic_model.pkl: The saved machine learning model
- model_columns.pkl: The list of columns the model expects
- requirements.txt: List of required Python libraries

Want to improve it?
--------------------
Some ideas:
- Show how confident the model is about the prediction
- Add a feature to upload CSV files for bulk prediction
- Use charts to make it look cooler
- Try more powerful ML models like Random Forest or XGBoost

Who made this?
--------------------
This app was created by Parth  – a B.Tech CSE student passionate about web development and machine learning.

License
--------------------
Free to use and modify for learning or personal projects.
Just give credit when you share it.

Thanks for checking this out! 🙂\
