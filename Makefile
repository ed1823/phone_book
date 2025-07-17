#!/bin/bash

lint:
	uv run pre-commit run --all-files
