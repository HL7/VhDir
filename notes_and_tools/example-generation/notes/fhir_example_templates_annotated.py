#*******************************************************************************
# FHIR profile string templates for creating example data
#*******************************************************************************

#****************************organization_template******************************

organization_template = '''<Organization  xmlns="http://hl7.org/fhir"> <!-- synthetic organization -->

	<id value="{f_id}"/>

	<meta>
        <profile value="http://hl7.org/fhir/uv/vhdir/StructureDefinition/vhdir-organization"/>
    </meta>

    <identifier> <!-- NPI -->
        <extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/identifier-status">
            <valueCode value="active"/>
        </extension>
        <use value="official"/>
        <type>
            <coding>
                <system value="http://terminology.hl7.org/CodeSystem/v2-0203"/>
                <code value="PRN"/>
                <display value="Provider number"/>
            </coding>
            <text value="NPI"/>
        </type>
        <system value="http://hl7.org/fhir/sid/us-npi"/>
        <value value="{npi}"/>
        <period>
            <start value="2004-04-21T11:57:00-05:00"/> <!-- could randomize this-->
        </period>
        <assigner>
            <display value="CMS"/>
        </assigner>
    </identifier>

	<active value="true"/> <!-- This record is active could randomize this as well-->

	<type> <!-- This organization is a healthcare provider/hospital -->
        <coding>
            <system value="http://terminology.hl7.org/CodeSystem/organization-type"/>
            <code value="{prov_type_code}"/>
            <display value="{prov_type_display}"/>
        </coding>
        <text value="{prov_type_text}"/>
	</type>

	<name value="{name}"/>
	
<!-- todo add aliases
    <alias value="DC Memorial Hospital"> 
        <extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/org-alias-type">
            <valueCoding>
                <system value="http://hl7.org/fhir/uv/vhdir/CodeSystem/codesystem-organizationdemographics"/>
                <code value="historical"/>
                <display value="Historical"/>
            </valueCoding>
        </extension>
        <extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/org-alias-period">
            <valuePeriod>
                <start value="1975"/>
                <end value="2000"/>
            </valuePeriod>
        </extension>
    </alias>
-->

	<telecom> <!-- Contact information -->

		<!-- eh: todo add contactpoint 

	    <extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/contactpoint-viaintermediary">
            <valueReference>
                <reference value="{contactpoint_location_reference}"/>
                <display value="{contactpoint_location_reference_display}"/>
            </valueReference>
        </extension>
	    <extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/contactpoint-availabletime">
            <extension url="allDay">
                <valueBoolean value="true"/>
            </extension>
        </extension>
-->
        <!-- Extracted/copied from FFMH -->
        <system value="phone"/>
        <value value="{phone}"/><!-- todo format phone -->
	</telecom>

	<address>
	    <extension url="http://hl7.org/fhir/StructureDefinition/geolocation">
            <extension url="latitude">
                <valueDecimal value="{LAT}"/>
            </extension>
            <extension url="longitude">
                <valueDecimal value="{LON}"/>
            </extension>
        </extension>
        <use value="work"/>
        <type value="both"/>
        <text value="{address}, {city}, {state} {zip}"/>
        <line value="{address}"/>
        <city value="{city}"/>
        <state value="{state}"/>
        <postalCode value="{zip}"/>
        <country value="USA"/>
	</address>
	{partof}
    <contact> <!-- Describes contact information for administrative inquiries  TODO randomize this -->
        <purpose>
            <coding>
                <system value="http://terminology.hl7.org/CodeSystem/contactentity-type"/>
                <code value="ADMIN"/>
                <display value="Administrative"/>
            </coding>
        </purpose>
        <name>
            <use value="official"/>
            <text value="{contact_fname} {contact_lname}"/>
            <family value="{contact_lname}"/>
            <given value="{contact_fname}"/>
        </name>
        <telecom>
            <extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/contactpoint-availabletime"> 
                <extension url="daysOfWeek">
                    <valueCode value="mon"/>
                </extension>
                <extension url="daysOfWeek">
                    <valueCode value="tue"/>
                </extension>
                <extension url="daysOfWeek">
                    <valueCode value="wed"/>
                </extension>
                <extension url="daysOfWeek">
                    <valueCode value="thu"/>
                </extension>
                <extension url="daysOfWeek">
                    <valueCode value="fri"/>
                </extension>
                <extension url="availableStartTime">
                    <valueTime value="07:00:00"/>
                </extension>
                <extension url="availableEndTime">
                    <valueTime value="18:00:00"/>
                </extension>
            </extension>
            <system value="phone"/>
            <value value="{phone}"/> <!-- for now is the same as above-->
            <use value="work"/>
        </telecom>
        <address> <!-- for now is the same as above-->
					    <extension url="http://hl7.org/fhir/StructureDefinition/geolocation">
				            <extension url="latitude">
				                <valueDecimal value="{LAT}"/>
				            </extension>
				            <extension url="longitude">
				                <valueDecimal value="{LON}"/>
				            </extension>
				        </extension>
				        <use value="work"/>
				        <type value="both"/>
				        <text value="{address}, {city}, {state} {zip}"/>
				        <line value="{address}"/>
				        <city value="{city}"/>
				        <state value="{state}"/>
				        <postalCode value="{zip}"/>
				        <country value="USA"/>
					</address>    </contact>

    <endpoint> <!-- A reference to an electronic endpoint -->
        <reference value="Endpoint/{f_id}-direct"/>
        <display value="{name} Direct address"/>
    </endpoint>

</Organization>'''


