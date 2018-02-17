FROM python:2.7

# Copy python source code
COPY . /tdd_course
WORKDIR /tdd_course

RUN ls -la
RUN pip install nose
RUN nosetests
RUN python setup.py test