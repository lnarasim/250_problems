echo 'Running pylint and finding potential bad practices/bugs'
python -m pylint pyproblems
pylint_status=$?
echo 'pylint status', $pylint_status

echo 'Running pytest on the entire project'
python -m pytest -v tests/
pytest_status=$?
echo 'pytest status', $pytest_status

exit $pylint_status | $pytest_status