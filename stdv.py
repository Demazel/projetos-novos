def stdv():
    import pandas as pd

    data = {'scores': [2, 3, 5, 8, 10, 9, 8, 82]}
    df = pd.DataFrame(data)

    # Calculate standard deviation of the 'scores' column
    std_dev_scores = df['scores'].std(ddof=0)
    print(f"Standard deviation of 'scores': {std_dev_scores}")
    
if __name__ == '__main__':
    stdv()