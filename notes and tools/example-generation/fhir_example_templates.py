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
<!-- todo ownership links
    <partOf> 
        <reference value="Organization/mtvernon"/>
        <display value="Mount Vernon Health System"/>
    </partOf>
-->
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
        <reference value="Endpoint/vhdir-{type}-{npi}-direct"/>
        <display value="{name} Direct address"/>
    </endpoint>

</Organization>'''

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
			<reference value="Endpoint/vhdir-{type}-{npi}"/>
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
		<!-- Home address is 1600 Pennsylvania Ave NW, Washington, DC 20006, USA at latitude 38.897957 and longitude -77.036560 -->
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
			
			<!-- the license is currently active and valid in Washington, DC  eh: randomize this and make max of two -->
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
			<system value="https://doh.{small_state}.gov/bomed"/> <!-- This is made up for now ... will need to research  -->
			<value value="{med_license}"/>
			<period>
				<start value="2018-06-19"/>  # ask how to create these...can randomize
				<end value="2021-06-19"/>
			</period>
			<assigner>
				<display value="{license_state_display} Board of Medicine"/>
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