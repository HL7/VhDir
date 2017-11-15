
## Definitions, Interpretations and Requirements common to all Validated Healthcare Directory  actors
{:.no_toc}

This section outlines important definitions and interpretations used in the Validated Healthcare Directory IG.
The conformance verbs used are defined in [FHIR Conformance Rules].

---

<!-- TOC  the css styling for this is \pages\assets\css\project.css under 'markdown-toc'-->
**Contents**

* Do not remove this line (it will not be displayed)
{:toc}

---

<!-- end TOC -->

| Date    | Comment/task                                                                              | Status      |
|---------|-------------------------------------------------------------------------------------------|-------------|  
| 11/6/17 | We need to discuss the level of detail we will have here. Dan will be adding              |             |
|         | general information                                                                       | In progress |
| mm/dd/yy| Next comment                                                                              | TBD         |

###  Validated Healthcare Directory 

The Validated Healthcare Directory is intended to provde an specification for the sharing of data from a validated dataset of data that supports a healthcare system and is maintained at a national level. The data is shared with organizations that in turn implement directories to satisfy their own, local requirements. 



### Must Support
In the context of Validated Healthcare Directory , *Must Support* on any data element SHALL be interpreted as follows:


* Validated Healthcare Directory Responders SHALL be capable of including the data element as part of the query results as specified by the [Validated Healthcare Directory Capability Statement].
* Validated Healthcare Directory Requestors SHALL be capable of processing resource instances containing the data elements without generating an error an causing the application to fail. In other words Validated Healthcare Directory Requestors SHOULD be capable of displaying the data elements for human use or storing it for other purposes.
* In situations where information on a particular data element is not present and the reason for absence is unknown, Validated Healthcare Directory Responders SHALL NOT include the data elements in the resource instance returned as part of the query results.
* When querying Validated Healthcare Directory Responders, Validated Healthcare Directory Requestors SHALL interpret missing data elements within resource instances as data not present in the Validated Healthcare Directory Responder's systems.
* In situations where information on a particular data element is missing and the Validated Healthcare Directory Responder knows the precise reason for the absence of data, Validated Healthcare Directory  Responders SHALL send the reason for the missing information using values (such as nullFlavors) from the value set where they exist or using the dataAbsentReason extension.
* Validated Healthcare Directory Requestors SHALL be able to process resource instances containing data elements asserting missing information.


* NOTE: Typically *Validated Healthcare Directory Responder* Actor = Server and *Validated Healthcare Directory Requestor Actor* = Client
* NOTE: Validated Healthcare Directory Responders who do not have the capability to store or return a data element tagged as Supported in Validated Healthcare Directory profiles can still claim conformance to the Validated Healthcare Directory profiles per the Validated Healthcare Directory conformance resources.
* NOTE: The above definition of Supported is derived from HL7v2 concept "Required but may be empty - RE" described in HL7v2 V28_CH02B_Conformance.doc.
* NOTE: Readers are advised to understand [FHIR Terminology] requirements, [FHIR RESTful API] based on the HTTP protocol, along with [FHIR Data Types], [FHIR Search] and [FHIR Resource] formats before implementing Validated Healthcare Directory  requirements.


### Overview of Validated Healthcare Directory - Resource Relationships 

### Practioner Role 

In the context of HcDir an Organization, at the highest level, is a “business entity”. This includes for profit and not-for profit organizations, educational institutions, governmental departments or programs, etc. Organization may be further defined though a hierarchical relationship of any number of levels. This can account for departments, divisions, or any other sub-unit of the higher level organization. Here, within the context of practitioner role, one can see relationships such as a provider that provides a particular service at a particular location and accepts insurance (as part of a particular network) all on behalf of an organization. 

<figure class="figure">
<figcaption class="figure-caption"><strong>Figure 1: Example 1 - In progress</strong></figcaption>
  <img src="assets/images/Diagram1.jpg" class="figure-img img-responsive img-rounded center-block" alt="Diagram1.jpg" />
