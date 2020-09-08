#!/usr/bin/env bash

# NOTE: This bash files works only if executed from the directory it is in as it uses relative path
#       access files
# Prerequisites: Python3 and pip3 installed


# Installing grpcio library
pip3 install -r requirements.txt


# Analyzers automated python files
python3 -m grpc_tools.protoc -I. --python_out=./output --grpc_python_out=./output ./strobesbufs/analyzers/analyzers_service.proto
python3 -m grpc_tools.protoc -I. --python_out=./output ./strobesbufs/analyzers/analyzers.proto


# Messier automated python files creation
python3 -m grpc_tools.protoc -I. --python_out=./output ./strobesbufs/messier/common.proto
python3 -m grpc_tools.protoc -I. --python_out=./output ./strobesbufs/messier/tasks/*.proto
python3 -m grpc_tools.protoc -I. --python_out=./output ./strobesbufs/messier/functions/*.proto
python3 -m grpc_tools.protoc -I. --python_out=./output ./strobesbufs/messier/analyzers/*.proto
python3 -m grpc_tools.protoc -I. --python_out=./output ./strobesbufs/messier/workflows/workflow.proto
python3 -m grpc_tools.protoc -I. --python_out=./output --grpc_python_out=./output ./strobesbufs/messier/workflows/services.proto


# Canis automated python files creation
python3 -m grpc_tools.protoc -I. --python_out=./output --grpc_python_out=./output ./strobesbufs/canis/*.proto


# Creating a new package
cd ./output/strobesbufs
rm -rf dist
echo "__version__ = \"$1\"" > ./__version__.py
python3 -m pip install --user --upgrade setuptools wheel
python3 setup.py sdist bdist_wheel
rm -rf build
echo "Package building completed, you can get the wheel or source in ./output/strobesbufs/dist directory!"