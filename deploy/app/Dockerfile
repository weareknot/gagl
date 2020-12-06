FROM python:latest

ENV PYTHONUNBUFFERED 1

# install geos, from https://stackoverflow.com/questions/39377911/oserror-when-trying-to-pip-install-shapely-inside-docker-container
ENV GEOS http://download.osgeo.org/geos/geos-3.8.1.tar.bz2

WORKDIR /install-postgis

WORKDIR /install-postgis/geos
ADD $GEOS /install-postgis/geos.tar.bz2
RUN tar xf /install-postgis/geos.tar.bz2 -C /install-postgis/geos --strip-components=1
RUN ./configure && make && make install
RUN ldconfig
WORKDIR /

COPY ./requirements.txt /requirements.txt
RUN pip install -U pip
RUN pip install -r /requirements.txt

COPY ./entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

WORKDIR /app

CMD ["/entrypoint"]
