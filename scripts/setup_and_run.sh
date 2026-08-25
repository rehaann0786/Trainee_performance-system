#!/bin/bash

set -e

echo "======================================"
echo "Trainee Performance Management System"
echo "======================================"

echo ""
echo "Checking Python..."
python --version

echo ""
echo "Installing dependencies..."
python -m pip install -r requirements.txt

echo ""
echo "Running database schema..."
psql -U postgres -f sql/schema.sql

echo ""
echo "Running database seed..."
psql -U postgres -d training_db -f sql/seed.sql

echo ""
echo "Running CSV ingestion..."
python -m scripts.ingest_csv

echo ""
echo "Running tests..."
python -m pytest

echo ""
echo "Starting application..."
python -m src.main