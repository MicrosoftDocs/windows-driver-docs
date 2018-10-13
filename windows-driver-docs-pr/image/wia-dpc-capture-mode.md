---
title: WIA\_DPC\_CAPTURE\_MODE
description: The WIA\_DPC\_CAPTURE\_MODE property sets the image capture mode.
ms.assetid: 32d117ac-fa20-49cc-a34e-31a1be88804e
keywords: ["WIA_DPC_CAPTURE_MODE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_CAPTURE_MODE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# WIA\_DPC\_CAPTURE\_MODE


The WIA\_DPC\_CAPTURE\_MODE property sets the image capture mode.

## <span id="ddk_wia_dpc_capture_mode_si"></span><span id="DDK_WIA_DPC_CAPTURE_MODE_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/write

Remarks
-------

The following table describes the three constants that are valid with the WIA\_DPC\_CAPTURE\_MODE property.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>CAPTUREMODE_BURST</p></td>
<td><p>Capture more than one image in quick succession as defined by the values of the [<strong>WIA_DPC_BURST_NUMBER</strong>](wia-dpc-burst-number.md) and [<strong>WIA_DPC_BURST_INTERVAL</strong>](wia-dpc-burst-interval.md) properties.</p></td>
</tr>
<tr class="even">
<td><p>CAPTUREMODE_NORMAL</p></td>
<td><p>Normal mode for the camera.</p></td>
</tr>
<tr class="odd">
<td><p>CAPTUREMODE_TIMELAPSE</p></td>
<td><p>Capture more than one image in succession as defined by the [<strong>WIA_DPC_TIMELAPSE_NUMBER</strong>](wia-dpc-timelapse-number.md) and [<strong>WIA_DPC_TIMELAPSE_INTERVAL</strong>](wia-dpc-timelapse-interval.md) properties.</p></td>
</tr>
</tbody>
</table>

 

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


[**WIA\_DPC\_BURST\_INTERVAL**](wia-dpc-burst-interval.md)

[**WIA\_DPC\_BURST\_NUMBER**](wia-dpc-burst-number.md)

[**WIA\_DPC\_TIMELAPSE\_INTERVAL**](wia-dpc-timelapse-interval.md)

[**WIA\_DPC\_TIMELAPSE\_NUMBER**](wia-dpc-timelapse-number.md)

 

 






