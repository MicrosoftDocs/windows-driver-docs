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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# JobToken element


The required **JobToken** element contains the device-created token for a new scan job.

Usage
-----

``` syntax
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
<td><p>[<strong>CreateScanJobResponse</strong>](createscanjobresponse.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>RetrieveImageRequest</strong>](retrieveimagerequest.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **JobToken** element is paired with the [**JobId**](jobid.md) element to uniquely represent a specific scan job. **JobToken** is passed to the scan device in the [**RetrieveImageRequest**](retrieveimagerequest.md) operation element to enable the device to verify that the scan requester actually created the scan job.

## <span id="see_also"></span>See also


[**CreateScanJobResponse**](createscanjobresponse.md)

[**JobId**](jobid.md)

[**RetrieveImageRequest**](retrieveimagerequest.md)

 

 






