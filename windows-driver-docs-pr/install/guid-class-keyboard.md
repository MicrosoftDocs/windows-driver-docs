---
title: GUID\_CLASS\_KEYBOARD
description: GUID\_CLASS\_KEYBOARD
ms.assetid: 9e90d18f-5298-4234-8b05-38e9b8ec5076
keywords: ["GUID_CLASS_KEYBOARD Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_CLASS_KEYBOARD
api_location:
- Ntddkbd.h
api_type:
- HeaderDef
---

# GUID\_CLASS\_KEYBOARD


GUID\_CLASS\_KEYBOARD is an obsolete identifier for the [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) for keyboard devices. Starting with Microsoft Windows 2000, use the [**GUID\_DEVINTERFACE\_KEYBOARD**](guid-devinterface-keyboard.md) class identifier for new instances of this class.

Remarks
-------

The HID samples that are provided in the WDK include the keyboard class driver. The keyboard class driver uses GUID\_CLASS\_KEYBOARD to register instances of this device interface class.

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
<td align="left"><p>Obsolete. Starting with Windows 2000, use GUID_DEVINTERFACE_KEYBOARD instead.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ntddkbd.h (include Ntddkbd.h)</td>
</tr>
</tbody>
</table>

## See also


[**GUID\_DEVINTERFACE\_KEYBOARD**](guid-devinterface-keyboard.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20GUID_CLASS_KEYBOARD%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





