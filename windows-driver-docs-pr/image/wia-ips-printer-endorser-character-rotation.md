---
title: WIA\_IPS\_PRINTER\_ENDORSER\_CHARACTER\_ROTATION
description: The WIA\_IPS\_PRINTER\_ENDORSER\_CHARACTER\_ROTATION property is used to configure the rotation of the individual characters in the printed or endorsed text.
ms.assetid: DCEF2CAF-08F3-432B-8688-E04DEAA523E0
keywords: ["WIA_IPS_PRINTER_ENDORSER_CHARACTER_ROTATION Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PRINTER_ENDORSER_CHARACTER_ROTATION
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_PRINTER\_ENDORSER\_CHARACTER\_ROTATION


The **WIA\_IPS\_PRINTER\_ENDORSER\_CHARACTER\_ROTATION** property is used to configure the rotation of the individual characters in the printed or endorsed text. If supported, individual character rotation can be done in addition to the rotation of the current imprinted or endorsed region that is described by the [**WIA\_IPS\_ROTATION**](wia-ips-rotation.md) property. This feature is available with Windows 8 and later versions of Windows.

Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read-Write

Remarks
-------

Valid values for the **WIA\_IPS\_PRINTER\_ENDORSER\_CHARACTER\_ROTATION** property are the same as the existing values for the **WIA\_IPS\_ROTATION** property.

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

 

 





