FROM python:alpine

RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev
ENV PERSONA_CLUSTER=docker
COPY . /apps/persona/

RUN pip install /apps/persona/

RUN python /apps/persona/manage.py migrate

RUN python /apps/persona/manage.py people_from_json fake_profiles.zip

EXPOSE 8000
# TODO: to use more efficient way i.e guincorn & nginx instead of using django to serve wsgi
CMD ['python', '/apps/persona/manage.py', 'runserver']

