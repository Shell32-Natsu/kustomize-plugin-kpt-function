FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY DemoTransformer.py .
RUN chmod a+r DemoTransformer.py

ENTRYPOINT [ "python", "./DemoTransformer.py" ]