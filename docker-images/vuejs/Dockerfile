FROM debian:latest

ARG user_name
ARG user_id
ARG grp_id

RUN apt-get update
RUN apt-get upgrade
RUN apt-get install -y \
  lsb-release \
  ca-certificates \
  apt-transport-https \
  software-properties-common \
  gnupg2 \
  sudo 

RUN apt-get update
RUN apt-get install -y \
  curl

RUN curl -fsSL https://deb.nodesource.com/setup_current.x | bash - && apt-get install -y nodejs

# create user

RUN groupadd -g "$grp_id" "$user_name" \
    && useradd -u "$user_id" -g "$grp_id" --shell /bin/bash --create-home "$user_name"

USER "$user_name"

COPY ./startup.sh /home/user/startup.sh
ENTRYPOINT ["/home/user/startup.sh"]