#!/bin/bash
echo '当前运行的Shell脚本路径:'$0
echo "完整路径："`pwd`
s_cd_to_path=$(cd `dirname $0`; pwd)
echo 切换到的目录:$s_cd_to_path
cd $s_cd_to_path
python3 manage.py runserver 0.0.0.0:9999
