PYTHONPATH=$PYTHONPATH:./source
echo 'Running pylint and finding potential bad practices/bugs'
python -m pylint source
status = $?
echo 'pylint status', $?

echo 'Running pytest on the entire project'
python -m pytest -v tests/
status = $?
echo 'pytest status', $?