#!/usr/bin/env pwsh

# NOTE: This Powershell script works only if executed from the directory it is in as it uses relative path
#       access files
# Prerequisites: Python3 and pip3 installed


# Parameters
param (
    [Parameter(Mandatory = $true)][string]$version
)


# Installing grpcio library
pip3 install -r requirements.txt


# Analyzers automated python files
python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. .\strobesbufs\analyzers\analyzers_service.proto
python3 -m grpc_tools.protoc -I. --python_out=. .\strobesbufs\analyzers\analyzers.proto


# Messier automated python files creation
python3 -m grpc_tools.protoc -I. --python_out=. .\strobesbufs\messier\common.proto
python3 -m grpc_tools.protoc -I. --python_out=. .\strobesbufs\messier\tasks\*.proto
python3 -m grpc_tools.protoc -I. --python_out=. .\strobesbufs\messier\functions\*.proto
python3 -m grpc_tools.protoc -I. --python_out=. .\strobesbufs\messier\analyzers\*.proto
python3 -m grpc_tools.protoc -I. --python_out=. .\strobesbufs\messier\workflows\workflow.proto
python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. .\strobesbufs\messier\workflows\services.proto


# Canis automated python files creation
python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. .\strobesbufs\canis\*.proto


# Creating a new package
Set-Location .\strobesbufs
Remove-Item .\dist -Recurse
$line = "__version__ = '$version'"
$line | Out-File -Encoding "UTF8" .\__version__.py
python3 -m pip install --user --upgrade setuptools wheel
python3 setup.py sdist bdist_wheel
Remove-Item .\build -Recurse
Remove-Item .\__pycache__ -Recurse
Write-Host "Package building completed, you can get the wheel or source in .\strobesbufs\dist directory!"