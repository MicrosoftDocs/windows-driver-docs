---
title: JobOriginatingUserName element
description: The required JobOriginatingUserName element specifies the name of the user who submitted the scan job.
ms.assetid: ba2dd472-1ac0-40bd-816c-02abc093b6ed
keywords: ["JobOriginatingUserName element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn JobOriginatingUserName
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# JobOriginatingUserName element


The required **JobOriginatingUserName** element specifies the name of the user who submitted the scan job.

Usage
-----

```xml
<wscn:JobOriginatingUserName>
  text
</wscn:JobOriginatingUserName>
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

The client or the security infrastructure, if any, provides the **JobOriginatingUserName** element. A client should supply a value to help users easily distinguish between the jobs that they submitted and jobs that other users submitted.

The WSD Scan Service can provide a default **JobOriginatingUserName** name in its [**DefaultScanTicket**](defaultscanticket.md) element. You can set this name in an implementation-specific manner.

The name of the job is specified in the [**JobName**](jobname.md) element.

## See also


[**DefaultScanTicket**](defaultscanticket.md)

[**JobDescription**](jobdescription.md)

[**JobEndState**](jobendstate.md)

[**JobName**](jobname.md)

[**JobSummary**](jobsummary.md)

 

 






