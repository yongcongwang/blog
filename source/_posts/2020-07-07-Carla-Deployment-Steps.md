---
title: Carla Deployment Steps
categories: software
tags:
  - autodrive
  - software
mathjax: true
comments: true
date: 2020-07-07 19:02:15
---

> Environment:
> OS: Ubuntu 18.04LTS
> GPU: Gtx 1650
> Carla: 0.9.8
> Engine: Unreal 4.2.2

Carla has two modes: one is offline mode, like a game through the keyboard to control the vehicle to drive in the simulation environment; the other is server mode, Carla hosts a simulation environment, the client receives data and sends a vehicle control signal to control the vehicle in Carla. The offline mode is relatively simple, run the script `./CarlaUE4.sh`. We prefer the use of server mode, the following steps are based on server mode. All steps refer to Carla [official documents](https://carla.readthedocs.io/en/stable/).

<!-- more -->

# Installation
Download the Linux installation package from [github](https://github.com/carla-simulator/carla/releases/) and unzip it:
```bash
./ImportAssets.sh
```
# Usage
1. Installation dependencies:
```
pip install --user pygame numpy
grep aaa
```
2. Start the server
```
./CarlaUE4.sh
```
3. Start the client
```
python3 spawn_npc.py
```
Then you can see the client controlling the vehicle in the simulation, other settings see the [official document](https://carla.readthedocs.io/en/stable/connecting_the_client/)

# Compilation
If the simulation is performed in the official simulation environment, the above steps are sufficient. If the simulation environment is to be modified, the project needs to be compiled. The steps are as follows:

## Installation dependency
```
sudo apt-get install build-essential clang-3.9 git cmake ninja-build python3-requests python-dev tzdata sed curl wget unzip autoconf libtool
```
The project is compiled using clang 3.9 and needs to set the default version of clang to 3.9:
```
sudo update-alternatives --install /usr/bin/clang++ clang++ /usr/lib/llvm-3.9/bin/clang++ 100
sudo update-alternatives --install /usr/bin/clang clang /usr/lib/llvm-3.9/bin/clang 100
```
If unsuccessful, switch manually with the following command:
```
sudo update-alternatives --config clang
```

## Compilation Unreal Engine
Unreal Engine is Carla's simulation engine, using version 4.18.

### Preparation
The source code is on github, but the repo is private and you need to join the `Epic Games` organization to see it, as follows:
1. Sign up for an account on the Unreal Engine website.
2. Find github in Personal-> Connected Accounts and click Connect
3. Log in to github in the pop-up window.

### Compilation
Confirm that the github account has been added to the `Epic Games` organization, then compile with the following command:
```
git clone --depth=1 -b 4.18 https://github.com/EpicGames/UnrealEngine.git ~/UnrealEngine_4.18
cd ~/UnrealEngine_4.18
./Setup.sh && ./GenerateProjectFiles.sh && make
```
### Bug
If you encounter a bug in the compilation, you can find a solution from the [Unreal document](https://forums.unrealengine.com/unreal-engine/announcements-and-releases/1745504-a-new-community-hosted-unreal-engine-wiki). The bug I encountered:
1. 'xlocale.h' file not found:
```
sudo ln -s /usr/include/locale.h /usr/include/xlocale.h
```

## Compilation Carla

### Download the source code
```
git clone https://github.com/carla-simulator/carla
```
### Installation dependency
```
./Setup.sh
```
Note that the last step of setup is to download `Content.tar.gz` from `Google Drive`. If you do not configure the agent, you should not be able to download and cause compilation failure. You can change the variable `SKIP_DOWNLOAD = false` of `Update.sh` to `true`, then manually download the file and unzip it to the `Unreal/CarlaUE4/Content` folder. Note that the file in the compressed package is placed in `Content`, not the folder `Content_0.8.2`. The correct file structure is:
```
Content
├── Blueprints
├── Collections
├── Developers
├── LICENSE
├── Maps
└── Static
```
### Compilation
#### First compilation
For the first time you need to compile all items, use the following command:
```
export UE4_ROOT=~/UnrealEngine_4.18
./Rebuild.sh
```
If there is no errors, the `Carla editor` will be activated at the end of the compilation. The interface is as follows:
![carla](https://user-images.githubusercontent.com/31853843/49566487-0eae1600-f92b-11e8-9eeb-0bd24a13c385.png)

#### Follow-up compilation
If there are only a few changes and you do not need to compile the entire project, you can use the following command to compile:
```
cd Unreal/CarlaUE4
make CarlaUE4Editor
```
### Load editor
After the project is compiled, you can open the editor with the following command:
```
cd Unreal/CarlaUE4
~/UnrealEngine_4.18/Engine/Binaries/Linux/UE4Editor "$PWD/CarlaUE4.uproject"
```
