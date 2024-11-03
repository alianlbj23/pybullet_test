#!/bin/bash

# 容器名稱
CONTAINER_NAME="moveit2_container"

#檢查容器是否存在
if [ "$(docker ps -aq -f name=${CONTAINER_NAME})" ]; then
    echo "發現同名容器，正在停止並刪除..."
    docker stop ${CONTAINER_NAME}
    docker rm ${CONTAINER_NAME}
fi

# 運行新的容器
docker run -it --rm \
    --name ${CONTAINER_NAME} \
    --network host \
    --privileged \
    --volume $(pwd)/src:/root/ws/src \
    --workdir /root/ws \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    moveit/moveit2:humble-release \
    /bin/bash