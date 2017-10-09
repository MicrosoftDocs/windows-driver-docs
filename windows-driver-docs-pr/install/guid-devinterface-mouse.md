---
title: GUID_DEVINTERFACE_MOUSE
description: GUID_DEVINTERFACE_MOUSE
ms.assetid: c5aff960-a78d-4429-ba3f-f2f91d9a56fa
keywords: ["GUID_DEVINTERFACE_MOUSE Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVINTERFACE_MOUSE
api_location:
- Ntddmou.h
api_type:
- HeaderDef
---

# GUID_DEVINTERFACE_MOUSE


The GUID_DEVINTERFACE_MOUSE [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for mouse devices.

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
<td align="left"><p>GUID_DEVINTERFACE_MOUSE</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{378DE44C-56EF-11D1-BC8C-00A0C91405DD}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Drivers for mouse devices register instances of this device interface class to notify the operating system and applications of the presence of mouse devices.

The system-supplied [mouse class driver](hid-non_hidclass_keyboard_and_mouse_devices) registers an instance of this device interface class for a mouse device. Access an instance of this device interface class by using the I/O interface supported by the mouse class driver.

For general information about supporting mouse devices, see [HID Architecture](https://msdn.microsoft.com/library/windows/hardware/jj126193) and [Features of the Kbdclass and Mouclass Drivers](hid-features_of_the_kbdclass_and_mouclass_drivers).

The WDK includes sample code for the system-supplied mouse class driver. The mouse class driver uses the obsolete identifier [**GUID_CLASS_MOUSE**](guid-class-mouse.md) to register an instance of this [device setup class](https://msdn.microsoft.com/library/windows/hardware/ff541509).

For information about the device interface class for keyboard devices, see [**GUID_DEVINTERFACE_KEYBOARD**](guid-devinterface-keyboard.md).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Microsoft Windows 2000 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ntddmou.h (include Ntddmou.h)</td>
</tr>
</tbody>
</table>

## See also


[**GUID_CLASS_MOUSE**](guid-class-mouse.md)

[**GUID_DEVINTERFACE_KEYBOARD**](guid-devinterface-keyboard.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20GUID_DEVINTERFACE_MOUSE%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





