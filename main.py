import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    """
    Returns a greeting message with an optional name from environment variables.

    This function retrieves a name from the NAME environment variable, defaulting
    to "World" if not set, and returns a formatted greeting string with version
    information.

    Returns:
        str: A greeting message in the format "Hello, {name}! Version 2.0"
            where {name} is either the value of the NAME environment variable
            or "World" if the environment variable is not set.
    """
    name = os.environ.get("NAME", "World")
    return f"Hello, {name}! Version 2.0"

@app.route("/health")
def health_check():
    """
    Health check endpoint.
    Returns a JSON object indicating the health status of the application
    and the port it is running on.
    """
    return {"status": "healthy", "port": os.environ.get("PORT", 8080)}

if __name__ == "__main__":
    # For local development only
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8080)),
        debug=False
    )