partof_org_template ='''
	<partOf>
		<!-- eh:  randomize whether belong to King Hospital System, Acme Healthcare or Blue Hope or none -->
		<reference value="Organization/vhdir-organization-{partof_org_npi}"/>
		<display value="{partof_org}"/>
	</partOf>'''

#*******************************practitioner_template***************************


practitioner_template ='''<Practitioner xmlns="http://hl7.org/fhir">
	<!-- synthetic practitioner -->
	
	<id value="{f_id}"/>
	<meta>
		<versionId value="1"/>
		<profile value="http://hl7.org/fhir/uv/vhdir/StructureDefinition/vhdir-practitioner"/>
	</meta>
	
<!--*******************************

 A reference to the practitioner's personal electronic endpoint (independent of their role with an organization)

url = 'type' Describes the practitioner's digital certificate. In this case, an identity certificate used for digitally signing, associated with the DirectTrust framework

************************************

	<extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/endpoint-reference">	
		<valueReference>
			<reference value="Endpoint/{f_id}-direct"/>
			<display value="{Type} {npi} Direct address"/>
		</valueReference>
	</extension>
	<extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/digitalcertificate">
		<extension url="type">
			<valueCoding>
				<system value="http://hl7.org/fhir/uv/vhdir/CodeSystem/codesystem-digitalcertificate"/>
				<code value="ind"/>
				<display value="Individual"/>
			</valueCoding>
		</extension>
		<extension url="use">
			<valueCoding>
				<system value="http://hl7.org/fhir/uv/vhdir/CodeSystem/codesystem-digitalcertificate"/>
				<code value="signing"/>
				<display value="Signing"/>
			</valueCoding>
		</extension>
		<extension url="certificateStandard">
			<valueCoding>
				<system value="http://hl7.org/fhir/uv/vhdir/CodeSystem/codesystem-digitalcertificate"/>
				<code value="x.509v3"/>
				<display value="x.509v3"/>
			</valueCoding>
		</extension>
		<extension url="certificate">
			<valueString value="TXkgbmFtZSBpcyBHZW9yZ2UgV2FzaGluZ3Rvbi4gVGhpcyBpcyBteSBjZXJ0aWZpY2F0ZS4gDQoNCi0tLS0tQkVHSU4gUFVCTElDIEtFWS0tLS0tDQpNSUdlTUEwR0NTcUdTSWIzRFFFQkFRVUFBNEdNQURDQmlBS0JnRkZLcjVGazJla2dYSjdwUXpKVzBWdm9NZzQ4DQpldk1DTUFTbk95M09rS1VyZlIwSGZHTmRUS216L3VpcWVjOGR3U1E5NFpKR3Njd3FzczVScmtYNkEzUHZsZmM3DQpkdlJNQlBxYzdsKzRrOHN5b2t4bzh4SW8vN0hLOE1kWW45dlhId1k5VWxGZDduRjZsbWN0Nzd3THMxNWdrZjN1DQpHVXErZ1RDV3hnZlYzbm05QWdNQkFBRT0NCi0tLS0tRU5EIFBVQkxJQyBLRVktLS0tLQ=="/>
		</extension>
		<extension url="expirationDate">
			<valueDate value="1970-09-03"/>
		</extension>
		<extension url="trustFramework">
			<valueCodeableConcept>
				<coding>
					<system value="http://hl7.org/fhir/uv/vhdir/CodeSystem/codesystem-digitalcertificate"/>
					<code value="direct"/>
					<display value="DirectTrust"/>
					<userSelected value="true"/>
				</coding>
			</valueCodeableConcept>
		</extension>
	</extension>
-->

<!--********************	e.g. The practitioner provides culturally competent care for a local Native American tribe, the Piscataway People *********


	<extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/accessibility">
		<valueCodeableConcept>
			<coding>
				<system value="http://hl7.org/fhir/uv/vhdir/CodeSystem/codesystem-accessibility"/>
				<code value="cultcomp"/>
				<display value="Cultural competence"/>
				<userSelected value="true"/>
			</coding>
			<text value="Coordinates care with tribal healers of the Piscataway People"/>
		</valueCodeableConcept>
	</extension>
	
-->
	<identifier>
		<!-- Practitioner's NPI number -->
		<extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/identifier-status">
			<valueCode value="active"/><!-- active  eh: check for deactive codes or randomize this -->
		</extension>
		<use value="official"/>
		<type>
			<coding>
				<system value="http://terminology.hl7.org/CodeSystem/v2-0203"/>
				<code value="PRN"/>
				<display value="Provider number"/>
				<userSelected value="true"/>
			</coding>
			<text value="NPI"/>
		</type>
		<system value="http://hl7.org/fhir/sid/us-npi"/>
		<value value="{npi}"/>
		<period>  <!--  EH: add more values and stop values to this -->
			<start value="2005-07-16T09:00:00-05:00"/>
		</period>
		<assigner>
			<display value="CMS"/>
		</assigner>
	</identifier>
	
	<active value="{active}"/> 
	<!-- This record is active  eh: randomize this -->
	<name>

		<use value="official"/>
		<text value="{fname} {lname}"/>
		<family value="{lname}"/>
		<given value="{fname}"/>
		<suffix value="{sname}"/>
	</name>
	<telecom>
		<!-- max of two-->
		<system value="phone"/>
		<value value="{phone0}"/> <!-- eh: todo format phone -->
		<use value="work"/>
		<rank value="1"/>
	</telecom>
	<telecom>
		<!-- Practitioner's phone max of two-->
		<system value="phone"/>
		<value value="{phone1}"/> <!-- eh: todo format phone -->
		<use value="work"/>
		<rank value="2"/>
	</telecom>
	<address>
	<extension url="http://hl7.org/fhir/StructureDefinition/geolocation">
		<extension url="latitude">
				<valueDecimal value="{LAT}"/>
		</extension>
		<extension url="longitude">
				<valueDecimal value="{LON}"/>
		</extension>
		</extension>
		<use value="home"/>
		<type value="both"/> <!-- eh:  todo make this a choice -->
		<text value="{address}, {city}, {state} {zip}"/>
		<line value="{address}"/>
		<city value="{city}"/>
		<state value="{state}"/>
		<postalCode value="{zip}"/>
		<country value="USA"/>
<!--  EH: todo add this in
		<period>
			<start value="1932-02-22"/> 
		</period>
	-->
	</address>
	<gender value="{gender}"/>
	<birthDate value="1964-06-19"/> <!--eh: do we need this -->
	
	{qualification} <!-- repeating qualification element -->
	{communication} <!-- repeating qualification element -->
	</Practitioner>'''
