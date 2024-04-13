---
title: DEVPKEY_Device_DriverCoInstallers
description: DEVPKEY_Device_DriverCoInstallers
keywords: ["DEVPKEY_Device_DriverCoInstallers Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_DriverCoInstallers
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.date: 10/17/2018
ms.topic: reference
---

# DEVPKEY_Device_DriverCoInstallers


The DEVPKEY_Device_DriverCoInstallers device property represents a list of DLL names, and entry points in the DLLs, that are registered as *co-installers* for a device instance.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr>
<th>Attribute</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_Device_DriverCoInstallers</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-string-list.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_STRING_LIST&lt;/strong&gt;](devprop-type-string-list.md)"><strong>DEVPROP_TYPE_STRING_LIST</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Data format</strong></p></td>
<td align="left"><p>"AbcCoInstall.dll,AbcCoInstallEntryPoint\0...AbcCoInstall.dll, AbcCoInstallEntryPoin\0\0"</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read-only access by installation applications and installers</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Corresponding registry value identifier and registry value name</strong></p></td>
<td align="left"><p>REGSTR_VAL_COINSTALLERS_32</p>
<p><strong>CoInstallers32</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The value of DEVPKEY_Device_DriverCoInstallers is supplied by the [**INF *DDInstall*.Coinstallers**](./inf-ddinstall-coinstallers-section.md) section in the INF file that installs a device.

You can call [**CM_Get_DevNode_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_propertyw) or [**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw) to retrieve the value of DEVPKEY_Device_DriverCoInstallers.

Windows Server 2003, Windows XP, and Windows 2000 support this property, but do not support the DEVPKEY_Device_DriverCoInstallers property key. On these earlier versions of Windows, you can access the value of this property by accessing the corresponding **CoInstallers32** registry value under the software key for the device instance. For information about how to access this property value on these earlier versions of Windows, see [Accessing Device Driver Properties](./accessing-device-driver-properties.md).

## Requirements

**Version**: Windows Vista and later versions of Windows
**Header**: Devpkey.h (include Devpkey.h)


## See also


[**INF *DDInstall*.Coinstallers Section**](./inf-ddinstall-coinstallers-section.md)

[**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw)

 

