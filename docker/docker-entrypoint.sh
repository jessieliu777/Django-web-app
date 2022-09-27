#!/bin/bash

echo "Process started"

if [ ${SERVICE_NAME} == "rm1_nginx" ]; then
  echo "Starting nginx..."
  nginx "-g daemon off;"
fi