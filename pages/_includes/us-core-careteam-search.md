

-----------

`GET/CareTeam?patient=[id]&status=active`


**Example:** GET [base]/CareTeam?patient=1137192&status=active


*Support:* Mandatory to support search by patient and status.

*Implementation Notes:* Search for all current care team members for a patient. Fetches a bundle of all current CareTeam resource(s) and the participants referenced by the CareTeam resource(s) for the specified patient. [(how to search by reference)], [(how to search by token)].





  [(how to search by reference)]: http://hl7.org/fhir/STU3/search.html#reference
  [(how to search by token)]: http://hl7.org/fhir/STU3/search.html#token
  [Composite Search Parameters]: http://hl7.org/fhir/STU3/search.html#combining
  [(how to search by date)]: http://hl7.org/fhir/STU3/search.html#date
  [(how to include referenced resources in search result)]: (http://hl7.org/fhir/STU3/search.html#include)
