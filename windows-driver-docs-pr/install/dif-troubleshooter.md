---
title: DIF_TROUBLESHOOTER
description: DIF_TROUBLESHOOTER
ms.assetid: e8477d4d-cc81-48aa-9d51-9f37c3cce0cb
keywords: ["DIF_TROUBLESHOOTER Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DIF_TROUBLESHOOTER
api_location:
- Setupapi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DIF_TROUBLESHOOTER


The DIF_TROUBLESHOOTER request allows an installer to start a troubleshooter for a device or to return CHM and HTM troubleshooter files for Windows to start.

**Note**  This DIF code is only supported on Windows Server 2003, Windows XP, and Microsoft Windows 2000.

 

### When Sent

When a user clicks the "Troubleshooter" button for a device in Device Manager.

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
Supplies a handle to the [device information set](https://msdn.microsoft.com/library/windows/hardware/ff541247) that contains the device.

<a href="" id="deviceinfodata"></a>*DeviceInfoData*  
Supplies a pointer to an [**SP_DEVINFO_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344) structure that identifies the device in the device information set.

<a href="" id="device-installation-parameters-"></a>Device Installation Parameters   
There are device installation parameters ([**SP_DEVINSTALL_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346)) associated with the *DeviceInfoData*.

<a href="" id="class-installation-parameters"></a>Class Installation Parameters  
An [**SP_TROUBLESHOOTER_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff553341) structure is associated with the *DeviceInfoData*.

### Installer Output

<a href="" id="class-installation-parameters"></a>Class Installation Parameters  
An installer might modify the [**SP_TROUBLESHOOTER_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff553341), setting a CHM or HTML file.

### Installer Return Value

If a co-installer does not handle this request, it returns NO_ERROR from its preprocessing pass.

If a co-installer handles this request, it does so in its postprocessing pass. If the co-installer supplies CHM and HTML files, it propagates the status it received (probably ERROR_DI_DO_DEFAULT). If the co-installer runs a troubleshooter and fixes the problem, the co-installer returns NO_ERROR. If the co-installer runs a troubleshooter but does not fix the problem, it propagates the status it received (ERROR_DI_DO_DEFAULT).

If a class installer supplies a CHM file and an HTML file, or the class installer runs a troubleshooter but does not fix the problem, the class installer returns ERROR_DI_DO_DEFAULT. Windows will subsequently call the default handler.

If a class installer starts its own troubleshooter and fixes the problem, the class installer returns NO_ERROR. Windows will not subsequently call the default handler.

If the class installer encounters an error, the installer returns an appropriate Win32 error code. Windows will not subsequently call the default handler.

### Default DIF Code Handler

None

There is no default handler for DIF_TROUBLESHOOTER, but the operating system provides default troubleshooters that attempt to resolve device problems if there are no installer-supplied troubleshooters.

### Installer Operation

An installer calls [**CM_Get_DevNode_Status**](https://msdn.microsoft.com/library/windows/hardware/ff538514) to get the device status and the CM problem code. Depending on the problem, an installer might provide a troubleshooter, a help file, or nothing. A troubleshooter can possibly resolve a problem with a device. If a troubleshooter resolves the problem, it should call **SetupDiCallClassInstaller** to send a DIF_PROPERTYCHANGE request of type DICS_PROPCHANGE. If an installer does not supply a troubleshooter for a device, it might supply a help file of problem-solving suggestions for the user.

If no installer runs its own troubleshooter, Windows runs HTML Help to display information to the user. If an installer supplied a CHM file in the class installation parameters, Windows displays that file. Otherwise, Windows displays system-supplied troubleshooting information.

The class installation parameters contain at most one **ChmFile** and **HtmlTroubleShooter** pair. If more than one installer specifies these values, Windows uses the values set by the last installer that handled the DIF request.

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
<td align="left"><p>Supported in Windows Server 2003, Windows XP, and Microsoft Windows 2000.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Setupapi.h (include Setupapi.h)</td>
</tr>
</tbody>
</table>

## See also


[**CM_Get_DevNode_Status**](https://msdn.microsoft.com/library/windows/hardware/ff538514)

[**SP_DEVINFO_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344)

[**SP_DEVINSTALL_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346)

[**SP_TROUBLESHOOTER_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff553341)

 

 






