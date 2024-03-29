# Use image with both python and node installed
FROM nikolaik/python-nodejs:python3.8-nodejs16

WORKDIR /app/backend

# Install Python dependencies
COPY ./backend/requirements.txt /app/backend/
RUN pip3 install --upgrade pip -r requirements.txt

# Install frontend dependencies
WORKDIR /app/frontend

COPY ./frontend/package.json ./
COPY ./frontend/package-lock.json ./

RUN npm install

# Add the rest of the code
COPY . /app/
COPY ./backend/scripts/ /app/

# Build static files
RUN npm run build

# Move all static files other than index.html to root/ for whitenoise middleware
WORKDIR /app/frontend/build

RUN mkdir root && mv *.ico *.json root

# Collect static files
RUN mkdir /app/backend/staticfiles

WORKDIR /app

# SECRET_KEY is only included here to avoid raising an error when generating static files.
# Add a real SECRET_KEY config variable in Heroku.
RUN DJANGO_SETTINGS_MODULE=core.settings.prod \
    SECRET_KEY=KEY_ONLY_FOR_STATIC_FILES \
    python3 backend/manage.py collectstatic --noinput
