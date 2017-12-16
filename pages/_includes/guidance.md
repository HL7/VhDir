
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

###  Validated Healthcare Directory 

The VHDir IG provides a specification for the exchange of data from a national source of validated provider information to organizations implementing healthcare directories to satisfy their own, local use cases. 


### Must Support
*Must Support* on any data element SHALL be interpreted as follows:


* Validated Healthcare Directory Responders SHALL be capable of including the data element as part of the query results as specified by the [Validated Healthcare Directory Capability Statement].
* Validated Healthcare Directory Requestors SHALL be capable of processing resource instances containing the data elements without generating an error and causing the application to fail. In other words Validated Healthcare Directory Requestors SHOULD be capable of displaying the data elements for human use or storing it for other purposes.
* In situations where information on a particular data element is not present and the reason for absence is unknown, Validated Healthcare Directory Responders SHALL NOT include the data elements in the resource instance returned as part of the query results.
* When querying Validated Healthcare Directory Responders, Validated Healthcare Directory Requestors SHALL interpret missing data elements within resource instances as data not present in the Validated Healthcare Directory Responder's systems.
* In situations where information on a particular data element is missing and the Validated Healthcare Directory Responder knows the precise reason for the absence of data, Validated Healthcare Directory  Responders SHALL send the reason for the missing information using values (such as nullFlavors) from the value set where they exist or using the dataAbsentReason extension.
* Validated Healthcare Directory Requestors SHALL be able to process resource instances containing data elements asserting missing information.


* NOTE: Typically *Validated Healthcare Directory Responder* Actor = Server and *Validated Healthcare Directory Requestor Actor* = Client
* NOTE: Validated Healthcare Directory Responders who do not have the capability to store or return a data element tagged as Supported in Validated Healthcare Directory profiles can still claim conformance to the Validated Healthcare Directory profiles per the Validated Healthcare Directory conformance resources.
* NOTE: The above definition of Supported is derived from HL7v2 concept "Required but may be empty - RE" described in HL7v2 V28_CH02B_Conformance.doc.
* NOTE: Readers are advised to understand [FHIR Terminology] requirements, [FHIR RESTful API] based on the HTTP protocol, along with [FHIR Data Types], [FHIR Search] and [FHIR Resource] formats before implementing Validated Healthcare Directory  requirements.


### Overview of Validated Healthcare Directory - Resource Relationships 

### Practitioner

A practitioner is a person who is directly or indirectly involved in the provisioning of healthcare.

### Practitioner Role 

PractionerRole describes the relationship between a practitioner and an organization. A practitioner provides services to the organization at a location.  Practitioners also participate in healthcare provider insurance networks through their role at an organization. 

<figure class="figure">
<figcaption class="figure-caption"><strong>Figure 1: PractionerRole </strong></figcaption>
  <img src="assets/images/Diagram1.jpg" class="figure-img img-responsive img-rounded center-block" alt="Diagram1.jpg" />
</figure>

### Organization Role

Similar to practitionerRole, OrganizationRole describes relationships between organizations. For example: 1) the relationship between an organization and an association it is a member of (e.g. hospitals in a hospital association),  2) an organization that provides services to another organization, such as an organization contracted to provide mental health care for another organization as part of a healthcare provider insurance network, and 3) distinct organizations forming a partnership to provide services (e.g. a cancer center).

<figure class="figure">
<figcaption class="figure-caption"><strong>Figure 2: Organization Role </strong></figcaption>
  <img src="assets/images/Diagram2.jpg" class="figure-img img-responsive img-rounded center-block" alt="Diagram2.jpg" />
</figure>

### Network / Product Plan

A network is a group of practitioners and organizations that provide healthcare services for individuals enrolled in a health insurance product/plan (typically on behalf of a payer).

<figure class="figure">
<figcaption class="figure-caption"><strong>Figure 3: Network / Product Plan </strong></figcaption>
  <img src="assets/images/Diagram3.jpg" class="figure-img img-responsive img-rounded center-block" alt="Diagram3.jpg" />
</figure>

### Using Codes in VhDir profiles

#### Extensible binding for CodeableConcept Datatype
{:.no_toc}

