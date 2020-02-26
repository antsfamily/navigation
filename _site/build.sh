mv _site ../temp

bundle exec jekyll build --trace --incremental

mv ../temp ./

cp -rf _site/* temp/
rm -rf _site
mv temp _site
