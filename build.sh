cd site
ls
git init
echo "1"
git add .
echo "2"
git config user.email "bordovskiy92@gmail.com"
git config user.name "soo-underground"
git commit -m "commit from aws codebuild"
echo "3"
echo $1
git remote add herokuautobild https://soo-underground:S22@github.com/soo-underground/soo-underground.github.io.git
echo "4"
git remote -v
echo "5"
git push --force origin master




