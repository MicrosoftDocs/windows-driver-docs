---
title: DEVPKEY\_DeviceClass\_Characteristics
description: DEVPKEY\_DeviceClass\_Characteristics
ms.assetid: dd50a97b-7230-46a5-b6d2-0f741d7ae5d4
keywords: ["DEVPKEY_DeviceClass_Characteristics Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_DeviceClass_Characteristics
api_location:
- Devpkey.h
api_type:
- HeaderDef
---

# DEVPKEY\_DeviceClass\_Characteristics


The DEVPKEY\_DeviceClass\_Characteristics device property represents the default device characteristics of all devices in a [device setup class](https://msdn.microsoft.com/library/windows/hardware/ff541509).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_DeviceClass_Characteristics</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p>[<strong>DEVPROP_TYPE_INT32</strong>](devprop-type-int32.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read-only access by installation applications and installers after a device setup class is installed</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Corresponding SPCRP_</strong><em>Xxx</em> <strong>identifier</strong></p></td>
<td align="left"><p>SPCRP_CHARACTERISTICS</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

You can set the value of DEVPKEY\_DeviceClass\_Characteristics when an installation application installs a device setup class. For information about how to install a device setup class and setting this property, see [**INF ClassInstall32 Section**](https://msdn.microsoft.com/library/windows/hardware/ff546335) and the information about the registry entry value **DeviceCharacteristics** that is provided in the "Special *value-entry-name* Keywords" section of [**INF AddReg Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320).

The value of DEVPKEY\_DeviceClass\_Characteristics is a bitwise OR of the FILE\_DEVICE\_*Xxx* flags that are defined in *Wdm.h* and *Ntddk.h*. For more information about device characteristics, see the *DeviceCharacteristics* parameter of the [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397) function.

You can call [**SetupDiGetClassProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551086) or [**SetupDiGetClassPropertyEx**](https://msdn.microsoft.com/library/windows/hardware/ff551090) to retrieve the value of DEVPKEY\_DeviceClass\_Characteristics.

Windows Server 2003 and Windows XP support this property, but do not support the DEVPKEY\_DeviceClass\_Characteristics property key. On these earlier versions of Windows, you can use the SPCRP\_CHARACTERISTICS identifier to access the value of this property. For information about how to access the value of this property, see [Retrieving Device Setup Class SPCRP\_Xxx Properties](https://msdn.microsoft.com/library/windows/hardware/ff550644).

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


[**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397)

[**INF AddReg Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320)

[**INF ClassInstall32 Section**](https://msdn.microsoft.com/library/windows/hardware/ff546335)

[**SetupDiGetClassProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551086)

[**SetupDiGetClassPropertyEx**](https://msdn.microsoft.com/library/windows/hardware/ff551090)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20DEVPKEY_DeviceClass_Characteristics%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





