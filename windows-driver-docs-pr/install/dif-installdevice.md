---
title: DIF_INSTALLDEVICE
description: DIF_INSTALLDEVICE
ms.assetid: 2d369086-c2b6-45a4-a87e-51ff5725938f
keywords: ["DIF_INSTALLDEVICE Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DIF_INSTALLDEVICE
api_location:
- Setupapi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DIF_INSTALLDEVICE


A DIF_INSTALLDEVICE request allows an installer to perform tasks before and/or after the device is installed.

### When Sent

After selecting the driver, registering any device co-installers, and registering any device interfaces.

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
<td align="left"><p>Can handle</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Class Installer</p></td>
<td align="left"><p>Can handle</p></td>
</tr>
</tbody>
</table>

 

### Installer Input

<a href="" id="deviceinfoset"></a>*DeviceInfoSet*  
Supplies a handle to the [device information set](https://msdn.microsoft.com/library/windows/hardware/ff541247) that contains the device to be installed.

<a href="" id="deviceinfodata"></a>*DeviceInfoData*  
Supplies a pointer to an [**SP_DEVINFO_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344) structure for the device in the device information set.

<a href="" id="device-installation-parameters-"></a>Device Installation Parameters   
There are device installation parameters ([**SP_DEVINSTALL_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346)) associated with the *DeviceInfoData*.

<a href="" id="class-installation-parameters"></a>Class Installation Parameters  
None

### Installer Output

<a href="" id="device-installation-parameters"></a>Device Installation Parameters  
An installer can modify the device installation parameters for the *DeviceInfoData*. For example, an installer might set the DI_NEEDREBOOT flag or it might set the DI_DONOTCALLCONFIGMG flag to prevent Windows from bringing the device online dynamically with its newly installed driver and settings.

### Installer Return Value

A co-installer typically returns NO_ERROR or ERROR_DI_POSTPROCESSING_REQUIRED. A co-installer might also return a Win32 error code.

If a class installer successfully handles this request and [**SetupDiCallClassInstaller**](https://msdn.microsoft.com/library/windows/hardware/ff550922) should subsequently call the default handler, the class installer returns ERROR_DI_DO_DEFAULT.

If the class installer successfully handles this request, including directly calling the default handler, the class installer should return NO_ERROR and **SetupDiCallClassInstaller** will not subsequently call the default handler again.

**Note**   The class installer can directly call the default handler, but the class installer should never attempt to supersede the operations of the default handler. For more information about calling a default DIF code handler, see [Calling Default DIF Code Handlers](https://msdn.microsoft.com/library/windows/hardware/ff537868).

 

If the class installer encounters an error, the installer should return an appropriate Win32 error code and **SetupDiCallClassInstaller** will not subsequently call the default handler.

### Default DIF Code Handler

[**SetupDiInstallDevice**](https://msdn.microsoft.com/library/windows/hardware/ff552039)

### Installer Operation

In response to a DIF_INSTALLDEVICE request an installer typically performs any final installation operations before the default handler installs the device. For example, an installer can check, and possibly modify, the upper-filter drivers and lower-filter drivers for the device that is listed in the registry.

Unless the DI_NOFILECOPY flag is set in the device installation parameters, an installer that handles this DIF request should copy files that are required for the device, such as driver files and control panel files.

If the DI_NOFILECOPY flag is clear but the DI_NOVCP flag is set, the installer must enqueue any file operations to the supplied file queue but must not commit the queue.

A co-installer can handle this DIF request in its preprocessing pass and/or in its postprocessing pass. In its preprocessing pass, a co-installer performs any operations that must occur before Windows loads the drivers and starts the device.

In its postprocessing pass, the device is up and running unless the DI_NEEDREBOOT flag was set. If this flag is set, Windows could not bring the device online dynamically.

If the installer returns a Win32 error code, Windows abandons the installation.

If Windows cannot locate an INF file for a new device, it sends DIF_INSTALLDEVICE in an attempt to install a [*null driver*](https://msdn.microsoft.com/library/windows/hardware/ff556313#wdkgloss-null-driver). The default handler ([**SetupDiInstallDevice**](https://msdn.microsoft.com/library/windows/hardware/ff552039)) checks whether the device either supports [*raw mode*](https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-raw-mode) or is a non-PnP device (reported by [**IoReportDetectedDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549597)), In the latter case, Windows installs a null driver for the device.

If this attempt fails, Windows sends DIF_INSTALLDEVICE again, this time with the DI_FLAGSEX_SETFAILEDINSTALL flag set in the [**SP_DEVINSTALL_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346) structure. In this case, the default handler just sets the FAILEDINSTALL flag in the device's **ConfigFlags** registry value. If the DI_FLAGSEX_SETFAILEDINSTALL flag is set, class installers must return NO_ERROR or ERROR_DI_DO_DEFAULT and co-installers must return NO_ERROR.

For more information about DIF codes, see [Handling DIF Codes](https://msdn.microsoft.com/library/windows/hardware/ff546094).

### **Calling the Default Handler SetupDiInstallDevice**

For general information about when and how to call a **SetupDiInstallDevice**, see [Calling Default DIF Code Handlers](https://msdn.microsoft.com/library/windows/hardware/ff537868).

In the rare situation where the class installer must perform operations after all **SetupDiInstallDevice** operations, except for starting a device, have completed, the class installer must:

1.  Perform operations that must be done before calling **SetupDiInstallDevice**.

2.  Set the DI_DONOTCALLCONFIGMGR flag in the SP_DEVINSTALL_PARAMS.**Flags** member for the device. If this flag is set, **SetupDiInstallDevice** performs all default installation operations except for starting the device.

3.  Call **SetupDiInstallDevice** to perform all default installation operations except for starting the device.

4.  Perform the operations that must be done after all default installation operations, except for starting the device, have completed.

5.  Call [**SetupDiRestartDevices**](https://msdn.microsoft.com/library/windows/hardware/ff552104) to start the device.

6.  Return NO_ERROR if the class installer successfully completed the installation operation or return a Win32 error if the installation operation failed.

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


[**DIF_INSTALLDEVICEFILES**](dif-installdevicefiles.md)

[**SetupDiInstallDevice**](https://msdn.microsoft.com/library/windows/hardware/ff552039)

[**SP_DEVINFO_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344)

[**SP_DEVINSTALL_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346)

 

 






