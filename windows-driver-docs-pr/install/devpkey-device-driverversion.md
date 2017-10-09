---
title: DEVPKEY\_Device\_DriverVersion
description: DEVPKEY\_Device\_DriverVersion
ms.assetid: 68df1313-e948-4aea-9b90-c838f7bf228d
keywords: ["DEVPKEY_Device_DriverVersion Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_DriverVersion
api_location:
- Devpkey.h
api_type:
- HeaderDef
---

# DEVPKEY\_Device\_DriverVersion


The PKEY\_Device\_DriverVersion device property represents the version of the driver that is currently installed on a device instance.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_Device_DriverVersion</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p>[<strong>DEVPROP_TYPE_STRING</strong>](devprop-type-string.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read-only access by installation applications and installers</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Corresponding registry value identifier and registry value name</strong></p></td>
<td align="left"><p>REGSTR_VAL_DRIVERVERSION</p>
<p><strong>DriverVersion</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The value of DEVPKEY\_Device\_DriverVersion is supplied by the [**INF DriverVer directive**](https://msdn.microsoft.com/library/windows/hardware/ff547394) that is included in the [**INF Version section**](https://msdn.microsoft.com/library/windows/hardware/ff547502) of an INF file that installs a device or is supplied by a device-specific INF **DriverVer** directive that is included in the [**INF *DDInstall* section**](https://msdn.microsoft.com/library/windows/hardware/ff547344) that installs a device.

You can call [**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963) to retrieve the value of PKEY\_Device\_DriverVersion.

Windows Server 2003, Windows XP, and Windows 2000 support this property, but do not support the DEVPKEY\_Device\_DriverVersion property key. On these earlier versions of Windows, you can access the value of this property by accessing the corresponding **DriverVersion** registry value under the software key for the device instance. For information about how to access this property value on these earlier versions of Windows, see [Accessing Device Driver Properties](https://msdn.microsoft.com/library/windows/hardware/ff537732).

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


[**INF *DDInstall* Section**](https://msdn.microsoft.com/library/windows/hardware/ff547344)

[**INF DriverVer Directive**](https://msdn.microsoft.com/library/windows/hardware/ff547394)

[**INF Version Section**](https://msdn.microsoft.com/library/windows/hardware/ff547502)

[**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20DEVPKEY_Device_DriverVersion%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





