if [ ! -n "$docker_repo_name" ] || [ ! -n "$docker_tag" ]; then
  echo "Error: Parameters not defined."
  exit 1
fi

docker run -it -p 7860:7860 \
  $docker_repo_name:$docker_tag