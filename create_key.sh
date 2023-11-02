#!/usr/bin/env bash
openssl genrsa -aes256 -out private.key 2048
openssl rsa -in private.key -out private.key
openssl req -new -x509 -nodes -sha1 -key private.key -out certificate.crt -addext 'subjectAltName = IP:127.0.0.1' -days 36500
sudo cp certifactes.crt /usr/local/share/ca-certificates/
sudo update-ca-certificates
