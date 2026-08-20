#!/bin/bash

if docker compose ps --status running app | grep -q devops-demo-app; then
    echo "Application: UP"
else
    echo "Application: DOWN"
fi

if docker compose ps --status running postgres | grep -q postgres; then
    echo "PostgreSQL:  UP"
else
    echo "PostgreSQL:  DOWN"
fi

if docker compose ps --status running redis | grep -q redis; then
    echo "Redis:       UP"
else
    echo "Redis:       DOWN"
fi
