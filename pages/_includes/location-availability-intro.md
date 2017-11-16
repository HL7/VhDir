An extension to describe the general availability of a location. Similar to the availability attributes found in the practitionerRole resource.

Consists of:
* availableTime - indicates the times the location is available
  * availableTime.daysOfWeek - indicates the day(s) of the week the location is available
  * availableTime.allDay - indicates the location is always available 
  * availableTime.availableStartTime - indicates when the location opens
  * availableTime.availableEndTime - indicates when the location closes
* notAvailable - indicates why a location is not available at a particular time
  * notAvailable.description - describes the reason the location is not available
  * notAvailable.during - indicates a period for which the location is not available
* availabilityExceptions - describes any exceptions to when this location is typically available

