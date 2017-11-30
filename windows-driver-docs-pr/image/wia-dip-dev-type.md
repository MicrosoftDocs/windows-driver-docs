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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_DIP_DEV_TYPE%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




