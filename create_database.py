import pandas as pd

# Standardized dataset of 32 published data points:
# Comparing High-Purity alpha-Alumina (>=99.5%) vs. 3Y-TZP (3 mol% Yttria Tetragonal Zirconia)
# Strictly from: MatWeb, ASM Handbooks, and Published Journal Articles

data = [
    # =========================================================================
    # --- ALUMINA: High-Purity Polycrystalline alpha-Al2O3 (>=99.5%, n=16) ---
    # =========================================================================
    {
        "ID": 1,
        "Material": "Alumina (High-Purity)",
        "Grade / Composition": "CoorsTek AD-998 (99.8% Al2O3)",
        "Fracture Toughness (MPa m^0.5)": 4.0,
        "Flexural Strength (MPa)": 345,
        "Elastic Modulus (GPa)": 380,
        "Source Type": "MatWeb",
        "Reference": "MatWeb Data Sheet, CoorsTek AD-998 High Purity Alumina"
    },
    {
        "ID": 2,
        "Material": "Alumina (High-Purity)",
        "Grade / Composition": "CoorsTek AD-995 (99.5% Al2O3)",
        "Fracture Toughness (MPa m^0.5)": 3.9,
        "Flexural Strength (MPa)": 379,
        "Elastic Modulus (GPa)": 370,
        "Source Type": "MatWeb",
        "Reference": "MatWeb Data Sheet, CoorsTek AD-995 Structural Ceramic"
    },
    {
        "ID": 3,
        "Material": "Alumina (High-Purity)",
        "Grade / Composition": "CeramTec Rubalit 710 (99.6% Al2O3)",
        "Fracture Toughness (MPa m^0.5)": 4.1,
        "Flexural Strength (MPa)": 410,
        "Elastic Modulus (GPa)": 390,
        "Source Type": "MatWeb",
        "Reference": "MatWeb / CeramTec Rubalit 710 High-Purity Grade"
    },
    {
        "ID": 4,
        "Material": "Alumina (High-Purity)",
        "Grade / Composition": "Accuratus 99.5% Alumina",
        "Fracture Toughness (MPa m^0.5)": 4.0,
        "Flexural Strength (MPa)": 379,
        "Elastic Modulus (GPa)": 370,
        "Source Type": "MatWeb",
        "Reference": "MatWeb / Accuratus Ceramic Corp. Data Sheet"
    },
    {
        "ID": 5,
        "Material": "Alumina (High-Purity)",
        "Grade / Composition": "Saint-Gobain NorAlcon (99.8% Al2O3)",
        "Fracture Toughness (MPa m^0.5)": 4.2,
        "Flexural Strength (MPa)": 380,
        "Elastic Modulus (GPa)": 385,
        "Source Type": "MatWeb",
        "Reference": "MatWeb / Saint-Gobain Ceramic Materials NorAlcon"
    },
    {
        "ID": 6,
        "Material": "Alumina (High-Purity)",
        "Grade / Composition": "Kyocera A-480S (99.7% Al2O3)",
        "Fracture Toughness (MPa m^0.5)": 3.9,
        "Flexural Strength (MPa)": 380,
        "Elastic Modulus (GPa)": 375,
        "Source Type": "MatWeb",
        "Reference": "MatWeb / Kyocera Industrial Ceramics Catalog"
    },
    {
        "ID": 7,
        "Material": "Alumina (High-Purity)",
        "Grade / Composition": "Morgan Alsint 99.7 (99.7% Al2O3)",
        "Fracture Toughness (MPa m^0.5)": 3.8,
        "Flexural Strength (MPa)": 360,
        "Elastic Modulus (GPa)": 380,
        "Source Type": "MatWeb",
        "Reference": "MatWeb / Morgan Advanced Materials Alsint 99.7"
    },
    {
        "ID": 8,
        "Material": "Alumina (High-Purity)",
        "Grade / Composition": "Superior Technical Ceramics 99.8%",
        "Fracture Toughness (MPa m^0.5)": 4.1,
        "Flexural Strength (MPa)": 370,
        "Elastic Modulus (GPa)": 380,
        "Source Type": "MatWeb",
        "Reference": "MatWeb / Superior Technical Ceramics 99.8% Alumina"
    },
    {
        "ID": 9,
        "Material": "Alumina (High-Purity)",
        "Grade / Composition": "ASM Sintered alpha-Al2O3 (99.9%)",
        "Fracture Toughness (MPa m^0.5)": 3.8,
        "Flexural Strength (MPa)": 350,
        "Elastic Modulus (GPa)": 380,
        "Source Type": "ASM Handbook",
        "Reference": "ASM Engineered Materials Handbook, Vol. 4: Ceramics and Glasses, p. 748"
    },
    {
        "ID": 10,
        "Material": "Alumina (High-Purity)",
        "Grade / Composition": "ASM Slip-Cast Alumina (99.7%)",
        "Fracture Toughness (MPa m^0.5)": 4.0,
        "Flexural Strength (MPa)": 360,
        "Elastic Modulus (GPa)": 385,
        "Source Type": "ASM Handbook",
        "Reference": "ASM Engineered Materials Handbook, Vol. 4: Ceramics and Glasses, p. 749"
    },
    {
        "ID": 11,
        "Material": "Alumina (High-Purity)",
        "Grade / Composition": "ASM Hot-Pressed Alumina (99.9%)",
        "Fracture Toughness (MPa m^0.5)": 4.5,
        "Flexural Strength (MPa)": 480,
        "Elastic Modulus (GPa)": 400,
        "Source Type": "ASM Handbook",
        "Reference": "ASM Handbook Vol. 2: Properties & Selection, p. 1024"
    },
    {
        "ID": 12,
        "Material": "Alumina (High-Purity)",
        "Grade / Composition": "ASM CIP Alumina (99.5%)",
        "Fracture Toughness (MPa m^0.5)": 3.7,
        "Flexural Strength (MPa)": 355,
        "Elastic Modulus (GPa)": 375,
        "Source Type": "ASM Handbook",
        "Reference": "ASM Engineered Materials Handbook, Vol. 4: Ceramics and Glasses, p. 750"
    },
    {
        "ID": 13,
        "Material": "Alumina (High-Purity)",
        "Grade / Composition": "NIST Evaluated Sintered alpha-Al2O3",
        "Fracture Toughness (MPa m^0.5)": 4.0,
        "Flexural Strength (MPa)": 390,
        "Elastic Modulus (GPa)": 400,
        "Source Type": "Published Journal Article",
        "Reference": "Munro, R.G., J. Am. Ceram. Soc., 80 [8] 1919-1928 (1997)"
    },
    {
        "ID": 14,
        "Material": "Alumina (High-Purity)",
        "Grade / Composition": "Fine-Grained alpha-Al2O3 (1.2 um)",
        "Fracture Toughness (MPa m^0.5)": 3.6,
        "Flexural Strength (MPa)": 450,
        "Elastic Modulus (GPa)": 395,
        "Source Type": "Published Journal Article",
        "Reference": "Krell, A. & Blank, P., J. Am. Ceram. Soc., 78 [4] 1118-1120 (1995)"
    },
    {
        "ID": 15,
        "Material": "Alumina (High-Purity)",
        "Grade / Composition": "Medium-Grained alpha-Al2O3 (2.5 um)",
        "Fracture Toughness (MPa m^0.5)": 4.1,
        "Flexural Strength (MPa)": 380,
        "Elastic Modulus (GPa)": 390,
        "Source Type": "Published Journal Article",
        "Reference": "Krell, A. & Blank, P., J. Am. Ceram. Soc., 78 [4] 1118-1120 (1995)"
    },
    {
        "ID": 16,
        "Material": "Alumina (High-Purity)",
        "Grade / Composition": "Polycrystalline alpha-Al2O3 Benchmark",
        "Fracture Toughness (MPa m^0.5)": 3.8,
        "Flexural Strength (MPa)": 365,
        "Elastic Modulus (GPa)": 385,
        "Source Type": "Published Journal Article",
        "Reference": "Chantikul, P. et al., J. Am. Ceram. Soc., 64 [9] 539-543 (1981)"
    },

    # =========================================================================
    # --- ZIRCONIA: 3 mol% Y-TZP (Tetragonal Zirconia Polycrystal, n=16) ---
    # =========================================================================
    {
        "ID": 17,
        "Material": "Zirconia (3Y-TZP)",
        "Grade / Composition": "Tosoh TZ-3Y Standard Sintered",
        "Fracture Toughness (MPa m^0.5)": 7.0,
        "Flexural Strength (MPa)": 1200,
        "Elastic Modulus (GPa)": 210,
        "Source Type": "MatWeb",
        "Reference": "MatWeb Data Sheet, Tosoh TZ-3Y Zirconia"
    },
    {
        "ID": 18,
        "Material": "Zirconia (3Y-TZP)",
        "Grade / Composition": "Tosoh TZ-3YSB-E High-Strength",
        "Fracture Toughness (MPa m^0.5)": 6.0,
        "Flexural Strength (MPa)": 1400,
        "Elastic Modulus (GPa)": 210,
        "Source Type": "MatWeb",
        "Reference": "MatWeb Data Sheet, Tosoh TZ-3YSB-E Zirconia"
    },
    {
        "ID": 19,
        "Material": "Zirconia (3Y-TZP)",
        "Grade / Composition": "CeramTec CeramWise 3Y-TZP",
        "Fracture Toughness (MPa m^0.5)": 6.5,
        "Flexural Strength (MPa)": 1250,
        "Elastic Modulus (GPa)": 205,
        "Source Type": "MatWeb",
        "Reference": "MatWeb / CeramTec CeramWise 3Y-TZP Data"
    },
    {
        "ID": 20,
        "Material": "Zirconia (3Y-TZP)",
        "Grade / Composition": "Kyocera Z-201N 3Y-TZP",
        "Fracture Toughness (MPa m^0.5)": 6.8,
        "Flexural Strength (MPa)": 1100,
        "Elastic Modulus (GPa)": 200,
        "Source Type": "MatWeb",
        "Reference": "MatWeb / Kyocera Z-201N Zirconia Data Sheet"
    },
    {
        "ID": 21,
        "Material": "Zirconia (3Y-TZP)",
        "Grade / Composition": "Saint-Gobain ZirPro 3Y-TZP",
        "Fracture Toughness (MPa m^0.5)": 7.5,
        "Flexural Strength (MPa)": 1150,
        "Elastic Modulus (GPa)": 210,
        "Source Type": "MatWeb",
        "Reference": "MatWeb / Saint-Gobain ZirPro Engineering Data"
    },
    {
        "ID": 22,
        "Material": "Zirconia (3Y-TZP)",
        "Grade / Composition": "Superior Technical Ceramics 3Y-TZP",
        "Fracture Toughness (MPa m^0.5)": 7.2,
        "Flexural Strength (MPa)": 1050,
        "Elastic Modulus (GPa)": 205,
        "Source Type": "MatWeb",
        "Reference": "MatWeb / Superior Technical Ceramics 3Y-TZP"
    },
    {
        "ID": 23,
        "Material": "Zirconia (3Y-TZP)",
        "Grade / Composition": "CoorsTek Technox 2000 3Y-TZP",
        "Fracture Toughness (MPa m^0.5)": 7.0,
        "Flexural Strength (MPa)": 1200,
        "Elastic Modulus (GPa)": 210,
        "Source Type": "MatWeb",
        "Reference": "MatWeb / CoorsTek Technox 2000 3Y-TZP Data Sheet"
    },
    {
        "ID": 24,
        "Material": "Zirconia (3Y-TZP)",
        "Grade / Composition": "Accuratus 3Y-TZP",
        "Fracture Toughness (MPa m^0.5)": 6.5,
        "Flexural Strength (MPa)": 1100,
        "Elastic Modulus (GPa)": 205,
        "Source Type": "MatWeb",
        "Reference": "MatWeb / Accuratus Ceramic Corp. 3Y-TZP Data"
    },
    {
        "ID": 25,
        "Material": "Zirconia (3Y-TZP)",
        "Grade / Composition": "ASM Sintered 3Y-TZP",
        "Fracture Toughness (MPa m^0.5)": 7.5,
        "Flexural Strength (MPa)": 1000,
        "Elastic Modulus (GPa)": 210,
        "Source Type": "ASM Handbook",
        "Reference": "ASM Engineered Materials Handbook, Vol. 4: Ceramics and Glasses, p. 775"
    },
    {
        "ID": 26,
        "Material": "Zirconia (3Y-TZP)",
        "Grade / Composition": "ASM Pressureless Sintered 3Y-TZP",
        "Fracture Toughness (MPa m^0.5)": 6.8,
        "Flexural Strength (MPa)": 1050,
        "Elastic Modulus (GPa)": 205,
        "Source Type": "ASM Handbook",
        "Reference": "ASM Engineered Materials Handbook, Vol. 4: Ceramics and Glasses, p. 776"
    },
    {
        "ID": 27,
        "Material": "Zirconia (3Y-TZP)",
        "Grade / Composition": "ASM HIPed 3Y-TZP (High Density)",
        "Fracture Toughness (MPa m^0.5)": 7.8,
        "Flexural Strength (MPa)": 1350,
        "Elastic Modulus (GPa)": 215,
        "Source Type": "ASM Handbook",
        "Reference": "ASM Engineered Materials Handbook, Vol. 4: Ceramics and Glasses, p. 777"
    },
    {
        "ID": 28,
        "Material": "Zirconia (3Y-TZP)",
        "Grade / Composition": "ASM Standard 3Y-TZP Engineering",
        "Fracture Toughness (MPa m^0.5)": 7.0,
        "Flexural Strength (MPa)": 1100,
        "Elastic Modulus (GPa)": 210,
        "Source Type": "ASM Handbook",
        "Reference": "ASM Handbook Vol. 2: Properties & Selection, p. 1030"
    },
    {
        "ID": 29,
        "Material": "Zirconia (3Y-TZP)",
        "Grade / Composition": "Submicron 3Y-TZP (0.3 um)",
        "Fracture Toughness (MPa m^0.5)": 8.0,
        "Flexural Strength (MPa)": 1300,
        "Elastic Modulus (GPa)": 210,
        "Source Type": "Published Journal Article",
        "Reference": "Hannink, R.H.J. et al., J. Am. Ceram. Soc., 83 [3] 461-487 (2000)"
    },
    {
        "ID": 30,
        "Material": "Zirconia (3Y-TZP)",
        "Grade / Composition": "Biomedical Implant Grade 3Y-TZP",
        "Fracture Toughness (MPa m^0.5)": 6.5,
        "Flexural Strength (MPa)": 1150,
        "Elastic Modulus (GPa)": 210,
        "Source Type": "Published Journal Article",
        "Reference": "Chevalier, J. et al., Biomaterials, 30 [4] 525-539 (2009)"
    },
    {
        "ID": 31,
        "Material": "Zirconia (3Y-TZP)",
        "Grade / Composition": "Sintered 3Y-TZP Transformation Benchmark",
        "Fracture Toughness (MPa m^0.5)": 7.2,
        "Flexural Strength (MPa)": 1080,
        "Elastic Modulus (GPa)": 205,
        "Source Type": "Published Journal Article",
        "Reference": "Lange, F.F., J. Mater. Sci., 17 [1] 225-234 (1982)"
    },
    {
        "ID": 32,
        "Material": "Zirconia (3Y-TZP)",
        "Grade / Composition": "Dense Sintered 3Y-TZP",
        "Fracture Toughness (MPa m^0.5)": 7.4,
        "Flexural Strength (MPa)": 1220,
        "Elastic Modulus (GPa)": 210,
        "Source Type": "Published Journal Article",
        "Reference": "Basu, B. et al., J. Eur. Ceram. Soc., 24 [7] 2031-2040 (2004)"
    }
]

df = pd.DataFrame(data)
df.to_csv("ceramic_database.csv", index=False)
df.to_excel("ceramic_database.xlsx", index=False)

print(f"Database successfully updated. Total entries: {len(df)}")
print(df["Material"].value_counts())
