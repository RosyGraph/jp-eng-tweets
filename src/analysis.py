import pandas as pd
from scipy.stats import f_oneway

from process_reports import load_df

df = load_df()

f, p = f_oneway(df["jp_comprehensiveness"], df["en_comprehensiveness"])
results = [{"name": "comprehensiveness", "f": f, "p": p}]
f, p = f_oneway(df["jp_relevance"], df["en_relevance"])
results.append({"name": "relevance", "f": f, "p": p})
f, p = f_oneway(df["jp_accuracy"], df["en_accuracy"])
results.append({"name": "accuracy", "f": f, "p": p})

anova_df = pd.DataFrame(results)
print(anova_df.to_markdown())
