---
title: DEVPKEY\_Device\_ConfigFlags
description: DEVPKEY\_Device\_ConfigFlags
ms.assetid: 67ff3b29-ba25-4dcd-b21b-75203ee17973
keywords: ["DEVPKEY_Device_ConfigFlags Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_ConfigFlags
api_location:
- Devpkey.h
api_type:
- HeaderDef
---

# DEVPKEY\_Device\_ConfigFlags


The DEVPKEY\_Device\_ConfigFlags device property represents the configuration flags that are set for a device instance.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_Device_ConfigFlags</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p>[<strong>DEVPROP_TYPE_INT32</strong>](devprop-type-int32.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read and write access by installation applications and installers</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Corresponding SPDRP_</strong><em>Xxx</em> <strong>identifier</strong></p></td>
<td align="left"><p>SPDRP_CONFIGFLAGS</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The value of DEVPKEY\_Device\_ConfigFlags is set during a device installation to indicate the current configuration of a device.

The configuration flags are represented by the CONFIGFLAG\_*Xxx* bitmasks that are defined in Regstr.h.

You can call [**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963) to retrieve the value of DEVPKEY\_Device\_ConfigFlags and call [**SetupDiSetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552163) to set DEVPKEY\_Device\_ConfigFlags.

Windows Server 2003, Windows XP, and Windows 2000 support this property, but do not support the DEVPKEY\_Device\_ConfigFlags property key. Instead, you can use the corresponding SPDRP\_CONFIGFLAGS identifier to access the value of the property on these earlier versions of Windows. For information about how to access this property value on these earlier versions of Windows, see [Accessing Device Instance SPDRP\_Xxx Properties](https://msdn.microsoft.com/library/windows/hardware/ff537737).

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
<td align="left"><p>Available in Windows Vista and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Devpkey.h (include Devpkey.h)</td>
</tr>
</tbody>
</table>

## See also


[**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963)

[**SetupDiSetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552163)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20DEVPKEY_Device_ConfigFlags%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





