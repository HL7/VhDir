This profile sets minimum expectations for searching for and fetching information associated with validation. It identifies which core elements, extensions, vocabularies and value sets **SHALL** be present in the validation resource when using this profile.

**Background & Scope**

The need for validated provider data is the impetus for this implementation guide. We propose the creation of a new resource for conveying information about the validation of any other piece of data, including how it was validated, who validated it, and where the data came from.

The core of the validation resource includes basic information about how the data was validated:

*  `validation.target` represents the data that is being validated.The target may be a resource, attribute, or set of attributes.
*  `validation.validationNeed` and `validation.frequency` describe when the target should be validated, and how often it must be revalidated
*  `validation.validationStatus` describes the current status of validation for the target. `validation.validationStatusDate` indicates when the validation status was last updated.
*  `validation.validationType` describes what the target is validated against (i.e. whether it is validated against a single primary source, whether it is validated against multiple sources, or whether attested information is acceptable and it isn't validated at all)
*  `validation.validationProcess` describes the primary validation process for the target
*  `validation.lastCompleted` and `validation.nextScheduled` describe the last completed and next scheduled dates of validation for the target, respectively
*  `validation.failureAction` describes what happens if the validation fails

The resource also provides information about entities involved in the validation process:

`validation.primarySource` provides information about the primary source(s) the target is validated against
*  `source` and `sourceOrg` identify the primary source, and `sourceType` indicates what the primary source is
*  `sourceValidationProcess`, `sourceValidationStatus`, and `sourceValidationDate` describe validation of the target performed by the primary source.
*  `sourcePush` and `sourcePushType` indicate whether a primary source can push updates or alerts about the target (e.g. if a license board suspends a practitioner's license)

`validation.attestation` provides information about who submitted the information being validated
*  `attestationSource` identifies the individual attesting to information, `attestationOrg` identifies the organization attesting to information
*  In some cases, an indivudal my attest to information themself. In others, an entity may submit attested information on the individual's behalf. `attestationMethod` indicates who is providing the attested information
*  `attestationDate` indicates when the information was attested to
*  `sourceCert` and `proxyCert` assert the identity of the individual attesting to information and any proxy providing attested information on their behalf. `signedSourceAttestation` and `signedProxyRight` assert that information was attested to/provided by the entity with the right to do so.

`validation.validator` provides information about the entity performing the validation of the target
*  `validatorOrg` identifes the validating organization, and `validatorCert` asserts their identity
*  `signedValidatorAttestation` asserts that the validator has validated the target
*  `dateValidated` indicates when the validating organization validated the target

**Examples:**

The following are example uses for the vhdir-validation profile:

-  TBD


**Mandatory Data Elements**

The following data-elements are mandatory (i.e data MUST be present). These are presented below in a simple human-readable explanation. The [**Formal Profile Definition**](#profile) below provides the  formal summary, definitions, and  terminology requirements.  

Each validation resource must have:

1.  At least one target in `validation.target`
1.  One indication of the frequency with which the target must be validated in `validation.validationNeed`
1.  One indication of the last validation status of the target in `validation.validationStatus`
1.  One date/time on which the validation status was last updated in `validation.validationStatusDate`
1.  One indication of what the target is validated against in `validation.validationType`
1.  One indication of what happens if validation of the target fails in `validation.failureAction`
1.  For each primary source described:
    1.  One URI for the primary source in `validation.primarySource.source`
    1.  One reference to the organization resource for the primary source in `validation.primarySource.sourceOrg`
    1.  At least one type of primary source in `validation.primarySource.sourceType`
    1.  At least one indication of the primary source validation process in `validation.primarySource.sourceValidationProcess`
    1.  One indication of whether the primary source can push updates/alerts about the target in `validation.primarySource.sourcePush`
1.  For each attestation source described:
    1.  One individual that attested to the target information in `validation.attestation.attestationSource`
    1.  One method indicating who is providing the attested data in `validation.attestation.attestationMethod`
    1.  One date at which the target information was attested to in `validation.attestation.attestationDate`
1.  For each validator described:
    1.  One reference to the organization resource for the validator in `validation.validator.validatorOrg`
    1.  One date on which the validator validated the target information in `validation.validator.dateValidated`


**Profile specific implementation guidance:**

- TBD


**Extensions:**

There are no extensions to the validation resource.


**Terminology**

TBD