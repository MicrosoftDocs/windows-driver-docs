---
title: WIA\_IPS\_OVER\_SCAN
description: The WIA\_IPS\_OVER\_SCAN property is used to enable and configure over scanning (scanning beyond physical document boundaries). The WIA minidriver creates and maintains this property.
ms.assetid: CAE654BE-B0AC-4182-83CE-C2BDA4792FE4
keywords: ["WIA_IPS_OVER_SCAN Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_OVER_SCAN
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/22/2018
ms.localizationpriority: medium
---

# WIA\_IPS\_OVER\_SCAN


The **WIA\_IPS\_OVER\_SCAN** property is used to enable and configure over scanning (scanning beyond physical document boundaries). The WIA minidriver creates and maintains this property.




Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/Write

Remarks
-------

The following table describes the valid values for the **WIA\_IPS\_OVER\_SCAN** property.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>WIA_OVER_SCAN_DISABLED</p></td>
<td><p>Over scanning is disabled. This is the required default value if the property is supported.</p></td>
</tr>
<tr class="even">
<td><p>WIA_ OVER_SCAN_TOP_BOTTOM</p></td>
<td><p>Over scan at the top and bottom sides of the document.</p></td>
</tr>
<tr class="odd">
<td><p>WIA_ OVER_SCAN_LEFT_RIGHT</p></td>
<td><p>Over scan at the left and right sides of the document.</p></td>
</tr>
<tr class="even">
<td><p>WIA_ OVER_SCAN_ ALL</p></td>
<td><p>Over scan at all sides of the document.</p></td>
</tr>
</tbody>
</table>

 

This property is valid for all programmable image data source items, including Flatbed (WIA\_CATEGORY\_FLATBED) and Feeder (WIA\_CATEGORY\_FEEDER) and is optional. When the property is supported, WIA\_OVER\_SCAN\_DISABLED is the required default value.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

 

 





