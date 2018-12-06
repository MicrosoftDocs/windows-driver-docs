---
title: WIA\_IPS\_PRINTER\_ENDORSER\_COUNTER
description: The WIA\_IPS\_PRINTER\_ENDORSER\_COUNTER property is used to configure the starting value and incrementing step for the imprinter/endorser counter at the beginning of a new WIA application session. The WIA minidriver creates and maintains this property.
ms.assetid: 3475A0DF-58EA-4B05-96EA-5BBE44655DB0
keywords: ["WIA_IPS_PRINTER_ENDORSER_COUNTER Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PRINTER_ENDORSER_COUNTER
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/22/2018
ms.localizationpriority: medium
---

# WIA\_IPS\_PRINTER\_ENDORSER\_COUNTER


The **WIA\_IPS\_PRINTER\_ENDORSER\_COUNTER** property is used to configure the starting value and incrementing step for the imprinter/endorser counter at the beginning of a new WIA application session. The WIA minidriver creates and maintains this property.




Property Type: VT\_UI4

Valid Values: WIA\_PROP\_RANGE

Access Rights: Read/Write

Remarks
-------

The mandatory default value for the **WIA\_IPS\_PRINTER\_ENDORSER\_COUNTER** property is 0 (first page).

The range step value describes the increment value for the printer/endorser counter value (the minidriver increments this value after each document page that gets scanned). This counter step has a different purpose and should not be confused with the step configurable through the [**WIA\_IPS\_PRINTER\_ENDORSER\_STEP**](wia-ips-printer-endorser-step.md) property.

This property is required to be supported by all Imprinter/Endorser data source items. The value of 0 (first page) is required.

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

 

 





