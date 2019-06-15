FROM python:3.7

RUN mkdir -p /opt/services/loan_management/src
WORKDIR /opt/services/loan_management/src

# use --system flag because we don't need an extra virtualenv
COPY Pipfile Pipfile.lock /opt/services/loan_management/src/
RUN pip install pipenv && pipenv install --system

COPY . /opt/services/loan_management/src

EXPOSE 8000

COPY ./docker/production/django/start.sh /start.sh
RUN sed -i 's/\r//' /start.sh
RUN chmod +x /start.sh

CMD ["/start.sh"]
