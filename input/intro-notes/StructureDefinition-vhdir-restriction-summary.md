####  Summary of the Mandatory Requirements and Key properties

1.  A coded value representing the status of the restriction in `consent.status`
1.  At least one coded and/or text value describing the type of restriction in `consent.category`
1.  At least one `actor` when describing access rights via `consent.provision`. Each actor must include a `reference` to a practitioner, organization, care team, or group. The `role` of each actor is fixed to code "IRCP" (information recipient) from the code system defined at <http://hl7.org/fhir/v3/ParticipationType>
