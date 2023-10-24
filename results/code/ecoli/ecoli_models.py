import cbmpy
from cbmpy.CBModel import Model, Reaction


iAF1260: Model = cbmpy.loadModel("../../input/iAF1260.xml")

# Set exchange reactions
reaction: Reaction
for reaction in iAF1260.reactions:
    if reaction.getSBOterm() == "SBO:0000627":
        reaction.is_exchange = True

for reaction in iAF1260.reactions:
    if reaction.getLowerBound() == -999999.0:
        reaction.setLowerBound(cbmpy.NINF)
    if reaction.getUpperBound() == 999999.0:
        reaction.setUpperBound(cbmpy.INF)

iAF1260.getReaction("R_EX_lys__L_e").setLowerBound(0)
iAF1260.getReaction("R_EX_leu__L_e").setLowerBound(0)


def get_leucine_knock_out_model():
    # Negative leucine (L)
    iAF1260_N_L: Model = iAF1260.clone()
    leucine = "M_leu__L_c"
    knock_out_gene_leucine = "G_b0074"
    leucine_gene_knock_out_associated_reaction = "R_IPPS"
    leucine_creating_reaction = "R_LEUTAi"

    # Knock out gene
    iAF1260_N_L.getGene(knock_out_gene_leucine).setInactive()

    return iAF1260_N_L


def get_lysine_knock_out_model():
    # Negative Lysine (K)
    iAF1260_N_K = iAF1260.clone()
    lysine = "M_lys__L_c"

    knock_out_gene_lysine = "G_b2838"
    associated_reaction = "R_DAPDC"

    # Make sure no lysine enters the system
    iAF1260_N_K.getGene(knock_out_gene_lysine).setInactive()

    return iAF1260_N_K
