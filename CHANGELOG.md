# Change Log

## Unreleased

## 0.0.10

Released on September 14th 2024

### Changed

* Map RSVP response from Y, N, etc to Yes, No
* Fix adult_count, child_count to map empty str from api back to 0

## 0.0.9

Released on September 14th 2024

### Changed

* RSVP Sug now returns data via API


## 0.0.8

Released on February 13th 2024

### Changed

* Updated parsing to expect more lower case keys in slot data


## 0.0.7

Released on September 13th 2023

### Changed

* Updated parsing to expect lower case keys in participant data


## 0.0.6

Released on August 30th 2023

### Changed

* Updated parsing to tolerate newline between name and guest count rather than space

## 0.0.5

Released on February 23rd 2023

### Changed

* When sourcing from api, trim whitespace from names

## 0.0.4

Released on January 2nd 2023

### Changed
* When sourcing from api, also apply name mappings and match names logic

## 0.0.3

Released on January 2nd 2023

### Added
* Added support for api-driven signups

## 0.0.2

Released on December 13th 2022

### Added

* Added CHANGELOG
* Added support for new variant - Slot / Datetime
* Added replace_names utility script for obfuscating names/comments in signup genius test data

### Changed

* When matching signups to a known set of names, do not override a name that has been explicitly mapped through 
* Fixed bs4 deprecation warning re use of *text=* with find()

### Removed


## 0.0.1

Released on October 24th 2022

### Added

* First version of the package, including:
	* Basic parsing of signup genius html into response objects
	* Supports two ways of coercing names of respondents:
		1. via an explicit name mapping and,
		2. via closest match to a population of known names

