---
title: Bulk Data and Subscriptions
layout: default
active: bulk-data
topofpage: true
sectionnumbering: true
F: http://build.fhir.org/

---

<p class="note-to-balloters">
<b>Informative only:</b> was not a part of the September 2018 ballotted content.<br/>
It will be updated based on the Bulk Data ballot outcome, and further implementation experience.
</p>
<br/>

## Background


Bulk data is a recent addition to the FHIR related specifications and has many uses. Primarily its for out of band data extraction for distribution.

There are several basic parts to FHIR's bulk data extract

* The scope of data selection
* The format of the bulk data extract (nd-json) *
* The async operation request and status tracking (as these processes may take significant processing time) *
* Retrieval of the completed export
* Closing/cleanup of the completed export *

<em>(The items marked with * can be considered quite mature, and unlikely to change from this point)</em>

The bulk data had been balloted and was still being reconciled and at the time of publication of this guide, the current development version can be found here:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[http://hl7.org/fhir/us/bulkdata/2019May/index.html](http://hl7.org/fhir/us/bulkdata/2019May/index.html)

The community discussions and questions around this draft specification are here:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[https://chat.fhir.org/#narrow/stream/179250-bulk-data](https://chat.fhir.org/#narrow/stream/179250-bulk-data)

## Healthcare Directory Bulk Data Specifics
### The scope of the data selection

For the directory bulk data extraction, to request an entire copy of all content in the directory, the scope selection can be defined at the top level, and just specifying that we would like to retrieve all content for the specified resource types from the base of the FHIR server.
```
GET [base]/$export?_type=Organization,Location,Practitioner,PractitionerRole,HealthcareService,VerificationResult, ...
```

A healthcare directory may curate such an extract on a nightly process, and just return this without needing to scan the live system, and the value returned in the <code>transactionTime</code> in the result should contain the timestamp at which this was generated (including timezone information), and that should be used in a subsequent call to retrieve changes since this point in time.

Once a system has a complete set of data, it is usually more efficient to ask for changes since a point in time, in which case the request should use the value above (<code>transactionTime</code>) to update the local directory.

```
GET [base]/$export?_type=Organization,Location,Practitioner, ... &_since=[transactionTime]
```

This behaves just the same as the initial request, with the exception of the content.

We would expect that this is more likely to return the current information, rather than from a pre-generated snapshot, as the transactionTime could be anything.

> <strong>Note:</strong> The current bulk data handling specification does not handle deleted items, and the recommendation is that periodically a complete download should be done to check for "gaps" to reconcile the deletions (which could also be due to security changes), however content shouldn't usually be "deleted" it should be marked as inactive, or end dated.
>
><strong>Proposal:</strong> Include deletions bundle(s) for each resource type to report the deletions (when using the _since parameter) which would be in a new property "deletions" in the process output, as demonstrated in the status tracking output section below. This bundle would have a type of "collection", and each entry would be as per a deleted item in a history.

```xml
<entry>
   <!-- no resource included for a delete -->
   <request>
     <method value="DELETE"/>
     <url value="PractitionerRole/[id]"/>
   </request>
   <!-- response carries the instant the server processed the delete -->
   <response>
     <lastModified value="2014-08-20T11:05:34.174Z"/>
   </response>
</entry>
```

> The total in the bundle will just be the count of deletions in the file, the total in the operation result will indicate the number of deletion bundles in the ndjson (same as the other types).
>
> If the caller doesn't want to use the deletions, they can just ignore the files in the output, and not download those specific files.


### List defined subsets

The previous sections are all that is defined by the FHIR Bulk Data extract specification, however we may choose to implement an additional parameter to this operation to permit the selection to also filter to resources that are included in a specified list resource. The approach is similar to the same capability defined by FHIR [http://hl7.org/fhir/search.html#list](http://hl7.org/fhir/search.html#list)

This could be used by client applications such as a Primary Care System that wanted to only periodically update using this technique, but only with resources that they currently have loaded in their "local directory" - internal black book, which were cached there from previous searches to the system.

```
GET [base]/$export?_type=Organization,Location,Practitioner,PractitionerRole,HealthcareService&_list=List/45
```

In this example the Primary Care System would be responsible for keeping <code>List/45</code> up to date with what it is tracking, and a national service may decide that permitting this List resource management is too much overhead, however local enterprise directories may support this type of functionality.

### Arbitrary subsets of data

The current bulk data export operations use the Group resource to define the set of data related to a Patient, and at present there is no definition for this to be done in the directory space, apart from at the resource type level. This is possible with search and subscriptions (which leverage search) by using search parameters on the resource types and setting the parameters of interest.

When defining a subset of data, consideration should be given to what happens when data is changed such that it no longer is within the context of the conditions.

One possibility would be to use a bundle of searches where each type has it's own search parameters, another is to use a <a href="http://hl7.org/fhir/r4/graphdefinition.html" class="external-link" rel="nofollow">GraphDefinition</a> resource.

This functionality should be the subject of a connectathon to determine practical solutions.

One possibility could be to leverage the List functionality described above to maintain a state of what <em>was</em> included in a previous content, however this obviously incurs additional overhead on the part of the server, and for many systems - especially those at scale like a national system - this is likely not practical.

### Format of the bulk data extract

The bulk extract format is always an nd-json file (new-line delimited json), and each file can only contain 1 resource type in it, but can be spread across multiple files, with either a size limit or count limit imposed by the extracting system, not the requestor.

The list of these files will be returned in the Complete status output, as described in the standard Bulk Data documentation.

### Starting the extract

There are 2 options for starting the extract, one that is a single operation specifying all the content, and the other to be for a specific type only. These were both covered in the selecting the scope section above.

Here I will only document the use of the global export, as an initial request.

The initial request:

```
GET [base]/$export?_type=Organization,Location,Practitioner,PractitionerRole,HealthcareService
```
with headers:
```
Accept: application/fhir+json</code>
Authentication: Bearer [bearer token]</code>
Prefer: respond-async</code>
```

This will return either:
* HTTP status code of <code>4XX</code> or <code>5XX</code> with an <code>OperationOutcome</code> resource body if the request fails,
* HTTP status code of <code>202 Accepted</code> when successful, with a <code>Content-Location</code> header with an absolute URI for subsequent status requests, and optionally an <code>OperationOutcome</code> in the resource body if desired

Example Content-Location: <a class="external-link" style="text-decoration: underline;text-align: left;" rel="nofollow" href="http://example.org/status-tracking/request-123">http://example.org/status-tracking/request-123</a> (note that this is not necessarily a FHIR endpoint, and isn't a true FHIR resource)

### Tracking the status of the extract

After a bulk data request has been started, the client MAY poll the URI provided in the <code>Content-Location</code> header.

```
GET http://example.org/status-tracking/request-123
```

This will return:

* HTTP status code of <code>202 Accepted</code> when still in progress (and no body returned)

* HTTP status code of <code>5XX</code> when a fatal error occurs, and an <code>OperationOutcome</code> in json format for the body with the detail of the error
_(Note this is a fatal error in processing, not some error encountered while processing files - a complete extract can contain errors)_
* HTTP status code of <code>200 OK</code> when the processing is complete, and the result is a json object as noted in the specification (and an example included below)

Refer to the build data specification for details of the completion event:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[https://github.com/smart-on-fhir/fhir-bulk-data-docs/blob/master/export.md#response---complete-status](https://github.com/smart-on-fhir/fhir-bulk-data-docs/blob/master/export.md#response---complete-status)

```javascript
{
    "transactionTime": "[instant]",
    "request": "[base]/$export?_type=Organization,Location,Practitioner,PractitionerRole,HealthcareService",
    "requiresAccessToken": true,
    "output": [
        {
            "type": "Practitioner",
            "url": "http://serverpath2/practitioner_file_1.ndjson",
            "count": 10000
        },
        {
            "type": "Practitioner",
            "url": "http://serverpath2/practitioner_file_2.ndjson",
            "count": 3017
        },
        {
            "type": "Location",
            "url": "http://serverpath2/location_file_1.ndjson",
            "count": 4182
        }
    ],
    // Note that this deletions property is a proposal, not part of the bulk data spec.
    "deletions": [
        {
            "type": "PractitionerRole",
            "url": "http://serverpath2/practitionerrole_deletions_1.ndjson", // the bundle will include the total number of deletions in the file
            "count": 23 // this is the number of bundles in the file, not the number of resources deleted
        }
    ],
    "error": [
        {
            "type": "OperationOutcome",
            "url": "http://serverpath2/err_file_1.ndjson",
            "count": 439
        }
    ]
}
```

### Retrieving the complete extract

Once the tracking of the extract returns a <code>200 OK</code> completed status, the body of the result will include the list of prepared files that you can download.

Then each of these URLs can be downloaded by a simple get, ensuring to pass the Bearer token if the result indicates <code>requiresAccessToken = true</code>

While downloading, also recommend including the header <code>Accept-Encoding: gzip</code> to compress the content as it comes down.

```
GET http://serverpath2/location_file_1.ndjson
```

(Note: our implementation will probably always gzip encode the content - as we are likely to store the processing files gzip encoded to save space in the storage system)

Once you have downloaded all the files you need, you should tell the server to cleanup, which is detailed next.

### Finishing the extract

This is the simplest part of the process, and that is just calling <code>DELETE</code> on the status tracking URL.

```
DELETE http://example.org/status-tracking/request-123
```

This then tells the server that we are all finished with the data, and it can be deleted/cleaned up. The server may also include some time based limits where it may only keep it for a set period of time before it automatically cleans it up.


## Subscriptions
A close relative to the bulk data extract is the subscriptions content - and how these will work in the context of Bulk Directory exchanges needs further experimentation and connectathon experiences.

These could be setup to monitor the directory for realtime changes to resources of interest, and are defined through the use of search parameters.

The "urgent notifications" channel is yet to be defined, but should enable specific actions such as license suspensions/revocations.


~~~json
   ...TODO edit this ...
~~~

The FHIR Subscription API allows directories to (push) data to multiple local directories based on a set of criteria in the form of a FHIR query which defined by the subscriber.  For example:

-  All the updated data for a particular jurisdiction or region
-  All the providers whose certification has been revoked or is expired or about to expire.

Any newly created or updated resources that meet the criteria triggers the  Server to notify the subscriber and "forward" the results of the search criteria (e.g., the updated Practitioner, PractitionerRole and Endpoint resource - to a specified target endpoint).  Note that an alternate workflow is a Server notification without a payload and then the subscriber would fetch the data through the REST API from a predetermined endpoint - typically a "middleman" server.

Below is an example subscription to push all new and updated Practitioners, PractiyionerRoles, and  Endpoints from the 'vhdir-demo' server to the 'local-dir':

~~~json
{
   "resourceType":"Bundle",
   "id":"VhDir-subscription-bundle",
   "meta":{
      "lastUpdated":"2017-01-24T01:43:30Z"
   },
   "type":"transaction",
   "entry":[
      {
         "fullUrl":"urn:uuid:61ebe359-bfdc-4613-8bf2-c5e300945f0a",
         "resource":{
            "resourceType":"Subscription",
            "id":"vhdir-connectathon-scenario-12p",
            "status":"requested",
            "contact":[
               {
                  "system":"phone",
                  "value":"ext 4123"
               }
            ],
            "end":"2020-01-01T00:00:00Z",
            "reason":"(push) healthcare directory data to multiple local directories",
            "criteria":"Practitioner?address-postalcode:contains=02108, 02109, 02110, 02111, 02113, 02114, 02115, 02116, 02118, 02119, 02120, 02121, 02122, 02124, 02125, 02126, 02127, 02128, 02129, 02130, 02131, 02132, 02134, 02135, 02136, 02151, 02152, 02163, 02199, 02203, 02210, 02215, 02467",
            "channel":{
               "type":"rest-hook",
               "endpoint":"https://local-dir/fhir",
               "payload":"application/fhir+json",
               "header":[
                  "Authorization: Bearer secret-token-abc-123"
               ]
            }
         },
         "request":{
            "method":"POST",
            "url":"Subscription"
         }
      },
      {
         "fullUrl":"urn:uuid:61ebe359-bfdc-4613-8bf2-c5e300945f0a",
         "resource":{
            "resourceType":"Subscription",
            "id":"vhdir-connectathon-scenario-12pr",
            "status":"requested",
            "contact":[
               {
                  "system":"phone",
                  "value":"ext 4123"
               }
            ],
            "end":"2020-01-01T00:00:00Z",
            "reason":"(push) healthcare directory data to multiple local directories",
            "criteria":"PractitionerRole?practitioner.address-postalcode:contains=02108, 02109, 02110, 02111, 02113, 02114, 02115, 02116, 02118, 02119, 02120, 02121, 02122, 02124, 02125, 02126, 02127, 02128, 02129, 02130, 02131, 02132, 02134, 02135, 02136, 02151, 02152, 02163, 02199, 02203, 02210, 02215, 02467",
            "channel":{
               "type":"rest-hook",
               "endpoint":"https://local-dir/fhir",
               "payload":"application/fhir+json",
               "header":[
                  "Authorization: Bearer secret-token-abc-123"
               ]
            }
         },
         "request":{
            "method":"POST",
            "url":"Subscription"
         }
      },
      {
         "fullUrl":"urn:uuid:61ebe359-bfdc-4613-8bf2-c5e300945f0a",
         "resource":{
            "resourceType":"Subscription",
            "id":"vhdir-connectathon-scenario-12pe",
            "status":"requested",
            "contact":[
               {
                  "system":"phone",
                  "value":"ext 4123"
               }
            ],
            "end":"2020-01-01T00:00:00Z",
            "reason":"(push) healthcare directory data to multiple local directories",
            "criteria":"Endpoint?_has:PractitionerRole:endpoint:practitioner.address-postalcode:contains=02108, 02109, 02110, 02111, 02113, 02114, 02115, 02116, 02118, 02119, 02120, 02121, 02122, 02124, 02125, 02126, 02127, 02128, 02129, 02130, 02131, 02132, 02134, 02135, 02136, 02151, 02152, 02163, 02199, 02203, 02210, 02215, 02467",
            "channel":{
               "type":"rest-hook",
               "endpoint":"https://local-dir/fhir",
               "payload":"application/fhir+json",
               "header":[
                  "Authorization: Bearer secret-token-abc-123"
               ]
            }
         },
         "request":{
            "method":"POST",
            "url":"Subscription"
         }
      }
   ]
}
~~~
