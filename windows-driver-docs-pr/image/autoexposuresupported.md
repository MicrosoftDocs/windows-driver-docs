---
title: AutoExposureSupported element
description: The required AutoExposureSupported element specifies whether the scan device supports automatic adjustment of the various exposure settings.
ms.assetid: 36ef003f-b049-4eb2-8fe3-53aa77db3065
keywords: ["AutoExposureSupported element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn AutoExposureSupported
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# AutoExposureSupported element


The required **AutoExposureSupported** element specifies whether the scan device supports automatic adjustment of the various exposure settings.

Usage
-----

```xml
<wscn:AutoExposureSupported>
  text
</wscn:AutoExposureSupported>
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

[**Exposure**](exposure.md)

If the scan device supports automatic adjustment of various [**Exposure**](exposure.md) settings, the WSD Scan Service should return 1 (**true**); otherwise, it should return 0 (**false**).

You cannot extend the allowed values for this element.

## See also


[**DeviceSettings**](devicesettings.md)

[**Exposure**](exposure.md)

 

 






