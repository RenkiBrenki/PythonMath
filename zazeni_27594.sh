mkdir docker_dir
cd docker_dir
docker run -it --name testing2 renki/pythonmath
docker rm testing2
cd ..
rmdir docker_dir
