from msa_sdk.variables import Variables
from msa_sdk.msa_api import MSA_API
import time

dev_var = Variables()
dev_var.add('seconds', var_type='Integer')

# test comment from John
context = Variables.task_call(dev_var)
time.sleep(int(context['seconds']))

ret = MSA_API.process_content('ENDED', 'Task OK', context, True)
print(ret)
