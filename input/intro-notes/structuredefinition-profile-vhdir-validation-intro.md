This profile sets minimum expectations for searching for and fetching information associated with validation. It identifies which core elements, extensions, vocabularies and value sets **SHALL** be present in the VerificationResult resource when using this profile.

**Background & Scope**

This implementation guide was developed to support the need for validated provider data in many different healthcare workflows. It profiles the verificationResult resource to convey information about the validation status of any data in a validated healthcare directory, including how it was validated, who validated it, and where the data came from.

This profile modifies the base VerificationResult resource in the following manner:

*  Constrains the cardinality of `VerificationResult.target` (1..*), `verificationResult.need` (1..1), `verificationResult.statusDate` (1..1), `verificationResult.validationType` (1..1), `verificationResult.validationProcess` (1..*), `verificationResult.failureAction` (1..1), `verificationResult.primarySource.type` (1..*), `verificationResult.attestation.communicatonMethod` (1..1), `verificationResult.attestation.date` (1..1)

*  All references SHALL conform to the appropriate Validated Healthcare Directory Implementation Guide profile


**Examples:**

The following are example uses for the vhdir-validation profile:

-  [Validation of a practitioner's medical license](VerificationResult-example-license.html)


**Mandatory Data Elements**

The following data-elements are mandatory (i.e data MUST be present). These are presented below in a simple human-readable explanation. The [**Formal Profile Definition**](#profile) below provides the  formal summary, definitions, and  terminology requirements.  

Each VerificationResult resource must have:
1.  At least one target in `verificationResult.target`
1.  A coded representation of how often the target is validated in `verificationResult.need`
1.  A coded representation of the target's current validation status in `verificationResult.status`
1.  A date/time when the target's validation status was last updated in `verificationResult.statusDate`
1.  A coded representation of whether the target is validated against a primary source(s) in `verificationResult.validationType`
1.  At least one coded/text representation of the process by which the target was validated in `verificationResult.validationProcess`
1.  A coded representation of what happens if validation of the target fails in `verificationResult.failureAction`
1.  For each primary source described:
    1.  At least one coded/text representation of the type of primary source in `verificationResult.primarySource.type`
1.  Information about the source of the attested information in `VerificationResult.attestation`, including a reference to a Practitioner, PractitionerRole, or Organization resource representing the source of the information in `VerificationResult.attestation.who`
1.  For each validator described:
    1.  One reference to the Organization resource for the validator in `verificationResult.validator.organization`


**Profile specific implementation guidance:**

The core of the verificationResult resource includes basic information about how data was validated:

*  `verificationResult.target` and `verificationResult.targetLocation` provide a means to describe the specific data that has been validated. The target is a reference to any resource, and the targetLocation is a FHIRpath expression indicating which specific element(s) in that resource have been validated.
*  `verificationResult.need` and `verificationResult.frequency` describe when the target should be validated, and how often it must be revalidated
*  `verificationResult.status` describes the current status of validation for the target. `verificationResult.statusDate` indicates when the validation status was last updated.
*  `verificationResult.validationType` describes what the target is validated against (i.e. whether it is validated against a single primary source, whether it is validated against multiple sources, or whether it wasn't validated because attested information is sufficient)
*  `verificationResult.validationProcess` describes the validation processes for validating the target
*  `verificationResult.lastPerformed` and `verificationResult.nextScheduled` describe the last completed and next scheduled dates of validation for the target
*  `verificationResult.failureAction` describes what happens if validation of the target fails

The resource also provides information about entities involved in the validation process:

`verificationResult.primarySource` provides information about the primary source(s) the target was validated against
*  `who` identifies the primary source, and `type` indicates what the primary source is
*  `communicationMethod` indicates how an entity can communicate with the primary source
*  `validationStatus`, and `validationDate` describe the status of the validation of the target against the primary source
*  `canPushUpdates` and `pushTypeAvailable` indicate whether a primary source can push updates or alerts (e.g. alerting the validated healthcare directory if a license board suspends a practitioner's license)

`verificationResult.attestation` provides information about who attested to the information being validated
*  `who` identifies the source of the attested information (a practitioner, practitionerRole, or organization), `onBehalfOf` identifies an entity the "who" is attesting on behalf of.
*  `communicationMethod` indicates how attested information is submitted/retrieved
*  `date` indicates when the information was attested to
*  `sourceIdentityCertificate` and `proxyIdentityCertificate` assert the identity of the individual attesting to information and any proxy providing attested information on their behalf. 
*  `sourceSignature` and `proxySignature` assert that information was attested to/provided by the entity with the right to do so.
`verificationResult.validator` provides information about the entity performing the validation of the target
*  `organization` identifies the validating organization, and `identityCertificate` asserts their identity
*  `attestationSignature` asserts that the validator has validated the target

