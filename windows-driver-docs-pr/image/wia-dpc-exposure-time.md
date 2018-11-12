---
title: WIA\_DPC\_EXPOSURE\_TIME
description: The WIA\_DPC\_EXPOSURE\_TIME property corresponds to the shutter speed, in seconds that are scaled by 10,000.
ms.assetid: 78f12aaa-4b7b-4ba3-a6af-791e97581d26
keywords: ["WIA_DPC_EXPOSURE_TIME Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_EXPOSURE_TIME
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DPC\_EXPOSURE\_TIME


The WIA\_DPC\_EXPOSURE\_TIME property corresponds to the shutter speed, in seconds that are scaled by 10,000.

## <span id="ddk_wia_dpc_exposure_time_si"></span><span id="DDK_WIA_DPC_EXPOSURE_TIME_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_RANGE or WIA\_PROP\_LIST

Access Rights: Read/write

Remarks
-------

Typically, a device uses the WIA\_DPC\_EXPOSURE\_TIME property only when the [**WIA\_DPC\_EXPOSURE\_MODE**](wia-dpc-exposure-mode.md) property is set to EXPOSUREMODE\_MANUAL or EXPOSUREMODE\_SHUTTER\_PRIORITY.

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

 

 






