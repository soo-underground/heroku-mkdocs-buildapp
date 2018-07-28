cd site
ls
git init
git add .
git config user.email "bordovskiy92@gmail.com"
git config user.name "soo-underground"
git commit -m "commit from aws codebuild"
git remote add origin https://soo-underground:S2shk442@github.com/soo-underground/soo-underground.github.io.git
git remote -v
git push --force origin master