---
title: WIA\_DPC\_FNUMBER
description: The WIA\_DPC\_FNUMBER property corresponds to the aperture of the lens, in units of the f-stop number scaled by 100.
ms.assetid: 85f3fbc8-8b20-45a7-8ed6-0d22ac7d7f6f
keywords: ["WIA_DPC_FNUMBER Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_FNUMBER
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DPC\_FNUMBER


The WIA\_DPC\_FNUMBER property corresponds to the aperture of the lens, in units of the f-stop number scaled by 100.

## <span id="ddk_wia_dpc_fnumber_si"></span><span id="DDK_WIA_DPC_FNUMBER_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/write

Remarks
-------

The setting of the WIA\_DPC\_FNUMBER property is typically valid only when the [**WIA\_DPC\_EXPOSURE\_MODE**](wia-dpc-exposure-mode.md) property is set to EXPOSUREMODE\_MANUAL or EXPOSUREMODE\_APERTURE\_PRIORITY.

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
<td><p>Obsolete in Windows Vista and later operating systems and should no longer be used. However, this property is still defined in Windows Vista for compatibility with applications and devices designed for Windows Server 2003, Windows XP, and previous versions of Windows.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

## See also


[**WIA\_DPC\_EXPOSURE\_MODE**](wia-dpc-exposure-mode.md)

 

 






