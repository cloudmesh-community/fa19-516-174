# craete a make file that does
# make image
# make run
# or python cms command with sys generate so we can call it anywhwer
# we showed in class how to do this with sys genertae
# its nt enough to just create a dockerfile

FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python", "app.py" ]