---
title: BrightnessSupported element
description: The required BrightnessSupported element specifies whether the scan device supports user control of the scan brightness setting.
ms.assetid: aa0eb627-694f-45a1-a923-07fc04b0612b
keywords: ["BrightnessSupported element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn BrightnessSupported
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# BrightnessSupported element


The required **BrightnessSupported** element specifies whether the scan device supports user control of the scan brightness setting.

Usage
-----

```xml
<wscn:BrightnessSupported>
  text
</wscn:BrightnessSupported>
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

If the scan device allows user control of the scan brightness setting, the WSD Scan Service should return 1 (**true**); otherwise, it should return 0 (**false**).

You cannot extend the allowed values for this element.

## See also


[**DeviceSettings**](devicesettings.md)

 

 






