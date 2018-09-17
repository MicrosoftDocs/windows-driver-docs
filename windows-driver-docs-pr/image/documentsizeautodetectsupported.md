---
title: DocumentSizeAutoDetectSupported element
description: The required DocumentSizeAutoDetectSupported element indicates whether the scan device can detect the size of the original media.
ms.assetid: 38baea3d-85bf-44e1-86bf-349d17981efa
keywords: ["DocumentSizeAutoDetectSupported element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn DocumentSizeAutoDetectSupported
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# DocumentSizeAutoDetectSupported element


The required **DocumentSizeAutoDetectSupported** element indicates whether the scan device can detect the size of the original media.

Usage
-----

``` syntax
<wscn:DocumentSizeAutoDetectSupported>
  text
</wscn:DocumentSizeAutoDetectSupported>
```

Attributes
----------

There are no attributes.

Text value
----------

Required. A Boolean value that must be 0, 1, false, or true.**falsetrue**

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
<td><p>[<strong>DeviceSettings</strong>](devicesettings.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

If the scan device can detect the size of the original media, the WSD Scan Service should return 1 (**true**); otherwise, it should return 0 (**false**).

You cannot extend the allowed values for this element.

## <span id="see_also"></span>See also


[**DeviceSettings**](devicesettings.md)

 

 






