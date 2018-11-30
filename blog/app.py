# Deployed at https://wegwbspy08.execute-api.us-east-1.amazonaws.com/dev/

from blog_project import create_app


app = create_app()

if __name__ == '__main__':
    print("initiating the web app...")
    app.run(debug=True)
