import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Names": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Scores": [85, 90, 78, 92, 88]
}
df = pd.DataFrame(data)  

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

#Histogram   
sns.histplot(df["Scores"], bins=5, kde=False, ax=axes[0], color='blue')
axes[0].set_title("Histogram of Scores")
axes[0].set_xlabel("Scores")
axes[0].set_ylabel("Frequency")

# Density Plot
sns.kdeplot(df["Scores"], fill=True, ax=axes[1], color='green')
axes[1].set_title("Density Plot of Scores")
axes[1].set_xlabel("Scores")
axes[1].set_ylabel("Density")

# Box Plot
sns.boxplot(y=df["Scores"], ax=axes[2], color='red')
axes[2].set_title("Box Plot of Scores")
axes[2].set_ylabel("Scores")

# Show plots
plt.tight_layout()
plt.show()
