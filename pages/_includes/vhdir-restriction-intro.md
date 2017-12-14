## Background and Context ##

The FHIR specification contains a security meta tag which can be used to inform systems of the sensitivity of resources. The tag can be used by access control mechanisms to ensure content isn't exposed inappropriately. However, the security meta tag can only indicate sensitivity at the resource level, and provides relatively little context about the restriction. We propose a new mechanism, usage-restriction, that extends the concept of restriction further into an individual resource, while providing additional information about the restriction itself. 

Useage-restriction can be applied to a resource, element, or combination thereof. If applied to a resource/element, the restriction is understood to apply to all of the properties of that resource/element, unless otherwise specified (e.g. if applied to an identifier on a practitioner, then all of the properties of that identifier are restricted)

It consists of:
* usage-restriction.target - indicates the resource(s), element(s), or combination thereof that the restriction applies to
* usage-restriction.type - indicates the type of restriction (e.g. based on an item in a data use agreement)
* usage-restriction.policy - indicates the policy defining the restriction
* usage-restriction.status - indicates the status of the restriction (i.e. whether it is active)
* usage-restriction.lastUpdated - indicates when the restriction was last updated
* usage-restriction.retrospective - indicates whether the restriction is retrospective
* usage-restriction.reason - indicates why the target is restricted
  - usage-restriction.reason.name - indicates the name of the restriction condition
  - usage-restriction.conditionalSource - Indicates whether information from another source is necessary to determine if something is restricted
  - usage-restriction.reasonType - indicates the type of restriction
* usage-restriction.accessRights - defines a group/class of individuals/orgs to which the target is not restricted
 
Usage-restriction is expected to be used as a modifier extension.

### Expected Implementations ###
