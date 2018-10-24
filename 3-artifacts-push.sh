cd docpage-source/my-project/site
ls
rm -rf .git
git init
#echo "git initiated"
git add .
echo "repo added" #delay
git config user.email "bordovskiy92@gmail.com"
git config user.name "soo-underground"
git commit -m "commit from heroku autobuild"
echo "config set"
echo $1
git remote add build https://soo-underground:$1@github.com/soo-underground/soo-underground.github.io.git
echo "password accepted, remote added"
git remote -v
git push --force build master
echo "artifacts pushed"