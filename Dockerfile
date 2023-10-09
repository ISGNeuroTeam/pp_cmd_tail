FROM python:3.9.7
LABEL authors="mashida"
ENV PYTHONUNBUFFERED=1

RUN mkdir /postprocessing_sdk
RUN git clone --branch feature/DEV-4320 https://github.com/ISGNeuroTeam/postprocessing_sdk.git

RUN mkdir /postprocessing_sdk/postprocessing_sdk/pp_cmd/readFile
RUN git clone https://github.com/ISGNeuroTeam/pp_cmd_readFile /postprocessing_sdk/postprocessing_sdk/pp_cmd/readFile

RUN chmod -R 0777 /postprocessing_sdk

ADD tail postprocessing_sdk/postprocessing_sdk/pp_cmd/
ADD tests postprocessing_sdk/postprocessing_sdk/pp_cmd/

#CMD ["python", "/postprocessing_sdk/postprocessing_sdk/pp_cmd/tail/server.py"]


