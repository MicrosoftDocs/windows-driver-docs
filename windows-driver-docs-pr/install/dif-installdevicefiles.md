---
title: DIF_INSTALLDEVICEFILES
description: DIF_INSTALLDEVICEFILES
ms.assetid: 544a9a88-156e-494d-9ef0-8070addfa86b
keywords: ["DIF_INSTALLDEVICEFILES Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DIF_INSTALLDEVICEFILES
api_location:
- Setupapi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DIF_INSTALLDEVICEFILES


A DIF_INSTALLDEVICEFILES request allows an installer to participate in copying the files to support a device or to make a list of the files for a device. The device files include files for the selected driver, any device interfaces, and any co-installers.

### When Sent

The [system-provided device installation components](https://msdn.microsoft.com/library/windows/hardware/ff728855) send this DIF request for a variety of reasons. Some device installation components send this DIF request before DIF_REGISTER_COINSTALLERS, DIF_INSTALLINTERFACES, and DIF_INSTALL_DEVICE to ensure that all the relevant files can be copied before proceeding with the installation. Some device installation components omit this DIF request and expect the files to be copied during the handling of those three DIF requests. In addition, some device installation components send this DIF request to retrieve the list of the files associated with a device.

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
Supplies a handle to the [device information set](https://msdn.microsoft.com/library/windows/hardware/ff541247) that contains the device whose supporting files are to be copied.

<a href="" id="deviceinfodata"></a>*DeviceInfoData*  
Supplies a pointer to an [**SP_DEVINFO_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344) structure that identifies the device in the device information set.

<a href="" id="device-installation-parameters-"></a>Device Installation Parameters   
There are device installation parameters ([**SP_DEVINSTALL_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346)) associated with the *DeviceInfoData*.

If the DI_NOVCP flag is set, the device installation parameters contain a valid **FileQueue** handle and installers that handle this DIF request add their file operations to this queue and do not commit the queue.

<a href="" id="class-installation-parameters"></a>Class Installation Parameters  
None

### Installer Output

<a href="" id="device-installation-parameters-"></a>Device Installation Parameters   
An installer can modify the **FileQueue**, if there is one.

### Installer Return Value

A co-installer can return NO_ERROR, ERROR_DI_POSTPROCESSING_REQUIRED, or a Win32 error code.

If a class installer successfully handles this request and [**SetupDiCallClassInstaller**](https://msdn.microsoft.com/library/windows/hardware/ff550922) should subsequently call the default handler, the class installer returns ERROR_DI_DO_DEFAULT.

If the class installer successfully handles this request, including directly calling the default handler, the class installer should return NO_ERROR and **SetupDiCallClassInstaller** will not subsequently call the default handler again.

**Note**  The class installer can directly call the default handler, but the class installer should never attempt to supersede the operations of the default handler.

 

For more information about calling the default handler, see [Calling Default DIF Code Handlers](https://msdn.microsoft.com/library/windows/hardware/ff537868).

If the class installer encounters an error, the installer should return an appropriate Win32 error code and **SetupDiCallClassInstaller** will not subsequently call the default handler.

### Default DIF Code Handler

[**SetupDiInstallDriverFiles**](https://msdn.microsoft.com/library/windows/hardware/ff552048)

### Installer Operation

In response to a DIF_INSTALLDEVICEFILES request an installer specifies any necessary file operations. For example, an installer can specify an additional file to be copied that is required for device installation. If the DI_NOVCP flag is set, an installer specifies file operations by adding them to the **FileQueue** in the device installation parameters. See the Microsoft Windows SDK for information about how to use file queues and for reference pages on file-queuing functions such as **SetupInstallFilesFromInfSection**.

If this DIF request is sent during device installation, and the installer returns a Microsoft Win32 error code, Windows stops the installation.

If a [system-provided device installation component](https://msdn.microsoft.com/library/windows/hardware/ff728855) sends this DIF request to retrieve a list of the files associated with a device, the component retrieves the file queue but does not commit the queue.

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


[**SetupDiInstallDriverFiles**](https://msdn.microsoft.com/library/windows/hardware/ff552048)

[**SP_DEVINFO_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344)

[**SP_DEVINSTALL_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346)

 

 






