---
title: WIA\_DIP\_DEV\_TYPE
description: The WIA\_DIP\_DEV\_TYPE property contains a device type and device subtype.
ms.assetid: 685c1cfa-cc3b-42e6-aef3-359ae7220715
keywords: ["WIA_DIP_DEV_TYPE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DIP_DEV_TYPE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DIP\_DEV\_TYPE


The WIA\_DIP\_DEV\_TYPE property contains a device type and device subtype. The WIA service creates and maintains this property

## <span id="ddk_wia_dip_dev_type_si"></span><span id="DDK_WIA_DIP_DEV_TYPE_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The device type and subtype are obtained from the driver's INF file of the device file. An application reads the WIA\_DIP\_DEV\_TYPE property to determine whether it is using a scanner, camera, or video device.

The following table describes the possible values for the device type.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Device type</th>
<th>Value</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>StiDeviceTypeDefault</strong></p></td>
<td><p>0x0000</p></td>
<td><p>Default device</p></td>
</tr>
<tr class="even">
<td><p><strong>StiDeviceTypeScanner</strong></p></td>
<td><p>0x0001</p></td>
<td><p>Scanner device</p></td>
</tr>
<tr class="odd">
<td><p><strong>StiDeviceTypeDigitalCamera</strong></p></td>
<td><p>0x0002</p></td>
<td><p>Camera device</p></td>
</tr>
<tr class="even">
<td><p><strong>StiDeviceTypeStreamingVideo</strong></p></td>
<td><p>0x0003</p></td>
<td><p>Video device</p></td>
</tr>
</tbody>
</table>

 

For more information about INF files, see [INF Files for WIA Devices](https://msdn.microsoft.com/library/windows/hardware/ff542770). The **StiDeviceType***Xxx* constants are defined in *Sti.h*.

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

 

 





