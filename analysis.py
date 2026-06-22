import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_excel("devsecops_pipeline_security_dataset (2).xlsx")

# ========================
# DATASET SUMMARY
# ========================

print("\n========================")
print("TOTAL RECORDS")
print("========================")
print(len(df))

print("\n========================")
print("SEVERITY DISTRIBUTION")
print("========================")
print(df["Vulnerability_Severity"].value_counts())

print("\n========================")
print("PIPELINE STAGE DISTRIBUTION")
print("========================")
print(df["CI_CD_Pipeline_Stage"].value_counts())

print("\n========================")
print("RESOURCE TYPE DISTRIBUTION")
print("========================")
print(df["Resource_Type"].value_counts())

print("\n========================")
print("PUBLIC EXPOSURE")
print("========================")
print(df["Public_Exposure"].value_counts())

# ========================
# CHART 1
# ========================

df["Vulnerability_Severity"].value_counts().plot(kind="bar")
plt.title("Severity Distribution")
plt.xlabel("Severity")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("severity_distribution.png")
plt.close()

# ========================
# CHART 2
# ========================

df["CI_CD_Pipeline_Stage"].value_counts().plot(kind="bar")
plt.title("Pipeline Stage Distribution")
plt.xlabel("Pipeline Stage")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("pipeline_distribution.png")
plt.close()

# ========================
# CHART 3
# ========================

df["Resource_Type"].value_counts().plot(kind="bar")
plt.title("Resource Type Distribution")
plt.xlabel("Resource Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("resource_distribution.png")
plt.close()

# ========================
# CHART 4
# ========================

df["Public_Exposure"].value_counts().plot(kind="bar")
plt.title("Public Exposure Distribution")
plt.xlabel("Exposure")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("public_exposure_distribution.png")
plt.close()

print("\n========================")
print("REPORT FINDINGS")
print("========================")

critical_count = (df["Vulnerability_Severity"] == "Critical").sum()
public_count = (df["Public_Exposure"] == "Yes").sum()

print(f"Critical Vulnerabilities: {critical_count}")
print(f"Publicly Exposed Resources: {public_count}")

print("\nCharts Generated Successfully")
print("1. severity_distribution.png")
print("2. pipeline_distribution.png")
print("3. resource_distribution.png")
print("4. public_exposure_distribution.png")