#*************************practitioner_communication_template*******************
practitioner_comm_template =[
	'''<communication>
		<!-- eh: todo
			<extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/communication-proficiency">
			<valueCodeableConcept>
				<coding>
					<code value="5"/>
					<display value="Native or bilingual proficiency"/>
					<userSelected value="true"/>
				</coding>
			</valueCodeableConcept>
		</extension> -->
		<coding>
			<system value="urn:ietf:bcp:47"/>
			<code value="en"/>
			<display value="English"/>
			<userSelected value="true"/>
		</coding> 
		<text value="English"/>
	</communication>''',
	'''<communication>
			<!-- eh: todo
				<extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/communication-proficiency">
				<valueCodeableConcept>
		<coding>
			<system value="urn:ietf:bcp:47"/>
			<code value="en"/>
			<display value="English"/>
			<userSelected value="true"/>
		</coding> 
				</valueCodeableConcept>
			</extension> -->
		<coding>
			<system value="urn:ietf:bcp:47"/>
			<code value="es"/>
			<display value="Spanish"/>
			<userSelected value="true"/>
		</coding> 
			<text value="English and Spanish"/>
		</communication>
		<communication>
			<!-- eh: todo
				<extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/communication-proficiency">
				<valueCodeableConcept>
					<coding>
						<code value="5"/>
						<display value="Native or bilingual proficiency"/>
						<userSelected value="true"/>
					</coding>
				</valueCodeableConcept>
			</extension> -->
			<coding>
				<system value="urn:ietf:bcp:47"/>
				<code value="{communication_code}"/>
				<display value="{communication_display}"/>
				<userSelected value="true"/>
			</coding> 
			<text value="{communication_display}"/>
		</communication>'''
			]

	
#*************************practitioner_qual_template****************************
	
