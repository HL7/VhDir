## Background and Context ##

The FHIR specification contains a security meta tag which can be used to inform systems of the sensitivity of resources. The tag can be used by access control mechanisms to ensure content isn't exposed inappropriately. However, the security meta tag can only indicate sensitivity at the resource level, and provides relatively little context about the restriction. 

This implementation guide profiles the Consent resource to provide additional details about the nature of restricted content. This extension provides a reference to the VhDir Consent profile. It is available to all other profiles in this implementation guide. 

This extension is typically expected to function as a reference to a [contained resource](https://www.hl7.org/fhir/references.html#contained).
