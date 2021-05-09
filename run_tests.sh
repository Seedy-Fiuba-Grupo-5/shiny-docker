#!/bin/sh
echo "[RUN_TESTS] Running tests ..."
docker-compose exec service_users_web pytest "backend_users/tests" -p no:warnings --cov="backend_users"
echo "[RUN_TESTS] Running flake8 inside all folders"
docker-compose exec service_users_web flake8 backend_users
