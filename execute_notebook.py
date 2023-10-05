import papermill as pm

# Run the notebook with different parameters
parameters_list = [{'length': 5, 'width': 3}, {'length': 10, 'width': 2}, {'length': 8, 'width': 4}, {'length': 10, 'width': 10}]

for parameters in parameters_list:
    pm.execute_notebook(
        'analysis.ipynb',
        'output_notebook.ipynb',
        parameters=parameters
    )
