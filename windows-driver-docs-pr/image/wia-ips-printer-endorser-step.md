---
title: WIA\_IPS\_PRINTER\_ENDORSER\_STEP
description: By default the imprinter/endorser imprints or endorses on each document page that is scanned.
ms.assetid: A4455204-6502-4BE7-9EE3-B5616089FA05
keywords: ["WIA_IPS_PRINTER_ENDORSER_STEP Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PRINTER_ENDORSER_STEP
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/22/2018
ms.localizationpriority: medium
---

# WIA\_IPS\_PRINTER\_ENDORSER\_STEP


By default the imprinter/endorser imprints or endorses on each document page that is scanned. This mandatory default behavior can be changed by the client by using the **WIA\_IPS\_PRINTER\_ENDORSER\_STEP** property. For example, the client application can set the current value to 2 to have every other scanned page imprinted/endorsed (0, 2, 4, 6, ...). The WIA minidriver creates and maintains this property.




Property Type: VT\_UI4

Valid Values: WIA\_PROP\_RANGE

Access Rights: Read/Write

Remarks
-------

The mandatory default value for the **WIA\_IPS\_PRINTER\_ENDORSER\_STEP** property is 1 (each page). A value of 0 is invalid.

As for most WIA\_PROP\_RANGE properties, the WIA minidriver can implement a range containing one single value, minimum equal with maximum and a step value of zero.

This property must be supported by all Imprinter/Endorser data source items. The value of 1 (each page) is required.

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

 

 





