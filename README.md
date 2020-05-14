# cutc-instagram

This project is a social media analytic service, born out of a need to monitor CUTC's Instagram (CUTC stands for the Canadian Undergraduate Tech Conference, learn more here: https://www.cutc.ca)

It's a Flask (Python backend) web app with three pages - a homepage, a login screen, and a profile page that displays analytics about the logged-in user. These analytics include a list of followers and followed accounts, fans of the user, accounts who recently unfollowed, and accounts that don't follow back the user. 

Due to Instagram's tighter restrictions over automated services, this tool is only for demonstrative purposes and should be tested carefully. User is responsible for moderating actions to avoid being banned from the platform. 

Notes: 
- Make sure you are running Python 3.6+ 
- When you open this project, go to the terminal and run 'pip install -r requirements.txt' to download all required modules
- To run this project, go to the terminal and run 'flask run'
