"""
Price Calculator Module
-----------------------
This module contains functions for price formatting and currency conversion.
"""


def format_price(price: float) -> int:
    """
    Format a price by rounding it to the nearest whole number.
    
    Args:
        price: The price as a float (e.g., 19.99)
    
    Returns:
        The price rounded to the nearest integer (e.g., 20)
    
    Example:
        >>> format_price(19.99)
        20
        >>> format_price(19.49)
        19
    """
    # BUG: This truncates instead of rounding!
    # int(19.99) = 19, but we want 20
    return int(price)


def convert_currency(amount: float, exchange_rate: float) -> float:
    """
    Convert an amount from one currency to another using the exchange rate.
    
    Args:
        amount: The amount to convert
        exchange_rate: The exchange rate to apply
    
    Returns:
        The converted amount
    
    Example:
        >>> convert_currency(100, 0.85)  # USD to EUR
        85.0
        >>> convert_currency(50, 1.18)   # EUR to USD
        59.0
    """
    # TODO: Implement this function!
    # Hint: It's a simple multiplication
    pass
