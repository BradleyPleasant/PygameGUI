import os
os.environ['UI_SNAPSHOT'] = '1'
os.environ['UI_EXIT_AFTER_SNAPSHOT'] = '1'
os.environ['UI_DEBUG'] = '1'

import runpy
runpy.run_path(r'c:\Users\IcoTw\PycharmProjects\PygameGUI\V0.3 Playground.py', run_name='__main__')
print('playground executed')

# This small runner was used temporarily to execute the playground under
# instrumented env vars (UI_DEBUG/UI_SNAPSHOT) and capture a single frame.
# I've removed its runtime logic; tell me if you want it restored.

# Note: the detailed visibility test is in run_v03_playground_test.py which creates simple colored boxes for each element.
