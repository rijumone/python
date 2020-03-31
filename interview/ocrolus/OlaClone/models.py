# models.py


class Customers():
    id = Column(Integer, primary_key=True)
    name = Column(String())
    status = Column(String()) # ENUM ['free', 'booked_enroute', 'in_trip']
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime)


class Drivers():
    id = Column(Integer, primary_key=True)
    status = Column(String()) # ENUM ['free', 'booked_enroute', 'in_trip', 'off_duty']
    name = Column(String())
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime)


class Trips():
    id = Column(Integer, primary_key=True)
    current_latitude = Column(Numeric())
    current_longitude = Column(Numeric())
    from_latitude = Column(Numeric())
    from_longitude = Column(Numeric())
    driver_id = Column(Integer, ForeignKey('drivers.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    amount = Column(Numeric())
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime)


class TripHistory():
    id = Column(Integer, primary_key=True)
    trip_id = Column(Integer, ForeignKey('trips.id'))
    status = Column(String()) # ENUM ['requested', 'driver_assigned', 'started', 'completed', 'cancelled']
    current_latitude = Column(Numeric())
    current_longitude = Column(Numeric())
    action_by = Column(String()) # ENUM ['driver', 'customer']
    action_by_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)


class Payments():
    id = Column(Integer, primary_key=True)
    trip_id = Column(Integer, ForeignKey('trips.id'))
    amount_received = Column(Numeric())
    payment_mode_id = Column(Integer, ForeignKey('payment_modes.id'))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime)

class PaymentModes():
    id = Column(Integer, primary_key=True)
    name = Column(String())

class CustomerPaymentMode():
    id = Column(Integer, primary_key=True)
    payment_mode_id = Column(Integer, ForeignKey('payment_modes.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))

class CurrentLocations():
    id = Column(Integer, primary_key=True)
    entity_id = Column(Integer())
    entity_type = Column(String()) # ENUM ['driver', 'customer']
    latitude = Column(Numeric())
    longitude = Column(Numeric())
    


"""
SELECT payment_mode_id, 
       name, 
       count(amount_received) 
FROM   `Payments` 
       INNER JOIN PaymentModes 
               ON PaymentModes.id = payment_mode_id 
GROUP  BY payment_mode_id 
ORDER  BY 3 DESC ;
"""