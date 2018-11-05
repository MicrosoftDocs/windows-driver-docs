---
title: DIF_FINISHINSTALL_ACTION
description: DIF_FINISHINSTALL_ACTION
ms.assetid: 76eba79b-7a8a-478e-aaea-8b36eee51846
keywords: ["DIF_FINISHINSTALL_ACTION Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DIF_FINISHINSTALL_ACTION
api_location:
- Setupapi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DIF_FINISHINSTALL_ACTION


A DIF_FINISHINSTALL_ACTION request allows an installer to run finish-install actions in an interactive administrator context after all other device installation operations have completed.

### When Sent

In Windows 8 and later versions, finish-install actions do not automatically run as part of device installation. To complete a device finish-install action, a user must click on “Finish installing device software” in the Action Center to complete the installation.

For more information, see [Running Finish-Install Actions](https://msdn.microsoft.com/library/windows/hardware/ff550700).

In Windows 7, the finish-install process runs only in the context of a user with administrator credentials at one of the following times:

-   The next time that a user who has administrator credentials logs on while the device is attached.
-   When the device is reattached.
-   When the user selects Scan for hardware changes in Device Manager.

If a user is signed in without administrative privileges, Windows prompts the user for consent and credentials to run the finish-install actions in an administrator context.

### Who Handles

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Class co-installer</p></td>
<td align="left"><p>Can handle</p></td>
</tr>
<tr class="even">
<td align="left"><p>Device co-installer</p></td>
<td align="left"><p>Can handle</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Class installer</p></td>
<td align="left"><p>Can handle</p></td>
</tr>
</tbody>
</table>

 

### Installer Input

<a href="" id="deviceinfoset"></a>*DeviceInfoSet*  
A handle to the [device information set](https://msdn.microsoft.com/library/windows/hardware/ff541247) that contains the device being installed.

<a href="" id="deviceinfodata"></a>*DeviceInfoData*  
A pointer to an [**SP_DEVINFO_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344) structure that represents the device being installed.

<a href="" id="device-installation-parameters-"></a>Device Installation Parameters   
There are device installation parameters (a [**SP_DEVINSTALL_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346) structure) associated with *DeviceInfoData*.

<a href="" id="class-installation-parameters"></a>Class Installation Parameters  
None

### Installer Output

<a href="" id="device-installation-parameters-"></a>Device Installation Parameters   
An installer sets the DI_NEEDREBOOT flag if a system restart is required to complete its finish-install actions.

### Installer Return Value

An installer returns one of the values that are listed in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Return value</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>ERROR_DI_DO_DEFAULT</p></td>
<td align="left"><p>Class installer: The installer has no finish-install actions, has successfully completed the finish-install actions, or has determined that it cannot ever successfully complete its finish install actions. Device installation should perform the default processing for the request.</p>
<p>Co-installer: Co-installers must not return this error code.</p></td>
</tr>
<tr class="even">
<td align="left"><p>NO_ERROR</p></td>
<td align="left"><p>Class installer: A class installer should not return this error code. If a class installer returns this error code, device installation does not perform the default processing for the request.</p>
<p>Co-installer: The installer has no finish-install actions, has successfully completed the finish-install actions, or has determined that it cannot ever successfully complete its finish install actions.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Win32 error code</p></td>
<td align="left"><p>Class installer or co-installer: The installer encountered an error while processing a finish-install action, and device installation should attempt to complete the finish-install actions the next time the device is enumerated in the context of an administrator.</p></td>
</tr>
</tbody>
</table>

 

### Default DIF Code Handler

Windows 7 uses [**SetupDiFinishInstallAction**](https://msdn.microsoft.com/library/windows/hardware/ff551022).

There is no default DIF Code Handler in Windows 8 and later versions, and [**SetupDiFinishInstallAction**](https://msdn.microsoft.com/library/windows/hardware/ff551022) has been removed.

### Comments

Because device installation cannot determine from an ERROR_DI_DO_DEFAULT return code or a NO_ERROR return code whether a finish-install action actually succeeded, the installer should notify the user of the status of a finish-installer action.

For more information about finish-install actions, see [How Device Installation Processes Finish-Install Actions](https://msdn.microsoft.com/library/windows/hardware/ff546216) and [Implementing Finish-Install Actions](https://msdn.microsoft.com/library/windows/hardware/ff546302).

For general information about DIF codes, see [Handling DIF Codes](https://msdn.microsoft.com/library/windows/hardware/ff546094) and [Calling Default DIF Code Handlers](https://msdn.microsoft.com/library/windows/hardware/ff537868).

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
<td align="left"><p>Supported in Windows Vista through Windows 7.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Setupapi.h (include Setupapi.h)</td>
</tr>
</tbody>
</table>

## See also


[**SetupDiFinishInstallAction**](https://msdn.microsoft.com/library/windows/hardware/ff551022)

 

 






