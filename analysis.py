import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_excel("606492885_1773918548660_5f26d2cb-1c80-4b6d-b008-6bc210ddaa17.xlsx")

print("\n========================")
print("DATASET COLUMNS")
print("========================")
print(df.columns)

print("\n========================")
print("TOTAL RECORDS")
print("========================")
print(len(df))

# Severity Distribution
print("\n========================")
print("SEVERITY DISTRIBUTION")
print("========================")
severity = df["Vulnerability_Severity"].value_counts()
print(severity)

# Resource Distribution
print("\n========================")
print("RESOURCE DISTRIBUTION")
print("========================")
resources = df["Resource_Type"].value_counts()
print(resources)

# Public Access Distribution
print("\n========================")
print("PUBLIC ACCESS DISTRIBUTION")
print("========================")
public_access = df["Public_Access"].value_counts()
print(public_access)

# Pipeline Status Distribution
print("\n========================")
print("PIPELINE STATUS DISTRIBUTION")
print("========================")
pipeline = df["CI_CD_Pipeline_Status"].value_counts()
print(pipeline)

# Dependency Distribution
print("\n========================")
print("TOP DEPENDENCIES")
print("========================")
dependencies = df["Application_Dependency"].value_counts()
print(dependencies)

# -----------------------------
# CHART 1 - Severity
# -----------------------------
plt.figure(figsize=(6,4))
severity.plot(kind="bar")
plt.title("Severity Distribution")
plt.tight_layout()
plt.savefig("severity_distribution.png")
plt.close()

# -----------------------------
# CHART 2 - Resources
# -----------------------------
plt.figure(figsize=(6,4))
resources.plot(kind="bar")
plt.title("Resource Distribution")
plt.tight_layout()
plt.savefig("resource_distribution.png")
plt.close()

# -----------------------------
# CHART 3 - Public Access
# -----------------------------
plt.figure(figsize=(6,4))
public_access.plot(kind="bar")
plt.title("Public Access Distribution")
plt.tight_layout()
plt.savefig("public_access_distribution.png")
plt.close()

# -----------------------------
# CHART 4 - Pipeline Status
# -----------------------------
plt.figure(figsize=(6,4))
pipeline.plot(kind="bar")
plt.title("Pipeline Status Distribution")
plt.tight_layout()
plt.savefig("pipeline_status_distribution.png")
plt.close()

print("\n========================")
print("REPORT FINDINGS")
print("========================")

critical = severity.get("Critical", 0)
public_yes = public_access.get("Yes", 0)

print(f"Critical Vulnerabilities: {critical}")
print(f"Publicly Accessible Resources: {public_yes}")

print("\nCharts Generated Successfully:")
print("1. severity_distribution.png")
print("2. resource_distribution.png")
print("3. public_access_distribution.png")
print("4. pipeline_status_distribution.png")