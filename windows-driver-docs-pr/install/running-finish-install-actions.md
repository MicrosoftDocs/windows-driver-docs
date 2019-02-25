---
title: Running Finish-Install Actions
description: Running Finish-Install Actions
ms.assetid: 9a5f8e7c-ba11-4a2a-82dd-32cd91c3cc39
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Running Finish-Install Actions


In Windows 8, and later versions of Windows, finish-install actions do not automatically run as part of device installation. When a device is installed with a driver that includes a finish-install action, the finish-install action will not automatically run. Instead, Windows prompts a user to “Finish installing device software” in the Notifications area or in Windows Action Center. Installing device software requires administrator permissions. If installation fails, the software must prompt the user to try the installation again. Installing supporting software that should accompany a driver can still be accomplished with a finish-install action, but it will not be installed automatically.

Prior to Windows 8, if a device is flagged as needing to perform a finish-install action, Windows initially attempts to complete the finish-install actions by running a finish-install process at one of the following times:

-   For a device that is installed during Windows setup, the first time that an administrator logs on to Windows after Windows setup is finished.

-   For a device that is installed or reinstalled after Windows is installed, after the core device installation operations have completed, as follows:
    -   For a [hardware-first installation](hardware-first-installation.md) of a device, Windows runs the initial finish-install process. If the current user is not an administrator, Windows will first prompt the user to enter the credentials of an administrator before it runs the initial finish-install process.

    -   For a [software-first installation](software-first-installation.md) of a device, Windows runs the initial finish-install process in the context of the administrator who initiated the installation or reinstallation.

Prior to Windows 8, if the initial attempt to complete the finish-install actions succeeds, the finish-install process clears the device as being flagged to perform a finish install action. If the initial attempt to complete the finish-install actions fails, the finish-install process does not clear the device as being flagged to perform a finish install action and exits. Subsequently, while the device remains flagged to perform a finish install action, Windows repeatedly attempts to complete the finish-install actions by running a new finish-install process whenever the device is enumerated, as follows:

-   While the device remains installed, the next time an administrator logs on.

-   If an administrator clicks Scan for hardware changes on the **Action** menu of Device Manager or an installation program calls [**CM_Reenumerate_DevNode**](https://msdn.microsoft.com/library/windows/hardware/ff539763) in the context of an administrator.

If the device is flagged to perform a finish-install action, the finish-install process calls [**SetupDiCallClassInstaller**](https://msdn.microsoft.com/library/windows/hardware/ff550922) to send a [**DIF_FINISHINSTALL_ACTION**](https://msdn.microsoft.com/library/windows/hardware/ff543684) request to installers for the device.

If an installer has finish-install actions, the installer performs finish-install actions and returns an appropriate error code for the [**DIF_FINISHINSTALL_ACTION**](https://msdn.microsoft.com/library/windows/hardware/ff543684) request. An installer returns one of the error codes in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Error code</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>ERROR_DI_DO_DEFAULT</p></td>
<td align="left"><p>Class installer: The class installer has successfully run its finish-install actions and is requesting that Windows perform its default processing.</p>
<p>The class installer also returns this error code if it has no finish-install actions, or a finish-install action fails and should not be attempted again.</p>
<p>Device or class co-installer: Co-installers do not return this error code.</p></td>
</tr>
<tr class="even">
<td align="left"><p>NO_ERROR</p></td>
<td align="left"><p>Class installer: The class installer has successfully run its finish-install action. Windows should not perform its default processing.</p>
<p>Device or class co-installer: The co-installer has either successfully run its finish-install actions or has no finish-install actions.</p>
<p>The co-installer also returns this error code if a finish-install action fails and should not be attempted again.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Microsoft Win32 error</p></td>
<td align="left"><p>The class installer, device co-installer, or class co-installer encountered an error while processing a finish-install action, but should attempt to process the finish-install action again.</p>
<p>By returning a Win32 error code, the installer indicates that Windows should run another finish-install process to complete the finish-install actions the next time the device is enumerated. The installer should also inform the user of this situation.</p></td>
</tr>
</tbody>
</table>

 

 

 





