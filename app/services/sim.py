from typing import List, Dict, Tuple
import  numpy as np
import random

def polyfit_predict(x: List[float], y: List[float], future_x: List[float]) -> List[float]:
    # if < 3 years played, can't use polyfit to create a curve
    d