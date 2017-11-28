---
title: WIA\_DPA\_DEVICE\_TIME
description: The WIA\_DPA\_DEVICE\_TIME property contains the current clock time that is stored on a device. The minidriver creates and maintains this property.
ms.assetid: 5f903eb8-6a9e-4f06-ba70-5c02d8b332e5
keywords: ["WIA_DPA_DEVICE_TIME Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPA_DEVICE_TIME
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_DPA\_DEVICE\_TIME


The WIA\_DPA\_DEVICE\_TIME property contains the current clock time that is stored on a device. The minidriver creates and maintains this property.

## <span id="ddk_wia_dpa_device_time_si"></span><span id="DDK_WIA_DPA_DEVICE_TIME_SI"></span>


Property Type: VT\_UI2 | VT\_VECTOR

Valid Values: WIA\_PROP\_NONE

Access Rights: Read/write or read-only

Remarks
-------

When the WIA\_DPA\_DEVICE\_TIME property is read, the minidriver should check the device's current clock time and should always return the current time. This property is supported only by devices that have an internal clock. If the device clock can be set, this property is read/write; otherwise, it is read-only. WIA devices report time in a SYSTEMTIME structure (which is described in the Microsoft Windows SDK documentation).

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_DPA_DEVICE_TIME%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




