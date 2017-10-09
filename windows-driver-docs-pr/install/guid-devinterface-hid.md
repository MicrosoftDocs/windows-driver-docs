---
title: GUID\_DEVINTERFACE\_HID
description: GUID\_DEVINTERFACE\_HID
ms.assetid: af2ebdaf-b7e9-4f79-abb6-60f1fb954b55
keywords: ["GUID_DEVINTERFACE_HID Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVINTERFACE_HID
api_location:
- Hidclass.h
api_type:
- HeaderDef
---

# GUID\_DEVINTERFACE\_HID


The GUID\_DEVINTERFACE\_HID [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for [HID collections](https://msdn.microsoft.com/library/windows/hardware/ff539861).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Attribute</th>
<th align="left">Setting</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Identifier</p></td>
<td align="left"><p>GUID_DEVINTERFACE_HID</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{4D1E55B2-F16F-11CF-88CB-001111000030}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Drivers for HID collections register instances of this device interface class to notify the operating system and applications of the presence of HID collections.

The system-supplied [HID class driver](https://msdn.microsoft.com/library/windows/hardware/jj126193) registers an instance of this device interface class for a HID collection. For example, the HID class driver registers an interface for a USB keyboard or mouse device. Access a HID collection by using the I/O interface supported by the HID class driver.

For information about HID devices and drivers, see [HIDClass Devices](hid-hidclass_devices).

For information about the device interface class for keyboard devices, see [**GUID\_DEVINTERFACE\_KEYBOARD**](guid-devinterface-keyboard.md).

For information about the device interface class for mouse devices, see [**GUID\_DEVINTERFACE\_MOUSE**](guid-devinterface-mouse.md).

The [**GUID\_CLASS\_INPUT**](guid-class-input.md) is an obsolete identifier for this device interface class; use GUID\_DEVINTERFACE\_HID instead.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Hidclass.h (include Hidclass.h)</td>
</tr>
</tbody>
</table>

## See also


[**GUID\_CLASS\_INPUT**](guid-class-input.md)

[**GUID\_DEVINTERFACE\_KEYBOARD**](guid-devinterface-keyboard.md)

[**GUID\_DEVINTERFACE\_MOUSE**](guid-devinterface-mouse.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20GUID_DEVINTERFACE_HID%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





