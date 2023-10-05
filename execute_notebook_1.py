# execute_notebook_1.py
import papermill as pm

input_notebook = 'notebook_example_1.ipynb'
output_notebook = 'output_notebook_1.ipynb'

# Execute notebook with different parameters
parameters_list = [{'a': 2, 'b': 8}, {'a': 10, 'b': 5}]

for parameters in parameters_list:
    pm.execute_notebook(
        input_notebook,
        output_notebook,
        parameters=parameters
    )

print("------Execution completed-------")