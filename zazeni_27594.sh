mkdir docker_dir
cd docker_dir
docker run -it --name test renki/pythonmath
docker rm test
cd ..
rmdir docker_dir
