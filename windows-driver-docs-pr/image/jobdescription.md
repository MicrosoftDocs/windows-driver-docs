---
title: JobDescription element
description: The required JobDescription element contains basic creation information for the currently identified job.
ms.assetid: 78b77a9b-2fe9-4261-996b-970e97c4c0a9
keywords: ["JobDescription element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn JobDescription
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# JobDescription element


The required **JobDescription** element contains basic creation information for the currently identified job.

Usage
-----

```xml
<wscn:JobDescription>
  child elements
</wscn:JobDescription>
```

Attributes
----------

There are no attributes.

## Child elements


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
<td><p>[<strong>JobInformation</strong>](jobinformation.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>JobName</strong>](jobname.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>JobOriginatingUserName</strong>](joboriginatingusername.md)</p></td>
</tr>
</tbody>
</table>

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
<td><p>[<strong>DefaultScanTicket</strong>](defaultscanticket.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ScanTicket</strong>](scanticket.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

A client sets the values for all **JobDescription** child elements and submits them in a [**CreateScanJobRequest**](createscanjobrequest.md) operation.

## See also


[**CreateScanJobRequest**](createscanjobrequest.md)

[**DefaultScanTicket**](defaultscanticket.md)

[**JobInformation**](jobinformation.md)

[**JobName**](jobname.md)

[**JobOriginatingUserName**](joboriginatingusername.md)

[**ScanTicket**](scanticket.md)

 

 






