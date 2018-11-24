---
title: DIF_ALLOW_INSTALL
description: DIF_ALLOW_INSTALL
ms.assetid: 0bcda90e-f9f1-4965-a08b-d884077a2e8b
keywords: ["DIF_ALLOW_INSTALL Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DIF_ALLOW_INSTALL
api_location:
- Setupapi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DIF_ALLOW_INSTALL


A DIF_ALLOW_INSTALL request asks the installers for a device whether Windows can proceed to install the device.

### When Sent

After selecting a driver for the device but before installing the device.

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
<td align="left"><p>Should not handle</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Class Installer</p></td>
<td align="left"><p>Can handle</p></td>
</tr>
</tbody>
</table>

 

### Installer Input

<a href="" id="deviceinfoset"></a>*DeviceInfoSet*  
Supplies a handle to the [device information set](https://msdn.microsoft.com/library/windows/hardware/ff541247) that contains the device.

<a href="" id="deviceinfodata"></a>*DeviceInfoData*  
Supplies a pointer to an [**SP_DEVINFO_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344) structure that identifies the device in the device information set.

<a href="" id="device-installation-parameters-"></a>Device Installation Parameters   
There are device installation parameters ([**SP_DEVINSTALL_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346)) associated with the *DeviceInfoData*.

<a href="" id="class-installation-parameters"></a>Class Installation Parameters  
None

### Installer Output

<a href="" id="none"></a>None  

### Installer Return Value

A co-installer can return NO_ERROR or a Win32 error. A co-installer should not return ERROR_DI_POSTPROCESSING_REQUIRED for this DIF request.

A class installer typically returns ERROR_DI_DO_DEFAULT or a Win32 error code.

Typical Win32 error codes for this DIF request include ERROR_DI_DONT_INSTALL and ERROR_NON_WINDOWS_NT_DRIVER.

**Note**  Class installers and co-installers should not freturn ERROR_REQUIRES_INTERACTIVE_WINDOWSTATION since that causes the device installation to fail. If the device installation requires user interaction, class installers and co-installers should support a [finish-install action](https://msdn.microsoft.com/library/windows/hardware/ff544940).

 

### Default DIF Code Handler

None

### Installer Operation

In response to a DIF_ALLOW_INSTALL request an installer confirms whether Windows can install the device.

An installer can fail this request if it determines that the selected driver is incorrect (for example, if the driver is a Windows 9x-only driver that will not work correctly on NT-based operating systems) or if it determines that a selected driver is known to have bugs.

An installer might fail this request if the DI_QUIETINSTALL flag is set in the device installation parameters and the installer has to display UI during device installation. However, this failure is rare because an installer can typically supply any UI pages in response to the DIF_NEWDEVICEWIZARD_FINISHINSTALL request. In that case, UI does not prevent the installer from succeeding a DIF_ALLOW_INSTALL request for which the quiet flag is set. However, if an installer cannot limit its UI to the finish-install case, the installer must fail this DIF request if the DI_QUIETINSTALL flag is set. An installer might have this restriction, for example, if it calls vendor-supplied code that displays UI.

If an installer fails this DIF request, Windows stops the installation.

If an installer fails this DIF request and DI_QUIETINSTALL is not set in the device installation parameters, the installer should display a dialog box with a message that explains why the device is not being installed.

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


[**SP_DEVINFO_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344)

[**SP_DEVINSTALL_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346)

 

 






