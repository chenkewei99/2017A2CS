# 1 a
## i
cityIn(London,UK).
## ii 
Visitedd(Strasbourg)>
# b
chile, argentina
# c
countriesIVisited(Country) IF cityIn(City, Country) AND iVisited(City).

# 2a
## i 
minimumAge (car, 18).
## ii
allowedToDrive(X, V) IF hasLicence (X) AND minimumAge (V, L) AND age (X, A) AND A>=L.
# b
## i
Who = jack
## ii
False
## iii
False
# c
## i
qualifiedCarDrivers(X) IF qualifiedDriver(X, car).
## ii
partQualified(X) IF passedTheoryTest(X) AND NOT passedDrivingTest(X, _).
# d
Clause 11 (true), clause 01 (instantiates L as 18), clause 05 (instantiates A
as 17), clause 15 ( A < L so it is false) result is false