</figure>

### Organization Role

Similar to the Practitioner Role above, Organization Role provides a means of describing the same data, but the reference point being the organization alone. Example include 1) the organizational members of an association (hospitals in a hospital association), 2) organizational members of an insurance network and the service they provide at specific location as part of the network, and 3) two distinct organizations in partnership creating a service (e.g. cancer center) at a location.

<figure class="figure">
<figcaption class="figure-caption"><strong>Figure 2: Example 2 - In progress</strong></figcaption>
  <img src="assets/images/Diagram2.jpg" class="figure-img img-responsive img-rounded center-block" alt="Diagram2.jpg" />
</figure>

### Network / Product Plan

Network is a group of practitioners and organizations optionally qualified by healthcare service and location that deliver healthcare services on behalf of a payer for individuals enrolled in a product/plan that have specific characteristics (e.g HMO, PPO, Specialty)

<figure class="figure">
<figcaption class="figure-caption"><strong>Figure 3: Example 3 - In Progress</strong></figcaption>
  <img src="assets/images/Diagram3.jpg" class="figure-img img-responsive img-rounded center-block" alt="Diagram3.jpg" />
</figure>

### Using Codes in VhDir profiles

#### Extensible binding for CodeableConcept Datatype
{:.no_toc}

Extensible binding to a value set definition for this IG means that if the data type is CodeableConcept, then one of the coding values SHALL be from the specified value set if a code applies, but if no suitable code exists in the value set and no further restrictions have been applied (such as the max valueset binding described in the next section), alternate code(s) may be provided in its place. If only text available, then just text may be used.

#### Extensible + Max-ValueSet binding for CodeableConcept Datatype
{:.no_toc}

For this IG, we have defined the Extensible + Max-ValueSet binding to allow for either a code from the defined value set or text if the code is not available.  (for example, legacy data). This means, unlike a FHIR extensible binding, alternate code(s) are not permitted and a text value SHALL be supplied if the code is not available.  However, multiple codings (translations) are allowed as is discussed below.

* * Review this example - should we retain, replace, or delete? 

Example: Immunization resource vaccineCode's CVX coding - the source only has the text "4-way Influenza" and no CVX code.

    \{
      "resourceType": "Immunization",
      ...
      "vaccineCode": {
        "text":"4-way Influenza"
      },
      ...
    }


#### Required binding for Code Datatype
{:.no_toc}

Required binding to a value set definition for this IG means that one of the codes from the specified value set SHALL be used. If only text is available or the local (proprietary, system) code cannot be mapped to one of the required codes the [core specification] provides guidance which we have summarized:

1.  Send the resource with the code element empty
2.  Use the [DataAbsentReason Extension] in the data type
3.  Use the code ‘unsupported’ - The source system wasn't capable of supporting this element.

Note that when a query uses a status parameter, a status will be ambiguous.

* * Review this example - should we retain, replace, or delete? 

Example: AllergyIntolerance resource with a status that is text only or cannot be mapped to the status value set.

     \{
       "resourceType”:“AllergyIntolerance”,
       ...
       “\_status”:{
        “url” : “http://hl7.org/fhir/STU3/StructureDefinition/data-absent-reason”,
       “valueCode” : “unsupported”
        ...
      },
     }

#### Required binding for CodeableConcept Datatype
{:.no_toc}

Required binding to a value set definition means that one of the codes from the specified value set SHALL be used and using only text is not valid. In this IG, we have defined the Extensible + Max-ValueSet binding to allow for either a code from the specified value set or text. Multiple codings (translations) are permitted as is discussed below.


#### Using multiple codes with CodeableConcept Datatype
{:.no_toc}

Alternate codes may be provided in addition to the standard codes defined in required or extensible value sets. The alternate codes are called “translations”. These translations may be equivalent to or narrower in meaning to the standard concept code.

* * Review this example - should we retain, replace, or delete? 

