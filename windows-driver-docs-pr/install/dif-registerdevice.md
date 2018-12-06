---
title: DIF_REGISTERDEVICE
description: DIF_REGISTERDEVICE
ms.assetid: cb5f12f4-d429-4f02-b560-08807ffa3793
keywords: ["DIF_REGISTERDEVICE Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DIF_REGISTERDEVICE
api_location:
- Setupapi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DIF_REGISTERDEVICE


The DIF_REGISTERDEVICE request allows an installer to participate in registering a newly created device instance with the PnP manager. Windows sends this DIF request for non-PnP devices.

### When Sent

When an installer reports a previously unknown device in response to a [**DIF_DETECT**](dif-detect.md) request. Windows sends this DIF request in the analyze phase of the Add Hardware Wizard before it installs the device. Windows also sends this request during non-PnP detection.

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
Supplies a handle to the [device information set](https://msdn.microsoft.com/library/windows/hardware/ff541247) that contains the device.

<a href="" id="deviceinfodata"></a>*DeviceInfoData*  
Supplies a pointer to an [**SP_DEVINFO_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344) structure that identifies the device in the device information set.

<a href="" id="device-installation-parameters-"></a>Device Installation Parameters   
There are device installation parameters ([**SP_DEVINSTALL_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346)) associated with the *DeviceInfoData*.

<a href="" id="class-installation-parameters-"></a>Class Installation Parameters   
None

### Installer Output

None

### Installer Return Value

A co-installer can return NO_ERROR or a Win32 error code. A co-installer should not return ERROR_DI_POSTPROCESSING_REQUIRED for this DIF request.

If an installer determines that the device is a duplicate it returns ERROR_DUPLICATE_FOUND.

If a class installer successfully handles this request and [**SetupDiCallClassInstaller**](https://msdn.microsoft.com/library/windows/hardware/ff550922) should subsequently call the default handler, the class installer returns ERROR_DI_DO_DEFAULT.

If the class installer successfully handles this request, including directly calling the default handler, the class installer should return NO_ERROR and **SetupDiCallClassInstaller** will not subsequently call the default handler again.

**Note**  The class installer can directly call the default handler, but the class installer should never attempt to supersede the operations of the default handler.

 

For more information about calling the default handler, see [Calling Default DIF Code Handlers](https://msdn.microsoft.com/library/windows/hardware/ff537868).

If the class installer encounters an error, the installer should return an appropriate Win32 error code and **SetupDiCallClassInstaller** will not subsequently call the default handler.

If the installer determines that the device is a duplicate, the installer returns ERROR_DUPLICATE_FOUND.

### Default DIF Code Handler

[**SetupDiRegisterDeviceInfo**](https://msdn.microsoft.com/library/windows/hardware/ff552091)

### Installer Operation

A [*device installation application*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-installation-application) typically sends this DIF request to register a non-PnP device with the PnP manager. Starting with Microsoft Windows 2000, non-PnP devices must be registered before they can be installed.

An installer typically handles this DIF request to do duplicate detection. Such an installer typically calls the default handler ([**SetupDiRegisterDeviceInfo**](https://msdn.microsoft.com/library/windows/hardware/ff552091)) and specifies its detection routine. If the registration is successful and the installer determines that the device is not a duplicate, the installer returns NO_ERROR.

A co-installer should perform any operations to handle this DIF request in its preprocessing pass. When the co-installer is called for postprocessing, the device instance has already been registered by either the class installer or the default handler.

If an installer returns an error for this DIF code, typically ERROR_DUPLICATE_FOUND, Windows deletes the device from the device information set.

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


[**DIF_DETECT**](dif-detect.md)

[**SetupDiRegisterDeviceInfo**](https://msdn.microsoft.com/library/windows/hardware/ff552091)

[**SP_DEVINFO_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344)

[**SP_DEVINSTALL_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346)

 

 






