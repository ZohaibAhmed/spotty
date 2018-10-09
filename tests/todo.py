"""
TODO for test:
1. test command outputs
2. test create-ami template (with TravisCI?), check how to test CF templates
    (integration tests for all CF templates)
3. test lambda functions: https://github.com/vandium-io/lambda-tester
    (or rewrite them to python files and test them right here)

TODO for the tool:
1. create "status" command
2. read lambda JS files, minify them and inject to templates
3. ? message: "restoring snapshot"
4. check if portal-gun got working rsync for Windows
    (just out of interest, anyway data should be synced before creating a CF template)


Publishing:

python setup.py sdist bdist_wheel
/d/Anaconda/envs/dog-project/Scripts/twine upload dist/*
"""

