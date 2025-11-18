def matched_bet_calculator():
    # Get user inputs
    back_stake = float(input("Enter bookmaker stake (£): "))
    back_odds = float(input("Enter bookmaker odds: "))
    lay_odds = float(input("Enter exchange lay odds: "))
    commission = 0

    # Calculate lay stake (balanced for commission)
    lay_stake = (back_odds * back_stake) / (lay_odds - commission)
    lay_stake = round(lay_stake, 2)  # Round to 2 decimal places

    # PnL calculations
    # Case 1: Back bet wins
    profit_bookmaker = back_stake * (back_odds - 1)
    loss_exchange = lay_stake * (lay_odds - 1)
    net_win = profit_bookmaker - loss_exchange

    # Case 2: Back bet loses
    loss_bookmaker = -back_stake
    profit_exchange = lay_stake * (1 - commission)
    net_lose = loss_bookmaker + profit_exchange

    # Output results
    print("\n--- Results ---")
    print(f"Lay stake to place: £{lay_stake:.2f}")
    print(f"If back bet wins: Net PnL = £{net_win:.2f}")
    print(f"If back bet loses: Net PnL = £{net_lose:.2f}")

if __name__ == "__main__":
    matched_bet_calculator()