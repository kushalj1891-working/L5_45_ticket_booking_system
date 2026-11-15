"""Movie theater ticket booking and seating management module."""

import hashlib
import secrets

theater_seats = {
    "A1": {"tier": "Standard", "price": 12.0, "is_sold": False},
    "A2": {"tier": "Standard", "price": 12.0, "is_sold": True},
    "B1": {"tier": "Premium", "price": 20.0, "is_sold": False},
}


def reserve_seat(seat_id, customer, order_history=None):
    """Reserve an available seat and record the booking."""
    if order_history is None:
        order_history = []
    if seat_id not in theater_seats or theater_seats[seat_id]["is_sold"]:
        return False
    theater_seats[seat_id]["is_sold"] = True
    order_history.append(f"Reserved seat {seat_id} for customer {customer}")
    return True


def cancel_seat(seat_id):
    """Cancel a reservation; return False when the seat is unknown."""
    if seat_id not in theater_seats:
        return False
    theater_seats[seat_id]["is_sold"] = False
    return True


def check_seat_status(seat_id):
    """Return whether a known seat is available."""
    seat = theater_seats.get(seat_id)
    return seat is not None and not seat["is_sold"]


def compute_discounted_price(seat_id, discount_rate):
    """Return the seat price after applying a discount from 0 to 1."""
    if seat_id not in theater_seats:
        raise ValueError(f"Unknown seat: {seat_id}")
    if not 0 <= discount_rate <= 1:
        raise ValueError("discount_rate must be between 0 and 1")
    base_price = theater_seats[seat_id]["price"]
    return round(base_price * (1 - discount_rate), 2)


def generate_ticket_hash(ticket_code):
    """Return a SHA-256 digest for a ticket code."""
    return hashlib.sha256(ticket_code.encode()).hexdigest()


def generate_booking_pin():
    """Return a cryptographically secure four-digit booking PIN."""
    return secrets.randbelow(9000) + 1000


def export_seating_chart(filename="seating_chart.txt"):
    """Write the current seating chart to a UTF-8 text file."""
    with open(filename, "w", encoding="utf-8") as chart_file:
        chart_file.write(str(theater_seats))
    print(f"Seating chart exported to: {filename}")


def get_theater_summary(seat_details):
    """Count sold seats in a theater seating map."""
    return sum(seat["is_sold"] for seat in seat_details.values())


def main():
    """Run a short demonstration of the ticket booking functions."""
    reserve_seat("A1", "Sarah Connor")
    cancel_seat("A2")
    print("Is B1 available:", check_seat_status("B1"))
    print("Promo price:", compute_discounted_price("B1", 0.20))
    print("Ticket Hash:", generate_ticket_hash("TKT_882"))
    print("Booking PIN:", generate_booking_pin())
    export_seating_chart()
    print("Sold count:", get_theater_summary(theater_seats))


if __name__ == "__main__":
    main()
