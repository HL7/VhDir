organization_template = '''
<Organization  xmlns="http://hl7.org/fhir"> <!-- synthetic organization -->

	<id value="vhdir-{prov_type}-{npi}"/>

	<meta>
        <profile value="http://hl7.org/fhir/uv/vhdir/StructureDefinition/vhdir-organization"/>
    </meta>

    <identifier> <!-- Founding Fathers Memorial Hospital NPI -->
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

	<name value="(name)"/> <!-- This organization is named Founding Fathers Memorial Hospital -->
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

	<telecom> <!-- Contact information for Founding Fathers can be found in the location resource for the hospital's main campus -->

		<!-- todo add contact

	    <extension url="http://hl7.org/fhir/uv/vhdir/StructureDefinition/contactpoint-viaintermediary">
            <valueReference>
                <reference value="Location/loc-ffmh"/>
                <display value="Founding Fathers Memorial Hospital"/>
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

	<address> <!-- Founding Fathers' address is 330 C Street SW, Washington, DC 20201, USA -->
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
            <text value="Abigail Adams"/>
            <family value="Adams"/>
            <given value="Abigail"/>
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

    <endpoint> <!-- A reference to an electronic endpoint for Founding Fathers -->
        <reference value="Endpoint/vhdir-{prov_type}-{npi}-direct"/>
        <display value="{name} Direct address"/>
    </endpoint>

</Organization>
'''