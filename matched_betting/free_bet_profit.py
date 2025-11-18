def free_bet_profit():
    print("=== Free Bet Profit Calculator (Stake Not Returned) ===")
    
    # Inputs
    free_bet = float(input("Free bet stake (£): ").strip())
    back_odds = float(input("Bookmaker back odds: ").strip())
    lay_stake_input = input("Exchange lay stake (£) [Leave blank to auto-calc]: ").strip()
    lay_odds = float(input("Exchange lay odds: ").strip())
    exchange_commission = float(input("Exchange commission (%): ").strip()) / 100.0
    bookmaker_commission = float(input("Bookmaker commission on winnings (%): ").strip()) / 100.0

    # Auto-calculate lay stake if not given
    if lay_stake_input == "":
        # back winnings after bookmaker commission
        net_back_win = (back_odds - 1) * free_bet * (1 - bookmaker_commission)
        lay_stake = net_back_win / (lay_odds - exchange_commission)
        auto_calc = True
    else:
        lay_stake = float(lay_stake_input)
        auto_calc = False

    # Back wins case:
    profit_bookmaker = (back_odds - 1) * free_bet * (1 - bookmaker_commission)  # free bet: stake not returned
    liability_exchange = lay_stake * (lay_odds - 1)
    pnl_back_wins = profit_bookmaker - liability_exchange

    # Back loses case:
    profit_exchange = lay_stake * (1 - exchange_commission)
    pnl_back_loses = profit_exchange

    # Guaranteed profit:
    guaranteed_profit = min(pnl_back_wins, pnl_back_loses)

    # Output
    print("\n--- Results ---")
    if auto_calc:
        print(f"Optimal lay stake: £{lay_stake:.2f}")
    print(f"If back wins: £{pnl_back_wins:.2f}")
    print(f"If back loses: £{pnl_back_loses:.2f}")
    print(f"Guaranteed profit: £{guaranteed_profit:.2f}")

if __name__ == "__main__":
    free_bet_profit()
