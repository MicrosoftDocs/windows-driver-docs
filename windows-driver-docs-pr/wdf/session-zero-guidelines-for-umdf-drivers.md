---
title: Session Zero Guidelines for UMDF Drivers
description: Session Zero Guidelines for UMDF Drivers
ms.assetid: 67EF6762-AA31-4D35-8EB3-04F9CD34C7D1
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Session Zero Guidelines for UMDF Drivers


Starting in Windows Vista, the operating system isolates services and system processes in Session 0, while applications run in subsequent, higher numbered sessions. Because the UMDF host process (WUDFHost.exe) is one of the system processes that run in session 0, UMDF drivers are isolated from applications. As a result, you must use the following guidelines when developing your driver:

-   Do not create a user interface (UI) element, such as a dialog box, or depend on user input. Because the user is not running in Session 0, he or she never sees the UI and cannot respond to it.

    Similarly, do not manipulate any UI elements. For example, a UMDF driver cannot enumerate windows in the user's session.

-   If your driver must communicate with a service, use a client/server mechanism such as remote procedure call (RPC) or named pipes.
-   Use caution when calling functions in the Windows API. Some functions may manipulate UI elements or attempt to access named objects in a user's session. Do not call Windows functions that you would not call from a user-mode service. As a general rule, a UMDF driver can safely call functions that are exported in kernel32.dll, but not functions exported in user32.dll.

    A UMDF driver might call Windows functions to perform the following tasks:

    -   A driver might call **SetupDi***Xxx* functions to retrieve a Plug and Play device property. For example, the [UMDF Sample Driver for OSR USB Fx2 Learning Kit](http://go.microsoft.com/fwlink/p/?linkid=256202) calls [**SetupDiGetDeviceRegistryProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551967) to retrieve the GUID for the device's bus type.
        **Note**  A UMDF driver cannot safely call many of the **SetupDi***Xxx* functions, but it is safe to call functions that retrieve device node properties.

         

    -   A driver that retrieves I/O requests from a manual queue might create a periodic timer to poll the queue. For example, the [WudfVhidmini](http://go.microsoft.com/fwlink/p/?linkid=256226) sample registers a timer callback routine by calling [**CreateThreadpoolTimer**](https://msdn.microsoft.com/library/windows/desktop/ms682466), and then sets a periodic timer by calling [**SetThreadpoolTimer**](https://msdn.microsoft.com/library/windows/desktop/ms686271).
        **Note**  Starting in version 1.11, UMDF provides support for work items. For more information, see [Using Work Items](using-workitems.md).

         

For additional information about using system services outside the frameworks, see Chapter 14 ("Beyond the Frameworks") of Orwick, Penny, and Guy Smith. *Developing Drivers with the Windows Driver Foundation*. Redmond, WA: Microsoft Press, 2007.

For additional information about session zero isolation, see [Impact of Session 0 Isolation on Services and Drivers in Windows](http://go.microsoft.com/fwlink/p/?linkid=240132).

 

 





