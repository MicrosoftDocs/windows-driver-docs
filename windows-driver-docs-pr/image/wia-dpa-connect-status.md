---
title: WIA\_DPA\_CONNECT\_STATUS
description: The WIA\_DPA\_CONNECT\_STATUS property contains the current connection status for a device. The WIA minidriver creates and maintains this property.
ms.assetid: 524fb89a-47a0-44a7-8f21-36e0abcfdd5c
keywords: ["WIA_DPA_CONNECT_STATUS Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPA_CONNECT_STATUS
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DPA\_CONNECT\_STATUS


The WIA\_DPA\_CONNECT\_STATUS property contains the current connection status for a device. The WIA minidriver creates and maintains this property.

## <span id="ddk_wia_dpa_connect_status_si"></span><span id="DDK_WIA_DPA_CONNECT_STATUS_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The following table lists the possible values for the WIA\_DPA\_CONNECT\_STATUS property.

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
<td><p>WIA_DEVICE_NOT_CONNECTED</p></td>
<td><p>The device is not connected.</p></td>
</tr>
<tr class="even">
<td><p>WIA_DEVICE_CONNECTED</p></td>
<td><p>The device is connected and operational.</p></td>
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
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

 

 





