import cbmpy
import numpy as np
from cbmpy.CBModel import Model, Reaction, Species

from medium import get_AA_medium_molarity, get_casein_medium_molarity

lacto: Model = cbmpy.loadModel("../../../models/bigg_models/LBUL_v13.xml")

for rid in lacto.getReactionIds():
    if rid.startswith("R_EX"):
        reaction: Reaction = lacto.getReaction(rid)
        reaction.is_exchange = True

# List exchanges and decide which can be open and which should be closed
# for rid in lacto.getExchangeReactionIds():
#     print(f"---------{rid}------------")
#     reaction: Reaction = lacto.getReaction(rid)
#     print(reaction.getLowerBound(), reaction.getUpperBound())
#     print("\n")

# Result is the same no matter these lines
lacto.getReaction("R_EX_glc__D_e").setLowerBound(0)
lacto.getReaction("R_EX_glc__D_e").setUpperBound(0)

print(cbmpy.doFBA(lacto))
FBAsol1 = lacto.getSolutionVector(names=True)
FBAsol1 = dict(zip(FBAsol1[1], FBAsol1[0]))
for rid in lacto.getExchangeReactionIds():
    reaction: Reaction = lacto.getReaction(rid)
    # THis one line below changes the result
    reaction.setUpperBound(1e10)
    if reaction.getLowerBound() <= -1:
        reaction.setLowerBound(-1e10)
    else:
        reaction.setLowerBound(0)


cas_medium = get_casein_medium_molarity()


for rid in lacto.getExchangeReactionIds():
    reaction: Reaction = lacto.getReaction(rid)
    species: Species = lacto.getSpecies(reaction.getSpeciesIds()[0])
    if species.getId() in cas_medium.keys():
        reaction.setLowerBound(-cas_medium[species.getId()])


print(cbmpy.doFBA(lacto))
FBAsol = lacto.getSolutionVector(names=True)
FBAsol = dict(zip(FBAsol[1], FBAsol[0]))

print(FBAsol)
lacto.getReaction("R_ATPM")
for key, value in FBAsol.items():
    ub = lacto.getReaction(key).getUpperBound()
    lb = lacto.getReaction(key).getLowerBound()

    if value != 0.0:
        if lb == value:
            print("LOWERBOUND")
            print(key)
    if value != 0.0:
        if ub == value:
            print("UPPERBOUND")
            print(key)


raise Exception

aa_medium = get_AA_medium_molarity()


for rid in lacto.getExchangeReactionIds():
    reaction: Reaction = lacto.getReaction(rid)
    species: Species = lacto.getSpecies(reaction.getSpeciesIds()[0])
    if species.getId() in aa_medium.keys():
        reaction.setLowerBound(-aa_medium[species.getId()])

print(cbmpy.doFBA(lacto))
FBAsol = lacto.getSolutionVector(names=True)
FBAsol = dict(zip(FBAsol[1], FBAsol[0]))
