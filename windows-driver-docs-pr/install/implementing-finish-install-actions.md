---
title: Implementing Finish-Install Actions
description: Implementing Finish-Install Actions
ms.assetid: accdf2f5-f324-41dc-afc1-18e03b422fcc
keywords:
- finish-install actions WDK device installations
- actions WDK finish-install
- DI_FLAGSEX_FINISHINSTALL_ACTION
- DIF_FINISHINSTALL_ACTION
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Implementing Finish-Install Actions


*Installers* (a class installer, class co-installer, or device co-installer) supply finish-install actions. A finish-install action can run an executable program, create a process, create a thread, or execute code in the device driver installation finish-install process.

To implement finish-install actions, an installer:

1.  Sets the DI_FLAGSEX_FINISHINSTALL_ACTION flag when the installer processes a [**DIF_NEWDEVICEWIZARD_FINISHINSTALL**](https://msdn.microsoft.com/library/windows/hardware/ff543702) DIF code and returns one of the following error codes:
    -   ERROR_DI_DO_DEFAULT if it is a class installer without finish-install wizard pages.
    -   NO_ERROR if it is a class installer with finish-install wizard pages or a co-installer with or without finish-install wizard pages.

2.  Performs the finish-install actions when it processes a [**DIF_FINISHINSTALL_ACTION**](https://msdn.microsoft.com/library/windows/hardware/ff543684) request.

    An installer returns one of the error codes in the following table.

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
    <td align="left"><p>Class installer: The class installer has successfully run its finish-install actions and is requesting Windows to perform its default processing. A class installer should also return this error code if it has no finish-install actions.</p>
    <p>Device or class co-installer: Co-installers do not return this error code.</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>NO_ERROR</p></td>
    <td align="left"><p>Class installer: The class installer has successfully run its finish-install action. Windows should not perform its default processing.</p>
    <p>Device or class co-installer: The co-installer has either successfully run its finish-install actions or has no finish-install actions.</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>Microsoft Win32 error</p></td>
    <td align="left"><p>The installer encountered an error, but the finish-install action should be attempted again. Returning a Win32 error code indicates that Windows should run another finish-install process to complete the finish-install actions the next time the device is enumerated.</p></td>
    </tr>
    </tbody>
    </table>




**Note**   If a finish-install action fails and should not be attempted again, a class installer returns ERROR_DI_DO_DEFAULT and a device or class co-installer returns NO_ERROR.




For information about how to develop finish-install actions, see [Guidelines for Implementing Finish-Install Actions](guidelines-for-implementing-finish-install-actions.md) For sample code that shows how to implement finish-install actions, see the following topics:

[Code Example: Finish-Install Actions in a Class Installer](code-example--finish-install-actions-in-a-class-installer.md)

[Code Example: Finish-Install Actions in a Co-installer](code-example--finish-install-actions-in-a-co-installer.md)









