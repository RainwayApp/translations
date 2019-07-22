#!/bin/sh

echo "Clearing bucket: s3://your-bucket/path/inside/bucket/if/you/want"
aws s3 rm s3://s3://rainwayfiles/i18n --recursive --region us-east-1