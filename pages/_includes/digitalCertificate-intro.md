An extension to describe digital certificates.

Consists of:
* `digitalCertificate.type` - indicates the type of digital certificate
* `digitalCertificate.use` - indicates the purpose of the digital certificate
* `digitalCertificate.certificateStandard` - indicates the certificate standard (currently only x.509v3 certificates are supported)
* `digitalCertificate.certificate` - the base64 encoding of the certificate
* `digitalCertificate.expirationDate` - indicates when the certificate expires
* `digitalCertificate.trustFramework` - indicates any trust frameworks supported by the certificate

digitalCertificate is an extension to the practitioner, organization, practitionerRole, and endpoint resources.