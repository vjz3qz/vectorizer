FROM python:3
WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir pipenv && pipenv install
CMD ["pipenv", "run", "python", "main.py", "-m", "flask", "run", "--host=0.0.0.0"]
