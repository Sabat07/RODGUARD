import json
import os

FILE = "reports.json"

print("=== ROADGUARD ===")

location = input("Enter road location: ")
description = input("Describe the hazard: ")

reports = []

if os.path.exists(FILE):
    with open(FILE, "r") as f:
        reports = json.load(f)

report = {
    "location": location,
    "description": description,
    "status": "Reported"
}

reports.append(report)

with open(FILE, "w") as f:
    json.dump(reports, f, indent=4)

print("\nReport saved successfully!")
print("\n=== ALL ROAD REPORTS ===")

for i, report in enumerate(reports, start=1):
    print(f"\nReport {i}")
    print("Location:", report["location"])
    print("Hazard:", report["description"])
    print("Status:", report["status"])