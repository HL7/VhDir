#*******************************************************************************
# FHIR profile string templates for creating example data
#*******************************************************************************

#****************************organization_template******************************

organization_template = '''<Organization  xmlns="http://hl7.org/fhir"> <!-- synthetic organization -->

	<id value="{f_id}"/>

	<meta>
        <profile value="http://hl7.org/fhir/uv/vhdir/StructureDefinition/vhdir-organization"/>
    </meta>

    <identifier> <!-- NPI  or NIPI-->
        <extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/identifier-status">
            <valueCode value="active"/>
        </extension>
        <use value="official"/>
        <type>
            <coding>
                <system value="http://terminology.hl7.org/CodeSystem/v2-0203"/>
                <code value="{identifier_type_code}"/>
                <display value="{identifier_type_display}"/>
            </coding>
            <text value="{identifier_type_text}"/>
        </type>
        <system value="http://hl7.org/fhir/sid/us-npi"/>
        <value value="{npi}"/>
        <period>
            <start value="2004-04-21T11:57:00-05:00"/>
        </period>
        <assigner>
            <display value="Centers for Medicare and Medicaid Services"/>
        </assigner>
    </identifier>

	<active value="true"/>

	<type>
        <coding>
            <system value="{prov_type_system}"/>
            <code value="{prov_type_code}"/>
            <display value="{prov_type_display}"/>
        </coding>
        <text value="{prov_type_text}"/>
	</type>

	<name value="{name}"/>
	

	<telecom>
        <system value="phone"/>
        <value value="{phone}"/>
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
    <contact> 
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
            <value value="{phone}"/> 
            <use value="work"/>
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
					</address>    </contact>

    <endpoint>
        <reference value="Endpoint/{f_id}-direct"/>
        <display value="{name} Direct address"/>
    </endpoint>

</Organization>'''


partof_org_template ='''
	<partOf>
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
	<identifier>
		<extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/identifier-status">
			<valueCode value="active"/>
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
		<period> 
			<start value="2005-07-16T09:00:00-05:00"/>
		</period>
		<assigner>
			<display value="CMS"/>
		</assigner>
	</identifier>
	
	<active value="{active}"/> 
	<name>

		<use value="official"/>
		<text value="{fname} {lname}"/>
		<family value="{lname}"/>
		<given value="{fname}"/>
		<suffix value="{sname}"/>
	</name>
	<telecom>
		<system value="phone"/>
		<value value="{phone0}"/>
		<use value="work"/>
		<rank value="1"/>
	</telecom>
	<telecom>
		<system value="phone"/>
		<value value="{phone1}"/> 
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
		<type value="both"/>
		<text value="{address}, {city}, {state} {zip}"/>
		<line value="{address}"/>
		<city value="{city}"/>
		<state value="{state}"/>
		<postalCode value="{zip}"/>
		<country value="USA"/>
	</address>
	<gender value="{gender}"/>
	<birthDate value="1964-06-19"/> 
	
	{qualification} 
	{communication}
	</Practitioner>'''
