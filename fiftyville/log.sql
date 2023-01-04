-- Keep a log of any SQL queries you execute as you solve the mystery.
-- Get a description of the crime scene as a starting point to solve the mystery
SELECT description
  FROM crime_scene_reports
 WHERE day = 28
   AND month = 7
   AND year = 2021
   AND street = "Humphrey Street";

-- Get the transcript of interviews with witnesses of the crime

SELECT transcript
  FROM interviews
 WHERE day = 28
   AND month = 7
   AND year = 2021
   AND transcript LIKE "%bakery%";


-- Get a list of license plates from cars that left the bakery parking lot during the 10 minute timeframe of the crimescene.
SELECT license_plate
  FROM bakery_security_logs
 WHERE day = 28
   AND month = 7
   AND year = 2021
   AND hour = 10
   AND minute BETWEEN 15 AND 25;

-- Get a list of suspects using the license plates from previous query (Vanessa, Barry, Iman, Sofia, Luca, Diana, Kelsey, Bruce)
SELECT name
  FROM people
 WHERE license_plate
    IN
       (SELECT license_plate
          FROM bakery_security_logs
         WHERE day = 28
           AND month = 7
           AND year = 2021
           AND hour = 10
           AND minute BETWEEN 15 AND 25);

-- Account numbers of those who used ATM on Leggett Street as per the second witness
SELECT account_number
  FROM atm_transactions
 WHERE day = 28
   AND month = 7
   AND year = 2021
   AND atm_location = "Leggett Street"
   AND transaction_type = "withdraw";

-- Get a list of suspects using ATM transactions as per the second witness (Kenny, Iman, Benista, Taylor, Brooke, Luca, Diana, Bruce, Kaelyn)

SELECT name
  FROM people
 WHERE id
    IN
       (SELECT person_id
          FROM bank_accounts
         WHERE account_number
            IN
               (SELECT account_number
                  FROM atm_transactions
                 WHERE day = 28
                   AND month = 7
                   AND year = 2021
                   AND atm_location = "Leggett Street"));

-- Get list of people who used the phone as per 3rd witness transcript
SELECT name
  FROM people
 WHERE phone_number
    IN
       (SELECT caller
          FROM phone_calls
         WHERE day = 28
           AND month = 7
           AND year = 2021
           AND duration < 60);
-- Get list of people who used earliest flight out of fiftyville the day after crime
SELECT name
  FROM people
 WHERE passport_number
    IN
      (SELECT passport_number
         FROM passengers
         JOIN flights
           ON passengers.flight_id = flights.id
        WHERE flight_id =
             (SELECT id
                FROM flights
               WHERE origin_airport_id =
                    (SELECT id
                       FROM airports
                      WHERE city = "Fiftyville")
                        AND day = 29
                        AND month = 7
                        AND year = 2021
                        ORDER BY hour LIMIT 1));
-- Finding the criminal by narrowing down the suspect list using the 3 transcript from witnesses (Bruce)

SELECT name
  FROM people
 WHERE license_plate
    IN
       (SELECT license_plate
          FROM bakery_security_logs
         WHERE day = 28
           AND month = 7
           AND year = 2021
           AND hour = 10
           AND minute BETWEEN 15 AND 25)
INTERSECT
SELECT name
  FROM people
 WHERE id
    IN
       (SELECT person_id
          FROM bank_accounts
         WHERE account_number
            IN
               (SELECT account_number
                  FROM atm_transactions
                 WHERE day = 28
                   AND month = 7
                   AND year = 2021
                   AND atm_location = "Leggett Street"))
INTERSECT
SELECT name
  FROM people
 WHERE phone_number
    IN
       (SELECT caller
          FROM phone_calls
         WHERE day = 28
           AND month = 7
           AND year = 2021
           AND duration < 60)
INTERSECT
SELECT name
  FROM people
 WHERE passport_number
    IN
      (SELECT passport_number
         FROM passengers
         JOIN flights
           ON passengers.flight_id = flights.id
        WHERE flight_id =
             (SELECT id
                FROM flights
               WHERE origin_airport_id =
                    (SELECT id
                       FROM airports
                      WHERE city = "Fiftyville")
                        AND day = 29
                        AND month = 7
                        AND year = 2021
                        ORDER BY hour LIMIT 1));

-- The city to which the thief escaped to

SELECT city
  FROM airports
 WHERE id =
      (SELECT destination_airport_id
         FROM flights
        WHERE id =
             (SELECT id
                FROM flights
               WHERE origin_airport_id =
                    (SELECT id
                       FROM airports
                      WHERE city = "Fiftyville")
                        AND day = 29
                        AND month = 7
                        AND year = 2021 ORDER BY hour LIMIT 1));
--Accomplice


SELECT name
  FROM people
 WHERE phone_number =
      (SELECT receiver
         FROM phone_calls
        WHERE caller =
             (SELECT phone_number
                FROM people
               WHERE name = "Bruce")
                 AND day = 28
                 AND month = 7
                 AND year = 2021
                 AND duration < 60);








--



