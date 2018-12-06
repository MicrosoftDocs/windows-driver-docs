---
title: WIA\_DIP\_PORT\_NAME
description: The WIA\_DIP\_PORT\_NAME property contains an installed device's port name, which is assigned by the kernel-mode driver that operates the device. The WIA service creates and maintains this property.
ms.assetid: ccb5d335-de56-477f-909c-cb2e55a0889a
keywords: ["WIA_DIP_PORT_NAME Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DIP_PORT_NAME
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DIP\_PORT\_NAME


The WIA\_DIP\_PORT\_NAME property contains an installed device's port name, which is assigned by the kernel-mode driver that operates the device. The WIA service creates and maintains this property.

## <span id="ddk_wia_dip_port_name_si"></span><span id="DDK_WIA_DIP_PORT_NAME_SI"></span>


Property Type: VT\_BSTR

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

An application reads the WIA\_DIP\_PORT\_NAME property to determine the port name.

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

 

 





