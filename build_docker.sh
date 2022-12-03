if [ ! -n "$docker_repo_name" ] || [ ! -n "$docker_tag" ]; then
  echo "Error: Parameters not defined."
  exit 1
fi

echo "docker_repo_name=$docker_repo_name"
echo "docker_tag=$docker_tag"
docker build -f Dockerfile -t $docker_repo_name:$docker_tag .