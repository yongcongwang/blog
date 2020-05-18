---
title: Build Blog Using Github Pages and Hexo
date: 2018-11-10 15:20:16
categories: software
---

> Environment: ubuntu 18.04
> Time: about 3h
<!-- more -->
## Deploy GitHubPages
Create a new [repo](https://github.com/new) in `github` named `yourname.github.io`

## Install hexo
### Before start
Make sure you have install following software:

#### Node.js
```
curl -sL https://deb.nodesource.com/setup_11.x | sudo -E bash -
sudo apt-get install -y nodejs
```

#### Git
```
sudo apt-get install git
```

### Install hexo
```
npm install -g hexo-cli
```

### Initialize blog folder
```
hexo init yourname.github.io
```

## Install next theme
### Download theme
```
cd your-hexo-site
git clone https://github.com/theme-next/hexo-theme-next themes/next
```

### Enable theme
1. Edit `blog config` file: 
```
vim your-hexo-site/_config.yaml
```
2. Change theme: `theme: next`

### Verify theme
1. Start up `hexo` server:
```
hexo s --debug
```
2. Open`http://localhost:4000`

### Other config
See [Offical Website](https://theme-next.iissnan.com/getting-started.html) guideline


### Edit config
```
blog/_config.yaml
```
then add: 
```
deploy:
  type: git
  repo: git@github.com:yourname/yourname.github.io.git
  branch: master
```

### Install deployer tool
```
npm install hexo-deployer-git --save
```

### Deploy to github
```
hexo g -d
```

## Bind domain

### Register domain
For examle, [Aliyun](https://wanwang.aliyun.com/domain/com/?spm=5176.10695662.1158081.1.1d6f4234zC9zRq)

### Edit blog config
```
vim blog/_config.yml
```
then add:
```
url: http://yongcong.wang
```

### Add **CNAME** file
Create `CNAME` file in `blog/public` folder, then add the domain:
```
touch your-hexo-site/public/CNAME
echo "yongcong.wang" > your-hexo-site/source/CNAME
```

### Deploy GitHubPage domain
In `Custom domain` of `github.com/yourname/yourname.github.io`, add domain

### Add DNS in Aliyun
#### Add record
1. Type: `CNAME`
2. Host: `www`
3. ISP Line: `default`
4. Value: `yourname.github.io`
5. `TTL`: `10min`

#### Add another record
1. Type: `A`
2. Host: `@`
3. ISP Line: `Default`
4. Value: `github repo ip`(use `ping yourname.github.io` command to get)

## Deploy website to `GitHubPages`
```
git init your-hexo-site
git remote add origin git@github.com:yourname/yourname.github.io.git
git add .
git commit -m "some comments"
git push origin hexo:master -f
git checkout hexo
```
## Usage
### Create new page
```
hexo new page "page-title" 
```

### Create new article
```
hexo new post "post-title"
```

### Edit article
```
vim your-hexo-site/source/_post/post-title.md
```

### Preview
```
hexo s
```
then open [localhost:4000](localhost:4000)

### Generate static website and deploy to GithubPages

```
hexo g -d
```
