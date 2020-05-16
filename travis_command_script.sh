echo 'Running pylint and finding potential bad practices/bugs'
python -m pylint source
pylint_status = $?
echo 'pylint status', $?

echo 'Running pytest on the entire project'
python -m pytest -v tests/
pytest_status = $?
echo 'pytest status', $?