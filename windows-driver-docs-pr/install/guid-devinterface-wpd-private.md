---
title: GUID\_DEVINTERFACE\_WPD\_PRIVATE
description: GUID\_DEVINTERFACE\_WPD\_PRIVATE
ms.assetid: 50292137-d648-41cf-928e-d72549f6321b
keywords: ["GUID_DEVINTERFACE_WPD_PRIVATE Device and Driver Installation"]
topic_type:
- apiref
api_name:
- GUID_DEVINTERFACE_WPD_PRIVATE
api_location:
- Portabledevice.h
api_type:
- HeaderDef
---

# GUID\_DEVINTERFACE\_WPD\_PRIVATE


The GUID\_DEVINTERFACE\_WPD\_PRIVATE [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for specialized [Windows Portable Devices](http://go.microsoft.com/fwlink/p/?linkid=106527) (WPD).

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
<td align="left"><p>GUID_DEVINTERFACE_WPD_PRIVATE</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{BA0C718F-4DED-49B7-BDD3-FABE28661211}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

GUID\_DEVINTERFACE\_WPD\_PRIVATE should be used only for private devices that are used by custom WPD applications. Generic WPD drivers and clients of WPD devices should not use instances of this device interface class.

Custom applications can enumerate private devices that register this interface by calling **IPortableDeviceManager::GetPrivateDevices** (documented in Windows SDK).

For information about the device interface class for generic WPD devices, see [**GUID\_DEVINTERFACE\_WPD**](guid-devinterface-wpd.md).

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
<td align="left"><p>Available in Windows Vista, Windows XP, and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Portabledevice.h (include Portabledevice.h)</td>
</tr>
</tbody>
</table>

## See also


[**GUID\_DEVINTERFACE\_WPD**](guid-devinterface-wpd.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20GUID_DEVINTERFACE_WPD_PRIVATE%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





