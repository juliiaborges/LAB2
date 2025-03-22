import pandas as pd
import os

def split_into_batches(csv_file="top_java_repos.csv", batch_size=100, output_dir="batches"):
    df = pd.read_csv(csv_file)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i in range(0, len(df), batch_size):
        batch_df = df.iloc[i:i + batch_size]
        batch_file = os.path.join(output_dir, f"batch_{i//batch_size + 1}.csv")
        batch_df.to_csv(batch_file, index=False)
        print(f"Lote salvo: {batch_file}")

if __name__ == "__main__":
    split_into_batches()
