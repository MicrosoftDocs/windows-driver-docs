---
title: JobToken element
description: The required JobToken element contains the device-created token for a new scan job.
ms.assetid: 09446fc0-074a-4f54-93fa-55b4dd467fad
keywords: ["JobToken element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn JobToken
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# JobToken element


The required **JobToken** element contains the device-created token for a new scan job.

Usage
-----

```xml
<wscn:JobToken>
  text
</wscn:JobToken>
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
<td><p><a href="createscanjobresponse.md" data-raw-source="[&lt;strong&gt;CreateScanJobResponse&lt;/strong&gt;](createscanjobresponse.md)"><strong>CreateScanJobResponse</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="retrieveimagerequest.md" data-raw-source="[&lt;strong&gt;RetrieveImageRequest&lt;/strong&gt;](retrieveimagerequest.md)"><strong>RetrieveImageRequest</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **JobToken** element is paired with the [**JobId**](jobid.md) element to uniquely represent a specific scan job. **JobToken** is passed to the scan device in the [**RetrieveImageRequest**](retrieveimagerequest.md) operation element to enable the device to verify that the scan requester actually created the scan job.

## See also


[**CreateScanJobResponse**](createscanjobresponse.md)

[**JobId**](jobid.md)

[**RetrieveImageRequest**](retrieveimagerequest.md)

 

 






