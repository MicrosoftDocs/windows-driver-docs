---
title: ScanData element
description: The required ScanData element contains the binary data that represents the scanned image.
ms.assetid: 9b29224c-b1e1-4c64-8a4a-476f9d6eea45
keywords: ["ScanData element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ScanData
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# ScanData element


The required **ScanData** element contains the binary data that represents the scanned image.

Usage
-----

```xml
<wscn:ScanData/>
```

Attributes
----------

There are no attributes.

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
<td><p><a href="retrieveimageresponse.md" data-raw-source="[&lt;strong&gt;RetrieveImageResponse&lt;/strong&gt;](retrieveimageresponse.md)"><strong>RetrieveImageResponse</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **ScanData** element contains an **xop:Include** element that specifies the location of the scan data relative to the SOAP Envelope/Body of a [**RetrieveImageResponse**](retrieveimageresponse.md) operation element. The actual scan data is appended to the SOAP Envelope/Body as a binary attachment.

## See also


[**RetrieveImageResponse**](retrieveimageresponse.md)

 

 






