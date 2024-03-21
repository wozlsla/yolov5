for file in *.jpeg; do
    # convert "$file" "${file%.jpeg}.jpg"
    magick "$file" "${file%.jpeg}.jpg"
done