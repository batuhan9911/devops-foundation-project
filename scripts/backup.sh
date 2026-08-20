#!/bin/bash

docker exec postgres pg_dump -U devops -d devopsdb > backup.sql
echo "Database backup completed."