#*************************practitioner_communication_template*******************
practitioner_comm_template =[
	'''<communication>
		<coding>
			<system value="urn:ietf:bcp:47"/>
			<code value="en"/>
			<display value="English"/>
			<userSelected value="true"/>
		</coding> 
		<text value="English"/>
	</communication>''',
	'''<communication>
		<coding>
			<system value="urn:ietf:bcp:47"/>
			<code value="es"/>
			<display value="Spanish"/>
			<userSelected value="true"/>
		</coding> 
			<text value="English and Spanish"/>
		</communication>
		<communication>
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
			<extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/identifier-status">
				<valueCode value="active"/> 
			</extension>
			<use value="official"/>
			<type>
				<text value="Medical License number"/>
			</type>
			<system value="{license_system}"/> 
			<value value="{med_license}"/>
			<period>
				<start value="2018-06-19"/>
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
	</qualification>'''

#***********************location_templates******************************


location_template = '''
<Location xmlns="http://hl7.org/fhir">
	<id value="{f_id}"/>
	<meta>
		<profile value="http://hl7.org/fhir/uv/vhdir/StructureDefinition/vhdir-location"/>
	</meta>
	<extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/accessibility">
		<valueCodeableConcept>
			<coding>
				<system value="http://hl7.org/fhir/uv/vhdir/CodeSystem/codesystem-accessibility"/>
				<code value="handiaccess"/>
				<display value="handicap accessible"/>
			</coding>
			<text value="Offers a variety of services and programs for persons with disabilities"/>
		</valueCodeableConcept>
	</extension>
	<extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/newpatients">
		<extension url="acceptingPatients">
			<valueBoolean value="true"/>
		</extension>
		<extension url="network">
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
		<extension url="network">
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
		<extension url="network">
			<valueReference>
				<!-- <reference value="Organization/vhdir-network-{npi}"/>  eh: todo -->
				<display value="Green Circle"/>
			</valueReference>
		</extension>
	</extension>
	<extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/newpatientprofile">
		<valueString value="This location accepts all types of patients"/>
	</extension>
	<identifier>
		<extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/identifier-status">
			<valueCode value="active"/>
		</extension>
		<use value="secondary"/>
		<system value="{location_identifier_system}"/>
		<value value="main campus"/>
		<assigner>
			<reference value="Organization/vhdir-organization-{npi}"/>
			<display value="{name}"/>
		</assigner>
	</identifier>
	<status value="active"/>
	<name value="{name}"/>
	<description value="Main campus of {name}"/>
	<type>
		<coding>
			<system value="http://nucc.org/provider-taxonomy"/>
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
	<position>
		<longitude value="{LON}"/>
		<latitude value="{LAT}"/>
	</position>
	<managingOrganization>
		<reference value="Organization/vhdir-organization-{npi}"/>
		<display value="{name}"/>
	</managingOrganization>
	<hoursOfOperation>
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
		<reference value="Endpoint/{f_id}-direct"/>
		<display value="{name} Direct address"/>
	</endpoint>
</Location>'''


#***********************HealthcareService_templates********************

healthcareservice_template ='''<HealthcareService xmlns="http://hl7.org/fhir">
 <!-- synthetic healthcareservice -->
  <id value="{f_id}"/>
  <meta>
    <profile value="http://hl7.org/fhir/uv/vhdir/StructureDefinition/vhdir-healthcareservice"/>
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
	
  <active value="true"/>
	
  <providedBy>
		<reference value="Organization/vhdir-org-{npi}"/>
		<display value="{name}"/>
  </providedBy>
	

  <type>
    <coding>
      <system value="http://{identifier_system}/service-types"/>
      <code value="{hcs_code}"/>
      <display value="{HCS_Name}"/>
    </coding>
		<text value="{HCS_Name}"/>
  </type>

{specialty} 

  <location>
    <reference value="Location/vhdir-location-{npi}"/>
    <display value="{name}"/>
  </location>

  <name value="{name} {HCS_Name} Services"/>

  <comment value="{service_list}"/> 

  <telecom>
	<system value="phone"/>
	<value value="{phone}"/>
	<use value="work"/>
	<rank value="1"/>
  </telecom>
	
  <serviceProvisionCode>
    <coding>
      <system value="http://terminology.hl7.org/CodeSystem/service-provision-conditions"/>
      <code value="cost"/>
      <display value="Fees apply"/>
    </coding>
  </serviceProvisionCode>

<referralMethod>
  <coding>
    <system value="http://terminology.hl7.org/CodeSystem/service-referral-method"/>
    <code value="phone"/>
    <display value="phone"/>
  </coding>
</referralMethod>
<referralMethod>
  <coding>
    <system value="http://terminology.hl7.org/CodeSystem/service-referral-method"/>
    <code value="fax"/>
    <display value="Fax"/>
  </coding>
</referralMethod>

<appointmentRequired value="true"/>

<availableTime>
  <daysOfWeek value="mon"/>
  <daysOfWeek value="tue"/>
  <daysOfWeek value="wed"/>
  <daysOfWeek value="thu"/>
  <daysOfWeek value="fri"/>
  <allDay value="false"/>
  <availableStartTime value="08:00:00"/>
  <availableEndTime value="18:00:00"/>
</availableTime>


<endpoint>
	<reference value="Endpoint/{f_id}-direct"/>
  <display value="Direct address for {name} {HCS_Name} Service"/>
</endpoint>
</HealthcareService>'''

#***********************hcs_specialty_template******************************


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
 <!-- synthetic practitionerrole -->

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
			<text value="Hospital ID"/>
		</type>
		<system value="{identifier_system}"/>
		<value value="{identifier_value}"/>
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
		<coding>
			<system value="http://nucc.org/provider-taxonomy"/>
			<code value="{type_code}"/>
			<display value="{type_code_display}"/>
		</coding>
		{addl_snomed_code_coding}
	</code>
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
	<telecom>

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

#***********************2nd_specialty_template******************************


addl_specialty_template = '''<specialty>
		<coding>
			<system value="http://nucc.org/provider-taxonomy"/>
			<code value="{specialty_code}"/>
			<display value="{specialty_display}"/>
		</coding>
		{addl_snomed_specialty_coding}
	</specialty>'''
	
#***********************addl_snomed_coding_template******************************

addl_snomed_coding_template = '''<coding>
			<system value="http://snomed.info/sct"/>
			<code value="{specialty_code}"/>
			<display value="{specialty_display}"/>
		</coding>'''

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
		<system value="{identifier_system}"/>
		<value value="{identifier_value}"/>
		<period>
			<start value="2016-02-22"/>
		</period>
	    <assigner>
	      <display value="{identifier_assigner_display}"/>
	    </assigner>
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
	<text value="Provider Member"/>
	</code>
	<telecom>
		<system value="phone"/>
		<value value="{location_phone}"/>
	</telecom>
	
	<endpoint>
		<reference value="Endpoint/{f_id}-direct"/>
	  <display value="Direct address for {fname} {lname} Network Member Role"/>
	</endpoint>
	
</PractitionerRole>'''

#****************

organizationrole_template = '''
<OrganizationAffiliation xmlns="http://hl7.org/fhir">
  <!--  describes the relationship between provider organization and network  -->
  <id value="{f_id}"/>
  
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
		<system value="{identifier_system}"/>
		<value value="{identifier_value}"/>
    <assigner>
      <display value="{identifier_assigner_display}"/>
    </assigner>
  </identifier>
  
  <active value="true"/>
  
  <organization>
		<reference value="Organization/vhdir-organization-{network_npi}"/>
		<display value="{network_name}"/>
	</organization>
  
  <participatingOrganization>
    <reference value="Organization/vhdir-organization-{org_npi}"/>
    <display value="{org_name}"/>
  </participatingOrganization>
  
  <code>
    <coding>
      <system value="http://hl7.org/fhir/organization-role"/>
      <code value="member"/>
      <display value="Member"/>
    </coding>
    <text value="Hospital Provider Member"/>
  </code>
  
  <endpoint>
		<reference value="Endpoint/{f_id}-direct"/>
	  <display value="Direct address for {org_name} Network Member Role"/>
	</endpoint>
</OrganizationAffiliation>'''



#***********************bundle_templates******************************

batch_bundle_template = '''<Bundle xmlns="http://hl7.org/fhir">
<id value="vhdir-{type}-examples-bundle"/>
 <type value="batch"/>
 <timestamp value="{timestamp}"/>
 {entries}
</Bundle>'''

entries_templ='''<entry>
 <fullUrl value="{server_path}/{f_id}"/>
 <resource>{example}</resource>
 <request> 
  <method value="PUT"/>
  <url value="{Type}/{f_id}"/>
 </request>
</entry>'''