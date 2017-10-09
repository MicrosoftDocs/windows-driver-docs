---
title: GUID\_DEVINTERFACE\_USB\_HUB
description: GUID\_DEVINTERFACE\_USB\_HUB
ms.assetid: 899b77ad-fa98-4078-9207-69b422e3d0d0
keywords: ["GUID_DEVINTERFACE_USB_HUB Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVINTERFACE_USB_HUB
api_location:
- Usbiodef.h
api_type:
- HeaderDef
---

# GUID\_DEVINTERFACE\_USB\_HUB


The GUID\_DEVINTERFACE\_USB\_HUB [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for [USB](https://msdn.microsoft.com/library/windows/hardware/ff538930) hub devices.

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
<td align="left"><p>GUID_DEVINTERFACE_USB_HUB</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{F18A0E88-C30C-11D0-8815-00A0C906BED8}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The system-supplied USB port driver registers instances of GUID\_DEVINTERFACE\_USB\_HUB to notify the operating system and applications of the presence of the root hub of host controller devices. The system-supplied USB hub driver registers instances of this class for additional hub devices, if any, that are supported by the host controller.

The Microsoft Windows Driver Kit (WDK) includes the [USBVIEW sample application](http://go.microsoft.com/fwlink/p/?linkid=256205). The USBVIEW sample uses the obsolete identifier [**GUID\_CLASS\_USBHUB**](guid-class-usbhub.md) to be notified of instances of this device interface class.

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
<td align="left">Usbiodef.h (include Usbiodef.h)</td>
</tr>
</tbody>
</table>

## See also


[**GUID\_CLASS\_USBHUB**](guid-class-usbhub.md)

[**GUID\_DEVINTERFACE\_USB\_DEVICE**](guid-devinterface-usb-device.md)

[**GUID\_DEVINTERFACE\_USB\_HOST\_CONTROLLER**](guid-devinterface-usb-host-controller.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20GUID_DEVINTERFACE_USB_HUB%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