Extensible binding to a value set definition for this IG means that if the data type is CodeableConcept, then one of the coding values SHALL be from the specified value set if a code applies, but if no suitable code exists in the value set and no further restrictions have been applied (such as the max valueset binding described in the next section), alternate code(s) may be provided in its place. If only text available, then just text may be used.

Example: Product/Plan's coverage type coding - the source only has the text “4-way Influenza” and no coverage type code.

\{
      "resourceType": "productPlan",
      ...
       "coverage.Type": {
        "text":"orthodontics - extended"
      },
      ...
}   

#### Extensible + Max-ValueSet binding for CodeableConcept Datatype
{:.no_toc}

For this IG, we have defined the Extensible + Max-ValueSet binding to allow for either a code from the defined value set or text if the code is not available.  (for example, legacy data). This means, unlike a FHIR extensible binding, alternate code(s) are not permitted and a text value SHALL be supplied if the code is not available.  However, multiple codings (translations) are allowed.

#### Required binding for Code Datatype
{:.no_toc}

Required binding to a value set definition for this IG means that one of the codes from the specified value set SHALL be used. If only text is available or the local (proprietary, system) code cannot be mapped to one of the required codes the [core specification] provides guidance which we have summarized:

1.  Send the resource with the code element empty
2.  Use the [DataAbsentReason Extension] in the data type
3.  Use the code ‘unsupported’ - The source system wasn't capable of supporting this element.

Note that when a query uses a status parameter, a status will be ambiguous.

Example: Endpoint resource with a status that is text only or cannot be mapped to the status value set.

     \{
       "resourceType”:“Endpoint”,
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
<!--
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

!-->

### Read (Fetch) resource notation:

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

For this RESTful search ([FHIR Search]), the parameters are a series of name=\[value\] pairs encoded in the URL. The search parameter names are defined for each resource. See [FHIR Search] for more information about searching in REST, messaging, and services.

### Syntax for searches limited by specific practitioner

There are several potential ways to search for resources associated with a specific practitioner depending on the context and implementation. These searches result in the same outcome.:

1. An explicitly defined practitioner using the practitioner' parameter that controls which set of resources are being searched by resource type.  Note that all the search interactions in this IG are published using this syntax:
  - **GET [base]/[Resource-type]?practitioner=24342{&otherparameters}**
   - There are several variations to this syntax which are listed below:

        -   GET \[base\]/\[Resource-type\]?Subject=\[id\]{&other parameters}
        -   GET \[base\]/\[Resource-type\]?Subject=practitioner/\[id\]{&other parameters}
        -   GET \[base\]/\[Resource-type\]?Subject.\_id=\[id\]{&other parameters}
        -   GET \[base\]/\[Resource-type\]?subject:=\[id\]{&other parameters}
        -   GET \[base\]/\[Resource-type\]?subject:practitioner=practitioner/\[id\]{&other parameters}
        -   GET \[base\]/\[Resource-type\]?subject:practitioner=\[https://%5Burl%5D/practitioner/id\]{&other parameters}
        -   GET \[base\]/\[Resource-type\]?subject:practitioner.\_id=\[id\]{&other parameters}
        -   GET \[base\]/\[Resource-type\]?practitioner:practitioner=\[https://%5Burl%5D/practitioner/id\]{&other parameter

1. The practitioner may be *implicit* in the context (e.g. using SMART). Then the practitioner parameter can be omitted:
  - **GET [base]/[Resource-type]{?other-parameters}**

1. practitioner [compartment] based search with a specified resource type in that compartment. **NOTE this IG does not support compartment based searches**.

### Across Platform Searches

Validated Healthcare Directory servers are not required to resolve full URLs that are external to their environment.

### Guidance on limiting the number of search results 
In order to manage the number of search results returned, the server may choose to return the results in a manner consistent with FHIR Bulk Data Access Standards. For a simple RESTful search, the page links are contained in the returned bundle as links. See the [FHIR Paging] (https://www.hl7.org/fhir/http.html#paging) and [Bulk Data Aceess] (http://www.healthintersections.com.au/?p=2689) for more information.

------------------------------------------------------------------------

 