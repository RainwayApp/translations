#!/bin/sh

echo "Clearing bucket: s3://rainwayfiles/i18n"
aws s3 rm s3://rainwayfiles/i18n --recursive --region us-east-1