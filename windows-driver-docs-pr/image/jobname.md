---
title: JobName element
description: The required JobName element specifies the client-supplied, user-friendly name of the scan job.
ms.assetid: b6d2baba-6a2e-4971-880b-9a4df66dc1ae
keywords: ["JobName element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn JobName
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# JobName element


The required **JobName** element specifies the client-supplied, user-friendly name of the scan job.

Usage
-----

```xml
<wscn:JobName>
  text
</wscn:JobName>
```

Attributes
----------

There are no attributes.

Text value
----------

Required. Any valid character string.

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
<td><p><a href="jobdescription.md" data-raw-source="[&lt;strong&gt;JobDescription&lt;/strong&gt;](jobdescription.md)"><strong>JobDescription</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="jobendstate.md" data-raw-source="[&lt;strong&gt;JobEndState&lt;/strong&gt;](jobendstate.md)"><strong>JobEndState</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><a href="jobsummary.md" data-raw-source="[&lt;strong&gt;JobSummary&lt;/strong&gt;](jobsummary.md)"><strong>JobSummary</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

A client should supply a value to help users easily distinguish between jobs that they submitted.

The WSD Scan Service can provide a default **JobName** name in its [**DefaultScanTicket**](defaultscanticket.md) element. You can set this name in an implementation-specific manner.

The name of the user who submitted the job is specified in the [**JobOriginatingUserName**](joboriginatingusername.md) element.

## See also


[**DefaultScanTicket**](defaultscanticket.md)

[**JobDescription**](jobdescription.md)

[**JobEndState**](jobendstate.md)

[**JobOriginatingUserName**](joboriginatingusername.md)

[**JobSummary**](jobsummary.md)

 

 






