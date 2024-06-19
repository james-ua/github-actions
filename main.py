import os
import sys
sys.path.append('../common')
sys.path.append(os.path.abspath('/Workspace/Scripts/CDP_EMEA/dp-n01-cdp-emea-consumer-behavior-reporting/src/python/databricks/common'))        
import cbrep_mappings_new as mapping

a = mapping.utils('world')
d = mapping.utils('Hello')
print(a,d)
