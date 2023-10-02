FROM python:3
WORKDIR /usr/src/app
COPY Pipfile ./
RUN pip install --no-cache-dir pipenv && pipenv install
COPY *.py .
CMD ["pipenv", "run", "python", "main.py", "-m", "flask", "--host=0.0.0.0"]