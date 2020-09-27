FROM python:3.8
RUN pip install pipenv
ENV PROJECT_DIR /usr/local/src/webapp
WORKDIR ${PROJECT_DIR}
COPY Pipfile Pipfile.lock ${PROJECT_DIR}/
RUN pipenv install --deploy --ignore-pipfile
COPY ./ ${PROJECT_DIR}/
CMD ["pipenv", "run", "flask", "run", "--port=8888", "--host=0.0.0.0"]

