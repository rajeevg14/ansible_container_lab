FROM docker.io/openjdk:11

RUN useradd --comment "sqlcl owner" --home-dir /home/sqlcl --uid 1000 --create-home --shell $(which bash) sqlcl

USER sqlcl
WORKDIR /home/sqlcl

ENV ZIPFILE=sqlcl-21.4.1.17.1458.zip

RUN curl -LO "https://download.oracle.com/otn_software/java/sqldeveloper/${ZIPFILE}" && \
        /usr/local/openjdk-11/bin/jar -xf ${ZIPFILE} && \
        rm ${ZIPFILE}

ENTRYPOINT ["bash", "/home/sqlcl/sqlcl/bin/sql", "/nolog"]