FROM python:3.12-slim-bookworm

RUN useradd -ms /bin/bash cfa_api

USER cfa_api

WORKDIR /home/cfa_api

COPY requirements.txt .

RUN python3 -m pip install --requirement requirements.txt

COPY tests .

COPY cfa_api .

ENTRYPOINT [ "python3" ]

CMD [ "-m", "pytest" ]