practitioner_qual_template = '''<qualification> 
		<extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/practitioner-qualification">
			
			<!-- the license is currently active and valid  eh: randomize this and make max of two -->
			<extension url="status">
				<valueCoding>
					<system value="http://hl7.org/fhir/resource-status"/>
					<code value="active"/>
					<display value="active"/>
				</valueCoding>
				
			</extension>
			<extension url="whereValid">
				<valueCodeableConcept>
					<coding>
						<system value="https://www.usps.com/"/>
						<code value="{license_state}"/>
						<display value="{license_state_display}"/>
						<userSelected value="true"/>
					</coding>
					<text value="{license_state_display}"/>
				</valueCodeableConcept>
			</extension>
		</extension>
		<identifier>
			<!-- eh: tdo make max of two -->
			<extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/identifier-status">
				<valueCode value="active"/> <!-- This record is active  eh: randomize this -->
			</extension>
			<use value="official"/>
			<type>
				<text value="Medical License number"/>
			</type>
			<system value="{license_system}"/> <!-- This is made up for now ... will need to research  -->
			<value value="{med_license}"/>
			<period>
				<start value="2018-06-19"/>  <!-- ask how to create these...can randomize -->
				<end value="2021-06-19"/>
			</period>
			<assigner>
				<display value="{license_assigner}"/>
			</assigner>
		</identifier>
		<code>
			<coding>
				<system value="{qual_code_system}"/>
				<code value="{qual_code}"/>
				<display value="{qual_code_display}"/>
				<userSelected value="true"/>
			</coding>
			<text value="{qual_code_display}"/>
		</code>
		<!--  eh: todo later ... discuss
		<period>
			<start value="2018-01-01"/>
			<end value="2020-01-01"/>
		</period>
		<issuer>
			<display value="http://qual_issuer"/>
		</issuer>
		-->
	</qualification>'''

#***********************location_templates******************************


location_template = '''
<Location xmlns="http://hl7.org/fhir">
	<id value="{f_id}"/>
	<meta>
		<profile value="http://hl7.org/fhir/uv/vhdir/StructureDefinition/vhdir-location"/>
	</meta>
	<extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/accessibility">
		<!-- Indicates that this location is handicap accessible and can provide assistance to persons with disabilities -->
		<valueCodeableConcept>
			<coding>
				<system value="http://hl7.org/fhir/uv/vhdir/CodeSystem/accessibility"/>
				<code value="handiaccess"/>
				<display value="handicap accessible"/>
			</coding>
			<text value="Offers a variety of services and programs for persons with disabilities"/>
		</valueCodeableConcept>
	</extension>
	<!-- eh: hold off on this for now
			
			E.g., This location uses the Revolutionary Professional EHR v10.4.3. The EHR product is certified to the 2014 Edition requirements. The product includes a patient portal.

	<extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/ehr">
		<extension url="developer">
			<valueString value="Revolutionary Health"/>
		</extension>
		<extension url="product">
			<valueString value="Revolutionary Professional EHR"/>
		</extension>
		<extension url="version">
			<valueString value="10.4.3"/>
		</extension>
		<extension url="certificationEdition">
			<valueCoding>
				<system value="http://hl7.org/fhir/uv/vhdir/CodeSystem/codesystem-ehrcharacteristics"/>
				<code value="2014"/>
				<display value="ONC 2014 Certification"/>
			</valueCoding>
		</extension>
		<extension url="patientAccess">
			<valueCodeableConcept>
				<coding>
					<system value="http://hl7.org/fhir/uv/vhdir/CodeSystem/codesystem-ehrcharacteristics"/>
					<code value="portal"/>
					<display value="patient portal"/>
				</coding>
			</valueCodeableConcept>
		</extension>
		<extension url="certificationID">
			<valueString value="04282014-1111-2"/>
		</extension>
	</extension>
-->
	<extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/newpatients">
		<extension url="acceptingPatients">
			<valueBoolean value="true"/>
		</extension>
		<extension url="acceptingPatients">
			<valueReference>
				<!-- <reference value="Organization/vhdir-network-{npi}"/>  eh: todo -->
				<display value="Acme Insurance Co"/>
			</valueReference>
		</extension>
	</extension>
	<extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/newpatients">
		<extension url="acceptingPatients">
			<valueBoolean value="true"/>
		</extension>
		<extension url="acceptingPatients">
			<valueReference>
				<!-- <reference value="Organization/vhdir-network-{npi}"/>  eh: todo -->
				<display value="Persona"/>
			</valueReference>
		</extension>
	</extension>
	<extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/newpatients">
		<extension url="acceptingPatients">
			<valueBoolean value="true"/>
		</extension>
		<extension url="acceptingPatients">
			<valueReference>
				<!-- <reference value="Organization/vhdir-network-{npi}"/>  eh: todo -->
				<display value="Green Circle"/>
			</valueReference>
		</extension>
	</extension>
	<extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/newpatientprofile">
		<valueString value="This location accepts all types of patients"/>
	</extension>
	<!--  eh: todo 
	<extension> url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/usage-restriction">
		<valueReference>
				<reference value="#vhdir-restriction-{npi}"/> 
				<display value="usage restriction"/>
		</valueReference>	
	</extension>
-->
	<identifier>
		<extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/identifier-status">
			<valueCode value="active"/>
		</extension>
		<use value="secondary"/>
		<system value="{location_identifier_system}"/>
		<value value="main campus"/>
		<!-- eh: randomize this too -->
		<assigner>
			<reference value="Organization/vhdir-organization-{npi}"/>
			<display value="{name}"/>
		</assigner>
	</identifier>
	<status value="active"/>
	<!--eh: todo randomize this-->
	<name value="{name}"/>
	<description value="Main campus of {name}"/>
	<type>
		<!-- mapped from Taxonomy Code -->
		<coding>
			<system value="http://www.wpc.edi.com/taxonomy"/>
			<code value="{type_code}"/>
			<display value="{type_code_display}"/>
			<userSelected value="true"/>
		</coding>
	</type>
	<telecom>
		<extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/contactpoint-availabletime">
			<extension url="allDay">
				<valueBoolean value="true"/>
			</extension>
		</extension>
		<system value="phone"/>
		<value value="{phone}"/>
		<use value="work"/>
		<rank value="1"/>
	</telecom>
	<address>
		<use value="work"/>
		<type value="both"/>
		<text value="{address}, {city}, {state} {zip}"/>
		<line value="{address}"/>
		<city value="{city}"/>
		<state value="{state}"/>
		<postalCode value="{zip}"/>
		<country value="USA"/>
	</address>
	<!-- eh: hold off since not easy to discern this from NPPESS data,  e.g.,	a collection of buildings or other locations such as a site or a campus 
	<physicalType>
		<coding>
			<system value="http://terminology.hl7.org/CodeSystem/location-physical-type"/>
			<code value="si"/>
			<display value="Site"/>
			<userSelected value="true"/>
		</coding>
	</physicalType>
-->
	<position>
		<!-- Coordinates of this location -->
		<longitude value="{LON}"/>
		<latitude value="{LAT}"/>
	</position>
	<managingOrganization>
		<!-- eh: link to org -->
		<reference value="Organization/vhdir-organization-{npi}"/>
		<display value="{name}"/>
	</managingOrganization>
	<hoursOfOperation>
		<!-- This location is always open -->
		<daysOfWeek value="mon"/>
		<daysOfWeek value="tue"/>
		<daysOfWeek value="wed"/>
		<daysOfWeek value="thu"/>
		<daysOfWeek value="fri"/>
		<daysOfWeek value="sat"/>
		<daysOfWeek value="sun"/>
		<allDay value="true"/>
	</hoursOfOperation>
	<availabilityExceptions value="visiting hours from 6:00 am - 10:00 pm"/>
	<endpoint>
		<!-- A reference to an electronic endpoint -->
		<reference value="Endpoint/{f_id}-direct"/>
		<display value="{name} Direct address"/>
	</endpoint>
</Location>'''


