---
title: WIA\_IPS\_PRINTER\_ENDORSER\_XOFFSET
description: The WIA\_IPS\_PRINTER\_ENDORSER\_XOFFSET property is used to configure the horizontal coordinate, in thousandths of an inch (0.001 \ 0034;), of the top-left corner of the imprinting/endorsing region, relative to the top-left corner of the physical document to be scanned and imprinted/endorsed. The WIA minidriver creates and maintains this property.
ms.assetid: 3B3E1A02-0401-455C-B341-37FBEB108E4F
keywords: ["WIA_IPS_PRINTER_ENDORSER_XOFFSET Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PRINTER_ENDORSER_XOFFSET
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/22/2018
ms.localizationpriority: medium
---

# WIA\_IPS\_PRINTER\_ENDORSER\_XOFFSET


The **WIA\_IPS\_PRINTER\_ENDORSER\_XOFFSET** property is used to configure the horizontal coordinate, in thousandths of an inch (0.001"), of the top-left corner of the imprinting/endorsing region, relative to the top-left corner of the physical document to be scanned and imprinted/endorsed. The WIA minidriver creates and maintains this property.




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

 

 





