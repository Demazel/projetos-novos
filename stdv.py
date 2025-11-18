def stdv():
    import pandas as pd

    data = {'scores': [20, 25, 19, 28, 23, 30]}
    df = pd.DataFrame(data)

    # Calculate standard deviation of the 'scores' column
    std_dev_scores = df['scores'].std()
    print(f"Standard deviation of 'scores': {std_dev_scores}")
    
if __name__ == '__main__':
    stdv()