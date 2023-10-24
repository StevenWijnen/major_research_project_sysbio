import cbmpy
import numpy as np
from cbmpy.CBModel import Model, Reaction, Species

from medium import get_AA_medium_molarity, get_casein_medium_molarity

strep = cbmpy.loadModel("../../../models/bigg_models/strep_therm.xml")
aa_medium = get_casein_medium_molarity()


for sid in aa_medium.keys():
    if sid not in strep.getSpeciesIds():
        print(sid)
