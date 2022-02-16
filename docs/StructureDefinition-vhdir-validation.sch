<?xml version="1.0" encoding="UTF-8"?>
<sch:schema xmlns:sch="http://purl.oclc.org/dsdl/schematron" queryBinding="xslt2">
  <sch:ns prefix="f" uri="http://hl7.org/fhir"/>
  <sch:ns prefix="h" uri="http://www.w3.org/1999/xhtml"/>
  <!-- 
    This file contains just the constraints for the profile VerificationResult
    It includes the base constraints for the resource as well.
    Because of the way that schematrons and containment work, 
    you may need to use this schematron fragment to build a, 
    single schematron that validates contained resources (if you have any) 
  -->
  <sch:pattern>
    <sch:title>f:VerificationResult</sch:title>
    <sch:rule context="f:VerificationResult">
      <sch:assert test="count(f:target) &gt;= 1">target: minimum cardinality of 'target' is 1</sch:assert>
      <sch:assert test="count(f:need) &gt;= 1">need: minimum cardinality of 'need' is 1</sch:assert>
      <sch:assert test="count(f:statusDate) &gt;= 1">statusDate: minimum cardinality of 'statusDate' is 1</sch:assert>
      <sch:assert test="count(f:validationType) &gt;= 1">validationType: minimum cardinality of 'validationType' is 1</sch:assert>
      <sch:assert test="count(f:validationProcess) &gt;= 1">validationProcess: minimum cardinality of 'validationProcess' is 1</sch:assert>
      <sch:assert test="count(f:failureAction) &gt;= 1">failureAction: minimum cardinality of 'failureAction' is 1</sch:assert>
      <sch:assert test="count(f:attestation) &gt;= 1">attestation: minimum cardinality of 'attestation' is 1</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult</sch:title>
    <sch:rule context="f:VerificationResult">
      <sch:assert test="not(parent::f:contained and f:contained)">If the resource is contained in another resource, it SHALL NOT contain nested Resources (inherited)</sch:assert>
      <sch:assert test="not(exists(for $id in f:contained/*/f:id/@value return $contained[not(parent::*/descendant::f:reference/@value=concat('#', $contained/*/id/@value) or descendant::f:reference[@value='#'])]))">If the resource is contained in another resource, it SHALL be referred to from elsewhere in the resource or SHALL refer to the containing resource (inherited)</sch:assert>
      <sch:assert test="not(exists(f:contained/*/f:meta/f:versionId)) and not(exists(f:contained/*/f:meta/f:lastUpdated))">If a resource is contained in another resource, it SHALL NOT have a meta.versionId or a meta.lastUpdated (inherited)</sch:assert>
      <sch:assert test="not(exists(f:contained/*/f:meta/f:security))">If a resource is contained in another resource, it SHALL NOT have a security label (inherited)</sch:assert>
      <sch:assert test="exists(f:text/h:div)">A resource should have narrative for robust management (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.meta</sch:title>
    <sch:rule context="f:VerificationResult/f:meta">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.implicitRules</sch:title>
    <sch:rule context="f:VerificationResult/f:implicitRules">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.language</sch:title>
    <sch:rule context="f:VerificationResult/f:language">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.text</sch:title>
    <sch:rule context="f:VerificationResult/f:text">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.extension</sch:title>
    <sch:rule context="f:VerificationResult/f:extension">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
      <sch:assert test="exists(f:extension)!=exists(f:*[starts-with(local-name(.), &quot;value&quot;)])">Must have either extensions or value[x], not both (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.modifierExtension</sch:title>
    <sch:rule context="f:VerificationResult/f:modifierExtension">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
      <sch:assert test="exists(f:extension)!=exists(f:*[starts-with(local-name(.), &quot;value&quot;)])">Must have either extensions or value[x], not both (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.target</sch:title>
    <sch:rule context="f:VerificationResult/f:target">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.targetLocation</sch:title>
    <sch:rule context="f:VerificationResult/f:targetLocation">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.need</sch:title>
    <sch:rule context="f:VerificationResult/f:need">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.status</sch:title>
    <sch:rule context="f:VerificationResult/f:status">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.statusDate</sch:title>
    <sch:rule context="f:VerificationResult/f:statusDate">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.validationType</sch:title>
    <sch:rule context="f:VerificationResult/f:validationType">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.validationProcess</sch:title>
    <sch:rule context="f:VerificationResult/f:validationProcess">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.frequency</sch:title>
    <sch:rule context="f:VerificationResult/f:frequency">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.lastPerformed</sch:title>
    <sch:rule context="f:VerificationResult/f:lastPerformed">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.nextScheduled</sch:title>
    <sch:rule context="f:VerificationResult/f:nextScheduled">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.failureAction</sch:title>
    <sch:rule context="f:VerificationResult/f:failureAction">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>f:VerificationResult/f:primarySource</sch:title>
    <sch:rule context="f:VerificationResult/f:primarySource">
      <sch:assert test="count(f:type) &gt;= 1">type: minimum cardinality of 'type' is 1</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.primarySource</sch:title>
    <sch:rule context="f:VerificationResult/f:primarySource">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.primarySource.extension</sch:title>
    <sch:rule context="f:VerificationResult/f:primarySource/f:extension">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
      <sch:assert test="exists(f:extension)!=exists(f:*[starts-with(local-name(.), &quot;value&quot;)])">Must have either extensions or value[x], not both (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.primarySource.modifierExtension</sch:title>
    <sch:rule context="f:VerificationResult/f:primarySource/f:modifierExtension">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
      <sch:assert test="exists(f:extension)!=exists(f:*[starts-with(local-name(.), &quot;value&quot;)])">Must have either extensions or value[x], not both (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.primarySource.who</sch:title>
    <sch:rule context="f:VerificationResult/f:primarySource/f:who">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.primarySource.type</sch:title>
    <sch:rule context="f:VerificationResult/f:primarySource/f:type">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.primarySource.communicationMethod</sch:title>
    <sch:rule context="f:VerificationResult/f:primarySource/f:communicationMethod">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.primarySource.validationStatus</sch:title>
    <sch:rule context="f:VerificationResult/f:primarySource/f:validationStatus">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.primarySource.validationDate</sch:title>
    <sch:rule context="f:VerificationResult/f:primarySource/f:validationDate">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.primarySource.canPushUpdates</sch:title>
    <sch:rule context="f:VerificationResult/f:primarySource/f:canPushUpdates">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.primarySource.pushTypeAvailable</sch:title>
    <sch:rule context="f:VerificationResult/f:primarySource/f:pushTypeAvailable">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>f:VerificationResult/f:attestation</sch:title>
    <sch:rule context="f:VerificationResult/f:attestation">
      <sch:assert test="count(f:who) &gt;= 1">who: minimum cardinality of 'who' is 1</sch:assert>
      <sch:assert test="count(f:communicationMethod) &gt;= 1">communicationMethod: minimum cardinality of 'communicationMethod' is 1</sch:assert>
      <sch:assert test="count(f:date) &gt;= 1">date: minimum cardinality of 'date' is 1</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.attestation</sch:title>
    <sch:rule context="f:VerificationResult/f:attestation">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.attestation.extension</sch:title>
    <sch:rule context="f:VerificationResult/f:attestation/f:extension">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
      <sch:assert test="exists(f:extension)!=exists(f:*[starts-with(local-name(.), &quot;value&quot;)])">Must have either extensions or value[x], not both (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.attestation.modifierExtension</sch:title>
    <sch:rule context="f:VerificationResult/f:attestation/f:modifierExtension">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
      <sch:assert test="exists(f:extension)!=exists(f:*[starts-with(local-name(.), &quot;value&quot;)])">Must have either extensions or value[x], not both (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.attestation.who</sch:title>
    <sch:rule context="f:VerificationResult/f:attestation/f:who">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.attestation.onBehalfOf</sch:title>
    <sch:rule context="f:VerificationResult/f:attestation/f:onBehalfOf">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.attestation.communicationMethod</sch:title>
    <sch:rule context="f:VerificationResult/f:attestation/f:communicationMethod">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.attestation.date</sch:title>
    <sch:rule context="f:VerificationResult/f:attestation/f:date">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.attestation.sourceIdentityCertificate</sch:title>
    <sch:rule context="f:VerificationResult/f:attestation/f:sourceIdentityCertificate">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.attestation.proxyIdentityCertificate</sch:title>
    <sch:rule context="f:VerificationResult/f:attestation/f:proxyIdentityCertificate">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.attestation.proxySignature</sch:title>
    <sch:rule context="f:VerificationResult/f:attestation/f:proxySignature">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.attestation.sourceSignature</sch:title>
    <sch:rule context="f:VerificationResult/f:attestation/f:sourceSignature">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.validator</sch:title>
    <sch:rule context="f:VerificationResult/f:validator">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.validator.extension</sch:title>
    <sch:rule context="f:VerificationResult/f:validator/f:extension">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
      <sch:assert test="exists(f:extension)!=exists(f:*[starts-with(local-name(.), &quot;value&quot;)])">Must have either extensions or value[x], not both (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.validator.modifierExtension</sch:title>
    <sch:rule context="f:VerificationResult/f:validator/f:modifierExtension">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
      <sch:assert test="exists(f:extension)!=exists(f:*[starts-with(local-name(.), &quot;value&quot;)])">Must have either extensions or value[x], not both (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.validator.organization</sch:title>
    <sch:rule context="f:VerificationResult/f:validator/f:organization">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.validator.identityCertificate</sch:title>
    <sch:rule context="f:VerificationResult/f:validator/f:identityCertificate">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>VerificationResult.validator.attestationSignature</sch:title>
    <sch:rule context="f:VerificationResult/f:validator/f:attestationSignature">
      <sch:assert test="@value|f:*|h:div">All FHIR elements must have a @value or children (inherited)</sch:assert>
    </sch:rule>
  </sch:pattern>
</sch:schema>
