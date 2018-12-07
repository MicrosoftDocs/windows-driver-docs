---
title: WIA\_IPS\_COLOR\_DROP
description: The WIA\_IPS\_COLOR\_DROP property is used to configure color filtering for the image data acquired from the hardware device. The WIA minidriver creates and maintains this property.
ms.assetid: A0F14FDF-194D-4948-B9D8-F3E0C2E34618
keywords: ["WIA_IPS_COLOR_DROP Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_COLOR_DROP
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_COLOR\_DROP


The **WIA\_IPS\_COLOR\_DROP** property is used to configure color filtering for the image data acquired from the hardware device. The WIA minidriver creates and maintains this property.



Property Type: VT\_I4 

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/Write

Remarks
-------

The following table describes the valid values for the **WIA\_IPS\_COLOR\_DROP** property.

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
<td><p>WIA_COLOR_DROP_DISABLED</p></td>
<td><p>Color drop is disabled. This is the required default value if the property is supported.</p></td>
</tr>
<tr class="even">
<td><p>WIA_COLOR_DROP_RED</p></td>
<td><p>The Red channel is dropped in the amount described by <a href="wia-ips-color-drop-red.md" data-raw-source="[&lt;strong&gt;WIA_IPS_COLOR_DROP_RED&lt;/strong&gt;](wia-ips-color-drop-red.md)"><strong>WIA_IPS_COLOR_DROP_RED</strong></a>.</p></td>
</tr>
<tr class="odd">
<td><p>WIA_COLOR_DROP_GREEN</p></td>
<td><p>The Green channel is dropped in the amount described by <a href="wia-ips-color-drop-green.md" data-raw-source="[&lt;strong&gt;WIA_IPS_COLOR_DROP_GREEN&lt;/strong&gt;](wia-ips-color-drop-green.md)"><strong>WIA_IPS_COLOR_DROP_GREEN</strong></a>.</p></td>
</tr>
<tr class="even">
<td><p>WIA_COLOR_DROP_BLUE</p></td>
<td><p>The Blue channel is dropped in the amount described by <a href="wia-ips-color-drop-blue.md" data-raw-source="[&lt;strong&gt;WIA_IPS_COLOR_DROP_BLUE&lt;/strong&gt;](wia-ips-color-drop-blue.md)"><strong>WIA_IPS_COLOR_DROP_BLUE</strong></a>.</p></td>
</tr>
<tr class="odd">
<td><p>WIA_COLOR_DROP_RGB</p></td>
<td><p>The Red, Green, and/or Blue channels are dropped in the amounts specified by <a href="wia-ips-color-drop-red.md" data-raw-source="[&lt;strong&gt;WIA_IPS_COLOR_DROP_RED&lt;/strong&gt;](wia-ips-color-drop-red.md)"><strong>WIA_IPS_COLOR_DROP_RED</strong></a>, <a href="wia-ips-color-drop-green.md" data-raw-source="[&lt;strong&gt;WIA_IPS_COLOR_DROP_GREEN&lt;/strong&gt;](wia-ips-color-drop-green.md)"><strong>WIA_IPS_COLOR_DROP_GREEN</strong></a>, and <a href="wia-ips-color-drop-blue.md" data-raw-source="[&lt;strong&gt;WIA_IPS_COLOR_DROP_BLUE&lt;/strong&gt;](wia-ips-color-drop-blue.md)"><strong>WIA_IPS_COLOR_DROP_BLUE</strong></a>.</p></td>
</tr>
</tbody>
</table>

 

This property is valid for all programmable image data source items, including Flatbed (WIA\_CATEGORY\_FLATBED) and Feeder (WIA\_CATEGORY\_FEEDER) and is optional. When the property is supported, WIA\_COLOR\_DROP\_DISABLED is the required default value.

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

 

 





