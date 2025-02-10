def validate_force(clan_tonnage, is_tonnage, base_limit):
    """
    Validate if the mixed force complies with the adjusted effective tonnage limit.

    Parameters:
        clan_tonnage (float): Tonnage of Clan units.
        is_tonnage (float): Tonnage of Inner Sphere units.
        base_limit (float): Base tonnage limit (e.g., 400).

    Returns:
        dict: Contains the effective cap, validity status, and unused tonnages.
    """
    # Clan units have a 25% handicap, effectively weighing more
    clan_handicap_factor = 1.33

    # Calculate weighted tonnage
    weighted_clan_tonnage = clan_tonnage * clan_handicap_factor
    effective_cap = weighted_clan_tonnage + is_tonnage

    # Check if the effective cap is within the base limit
    is_valid = effective_cap <= base_limit

    # Calculate remaining tonnage
    remaining_tonnage = base_limit - effective_cap if is_valid else 0
    unused_clan_tonnage = remaining_tonnage / clan_handicap_factor if remaining_tonnage > 0 else 0
    unused_is_tonnage = remaining_tonnage if remaining_tonnage > 0 else 0

    return {
        "Effective Cap": effective_cap,
        "Is Valid": is_valid,
        "Remaining Tonnage": remaining_tonnage,
        "Unused Clan Tonnage": unused_clan_tonnage,
        "Unused IS Tonnage": unused_is_tonnage
    }

# Example usage
if __name__ == "__main__":
    print("\n==========================")
    print("      MIXED FORCE VALIDATOR")
    print("==========================\n")
    
    # Input values
    try:
        clan_tonnage = float(input("Enter Clan Tonnage (tons): "))
        is_tonnage = float(input("Enter Inner Sphere Tonnage (tons): "))
        base_limit = float(input("Enter Base Tonnage Limit (tons): "))
    except ValueError:
        print("\n[ERROR] Please enter valid numeric values.")
        exit()

    # Validate the force
    result = validate_force(clan_tonnage, is_tonnage, base_limit)

    # Output the results
    print("\n==========================")
    print("         RESULTS")
    print("==========================\n")
    print(f"Effective Cap: {result['Effective Cap']:.2f} tons")
    print("Status: " + ("\033[92mVALID\033[0m" if result['Is Valid'] else "\033[91mINVALID\033[0m"))

    if result['Is Valid']:
        print(f"\nRemaining Tonnage: {result['Remaining Tonnage']:.2f} tons")
        print(f"Unused Clan Tonnage: {result['Unused Clan Tonnage']:.2f} tons")
        print(f"Unused Inner Sphere Tonnage: {result['Unused IS Tonnage']:.2f} tons")
    else:
        print("\nYour force composition exceeds the base limit. Adjust your units to comply.")

    print("\n==========================")
    print("        END OF REPORT")
    print("==========================\n")

