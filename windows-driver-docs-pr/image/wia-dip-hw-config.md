---
title: WIA\_DIP\_HW\_CONFIG
description: The WIA\_DIP\_HW\_CONFIG property indicates the type of connection that a device is using. The WIA service creates and maintains this property, and only the WIA service can change it.
ms.assetid: c79e9651-120c-4f99-83d2-1920f7fccc73
keywords: ["WIA_DIP_HW_CONFIG Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DIP_HW_CONFIG
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DIP\_HW\_CONFIG


The WIA\_DIP\_HW\_CONFIG property indicates the type of connection that a device is using. The WIA service creates and maintains this property, and only the WIA service can change it.

## <span id="ddk_wia_dip_hw_config_si"></span><span id="DDK_WIA_DIP_HW_CONFIG_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

An application reads the WIA\_DIP\_HW\_CONFIG property to determine the device's connection type.

The following table describes the possible values for WIA\_DIP\_HW\_CONFIG.

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
<td><p>1</p></td>
<td><p>Generic WDM device</p></td>
</tr>
<tr class="even">
<td><p>2</p></td>
<td><p>SCSI device</p></td>
</tr>
<tr class="odd">
<td><p>4</p></td>
<td><p>USB device</p></td>
</tr>
<tr class="even">
<td><p>8</p></td>
<td><p>Serial device</p></td>
</tr>
<tr class="odd">
<td><p>16</p></td>
<td><p>Parallel device</p></td>
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

 

 





