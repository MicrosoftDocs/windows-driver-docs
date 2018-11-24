---
title: JobId element
description: The required JobId element uniquely identifies a job within a scanner.
ms.assetid: ae9199c1-c45a-4147-b4f0-f37a9a0f1b22
keywords: ["JobId element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn JobId
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# JobId element


The required **JobId** element uniquely identifies a job within a scanner.

Usage
-----

```xml
<wscn:JobId>
  text
</wscn:JobId>
```

Attributes
----------

There are no attributes.

Text value
----------

Required. An integer value from 1 through 2147483648.

## Child elements


There are no child elements.

## Parent elements


<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th>Element</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="canceljobrequest.md" data-raw-source="[&lt;strong&gt;CancelJobRequest&lt;/strong&gt;](canceljobrequest.md)"><strong>CancelJobRequest</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="createscanjobresponse.md" data-raw-source="[&lt;strong&gt;CreateScanJobResponse&lt;/strong&gt;](createscanjobresponse.md)"><strong>CreateScanJobResponse</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><a href="getjobelementsrequest.md" data-raw-source="[&lt;strong&gt;GetJobElementsRequest&lt;/strong&gt;](getjobelementsrequest.md)"><strong>GetJobElementsRequest</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="jobendstate.md" data-raw-source="[&lt;strong&gt;JobEndState&lt;/strong&gt;](jobendstate.md)"><strong>JobEndState</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><a href="jobstatus.md" data-raw-source="[&lt;strong&gt;JobStatus&lt;/strong&gt;](jobstatus.md)"><strong>JobStatus</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="jobsummary.md" data-raw-source="[&lt;strong&gt;JobSummary&lt;/strong&gt;](jobsummary.md)"><strong>JobSummary</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><a href="retrieveimagerequest.md" data-raw-source="[&lt;strong&gt;RetrieveImageRequest&lt;/strong&gt;](retrieveimagerequest.md)"><strong>RetrieveImageRequest</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The WSD Scan Service returns a **JobId** element to a client through a [**CreateScanJobResponse**](createscanjobresponse.md) operation element. The client uses the returned **JobId** when it initiates a scan request through the [**RetrieveImageRequest**](retrieveimagerequest.md) operation element.

**JobId** does not need to be globally unique. The WSD Scan Service should not reuse a recently assigned value so that a client does not confuse a current scan job with an older job.

You cannot extend the allowed values for the **JobId** element.

## See also


[**CancelJobRequest**](canceljobrequest.md)

[**CreateScanJobResponse**](createscanjobresponse.md)

[**GetJobElementsRequest**](getjobelementsrequest.md)

[**JobEndState**](jobendstate.md)

[**JobStatus**](jobstatus.md)

[**JobSummary**](jobsummary.md)

[**RetrieveImageRequest**](retrieveimagerequest.md)

 

 






