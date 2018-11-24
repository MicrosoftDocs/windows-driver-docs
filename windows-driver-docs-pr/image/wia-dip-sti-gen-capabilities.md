---
title: WIA\_DIP\_STI\_GEN\_CAPABILITIES
description: The WIA\_DIP\_STI\_GEN\_CAPABILITIES property contains the generic STI capabilities for a device, which are obtained from the driver's INF file. The WIA service creates and maintains this property.
ms.assetid: 9429d065-43ed-41b9-a525-267ec44a94e7
keywords: ["WIA_DIP_STI_GEN_CAPABILITIES Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DIP_STI_GEN_CAPABILITIES
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DIP\_STI\_GEN\_CAPABILITIES


The WIA\_DIP\_STI\_GEN\_CAPABILITIES property contains the generic STI capabilities for a device, which are obtained from the driver's INF file. The WIA service creates and maintains this property.

## <span id="ddk_wia_dip_sti_gen_capabilities_si"></span><span id="DDK_WIA_DIP_STI_GEN_CAPABILITIES_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

An application reads the WIA\_DIP\_STI\_GEN\_CAPABILITIES property to determine the generic STI capabilities of the device.

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

 

 





