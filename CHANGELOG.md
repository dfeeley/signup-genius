# Change Log

## Unreleased

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