Example of multiple translation for Body Weight concept code.


    "code": {
        "coding": [
         {
            "system": "http://loinc.org",  //NOTE:this is the standard concept defined in the value set//
            "code": "29463-7",
            "display": "Body Weight"
          },
    //NOTE:this is a translation to a more specific concept
         {
            "system": "http://loinc.org",
            "code": "3141-9",
            "display": "Body Weight Measured"
          },
    //NOTE:this is a translation to a different code system (Snomed CT)
         {
            "system": "http://snomed.info/sct",
            "code":  “364589006”,
            "display": "Body Weight"
          }
    //NOTE:this is a translation to a locally defined code
         {
            "system": "http://AcmeHealthCare.org",
            "code":  “BWT”,
            "display": "Body Weight"
          }
        ],
        "text": "weight"
      },

Example of translation of CVX vaccine code to NDC code.


    "vaccineCode" : {
        "coding" : [
          {
            "system" : "http://hl7.org/fhir/STU3/sid/cvx",
            "code" : "158",
            "display" : "influenza, injectable, quadrivalent"
          },
          {
            "system" : "http://hl7.org/fhir/STU3/sid/ndc",
            "code" : "49281-0623-78",
            "display" : "FLUZONE QUADRIVALENT"
          }
        ]
      },

### Read(Fetch) resource notation:

Interactions on profile pages are defined with the syntax:

 **`GET [base]/[Resource-type]/[id] {parameters}`**

