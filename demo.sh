#!/bin/bash
gunicorn demo:app -p demo.pid -b 0.0.0.0:8080 -D
