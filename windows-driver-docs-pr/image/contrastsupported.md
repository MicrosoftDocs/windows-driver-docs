---
title: ContrastSupported element
description: The required ContrastSupported element specifies whether the scan device supports user control of the scan contrast setting.
ms.assetid: 9b865f9f-b5f6-4bb3-9f24-3df896845e96
keywords: ["ContrastSupported element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ContrastSupported
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# ContrastSupported element


The required **ContrastSupported** element specifies whether the scan device supports user control of the scan contrast setting.

Usage
-----

```xml
<wscn:ContrastSupported>
  text
</wscn:ContrastSupported>
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
<td><p><a href="devicesettings.md" data-raw-source="[&lt;strong&gt;DeviceSettings&lt;/strong&gt;](devicesettings.md)"><strong>DeviceSettings</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

If the scan device allows user control of the scan contrast setting, the WSD Scan Service should return 1 (**true**); otherwise, it should return 0 (**false**).

You cannot extend the allowed values for this element.

## See also


[**DeviceSettings**](devicesettings.md)

 

 






