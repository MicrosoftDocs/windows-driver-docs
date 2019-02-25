---
title: DIF_FIRSTTIMESETUP
description: DIF_FIRSTTIMESETUP
ms.assetid: 6ac4da58-3f4f-4fcd-96e2-c480975159e0
keywords: ["DIF_FIRSTTIMESETUP Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DIF_FIRSTTIMESETUP
api_location:
- Setupapi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DIF_FIRSTTIMESETUP


This DIF code is reserved for system use. Vendor-supplied installers must not handle this request unless the vendor provides non-PnP devices that must be detected by the installer.

A DIF_FIRSTTIMESETUP request directs an installer to perform any class-specific installation tasks that have to be completed during the initial installation of the operating system.

### When Sent

During GUI-mode setup.

### Who Handles

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Class Co-installer</p></td>
<td align="left"><p>Can handle</p></td>
</tr>
<tr class="even">
<td align="left"><p>Device Co-installer</p></td>
<td align="left"><p>Does not handle</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Class Installer</p></td>
<td align="left"><p>Can handle</p></td>
</tr>
</tbody>
</table>

 

### Installer Input

<a href="" id="deviceinfoset"></a>*DeviceInfoSet*  
Supplies a handle to the device information set. There is a [device setup class](https://msdn.microsoft.com/library/windows/hardware/ff541509) associated with the *DeviceInfoSet*.

<a href="" id="deviceinfodata"></a>*DeviceInfoData*  
None

<a href="" id="device-installation-parameters-"></a>Device Installation Parameters   
There are device installation parameters ([**SP_DEVINSTALL_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346)) associated with the *DeviceInfoSet*.

<a href="" id="class-installation-parameters"></a>Class Installation Parameters  
None

### Installer Output

<a href="" id="deviceinfoset"></a>*DeviceInfoSet*  
An installer adds a device information element to the *DeviceInfoSet* for each detected device it wants to have installed. An installer might also build a global class driver list.

<a href="" id="device-installation-parameters"></a>Device Installation Parameters  
An installer can modify the device installation parameters for the *DeviceInfoSet* or for new device information elements it creates.

### Installer Return Value

A class co-installer can detect devices during preprocessing or postprocessing. Such a co-installer returns ERROR_DI_POSTPROCESSING_REQUIRED (for postprocessing) and/or returns NO_ERROR or a Win32 error code after its detection operations. If a co-installer does not detect devices, it returns NO_ERROR from its preprocessing pass.

If a class installer detects devices, the installer returns NO_ERROR or an appropriate Win32 error code. If a class installer does not handle this DIF request, the installer returns ERROR_DI_DO_DEFAULT.

### Default DIF Code Handler

None

### Installer Operation

To detect non-PnP devices during GUI-mode setup, an installer must handle the DIF_FIRSTTIMESETUP request. GUI-mode setup does not send a [**DIF_DETECT**](dif-detect.md) request to the installer.

GUI-mode setup sends a DIF_FIRSTTIMESETUP request with an empty *DeviceInfoSet*. The installers can perform legacy detection of non-PnP devices and add them to the *DeviceInfoSet*. System-supplied installers can also handle this DIF request when migrating legacy device installations from Windows 9x/Me or Windows NT to Microsoft Windows 2000 and later versions of Windows.

An installer detects new devices of its setup class, based on registry information, by calling into a kernel-mode detection component, or by consulting *unattend.txt* information that is stored when a migration DLL ran during an operating system upgrade.

If an installer detects a non-PnP device, the installer should select a driver for the device as follows: create a device information element ([**SetupDiCreateDeviceInfo**](https://msdn.microsoft.com/library/windows/hardware/ff550952)), set the SPDRP_HARDWAREID property by calling [**SetupDiSetDeviceRegistryProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552169), call [**SetupDiBuildDriverInfoList**](https://msdn.microsoft.com/library/windows/hardware/ff550917), and then call [**SetupDiCallClassInstaller**](https://msdn.microsoft.com/library/windows/hardware/ff550922) to send a [**DIF_SELECTBESTCOMPATDRV**](dif-selectbestcompatdrv.md) request.

If one or more installers detect device(s) in response to this DIF code, GUI-mode setup attempts to install the device(s). GUI-mode setup attempts to install all devices in the list; if an installer returns a device that was previously configured, GUI-mode setup will install the device twice.

An installer must handle this DIF request silently. That is, without displaying UI to the user.

Installers should not perform tasks when they handle this DIF request that require the computer to be restarted. For example, a class installer should not set drivers to load at the next startup for the purpose of determining which drivers succeed after the restart.

To detect non-PnP devices during GUI-mode setup, an installer must handle this request. GUI-mode setup does not send a DIF_DETECT request.

For more information about DIF codes, see [Handling DIF Codes](https://msdn.microsoft.com/library/windows/hardware/ff546094).

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
<td align="left"><p>Supported in Microsoft Windows 2000 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Setupapi.h (include Setupapi.h)</td>
</tr>
</tbody>
</table>

## See also


[**DIF_SELECTBESTCOMPATDRV**](dif-selectbestcompatdrv.md)

[**SetupDiBuildDriverInfoList**](https://msdn.microsoft.com/library/windows/hardware/ff550917)

[**SetupDiCallClassInstaller**](https://msdn.microsoft.com/library/windows/hardware/ff550922)

[**SetupDiCreateDeviceInfo**](https://msdn.microsoft.com/library/windows/hardware/ff550952)

[**SetupDiSetDeviceRegistryProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552169)

[**SP_DEVINFO_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344)

[**SP_DEVINSTALL_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346)

 

 






