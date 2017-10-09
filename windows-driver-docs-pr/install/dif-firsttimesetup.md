---
title: DIF\_FIRSTTIMESETUP
description: DIF\_FIRSTTIMESETUP
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
---

# DIF\_FIRSTTIMESETUP


This DIF code is reserved for system use. Vendor-supplied installers must not handle this request unless the vendor provides non-PnP devices that must be detected by the installer.

A DIF\_FIRSTTIMESETUP request directs an installer to perform any class-specific installation tasks that have to be completed during the initial installation of the operating system.

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
There are device installation parameters ([**SP\_DEVINSTALL\_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346)) associated with the *DeviceInfoSet*.

<a href="" id="class-installation-parameters"></a>Class Installation Parameters  
None

### Installer Output

<a href="" id="deviceinfoset"></a>*DeviceInfoSet*  
An installer adds a device information element to the *DeviceInfoSet* for each detected device it wants to have installed. An installer might also build a global class driver list.

<a href="" id="device-installation-parameters"></a>Device Installation Parameters  
An installer can modify the device installation parameters for the *DeviceInfoSet* or for new device information elements it creates.

### Installer Return Value

A class co-installer can detect devices during preprocessing or postprocessing. Such a co-installer returns ERROR\_DI\_POSTPROCESSING\_REQUIRED (for postprocessing) and/or returns NO\_ERROR or a Win32 error code after its detection operations. If a co-installer does not detect devices, it returns NO\_ERROR from its preprocessing pass.

If a class installer detects devices, the installer returns NO\_ERROR or an appropriate Win32 error code. If a class installer does not handle this DIF request, the installer returns ERROR\_DI\_DO\_DEFAULT.

### Default DIF Code Handler

None

### Installer Operation

To detect non-PnP devices during GUI-mode setup, an installer must handle the DIF\_FIRSTTIMESETUP request. GUI-mode setup does not send a [**DIF\_DETECT**](dif-detect.md) request to the installer.

GUI-mode setup sends a DIF\_FIRSTTIMESETUP request with an empty *DeviceInfoSet*. The installers can perform legacy detection of non-PnP devices and add them to the *DeviceInfoSet*. System-supplied installers can also handle this DIF request when migrating legacy device installations from Windows 9x/Me or Windows NT to Microsoft Windows 2000 and later versions of Windows.

An installer detects new devices of its setup class, based on registry information, by calling into a kernel-mode detection component, or by consulting *unattend.txt* information that is stored when a migration DLL ran during an operating system upgrade.

If an installer detects a non-PnP device, the installer should select a driver for the device as follows: create a device information element ([**SetupDiCreateDeviceInfo**](https://msdn.microsoft.com/library/windows/hardware/ff550952)), set the SPDRP\_HARDWAREID property by calling [**SetupDiSetDeviceRegistryProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552169), call [**SetupDiBuildDriverInfoList**](https://msdn.microsoft.com/library/windows/hardware/ff550917), and then call [**SetupDiCallClassInstaller**](https://msdn.microsoft.com/library/windows/hardware/ff550922) to send a [**DIF\_SELECTBESTCOMPATDRV**](dif-selectbestcompatdrv.md) request.

If one or more installers detect device(s) in response to this DIF code, GUI-mode setup attempts to install the device(s). GUI-mode setup attempts to install all devices in the list; if an installer returns a device that was previously configured, GUI-mode setup will install the device twice.

An installer must handle this DIF request silently. That is, without displaying UI to the user.

Installers should not perform tasks when they handle this DIF request that require the computer to be restarted. For example, a class installer should not set drivers to load at the next startup for the purpose of determining which drivers succeed after the restart.

To detect non-PnP devices during GUI-mode setup, an installer must handle this request. GUI-mode setup does not send a DIF\_DETECT request.

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


[**DIF\_SELECTBESTCOMPATDRV**](dif-selectbestcompatdrv.md)

[**SetupDiBuildDriverInfoList**](https://msdn.microsoft.com/library/windows/hardware/ff550917)

[**SetupDiCallClassInstaller**](https://msdn.microsoft.com/library/windows/hardware/ff550922)

[**SetupDiCreateDeviceInfo**](https://msdn.microsoft.com/library/windows/hardware/ff550952)

[**SetupDiSetDeviceRegistryProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552169)

[**SP\_DEVINFO\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344)

[**SP\_DEVINSTALL\_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20DIF_FIRSTTIMESETUP%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