#***********************HealthcareService_templates********************

healthcareservice_template ='''<HealthcareService xmlns="http://hl7.org/fhir">
  <id value="{f_id}"/>
  <meta>
    <profile value="http://hl7.org/fhir/uv/vhdir/StructureDefinition/vhdir-healthcareservice"/>
  </meta>
	
<!-- eh:todo
  <extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/newpatients">
    <extension url="acceptingPatients">
      <valueBoolean value="true"/>
    </extension>
    <extension url="network">
      <valueReference>
        <reference value="Organization/patriotppo"/>
        <display value="Patriot Preferred Provider Network"/>
      </valueReference>
    </extension>
  </extension>
-->
  <identifier>
    <extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/identifier-status">
      <valueCode value="active"/>
    </extension>
    <use value="secondary"/>
    <type>
      <coding>
        <system value="http://terminology.hl7.org/CodeSystem/v2-0203"/>
        <code value="PRN"/>
      </coding>
      <text value="Healthcare Service Number"/>
    </type>
    <system value="{identifier_system}"/>
    <value value="{identifier_value}"/>
    <assigner>
      <reference value="Organization/vhdir-organization-{npi}"/>
      <display value="{name}"/>
    </assigner>
  </identifier>
	
  <active value="true"/><!--eh: todo randomize this-->
	
  <providedBy>
		<reference value="Organization/vhdir-org-{npi}"/>
		<display value="{name}"/>
  </providedBy>
	
<!--	eh : todo align with organization_type
  <category>
    <coding>
      <system value="http://terminology.hl7.org/CodeSystem/service-category"/>
      <code value="35"/>
      <display value="Hospital"/>
    </coding>
  </category>
-->

  <type>
<!-- eh: todo: map NUCC to service code: simple text for now
    <coding>
      <system value="http://hl7.org/fhir/ValueSet/service-type"/>
      <code value="hcs_type_code"/>
      <display value="hcs_type_display"/>
    </coding>
	-->
		<text value="{HCS_Name}"/>
  </type>

{specialty} 	<!-- eh: random list of 5-10 nucc for each to specialty codes : simple text for now -->

  <location>
    <reference value="Location/vhdir-location-{npi}"/>
    <display value="{name}"/>
  </location>

  <name value="{name} {HCS_Name} Services"/>

  <comment value="{service_list}"/> <!-- from services list-->

  <telecom>
		<!--  eh: todo
    <extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/contactpoint-viaintermediary">
      <valueReference>
        <reference value="Location/vhdir-location-{npi}"/>
        <display value="{name}"/>
      </valueReference>
    </extension>
	-->
	<system value="phone"/>
	<value value="{phone}"/>
	<use value="work"/>
	<rank value="1"/>
  </telecom>
	
  <serviceProvisionCode>
    <!-- Fees apply for this service -->
    <coding>
      <system value="http://terminology.hl7.org/CodeSystem/service-provision-conditions"/>
      <code value="cost"/>
      <display value="Fees apply"/>
    </coding>
  </serviceProvisionCode>
	
  <!--		<eligibility>
  <code>-->
    <!-- There are no eligibility requirements for this service -->
    <!--		<text value="None"/>
  </code>
  <comment value="No specific eligibility requirements"/>
</eligibility>-->

<referralMethod>
  <!-- this service accepts referrals via phone -->
  <coding>
    <system value="http://terminology.hl7.org/CodeSystem/service-referral-method"/>
    <code value="phone"/>
    <display value="phone"/>
  </coding>
</referralMethod>
<referralMethod>
  <!-- and via fax -->
  <coding>
    <system value="http://terminology.hl7.org/CodeSystem/service-referral-method"/>
    <code value="fax"/>
    <display value="Fax"/>
  </coding>
</referralMethod>

<appointmentRequired value="true"/>
<!-- An appointment is required for this service -->

<availableTime>
  <!-- This service is available Mon-Fri, 8:00 am - 6:00 pm -->
  <daysOfWeek value="mon"/>
  <daysOfWeek value="tue"/>
  <daysOfWeek value="wed"/>
  <daysOfWeek value="thu"/>
  <daysOfWeek value="fri"/>
  <allDay value="false"/>
  <availableStartTime value="08:00:00"/>
  <availableEndTime value="18:00:00"/>
</availableTime>

<!-- eh:todo
<availabilityExceptions value="No interventional cardiac procedures are scheduled on Wednesdays"/>
-->

<endpoint>
	<reference value="Endpoint/{f_id}-direct"/>
  <display value="Direct address for {name} {HCS_Name} Service"/>
</endpoint>
</HealthcareService>'''

