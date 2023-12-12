#!/bin/bash

while IFS= read -r container_name_or_id; do
    docker stop "$container_name_or_id"
done < containers.txt

