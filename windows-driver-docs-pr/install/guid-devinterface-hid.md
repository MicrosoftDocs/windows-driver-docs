---
title: GUID_DEVINTERFACE_HID
description: GUID_DEVINTERFACE_HID
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
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GUID_DEVINTERFACE_HID


The GUID_DEVINTERFACE_HID [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for [HID collections](https://msdn.microsoft.com/library/windows/hardware/ff539861).

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

For information about HID devices and drivers, see [HIDClass Devices](../hid/binding-minidrivers-to-the-hid-class.md).

For information about the device interface class for keyboard devices, see [**GUID_DEVINTERFACE_KEYBOARD**](guid-devinterface-keyboard.md).

For information about the device interface class for mouse devices, see [**GUID_DEVINTERFACE_MOUSE**](guid-devinterface-mouse.md).

The [**GUID_CLASS_INPUT**](guid-class-input.md) is an obsolete identifier for this device interface class; use GUID_DEVINTERFACE_HID instead.

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


[**GUID_CLASS_INPUT**](guid-class-input.md)

[**GUID_DEVINTERFACE_KEYBOARD**](guid-devinterface-keyboard.md)

[**GUID_DEVINTERFACE_MOUSE**](guid-devinterface-mouse.md)

 

 