hcs_specialty_template ='''<specialty>
	<coding>
		<system value="http://nucc.org/provider-taxonomy"/>
		<code value="{specialty_code}"/>
		<display value="{specialty_display}"/>
	</coding>
	<text value="{specialty_display}"/>
</specialty>'''

#***********************practitionerrole_templates******************************


practitionerrole_template = '''
<PractitionerRole xmlns="http://hl7.org/fhir">
	<id value="{f_id}"/> <!-- eh: one role per practitioner to start use nppes to give second role based on taxonomy_codes -->
	
	<meta>
		<profile value="http://hl7.org/fhir/uv/vhdir/StructureDefinition/vhdir-practitionerrole"/>
	</meta>
	
	<!-- eh:todo
	e.g.,Dr. Washington is a member of the Patriot PPO insurance network in this role

	<extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/network-reference">
		<valueReference>
			<reference value="Organization/patriotppo"/>
			<display value="Patriot Preferred Provider Network"/>
		</valueReference>
	</extension>
-->
<!-- eh:todo
e.g.,	An x.509v3 digital identity certificate associated with Dr. Washington


	<extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/digitalcertificate">
		<extension url="type">
			<valueCoding>
				<system value="http://hl7.org/fhir/uv/vhdir/CodeSystem/codesystem-digitalcertificate"/>
				<code value="ind"/>
				<display value="Individual"/>
			</valueCoding>
		</extension>
		<extension url="use">
			<valueCoding>
				<system value="http://hl7.org/fhir/uv/vhdir/CodeSystem/codesystem-digitalcertificate"/>
				<code value="signing"/>
				<display value="Signing"/>
			</valueCoding>
		</extension>
		<extension url="certificateStandard">
			<valueCoding>
				<system value="http://hl7.org/fhir/uv/vhdir/CodeSystem/codesystem-digitalcertificate"/>
				<code value="x.509v3"/>
				<display value="x.509v3"/>
			</valueCoding>
		</extension>
		<extension url="certificate">
			<valueString value="TXkgbmFtZSBpcyBHZW9yZ2UgV2FzaGluZ3Rvbi4gVGhpcyBpcyBteSBjZXJ0aWZpY2F0ZS4gDQoNCi0tLS0tQkVHSU4gUFVCTElDIEtFWS0tLS0tDQpNSUdlTUEwR0NTcUdTSWIzRFFFQkFRVUFBNEdNQURDQmlBS0JnRkZLcjVGazJla2dYSjdwUXpKVzBWdm9NZzQ4DQpldk1DTUFTbk95M09rS1VyZlIwSGZHTmRUS216L3VpcWVjOGR3U1E5NFpKR3Njd3FzczVScmtYNkEzUHZsZmM3DQpkdlJNQlBxYzdsKzRrOHN5b2t4bzh4SW8vN0hLOE1kWW45dlhId1k5VWxGZDduRjZsbWN0Nzd3THMxNWdrZjN1DQpHVXErZ1RDV3hnZlYzbm05QWdNQkFBRT0NCi0tLS0tRU5EIFBVQkxJQyBLRVktLS0tLQ=="/>
		</extension>
		<extension url="expirationDate">
			<valueDate value="1970-09-03"/>
		</extension>
		<extension url="trustFramework">
			<valueCodeableConcept>
				<coding>
					<system value="http://hl7.org/fhir/uv/vhdir/CodeSystem/codesystem-digitalcertificate"/>
					<code value="direct"/>
					<display value="DirectTrust"/>
					<userSelected value="true"/>
				</coding>
			</valueCodeableConcept>
		</extension>
	</extension>
-->

<!-- eh:todo e.g.,Dr. Washington is accepting new patients with health plans associated with the Patriot PPO

	<extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/newpatients">
		<extension url="acceptingPatients">
			<valueBoolean value="true"/>
		</extension>
		<extension url="network">
			<valueReference>
				<reference value="Organization/patriotppo"/>
				<display value="Patriot Preferred Provider Network"/>
			</valueReference>
		</extension>
	</extension>
-->

<!-- eh:todo e.g., Describes conditions under which Dr. Washington is accepting new patients in this role 

	<extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/newpatientprofile">
		<valueString value="New patients are accepted via referral from providers participating in Patriot PPO"/>
	</extension>
-->

<!-- eh:todo e.g.,Information about Dr. Washington's registration w/the DEA to prescribe controlled substances at this location

	<extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/qualification">
		<extension url="identifier">
			<valueIdentifier>
				<use value="official"/>
				<type>
					<coding>
						<system value="http://terminology.hl7.org/CodeSystem/v2-0203"/>
						<code value="PRN"/>
						<display value="Provider number"/>
					</coding>
					<text value="DEA Registration Number"/>
				</type>
				<system value="https://www.deadiversion.usdoj.gov/"/>
				<value value="CW1234563"/>
				<period>
					<start value="2016-02-26"/>
					<end value="2019-02-26"/>
				</period>
				<assigner>
					<identifier>
						<value value="US Drug Enforcement Administration (DEA)"/>
					</identifier>
					<display value="US Drug Enforcement Administration (DEA)"/>
				</assigner>
			</valueIdentifier>
		</extension>
		<extension url="code">
			<valueCodeableConcept>
				<text value="DEA Registration Number"/>
			</valueCodeableConcept>
		</extension>
		<extension url="issuer">
			<valueReference>
				<identifier>
					<value value="US Drug Enforcement Administration (DEA)"/>
				</identifier>
				<display value="US Drug Enforcement Administration (DEA)"/>
			</valueReference>
		</extension>
		<extension url="status">
			<valueCoding>
				<system value="http://hl7.org/fhir/resource-status"/>
				<code value="active"/>
				<display value="active"/>
			</valueCoding>
		</extension>
		<extension url="period">
			<valuePeriod>
				<start value="2016-02-26"/>
				<end value="2019-02-26"/>
			</valuePeriod>
		</extension>
	</extension>
-->

	<identifier>
		
		<extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/identifier-status">
			<valueCode value="active"/>
		</extension>
		
		<use value="secondary"/>
		<type>
			<coding>
				<system value="http://terminology.hl7.org/CodeSystem/v2-0203"/>
				<code value="PRN"/>
				<display value="Provider number"/>
			</coding>
			<text value="Hospital ID"/>
		</type>
		<system value="{identifier_system}"/><!-- create from assigned org -->
		<value value="{identifier_value}"/><!--grab PRN or create one-->
		<period>
			<start value="2016-02-22"/><!-- randomize-->
		</period>
	<!--eh: todo
		<assigner>
			<reference value="{identifier_assigner}"/>
			<display value="{identifier_assigner_display}"/>
		</assigner>
	-->
	</identifier>
	
	<active value="true"/>
	<period>
		<start value="2016-02-22"/><!--eh: should the same identifier period randomize -->
	</period>
	
	<practitioner>
		<!-- George Washington -->
		<reference value="Practitioner/vhdir-practitioner-{pract_npi}"/><!--baed on practitioner-->
		<display value="{fname} {lname}"/>
	</practitioner>
	
	<organization>
		<!-- Founding Fathers Memorial Hospital -->
		<reference value="Organization/vhdir-organization-{org_npi}"/><!--randomly assign to o based on lat lon or zip - get org list by zip-->
		<display value="{org_name}"/>
	</organization>
	
	<code>
		<coding>
			<system value="http://www.wpc.edi.com/taxonomy"/>
			<code value="{type_code}"/><!-- use nucc_role mapping codes? add second or third if present?-->
			<display value="{type_code_display}"/>
		</coding>
	</code>
	<specialty>
		<coding>
			<system value="http://www.wpc.edi.com/taxonomy"/>	<!-- use nucc  specialty_displayn maps-->
			<code value="{specialty_code}"/>
			<display value="{specialty_display}"/>
		</coding>
	</specialty>
	<location>
		<reference value="Location/vhdir-location-{org_npi}"/>
		<display value="{org_name}"/>
	</location>
	<healthcareService>
		<reference value="HealthcareService/vhdir-{hcs_code}-healthcareservice-{org_npi}"/>
		<display value="{org_name} {HCS_Name} Healthcare Service"/>
	</healthcareService>
	<telecom>
		<!-- 
		<extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/contactpoint-viaintermediary">
			<valueReference>
				<reference value="Location/loc-ffmh-hvi"/>
				<display value="Founding Fathers Memorial Hospital, Heart and Vascular Institute"/>
			</valueReference>
		</extension>
	-->

		<system value="phone"/>
		<value value="{location_phone}"/>
	</telecom>
	
	<availableTime>
		<daysOfWeek value="mon"/>
		<daysOfWeek value="tue"/>
		<daysOfWeek value="wed"/>
		<daysOfWeek value="thu"/>
		<availableStartTime value="09:00:00"/>
		<availableEndTime value="12:00:00"/>
	</availableTime>
	
	<endpoint>
		<reference value="Endpoint/{f_id}-direct"/>
	  <display value="Direct address for {fname} {lname} {type_code_display} Role"/>
	</endpoint>
	
</PractitionerRole>
'''

