FROM registry.access.redhat.com/ubi8/ubi:latest
RUN yum install -y golang && yum install -y git && git clone https://github.com/projectdiscovery/nuclei.git && cd nuclei/v2/cmd/nuclei && go build && mv nuclei /usr/local/bin/
ENTRYPOINT ["nuclei"]