FROM ubuntu:latest

RUN apt-get update && apt-get install -y git

RUN source_pkg="none-shall-pass-rustic"
RUN response=$(curl -sL "https://api.github.com/repos/thevickypedia/$source_pkg/releases/latest")
RUN release_id=$(echo "$response" | jq -r '.id')
RUN tag_name=$(echo "$response" | jq -r '.tag_name')
RUN published_at=$(echo "$response" | jq -r '.published_at')
RUN asset_id=$(echo "$response" | jq -r '.assets[0].id')
RUN echo "'$source_pkg' $tag_name publised at $published_at"
RUN echo "Latest Release ID: $release_id"
RUN echo "Asset ID: $asset_id"
RUN download_url=$(echo "$response" | jq -r '.assets[0].browser_download_url')
RUN curl -o asset -LH "Accept: application/octet-stream" "$download_url"
RUN chmod +x asset

ENTRYPOINT ["./asset"]