#***********************Pract Role for network member******************************

practitionerrole_network_template = '''
<PractitionerRole xmlns="http://hl7.org/fhir">
 <!-- synthetic practitionerrole for healthcare provider in network -->

	<id value="{f_id}"/> 
	
	<meta>
		<profile value="http://hl7.org/fhir/uv/vhdir/StructureDefinition/vhdir-practitionerrole"/>
	</meta>
	
	<identifier>
		
		<extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/identifier-status">
			<valueCode value="active"/>
		</extension>
		
		<use value="secondary"/>
		<type>
			<coding>
				<system value="http://terminology.hl7.org/CodeSystem/v2-0203"/>
				<code value="PRN"/>
				<display value="Provider number"/>
			</coding>
			<text value="Network Provider ID"/>
		</type>
		<system value="{identifier_system}"/>  # urlify
		<value value="{identifier_value}"/> # get_prov_identifier randomly assigned numeric number
		<period>
			<start value="2016-02-22"/>
		</period>
	</identifier>
	
	<active value="true"/>
	<period>
		<start value="2016-02-22"/>
	</period>
	
	<practitioner>
		<reference value="Practitioner/vhdir-practitioner-{pract_npi}"/>
		<display value="{fname} {lname}"/>
	</practitioner>

	<organization>
		<reference value="Organization/vhdir-organization-{org_npi}"/>
		<display value="{org_name}"/>
	</organization>

	<code>
<!-- no code for now ?
		<coding>
			<system value="http://nucc.org/provider-taxonomy"/>
			<code value="{type_code}"/>
			<display value="{type_code_display}"/>
		</coding>
		{addl_snomed_code_coding}
-->
	<text value="Provider Member"/>
	</code>
<!--
	<specialty>
		<coding>
			<system value="http://nucc.org/provider-taxonomy"/>
			<code value="{specialty_code}"/>
			<display value="{specialty_display}"/>
		</coding>
		{addl_snomed_specialty_coding}
	</specialty>
	{addl_specialty}
	<location>
		<reference value="Location/vhdir-location-{org_npi}"/>
		<display value="{org_name}"/>
	</location>
	<healthcareService>
		<reference value="HealthcareService/vhdir-{hcs_code}-healthcareservice-{org_npi}"/>
		<display value="{org_name} {HCS_Name} Healthcare Service"/>
	</healthcareService>
-->
	<telecom>

		<system value="phone"/>
		<value value="{location_phone}"/>
	</telecom>
<!--	
	<availableTime>
		<daysOfWeek value="mon"/>
		<daysOfWeek value="tue"/>
		<daysOfWeek value="wed"/>
		<daysOfWeek value="thu"/>
		<availableStartTime value="09:00:00"/>
		<availableEndTime value="12:00:00"/>
	</availableTime>
-->
	<endpoint>
		<reference value="Endpoint/{f_id}-direct"/>
	  <display value="Direct address for {fname} {lname} Network Member Role"/>
	</endpoint>
	
</PractitionerRole>'''



#***********************bundle_templates******************************

batch_bundle_template = '''<Bundle xmlns="http://hl7.org/fhir">
<id value="vhdir-{type}-examples-bundle"/>
 <type value="batch"/>
 <timestamp value="{timestamp}"/>
 {entries}
</Bundle>'''

entries_templ='''<entry>
 <fullUrl value="{server_path}/{f_id}"/><!-- 0..1 URI for resource (Absolute URL server address or URI for UUID/OID) -->
 <resource>{example}</resource>
 <request>  <!-- ?? 0..1 Additional execution information (transaction/batch/history) -->
  <method value="PUT"/>
  <url value="{Type}/{f_id}"/><!-- 1..1 URL for HTTP equivalent of this entry -->
 </request>
</entry>'''