-   GET is the HTTP verb used for fetching a resource
-   Content surrounded by \[\] is mandatory, and will be replaced by the string literal identified.
    -   base: The Service Root URL (e.g. “<https://fhir-open-api-dstu2.smarthealthit.org>”)
    -   Resource-type: The name of a resource type (e.g. “Patient”)
    -   id: The Logical Id of a resource(e.g. “24342”)
-   Content surrounded by {} is optional
    -   parameters: URL parameters as defined for the particular interaction (e.g."?\_format=xml"}

For more information see the [FHIR RESTful API]

### Search Syntax

In the simplest case, a search is executed by performing a GET operation in the RESTful framework:

**GET [base]/[Resource-type]?name=value&...**

For this RESTful search ([FHIR Search]), the parameters are a series of name=\[value\] pairs encoded in the URL. The search parameter names are defined for each resource. For example, the Observation resource the name “code” for search on the LOINC code. See [FHIR Search] for more information about searching in REST, messaging, and services.

### Syntax for searches limited by patient (To be revised)

There are several potential ways to search for resources associated with a specific patient depending on the context and implementation. These searches result in the same outcome.:

1. An explicitly defined patient using the 'patient' parameter that controls which set of resources are being searched by resource type.  Note that all the search interactions in this IG are published using this syntax:
  - **GET [base]/[Resource-type]?patient=24342{&otherparameters}**
   - There are several variations to this syntax which are listed below:

        -   GET \[base\]/\[Resource-type\]?Subject=\[id\]{&other parameters}
        -   GET \[base\]/\[Resource-type\]?Subject=Patient/\[id\]{&other parameters}
        -   GET \[base\]/\[Resource-type\]?Subject.\_id=\[id\]{&other parameters}
        -   GET \[base\]/\[Resource-type\]?subject:Patient=\[id\]{&other parameters}
        -   GET \[base\]/\[Resource-type\]?subject:Patient=Patient/\[id\]{&other parameters}
        -   GET \[base\]/\[Resource-type\]?subject:Patient=\[https://%5Burl%5D/Patient/id\]{&other parameters}
        -   GET \[base\]/\[Resource-type\]?subject:Patient.\_id=\[id\]{&other parameters}
        -   GET \[base\]/\[Resource-type\]?patient:Patient=\[https://%5Burl%5D/Patient/id\]{&other parameter

1. The patient may be *implicit* in the context (e.g. using SMART). Then the patient parameter can be omitted:
  - **GET [base]/[Resource-type]{?other-parameters}**

1. Patient [compartment] based search with a specified resource type in that compartment. **NOTE this IG does not support compartment based searches**.

### Across Platform Searches

Validated Healthcare Directory servers are not required to resolve full URLs that are external to their environment.

### Guidance on limiting the number of search results (to be revised)

In order to manage the number of search results returned, the server may choose to return the results in a manner consistent with FHIR Bulk Data Access Standards. For a simple RESTful search, the page links are contained in the returned bundle as links. See the [FHIR Paging] for more information.

------------------------------------------------------------------------

  [core specification]: http://hl7.org/fhir/STU3/search.html#return

[FHIR RESTful API]: http://hl7.org/fhir/STU3/http.html
[FHIR Search]: http://hl7.org/fhir/STU3/search.html
[FHIR Terminology]: http://hl7.org/fhir/STU3/terminologies.html
[FHIR Paging]: http://hl7.org/fhir/STU3/http.html#paging
[HTTP]: http://hl7.org/fhir/STU3/http.html
[FHIR Data Types]: http://hl7.org/fhir/STU3/datatypes.html
[FHIR Resource]: http://hl7.org/fhir/STU3/resource.html
[Issue \#39]: https://github.com/argonautproject/implementation-program/issues/39
[compartment]: http://hl7.org/fhir/STU3/compartmentdefinition.html
[core specification]: http://hl7.org/fhir/STU3/extensibility.html#2.20.0.2.2
[DataAbsentReason Extension]: http://hl7.org/fhir/STU3/extension-data-absent-reason.html
[http://hl7.org/fhir/STU3/StructureDefinition/data-absent-reason]: http://hl7.org/fhir/STU3/StructureDefinition/data-absent-reason
[FHIR Conformance Rules]: http://hl7.org/fhir/STU3/conformance-rules.html
[Quantity]: http://hl7.org/fhir/STU3/datatypes.html#quantity
[UCUM]: http://unitsofmeasure.org
[VhDir Server Capability Statement]: CapabilityStatement-server.html
[HL7 U.S. Data Access Framework (DAF)]: http://wiki.siframework.org/Data+Access+Framework+Homepage
[UCUM Codes value set]: http://hl7.org/fhir/STU3/valueset-ucum-units.html
[2015 Edition Common Clinical Data Set (CCDS)]: https://www.healthit.gov/sites/default/files/2015Ed_CCG_CCDS.pdf
[Validated Healthcare Directory  Patient Profile]: StructureDefinition-us-core-patient.html
[Validated Healthcare Directory  Smoking Status Observation Profile]: StructureDefinition-us-core-smokingstatus.html
[Validated Healthcare Directory  Condition Profile]: StructureDefinition-us-core-condition.html
[Validated Healthcare Directory  Medication Profile]: StructureDefinition-us-core-medication.html
[Validated Healthcare Directory  Medication Statement Profile]: StructureDefinition-us-core-medicationstatement.html
[Validated Healthcare Directory  Medication Request Profile]: StructureDefinition-us-core-medicationrequest.html
[Validated Healthcare Directory  Allergies Profile]: StructureDefinition-us-core-allergyintolerance.html
[Validated Healthcare Directory  Diagnostic Report Profile]: StructureDefinition-us-core-diagnosticreport.html
[Validated Healthcare Directory  Procedure Profile]: StructureDefinition-us-core-procedure.html
[Validated Healthcare Directory  CareTeam Profile]: StructureDefinition-us-core-careteam.html
[Validated Healthcare Directory  Immunization Profile]: StructureDefinition-us-core-immunization.html
[Validated Healthcare Directory  Implanted Device Profile]: StructureDefinition-us-core-device.html
[Validated Healthcare Directory  CarePlan Profile]: StructureDefinition-us-core-careplan.html
[Validated Healthcare Directory  Goal Profile]: StructureDefinition-us-core-goal.html
[Validated Healthcare Directory  Result Observation Profile]: StructureDefinition-us-core-observationresults.html
[Vital Signs Profile]: http://hl7.org/fhir/STU3/vitalsigns.html
