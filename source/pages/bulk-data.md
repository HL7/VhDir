---
title: Bulk Data and Subscriptions
layout: default
active: guidance
topofpage: true
sectionnumbering: true
F: http://build.fhir.org/
---

<h2 style="margin-left: 0.0px;text-align: left;" id="BulkDataandDirectories-Background">Background</h2>

> This page is <b>informative only</b> information, and was not a part of the ballotted material.
> It provides basic guidance on applying the core async processing, along with 
> the system wide $export operation defined in the bulk data implementation guide.
> Along with some suggestions with extensions that may be considered.

Bulk data is a recent addition to the FHIR related specifications and has many uses. Primarily its for out of band data extraction for distribution.

There are several basic parts to FHIR's bulk data extract

* The scope of data selection
* The format of the bulk data extract (nd-json) *
* The async operation request and status tracking (as these processes may take significant processing time) *
* Retrieval of the completed export
* Closing/cleanup of the completed export *

<em>(The items marked with * can be considered quite mature, and unlikely to change from this point)</em>

The bulk data had been balloted and was still being reconciled and at the time of publication of this guide, the current development version can be found here:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[http://build.fhir.org/ig/HL7/bulk-data-export](http://build.fhir.org/ig/HL7/bulk-data-export)

The community discussions and questions around this draft specification are here:

<p style="margin-left: 30.0px;text-align: left;">
<a class="external-link" rel="nofollow" href="https://chat.fhir.org/#narrow/stream/179250-bulk-data" style="text-decoration: none;">https://chat.fhir.org/#narrow/stream/179250-bulk-data</a>
</p>

<h2 style="margin-left: 0.0px;text-align: left;" id="BulkDataandDirectories-HealthcareDirectoryBulkDataSpecifics">Healthcare Directory Bulk Data Specifics</h2>
<h3 id="BulkDataandDirectories-Thescopeofthedataselection">The scope of the data selection</h3>
<p style="margin-left: 0.0px;text-align: left;">For the directory bulk data extraction, to request an entire copy of all content in the directory, the scope selection can be defined at the top level, and just specifying that we would like to retrieve all content for the specified resource types from the base of the FHIR server.</p>
<div class="table-wrap">
<table class="wrapped confluenceTable" style="text-align: left;margin-left: 0.0px;">
<colgroup>
<col/>
</colgroup>
<tbody style="text-align: left;margin-left: 0.0px;">
<tr style="text-align: left;margin-left: 0.0px;">
<td style="text-align: left;" class="confluenceTd">
<p style="margin-left: 0.0px;text-align: left;">
<code class="java plain" style="text-align: left;margin-left: 0.0px;">GET [base]/$export?_type=Organization,Location,Practitioner,PractitionerRole,HealthcareService,VerificationResult, ...</code>
</p>
</td>
</tr>
</tbody>
</table>
</div>
<p style="margin-left: 0.0px;text-align: left;">A healthcare directory may curate such an extract on a nightly process, and just return this without needing to scan the live system, and the value returned in the <strong>
<code>transactionTime</code>
</strong>
<span style="text-decoration: none;color: rgb(36,41,46);"> in the result should contain the timestamp at which this was generated (including timezone information), and that should be used in a subsequent call to retrieve changes since this point in time.</span>
</p>
<p style="margin-left: 0.0px;text-align: left;">
<span style="text-decoration: none;color: rgb(36,41,46);">Once a system has a complete set of data, it is usually more efficient to ask for changes since a point in time, in which case the request should use the value above (<code>
<strong>transactionTime</strong>
</code>) to update the local directory.</span>
</p>
<div class="table-wrap">
<table class="wrapped confluenceTable" style="text-align: left;margin-left: 0.0px;">
<colgroup>
<col/>
</colgroup>
<tbody style="text-align: left;margin-left: 0.0px;">
<tr style="text-align: left;margin-left: 0.0px;">
<td style="text-align: left;" class="confluenceTd">
<p style="margin-left: 0.0px;text-align: left;">
<code class="java plain" style="text-align: left;margin-left: 0.0px;">GET [base]/$export?_type=Organization,Location,Practitioner, ... &amp;_since=[transactionTime]</code>
</p>
</td>
</tr>
</tbody>
</table>
</div>
<p style="margin-left: 0.0px;text-align: left;">
<br/>
</p>
<p style="margin-left: 0.0px;text-align: left;">
<span style="color: rgb(36,41,46);text-decoration: none;">This behaves just the same as the initial request, with the exception of the content. </span>
</p>
<p style="margin-left: 0.0px;text-align: left;">
<span style="color: rgb(36,41,46);text-decoration: none;">We would expect that this is more likely to return the current information, rather than from a pre-generated snapshot, as the transactionTime could be anything.</span>
</p>
<blockquote>
<p style="margin-left: 0.0px;">
<span style="color: rgb(36,41,46);text-decoration: none;">
<strong>Note:</strong> The current bulk data handling specification does not handle deleted items, and the recommendation is that periodically a complete download should be done to check for &quot;gaps&quot; to reconcile the deletions (which could also be due to security changes), however content shouldn't usually be &quot;deleted&quot; it should be marked as inactive, or end dated.</span>
</p>
<p style="margin-left: 0.0px;">
<span style="color: rgb(0,96,0);">
<span style="color: rgb(0,51,102);">
<strong>Proposal:</strong>
</span> Include deletions bundle(s) for each resource type to report the deletions (when using the _since parameter) which would be in a new property &quot;deletions&quot; in the process output, as demonstrated in the status tracking output section below. This bundle would have a type of &quot;</span>
<span style="color: rgb(0,96,0);">collection&quot;, and each entry would be as per a deleted item in a history</span>
</p>
<div class="table-wrap">
<table class="wrapped confluenceTable" style="text-align: left;margin-left: 0.0px;">
<colgroup>
<col/>
</colgroup>
<tbody style="text-align: left;margin-left: 0.0px;">
<tr style="text-align: left;margin-left: 0.0px;">
<td style="text-align: left;" class="confluenceTd">
<p style="margin-left: 0.0px;text-align: left;">
<span style="color: rgb(51,51,51);text-decoration: none;">  &lt;entry&gt;<br/>
</span>
</p>
<p style="margin-left: 0.0px;text-align: left;">
<span style="color: rgb(51,51,51);text-decoration: none;">    &lt;!-- no resource included for a delete --&gt;<br/>    &lt;request&gt;<br/>      &lt;method value=&quot;DELETE&quot;/&gt;<br/>      &lt;url value=&quot;PractitionerRole/[id]&quot;/&gt;<br/>    &lt;/request&gt;<br/>    &lt;!-- response carries the instant the server processed the delete --&gt;<br/>    &lt;response&gt;<br/>      &lt;lastModified value=&quot;2014-08-20T11:05:34.174Z&quot;/&gt;<br/>    &lt;/response&gt;<br/>  &lt;/entry&gt;</span>
</p>
</td>
</tr>
</tbody>
</table>
</div>
<p class="auto-cursor-target">The total in the bundle will just be the count of deletions in the file, the total in the operation result will indicate the number of deletion bundles in the ndjson (same as the other types).</p>
<p>If the caller doesn't want to use the deletions, they can just ignore the files in the output, and not download those specific files.</p>
</blockquote>

<h3 class="auto-cursor-target" id="BulkDataandDirectories-Listdefinedsubsets">List defined subsets</h3>

<p style="margin-left: 0.0px;text-align: left;">The previous sections are all that is defined by the FHIR Bulk Data extract specification, however we may choose to implement an additional parameter to this operation to permit the selection to also filter to resources that are included in a specified list resource. The approach is similar to the same capability defined by FHIR <a rel="nofollow" style="text-decoration: none;" class="external-link" href="http://hl7.org/fhir/search.html#list">http://hl7.org/fhir/search.html#list</a>
</p>
<p style="margin-left: 0.0px;text-align: left;">This could be used by client applications such as a Primary Care System that wanted to only periodically update using this technique, but only with resources that they currently have loaded in their &quot;local directory&quot; - internal black book, which were cached there from previous searches to the system.</p>
<div class="table-wrap">
<table class="wrapped confluenceTable" style="text-align: left;margin-left: 0.0px;">
<colgroup>
<col/>
</colgroup>
<tbody style="text-align: left;margin-left: 0.0px;">
<tr style="text-align: left;margin-left: 0.0px;">
<td style="text-align: left;" class="confluenceTd">
<p style="margin-left: 0.0px;text-align: left;">
<code class="java plain" style="text-align: left;margin-left: 0.0px;">GET [base]/$export?_type=Organization,Location,Practitioner,PractitionerRole,HealthcareService&amp;_list=List/</code>
<code class="java value" style="text-align: left;margin-left: 0.0px;">45</code>
</p>
</td>
</tr>
</tbody>
</table>
</div>
<p style="margin-left: 0.0px;text-align: left;">In this example the Primary Care System would be responsible for keeping <code>List/45</code> up to date with what it is tracking, and a national service may decide that permitting this List resource management is too much overhead, however local enterprise directories may support this type of functionality.</p>
<h4 style="margin-left: 0.0px;text-align: left;" id="BulkDataandDirectories-Arbitrarysubsetsofdata">Arbitrary subsets of data</h4>
<p style="margin-left: 0.0px;text-align: left;">The current bulk data export operations use the Group resource to define the set of data related to a Patient, and at present there is no definition for this to be done in the directory space, apart from at the resource type level. This is possible with search and subscriptions (which leverage search) by using search parameters on the resource types and setting the parameters of interest.</p>
<p style="margin-left: 0.0px;text-align: left;">When defining a subset of data, consideration should be given to what happens when data is changed such that it no longer is within the context of the conditions.</p>
<p style="margin-left: 0.0px;text-align: left;">One possibility would be to use a bundle of searches where each type has it's own search parameters, another is to use a <a href="http://hl7.org/fhir/r4/graphdefinition.html" class="external-link" rel="nofollow">GraphDefinition</a> resource.</p>
<p style="margin-left: 0.0px;text-align: left;">This functionality should be the subject of a connectathon to determine practical solutions.</p>
<p style="margin-left: 0.0px;text-align: left;">One possibility could be to leverage the List functionality described above to maintain a state of what <em>was</em> included in a previous content, however this obviously incurs additional overhead on the part of the server, and for many systems - especially those at scale like a national system - this is likely not practical.</p>
<h3 id="BulkDataandDirectories-Formatofthebulkdataextract">Format of the bulk data extract</h3>
<p style="margin-left: 0.0px;text-align: left;">The bulk extract format is always an nd-json file (new-line delimited json), and each file can only contain 1 resource type in it, but can be spread across multiple files, with either a size limit or count limit imposed by the extracting system, not the requestor.</p>
<p style="margin-left: 0.0px;text-align: left;">The list of these files will be returned in the Complete status output, as described in the standard Bulk Data documentation.</p>
<h3 id="BulkDataandDirectories-Startingtheextract">Starting the extract</h3>
<p style="margin-left: 0.0px;text-align: left;">There are 2 options for starting the extract, one that is a single operation specifying all the content, and the other to be for a specific type only. These were both covered in the selecting the scope section above.</p>
<p style="margin-left: 0.0px;text-align: left;">Here I will only document the use of the global export, as an initial request.</p>
<p style="margin-left: 0.0px;text-align: left;">The initial request:</p>
<div class="table-wrap">
<table class="wrapped confluenceTable" style="text-align: left;margin-left: 0.0px;">
<colgroup>
<col/>
</colgroup>
<tbody style="text-align: left;margin-left: 0.0px;">
<tr style="text-align: left;margin-left: 0.0px;">
<td style="text-align: left;" class="confluenceTd">
<p style="margin-left: 0.0px;text-align: left;">
<code class="java plain" style="text-align: left;margin-left: 0.0px;">GET [base]/$export?_type=Organization,Location,Practitioner,PractitionerRole,HealthcareService</code>
<br/>
<code class="java plain" style="text-align: left;margin-left: 0.0px;">with headers:</code>
<br/>
<code class="java plain" style="text-align: left;margin-left: 0.0px;">Accept: application/fhir+json</code>
<br/>
<code class="java plain" style="text-align: left;margin-left: 0.0px;">Authentication: Bearer [bearer token]</code>
<br/>
<code class="java plain" style="text-align: left;margin-left: 0.0px;">Prefer: respond-async</code>
</p>
</td>
</tr>
</tbody>
</table>
</div>
<p style="margin-left: 0.0px;text-align: left;">This will return either:</p>
<ul style="text-decoration: none;text-align: left;margin-left: 0.0px;">
<li style="list-style-type: disc;">a status 4XX or 5XX with an <code>OperationOutcome</code> resource body if the request fails,</li>
<li style="list-style-type: disc;">or a status 202 Accepted when successful, with a <code>Content-Location</code>
<span style="color: rgb(36,41,46);text-decoration: none;"> header with an absolute URI for subsequent status requests, and optionally an <code>OperationOutcome</code> in the resource body if desired</span>
</li>
</ul>
<p style="margin-left: 0.0px;text-align: left;">
<span style="color: rgb(36,41,46);text-decoration: none;">Example Content-Location: <a class="external-link" style="text-decoration: underline;text-align: left;" rel="nofollow" href="http://example.org/status-tracking/request-123">http://example.org/status-tracking/request-123</a> (note that this is not necessarily a FHIR endpoint, and isn't a true FHIR resource)</span>
</p>
<h3 style="margin-left: 0.0px;text-align: left;" id="BulkDataandDirectories-Trackingthestatusoftheextract">
<span style="color: rgb(36,41,46);text-decoration: none;">Tracking the status of the extract</span>
</h3>
<p style="margin-left: 0.0px;text-align: left;">
<span style="color: rgb(36,41,46);text-decoration: none;">After a bulk data request has been started, the client MAY poll the URI provided in the </span>
<code style="text-decoration: none;text-align: left;margin-left: 0.0px;">Content-Location</code>
<span style="color: rgb(36,41,46);text-decoration: none;"> header.</span>
</p>
<div class="table-wrap">
<table class="wrapped confluenceTable" style="text-align: left;margin-left: 0.0px;">
<colgroup>
<col/>
</colgroup>
<tbody style="text-align: left;margin-left: 0.0px;">
<tr style="text-align: left;margin-left: 0.0px;">
<td style="text-align: left;" class="confluenceTd">
<p style="margin-left: 0.0px;text-align: left;">
<code class="java plain" style="text-align: left;margin-left: 0.0px;">GET http:</code>
<code class="java comments" style="text-align: left;margin-left: 0.0px;">//<a href="http://example.org/status-tracking/request-123" class="external-link" rel="nofollow">example.org/status-tracking/request-123</a>
</code>
</p>
</td>
</tr>
</tbody>
</table>
</div>
<p style="margin-left: 0.0px;text-align: left;">This will return:</p>
<ul style="text-decoration: none;text-align: left;margin-left: 0.0px;">
<li style="list-style-type: disc;">
<span style="color: rgb(36,41,46);text-decoration: none;">HTTP Status Code of </span>
<code style="text-decoration: none;text-align: left;margin-left: 0.0px;">202 Accepted</code> when still in progress (and no body returned)</li>
<li style="list-style-type: disc;">
<span style="color: rgb(36,41,46);text-decoration: none;">HTTP status code of </span>
<code style="text-decoration: none;text-align: left;margin-left: 0.0px;">5XX</code> when a fatal error occurs, and an <code>OperationOutcome</code> in json format for the body with the detail of the error<br style="margin-left: 0.0px;"/>(Note this is a fatal error in processing, not some error encountered while processing files - a complete extract can contain errors)</li>
<li style="list-style-type: disc;">
<span style="color: rgb(36,41,46);text-decoration: none;">HTTP status of </span>
<code style="text-decoration: none;text-align: left;margin-left: 0.0px;">200 OK</code> when the processing is complete, and the result is a json object as noted in the specification (and an example included below)</li>
</ul>
<p style="margin-left: 0.0px;text-align: left;">Refer to the build data specification for details of the completion event:</p>
<p style="margin-left: 0.0px;text-align: left;">
<a style="text-decoration: none;" href="https://github.com/smart-on-fhir/fhir-bulk-data-docs/blob/master/export.md#response---complete-status" rel="nofollow" class="external-link">https://github.com/smart-on-fhir/fhir-bulk-data-docs/blob/master/export.md#response---complete-status</a>
</p>
<div class="table-wrap">
<table class="wrapped confluenceTable" style="text-align: left;margin-left: 0.0px;">
<colgroup>
<col/>
</colgroup>
<tbody style="text-align: left;margin-left: 0.0px;">
<tr style="text-align: left;margin-left: 0.0px;">
<td style="text-align: left;" class="confluenceTd">
<p style="margin-left: 0.0px;text-align: left;">
<code class="js plain" style="text-align: left;margin-left: 0.0px;">{</code>
<br/>
<code class="js spaces" style="text-align: left;margin-left: 0.0px;">
</code>
<code class="js string" style="text-align: left;margin-left: 0.0px;">&quot;transactionTime&quot;</code>
<code class="js plain" style="text-align: left;margin-left: 0.0px;">: </code>
<code class="js string" style="text-align: left;margin-left: 0.0px;">&quot;[instant]&quot;</code>
<code class="js plain" style="text-align: left;margin-left: 0.0px;">,</code>
<br/>
<code class="js spaces" style="text-align: left;margin-left: 0.0px;">
</code>
<code class="js string" style="text-align: left;margin-left: 0.0px;">&quot;request&quot;</code>
<code class="js plain" style="text-align: left;margin-left: 0.0px;">: </code>
<code class="js string" style="text-align: left;margin-left: 0.0px;">&quot;[base]/$export?_type=Organization,Location,Practitioner,PractitionerRole,HealthcareService&quot;</code>
<code class="js plain" style="text-align: left;margin-left: 0.0px;">, </code>
<br/>
<code class="js spaces" style="text-align: left;margin-left: 0.0px;">
</code>
<code class="js string" style="text-align: left;margin-left: 0.0px;">&quot;requiresAccessToken&quot;</code>
<code class="js plain" style="text-align: left;margin-left: 0.0px;">: </code>
<code class="js keyword" style="text-align: left;margin-left: 0.0px;">true</code>
<code class="js plain" style="text-align: left;margin-left: 0.0px;">,</code>
<br/>
<code class="js spaces" style="text-align: left;margin-left: 0.0px;">
</code>
<code class="js string" style="text-align: left;margin-left: 0.0px;">&quot;output&quot;</code>
<code class="js plain" style="text-align: left;margin-left: 0.0px;">: [{</code>
<br/>
<code class="js spaces" style="text-align: left;margin-left: 0.0px;">
</code>
<code class="js string" style="text-align: left;margin-left: 0.0px;">&quot;type&quot;</code>
<code class="js plain" style="text-align: left;margin-left: 0.0px;">: </code>
<code class="js string" style="text-align: left;margin-left: 0.0px;">&quot;Practitioner&quot;</code>
<code class="js plain" style="text-align: left;margin-left: 0.0px;">,</code>
<br/>
<code class="js spaces" style="text-align: left;margin-left: 0.0px;">
</code>
<code class="js string" style="text-align: left;margin-left: 0.0px;">&quot;url&quot;</code>
<code class="js plain" style="text-align: left;margin-left: 0.0px;">: </code>
<code class="js string" style="text-align: left;margin-left: 0.0px;">&quot;<a href="http://serverpath2/practitioner_file_1.ndjson" style="text-decoration: none;text-align: left;margin-left: 0.0px;" class="external-link" rel="nofollow">http://serverpath2/practitioner_file_1.ndjson</a>&quot;</code>
<code class="js plain" style="text-align: left;margin-left: 0.0px;">,</code>
<br/>
<code class="js spaces" style="text-align: left;margin-left: 0.0px;">
</code>
<code class="js string" style="text-align: left;margin-left: 0.0px;">&quot;count&quot;</code>
<code class="js plain" style="text-align: left;margin-left: 0.0px;">: 10000</code>
<br/>
<code class="js spaces" style="text-align: left;margin-left: 0.0px;">
</code>
<code class="js plain" style="text-align: left;margin-left: 0.0px;">},{</code>
<br/>
<code class="js spaces" style="text-align: left;margin-left: 0.0px;">
</code>
<code class="js string" style="text-align: left;margin-left: 0.0px;">&quot;type&quot;</code>
<code class="js plain" style="text-align: left;margin-left: 0.0px;">: </code>
<code class="js string" style="text-align: left;margin-left: 0.0px;">&quot;Practitioner&quot;</code>
<code class="js plain" style="text-align: left;margin-left: 0.0px;">,</code>
<br/>
<code class="js spaces" style="text-align: left;margin-left: 0.0px;">
</code>
<code class="js string" style="text-align: left;margin-left: 0.0px;">&quot;url&quot;</code>
<code class="js plain" style="text-align: left;margin-left: 0.0px;">: </code>
<code class="js string" style="text-align: left;margin-left: 0.0px;">&quot;<a href="http://serverpath2/practitioner_file_2.ndjson" style="text-decoration: none;text-align: left;margin-left: 0.0px;" class="external-link" rel="nofollow">http://serverpath2/practitioner_file_2.ndjson</a>&quot;</code>
<code class="js plain" style="text-align: left;margin-left: 0.0px;">,</code>
<br/>
<code class="js spaces" style="text-align: left;margin-left: 0.0px;">
</code>
<code class="js string" style="text-align: left;margin-left: 0.0px;">&quot;count&quot;</code>
<code class="js plain" style="text-align: left;margin-left: 0.0px;">: 3017</code>
<br/>
<code class="js spaces" style="text-align: left;margin-left: 0.0px;">
</code>
<code class="js plain" style="text-align: left;margin-left: 0.0px;">},{</code>
<br/>
<code class="js spaces" style="text-align: left;margin-left: 0.0px;">
</code>
<code class="js string" style="text-align: left;margin-left: 0.0px;">&quot;type&quot;</code>
<code class="js plain" style="text-align: left;margin-left: 0.0px;">: </code>
<code class="js string" style="text-align: left;margin-left: 0.0px;">&quot;Location&quot;</code>
<code class="js plain" style="text-align: left;margin-left: 0.0px;">,</code>
<br/>
<code class="js spaces" style="text-align: left;margin-left: 0.0px;">
</code>
<code class="js string" style="text-align: left;margin-left: 0.0px;">&quot;url&quot;</code>
<code class="js plain" style="text-align: left;margin-left: 0.0px;">: </code>
<code class="js string" style="text-align: left;margin-left: 0.0px;">&quot;<a href="http://serverpath2/location_file_1.ndjson" style="text-decoration: none;text-align: left;margin-left: 0.0px;" class="external-link" rel="nofollow">http://serverpath2/location_file_1.ndjson</a>&quot;</code>
<code class="js plain" style="text-align: left;margin-left: 0.0px;">,</code>
<br/>
<code class="js spaces" style="text-align: left;margin-left: 0.0px;">
</code>
<code class="js string" style="text-align: left;margin-left: 0.0px;">&quot;count&quot;</code>
<code class="js plain" style="text-align: left;margin-left: 0.0px;">: 4182</code>
<br/>
<code class="js spaces" style="text-align: left;margin-left: 0.0px;">
</code>
<code class="js plain" style="text-align: left;margin-left: 0.0px;">}],</code>
</p>
<p style="margin-left: 0.0px;text-align: left;">// Note that this deletions property is a proposal, not part of the bulk data spec.<br/>
<code class="js spaces" style="text-align: left;margin-left: 0.0px;">
<code class="js string" style="text-decoration: none;text-align: left;margin-left: 0.0px;">&quot;deletions&quot;</code>
<span style="color: rgb(23,43,77);text-decoration: none;">
</span>
<code class="js plain" style="text-decoration: none;text-align: left;margin-left: 0.0px;">: [{</code>
<br style="text-decoration: none;text-align: left;margin-left: 0.0px;"/>
<code class="js spaces" style="text-decoration: none;text-align: left;margin-left: 0.0px;">
</code>
<code class="js string" style="text-decoration: none;text-align: left;margin-left: 0.0px;">&quot;type&quot;</code>
<span style="color: rgb(23,43,77);text-decoration: none;">
</span>
<code class="js plain" style="text-decoration: none;text-align: left;margin-left: 0.0px;">: </code>
<code class="js string" style="text-decoration: none;text-align: left;margin-left: 0.0px;">&quot;PractitionerRole&quot;</code>
<code class="js plain" style="text-decoration: none;text-align: left;margin-left: 0.0px;">,</code>
<br style="text-decoration: none;text-align: left;margin-left: 0.0px;"/>
<code class="js spaces" style="text-decoration: none;text-align: left;margin-left: 0.0px;">
</code>
<code class="js string" style="text-decoration: none;text-align: left;margin-left: 0.0px;">&quot;url&quot;</code>
<span style="color: rgb(23,43,77);text-decoration: none;">
</span>
<code class="js plain" style="text-decoration: none;text-align: left;margin-left: 0.0px;">: </code>
<code class="js string" style="text-decoration: none;text-align: left;margin-left: 0.0px;">&quot;<a style="text-decoration: none;text-align: left;margin-left: 0.0px;" href="http://serverpath2/err_file_1.ndjson" class="external-link" rel="nofollow">http://serverpath2/practitionerrole_deletions_1.ndjson</a>&quot;</code>
<code class="js plain" style="text-decoration: none;text-align: left;margin-left: 0.0px;">, // the bundle will include the total</code> number of deletions in the file<br style="text-decoration: none;text-align: left;margin-left: 0.0px;"/>
<code class="js spaces" style="text-decoration: none;text-align: left;margin-left: 0.0px;">
</code>
<code class="js string" style="text-decoration: none;text-align: left;margin-left: 0.0px;">&quot;count&quot;</code>
<span style="color: rgb(23,43,77);text-decoration: none;">
</span>
<code class="js plain" style="text-decoration: none;text-align: left;margin-left: 0.0px;">: 23 // this is the number of bundles in the file, not the number of resources deleted</code>
<br style="text-decoration: none;text-align: left;margin-left: 0.0px;"/>
<code class="js spaces" style="text-decoration: none;text-align: left;margin-left: 0.0px;">
</code>
<code class="js plain" style="text-decoration: none;text-align: left;margin-left: 0.0px;">}]</code>,</code>
</p>
<p style="margin-left: 0.0px;text-align: left;">
<code class="js spaces" style="text-align: left;margin-left: 0.0px;">
</code>
<code class="js string" style="text-align: left;margin-left: 0.0px;">&quot;error&quot;</code>
<code class="js plain" style="text-align: left;margin-left: 0.0px;">: [{</code>
<br/>
<code class="js spaces" style="text-align: left;margin-left: 0.0px;">
</code>
<code class="js string" style="text-align: left;margin-left: 0.0px;">&quot;type&quot;</code>
<code class="js plain" style="text-align: left;margin-left: 0.0px;">: </code>
<code class="js string" style="text-align: left;margin-left: 0.0px;">&quot;OperationOutcome&quot;</code>
<code class="js plain" style="text-align: left;margin-left: 0.0px;">,</code>
<br/>
<code class="js spaces" style="text-align: left;margin-left: 0.0px;">
</code>
<code class="js string" style="text-align: left;margin-left: 0.0px;">&quot;url&quot;</code>
<code class="js plain" style="text-align: left;margin-left: 0.0px;">: </code>
<code class="js string" style="text-align: left;margin-left: 0.0px;">&quot;<a style="text-decoration: none;text-align: left;margin-left: 0.0px;" href="http://serverpath2/err_file_1.ndjson" class="external-link" rel="nofollow">http://serverpath2/err_file_1.ndjson</a>&quot;</code>
<code class="js plain" style="text-align: left;margin-left: 0.0px;">,</code>
<br/>
<code class="js spaces" style="text-align: left;margin-left: 0.0px;">
</code>
<code class="js string" style="text-align: left;margin-left: 0.0px;">&quot;count&quot;</code>
<code class="js plain" style="text-align: left;margin-left: 0.0px;">: 439</code>
<br/>
<code class="js spaces" style="text-align: left;margin-left: 0.0px;">
</code>
<code class="js plain" style="text-align: left;margin-left: 0.0px;">}]</code>
<br/>
<code class="js spaces" style="text-align: left;margin-left: 0.0px;">
</code>
<code class="js plain" style="text-align: left;margin-left: 0.0px;">}</code>
</p>
</td>
</tr>
</tbody>
</table>
</div>
<p style="margin-left: 0.0px;text-align: left;">
<br/>
</p>
<h3 style="text-decoration: none;text-align: left;margin-left: 0.0px;" id="BulkDataandDirectories-Retrievingthecompleteextract">Retrieving the complete extract</h3>
<p style="margin-left: 0.0px;text-align: left;">Once the tracking of the extract returns a <strong style="margin-left: 0.0px;">200 OK</strong> completed status, the body of the result will include the list of prepared files that you can download.</p>
<p style="margin-left: 0.0px;text-align: left;">Then each of these URLs can be downloaded by a simple get, ensuring to pass the Bearer token if the result indicates <strong style="margin-left: 0.0px;">
<span style="color: rgb(3,47,98);text-decoration: none;">requiresAccessToken</span> = true</strong>
</p>
<p style="margin-left: 0.0px;text-align: left;">While downloading, also recommend including the header Accept-Encoding: gzip to compress the content as it comes down.</p>
<div class="table-wrap">
<table class="wrapped confluenceTable" style="text-align: left;margin-left: 0.0px;">
<colgroup>
<col/>
</colgroup>
<tbody style="text-align: left;margin-left: 0.0px;">
<tr style="text-align: left;margin-left: 0.0px;">
<td style="text-align: left;" class="confluenceTd">
<p style="margin-left: 0.0px;text-align: left;">
<code class="java plain" style="text-align: left;margin-left: 0.0px;">GET http:</code>
<code class="java comments" style="text-align: left;margin-left: 0.0px;">//serverpath2/location_file_1.ndjson</code>
</p>
</td>
</tr>
</tbody>
</table>
</div>
<p style="margin-left: 0.0px;text-align: left;">(Note: our implementation will probably always gzip encode the content - as we are likely to store the processing files gzip encoded to save space in the storage system)</p>
<p style="margin-left: 0.0px;text-align: left;">Once you have downloaded all the files you need, you should tell the server to cleanup, which is detailed next.</p>
<h3 style="text-decoration: none;text-align: left;margin-left: 0.0px;" id="BulkDataandDirectories-Finishingtheextract">Finishing the extract</h3>
<p style="margin-left: 0.0px;text-align: left;">This is the simplest part of the process, and that is just calling <strong style="margin-left: 0.0px;">DELETE</strong> on the status tracking URL.</p>
<div class="table-wrap">
<table class="wrapped confluenceTable" style="text-align: left;margin-left: 0.0px;">
<colgroup>
<col/>
</colgroup>
<tbody style="text-align: left;margin-left: 0.0px;">
<tr style="text-align: left;margin-left: 0.0px;">
<td style="text-align: left;" class="confluenceTd">
<p style="margin-left: 0.0px;text-align: left;">
<code class="java plain" style="text-align: left;margin-left: 0.0px;">DELETE http:</code>
<code class="java comments" style="text-align: left;margin-left: 0.0px;">//<a href="http://example.org/status-tracking/request-123" class="external-link" rel="nofollow">example.org/status-tracking/request-123</a>
</code>
</p>
</td>
</tr>
</tbody>
</table>
</div>
<p style="margin-left: 0.0px;text-align: left;">This then tells the server that we are all finished with the data, and it can be deleted/cleaned up. The server may also include some time based limits where it may only keep it for a set period of time before it automatically cleans it up.</p>
<p style="margin-left: 0.0px;text-align: left;">
<span style="color: rgb(36,41,46);text-decoration: none;">
<br/>
</span>
</p>
<h2 style="margin-left: 0.0px;text-align: left;" id="BulkDataandDirectories-Subscriptions">Subscriptions</h2>
<p style="margin-left: 0.0px;text-align: left;">A close relative to the bulk data extract is the subscriptions content - and how these will work in the context of Bulk Directory exchanges needs further experimentation and connectathon experiences.</p>
<p style="margin-left: 0.0px;text-align: left;">These could be setup to monitor the directory for realtime changes to resources of interest, and are defined through the use of search parameters</p>
<p style="margin-left: 0.0px;text-align: left;">The &quot;urgent notifications&quot; channel is yet to be defined, but should enable specific actions such as license suspensions/revocations.</p>
<p style="margin-left: 0.0px;text-align: left;">
<br/>
</p>

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
