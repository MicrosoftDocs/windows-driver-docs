---
title: Proximity Sensor Property
description: This property is an optional enumeration property.
ms.assetid: 574955CC-F8BF-4E8C-9A9A-E06802C5DB0C
ms.author: windowsdriverdev
ms.date: 01/04/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Proximity Sensor Property


\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

This property is an optional enumeration property.

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Property key</th>
<th>Type</th>
<th>Access (R/O, R/W)</th>
<th>Required/Optional</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>DEVPKEY_Sensor_ProximityType</p></td>
<td><p>VT_UI4</p></td>
<td><p>R/O</p></td>
<td><p>Optional</p></td>
<td><p>Describes the type of proximity being detected. It can be HumanProximity or ObjectProximity. For more information, see the ProximityType enumeration.</p></td>
</tr>
</tbody>
</table>

 

## <span id="Requirements"></span><span id="requirements"></span><span id="REQUIREMENTS"></span>Requirements


**Header:** Sensorsdef.h

## <span id="related_topics"></span>Related topics


[Other sensor properties](other-sensor-properties.md)

 

 






