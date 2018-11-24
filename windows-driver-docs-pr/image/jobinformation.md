---
title: JobInformation element
description: The optional JobInformation element describes the intended use of the job.
ms.assetid: 0e5d41a0-49df-43db-a2e6-3639e60d2378
keywords: ["JobInformation element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn JobInformation
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# JobInformation element


The optional **JobInformation** element describes the intended use of the job.

Usage
-----

```xml
<wscn:JobInformation>
  text
</wscn:JobInformation>
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
</tbody>
</table>

Remarks
-------

The **JobInformation** value is useful when the client will reuse the scan ticket that is used to create the job.

## See also


[**JobDescription**](jobdescription.md)

 

 






