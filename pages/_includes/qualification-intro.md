An extension to add qualifications for an organization (e.g. accreditation) or practitionerRole (e.g. registered to prescribe controlled substances). The extension includes:

*  `qualification.identifier` provides an identifier for the qualification
*  `qualification.code` indicates the type of qualification
*  `qualificaton.issuer` includes a reference to the organization that issued the qualification
*  `qualification.status` describes the current status of the qualification (i.e. active, inactive, issued in error, revoked, pending, unknown)
*  `qualification.period` indicates a period of time during which the current status applies
*  `qualification.whereValid` indicates where the qualification is valid. Users may select any number of specific locations, classes of locations, or combination thereof
*  `qualification.history` presents a series of historical statuses for the qualification and the period of time associated with each status