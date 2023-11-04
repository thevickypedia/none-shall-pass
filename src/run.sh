source_pkg="none-shall-pass-rustic"
response=$(curl -sL "https://api.github.com/repos/thevickypedia/$source_pkg/releases/latest")

release_id=$(echo "$response" | jq -r '.id')
tag_name=$(echo "$response" | jq -r '.tag_name')
published_at=$(echo "$response" | jq -r '.published_at')
asset_id=$(echo "$response" | jq -r '.assets[0].id')

echo "'$source_pkg' $tag_name publised at $published_at"
echo "Latest Release ID: $release_id"
echo "Asset ID: $asset_id"

# download_url="https://api.github.com/repos/thevickypedia/$source_pkg/releases/assets/$asset_id"
download_url=$(echo "$response" | jq -r '.assets[0].browser_download_url')
curl -o asset -LH "Accept: application/octet-stream" "$download_url"

chmod +x asset
ls -ltrh
./asset ${{ github.repository_owner }} ${{ github.event.repository.name }} true false ""
