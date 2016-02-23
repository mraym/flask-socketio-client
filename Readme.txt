# Create virtualenv
virtualenv venv

# Activate your virtual enviornment
. venv/bin/activate

# Do your pip installs
pip install flask
pip install CORS

# Run the app in the background
python app.py >> out.log 2>&1 &
