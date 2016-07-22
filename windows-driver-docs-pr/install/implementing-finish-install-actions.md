---
title: Implementing Finish-Install Actions
description: Implementing Finish-Install Actions
ms.assetid: accdf2f5-f324-41dc-afc1-18e03b422fcc
keywords: ["finish-install actions WDK device installations", "actions WDK finish-install", "DI_FLAGSEX_FINISHINSTALL_ACTION", "DIF_FINISHINSTALL_ACTION"]
---

# Implementing Finish-Install Actions


*Installers* (a class installer, class co-installer, or device co-installer) supply finish-install actions. A finish-install action can run an executable program, create a process, create a thread, or execute code in the device driver installation finish-install process.

To implement finish-install actions, an installer:

1.  Sets the DI\_FLAGSEX\_FINISHINSTALL\_ACTION flag when the installer processes a [**DIF\_NEWDEVICEWIZARD\_FINISHINSTALL**](https://msdn.microsoft.com/library/windows/hardware/ff543702) DIF code and returns one of the following error codes:
    -   ERROR\_DI\_DO\_DEFAULT if it is a class installer without finish-install wizard pages.
    -   NO\_ERROR if it is a class installer with finish-install wizard pages or a co-installer with or without finish-install wizard pages.

2.  Performs the finish-install actions when it processes a [**DIF\_FINISHINSTALL\_ACTION**](https://msdn.microsoft.com/library/windows/hardware/ff543684) request.

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

     

    **Note**   If a finish-install action fails and should not be attempted again, a class installer returns ERROR\_DI\_DO\_DEFAULT and a device or class co-installer returns NO\_ERROR.

     

For information about how to develop finish-install actions, see [Guidelines for Implementing Finish-Install Actions](guidelines-for-implementing-finish-install-actions.md) For sample code that shows how to implement finish-install actions, see the following topics:

[Code Example: Finish-Install Actions in a Class Installer](code-example--finish-install-actions-in-a-class-installer.md)

[Code Example: Finish-Install Actions in a Co-installer](code-example--finish-install-actions-in-a-co-installer.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Implementing%20Finish-Install%20Actions%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




