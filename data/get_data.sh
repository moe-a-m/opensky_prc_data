# Install minio from https://min.io/docs/minio/macos/index.html for mac 
# or https://min.io/docs/minio/windows/index.html for windows
# replace the bucket access key and secret from the json response file
mc alias set dc24 https://s3.opensky-network.org/ <bucket_access_key> <bucket_access_secret>
mc cp --recursive dc24/competition-data/2022-01 .
mc cp --recursive dc24/competition-data/2022-02 .
mc cp --recursive dc24/competition-data/2022-03 .