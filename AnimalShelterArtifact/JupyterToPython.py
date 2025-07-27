import json

with open("C:\\Users\\Mobiu\\OneDrive\\Desktop\\SNHU\\SNHU_Year_4\\Term_1\\CS-499_CS_Capstone\\Week 1 Artifacts\\Database\\ProjectTwoDashboard.ipynb", "r", encoding="utf-8") as f:
    notebook = json.load(f)

with open("C:\\Users\\Mobiu\\OneDrive\\Desktop\\SNHU\\SNHU_Year_4\\Term_1\\CS-499_CS_Capstone\\Week 1 Artifacts\\Database\\ShelterDashboard.py", "w", encoding="utf-8") as out:
    for cell in notebook["cells"]:
        if cell["cell_type"] == "code":
            out.write("".join(cell["source"]) + "\n\n")