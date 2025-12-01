def main():
    
    import pandas as pd
    import matplotlib.pyplot as plt
    
    df_nba_stats = pd.read_csv("nba_player_stats.csv")
    
    df_ppg = df_nba_stats["PPG"]
    
    plt.hist(df_ppg)
    plt.show()
    
if __name__ == "__main__":
    main()