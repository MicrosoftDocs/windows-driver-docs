---
title: WIA\_DIP\_SERVER\_NAME
description: The WIA\_DIP\_SERVER\_NAME property contains the name of the server that a WIA minidriver is running on.
ms.assetid: 93fec2b1-dc41-48cf-990b-f6aa99133835
keywords: ["WIA_DIP_SERVER_NAME Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DIP_SERVER_NAME
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DIP\_SERVER\_NAME


The WIA\_DIP\_SERVER\_NAME property contains the name of the server that a WIA minidriver is running on.

## <span id="ddk_wia_dip_server_name_si"></span><span id="DDK_WIA_DIP_SERVER_NAME_SI"></span>


Property Type: VT\_BSTR

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The default value of WIA\_DIP\_SERVER\_NAME is "local". This property should contain the string "local" when an application is connected to a device on the same computer.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Optional for Microsoft Windows XP and later operating systems.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

 

 





