# Yogurt medium as defined by: 10.3390/microorganisms10091771

# Concentration in g/L

basic_medium = {
    "M_lcts_e": 15.75,  # TODO NOT IN strep model`?`
    "M_urea_e": 0.12,
    "M_ade_e": 1,  # Adenine
    "M_gua_e": 1,  # Guanine
    "M_ura_e": 1,  # Uracil
    "M_xan_e": 1,  # Xanthine
}
# Not neccesarry probably
vitamins = {
    # Vitamins
    "M_btn_e": 0.0002,
    "M_ribflv_e": 0.0005,  # Riboflavin
    # "M_folic_acid_e": 0.0002,  # TODO No offical name found in bigg ??
    # "M_pydx_e": 0.001,  # TODO Original name: Pyridoxal hydrochloride; could also refer to M_pydx5p_c???
    # "M_thm_e": 0.0005,  # TODO Thiamine chloride hydrochloride could also be M_thmpp_c
    # "M_ncam_c": 0.0005,  # nicotinamide TODO there is no extracellular metabolite for this one!!!!!!! make it and an exchange reaction in streptococus?
    # "M_cyanocobalamin_e": 0.0005,  # TODO not found in the models?
    # "M_4abz_e": 0.0005,  # TODO 4-Aminobenzoic acid	 -> is this the correct one?
    # "M_d_pantothenic_acid_hemicalcium_salt_e": 0.004,  # TODO not found in the model?
    # "#M_dl_6_8_thioctic_acid_e": 0.0005,
    # trace elements
}

# Concentration in g/L
AA = {
    "M_ala__L_e": 0.1,
    "M_arg__L_e": 0.317,
    "M_asp__L_e": 0.499,
    "M_cys__L_e": 0.3,
    "M_glu__L_e": 0.331,
    "M_gln__L_e": 0.29,
    "M_gly_e": 0.16,
    "M_his__L_e": 0.273,
    "M_ile__L_e": 0.361,
    "M_leu__L_e": 0.6,
    "M_lys__L_e": 0.351,
    "M_met__L_e": 0.119,
    "M_phe__L_e": 0.34,
    "M_pro__L_e": 0.921,
    "M_ser__L_e": 0.359,
    "M_thr__L_e": 0.3,
    "M_trp__L_e": 0.102,
    "M_tyr__L_e": 0.12,
    "M_val__L_e": 0.468,
    # No casein
    "M_cas_e": 0,
}

# Concentration in g/L
casein = {
    "M_cas_e": 2,
    # Set the amino acids to zero
    "M_ala__L_e": 0,  # L-Alanine
    "M_arg__L_e": 0,  # L-Arginine
    "M_asp__L_e": 0,  # L-Asparagine
    "M_asp__L_e": 0,  # L-Aspartic acid
    "M_cys__L_e": 0,  # L-Cysteine
    "M_glu__L_e": 0,  # L-Glutamic acid
    "M_gln__L_e": 0,  # L-Glutamine
    "M_gly_e": 0,  # Glycine
    "M_his__L_e": 0,  # L-Histidine
    "M_ile__L_e": 0,  # L-Isoleucine
    "M_leu__L_e": 0,  # L-Leucine
    "M_lys__L_e": 0,  # L-Lysine
    "M_met__L_e": 0,  # L-Methionine
    "M_phe__L_e": 0,  # L-Phenylalanine
    "M_pro__L_e": 0,  # L-Proline
    "M_ser__L_e": 0,  # L-Serine
    "M_thr__L_e": 0,  # L-Threonine
    "M_trp__L_e": 0,  # L-Tryptophan
    "M_tyr__L_e": 0,  # L-Tyrosine
    "M_val__L_e": 0,  # L-Valine
}

# Molar mass dict g/mol
MM_dict = {
    # Other
    "M_lac__D_e": 90.08,
    "M_lcts_e": 342.3,
    "M_urea_e": 60.06,
    # nucleobases
    "M_ade_e": 135.13,  # Adenine
    "M_gua_e": 151.13,  # Guanine
    "M_ura_e": 112.09,  # Uracil
    "M_xan_e": 152.11,  # Xanthine
    # Vitamins
    "M_btn_e": 244.31,
    "M_ribflv_e": 376.36,  # Riboflavin
    # tracer elemetns
    # Amino acids
    "M_ala__L_e": 89.09,
    "M_arg__L_e": 174.20,
    "M_asp__L_e": 132.12,
    "M_cys__L_e": 121.16,
    "M_glu__L_e": 147.13,
    "M_gln__L_e": 146.15,
    "M_gly_e": 75.07,
    "M_his__L_e": 209.63,  # Monochloride
    "M_ile__L_e": 131.17,
    "M_leu__L_e": 131.18,
    "M_lys__L_e": 146.19,
    "M_met__L_e": 149.21,
    "M_phe__L_e": 165.19,
    "M_pro__L_e": 115.13,
    "M_ser__L_e": 105.09,
    "M_thr__L_e": 119.12,
    "M_trp__L_e": 204.23,
    "M_tyr__L_e": 181.19,
    "M_val__L_e": 117.15,
    # Casine
    "M_cas_e": 2061.96,  # Picked one
}


def get_AA_medium():
    return {**basic_medium, **AA}


def get_casein_medium():
    return {**basic_medium, **casein}


def get_AA_casein_medium():
    return {**basic_medium, **casein, **AA}


def convert_to_mili_molarity(dict):
    return {key: (dict[key] / MM_dict[key]) * 1000 for key in dict.keys()}


def get_AA_medium_molarity():
    return convert_to_mili_molarity(get_AA_medium())


def get_casein_medium_molarity():
    return convert_to_mili_molarity(get_casein_medium())
