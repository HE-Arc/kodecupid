FROM debian:latest

ARG user_name
ARG user_id
ARG grp_id

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y \
  pipenv
  
# create user
RUN groupadd -g "$grp_id" "$user_name" \
    && useradd -u "$user_id" -g "$grp_id" --shell /bin/bash --create-home "$user_name"

USER "$user_name"

COPY ./startup.sh /home/user/startup.sh
ENTRYPOINT ["/home/user/startup.sh"]