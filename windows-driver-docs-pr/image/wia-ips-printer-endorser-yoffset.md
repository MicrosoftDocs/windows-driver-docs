---
title: WIA\_IPS\_PRINTER\_ENDORSER\_YOFFSET
description: The WIA\_IPS\_PRINTER\_ENDORSER\_YOFFSET property is used to configure the vertical coordinate, in thousandths of an inch (0.001 \ 0034;), of the top-left corner of the imprinting/endorsing region, relative to the top-left corner of the physical document to be scanned and imprinted/endorsed. The WIA minidriver creates and maintains this property.
ms.assetid: C04A4EAC-237A-44D6-AB05-CD561DA72CE8
keywords: ["WIA_IPS_PRINTER_ENDORSER_YOFFSET Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PRINTER_ENDORSER_YOFFSET
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/22/2018
ms.localizationpriority: medium
---

# WIA\_IPS\_PRINTER\_ENDORSER\_YOFFSET


The **WIA\_IPS\_PRINTER\_ENDORSER\_YOFFSET** property is used to configure the vertical coordinate, in thousandths of an inch (0.001"), of the top-left corner of the imprinting/endorsing region, relative to the top-left corner of the physical document to be scanned and imprinted/endorsed. The WIA minidriver creates and maintains this property.




Property Type: VT\_UI4

Valid Values: WIA\_PROP\_RANGE

Access Rights: Read/Write

Remarks
-------

The WIA minidriver can update the valid range of values and the current value (if it becomes out of range) to the closest available position when the [**WIA\_IPS\_PRINTER\_ENDORSER**](wia-ips-printer-endorser.md) property is changed to a new specific input source (in other words, from flatbed to feeder).

This property is optional for all Imprinter/Endorser data source items.

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

 

 





