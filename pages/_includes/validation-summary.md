#### Complete Summary of the Mandatory Requirements

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