import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from funciones.restar import restar

def test_restar(): 
    assert restar(10, 4) == 6 
    assert restar(0, 0) == 0




