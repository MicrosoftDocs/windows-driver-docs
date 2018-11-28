---
title: Te.Service
description: Some TAEF features, such as Cross Machine Test Execution and RunAs, require that Te.Service is installed and started.
ms.assetid: 2F137748-865C-45de-8F60-B607EEB791C0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Te.Service


Some TAEF features, such as [Cross Machine Test Execution](cross-machine-execution.md) and [RunAs](runas.md), require that Te.Service is installed and started.

## <span id="installing_and_starting_te.service"></span><span id="INSTALLING_AND_STARTING_TE.SERVICE"></span>Installing and Starting Te.Service


-   Ensure that Wex.Services.exe, Wex.Common.dll, and Wex.Communication.dll all exist in the same directory. The default location is the \\Testing\\Runtimes\\TAEF subdirectory of the WDK
-   From an elevated command prompt, type the following:

    ``` syntax
    cd [your Wex.Services.exe directory]
    Wex.Services.exe /install:Te.Service
    sc start Te.Service
    ```

    **Note**  On CoreSystem, Te.Service can run as a console application instead of a service.




``` syntax
cd [your Wex.Services.exe directory]
Wex.Services.exe /run:Te.Service
```


## <span id="stopping_and_removing_te.service"></span><span id="STOPPING_AND_REMOVING_TE.SERVICE"></span>Stopping and Removing Te.Service


-   From an elevated command prompt, type the following:

    ``` syntax
    cd [your Wex.Services.exe directory]
    sc stop Te.Service
    Wex.Services.exe /remove:Te.Service
    ```

    On CoreSystem, close the console application running Te.Service.

## <span id="Processor_Architectures_Supported"></span><span id="processor_architectures_supported"></span><span id="PROCESSOR_ARCHITECTURES_SUPPORTED"></span>Processor Architectures Supported


Both the x86 and x64 versions of Te.Service support executing x86 and x64 tests.

## <span id="Safe_Mode_Installation_Instructions"></span><span id="safe_mode_installation_instructions"></span><span id="SAFE_MODE_INSTALLATION_INSTRUCTIONS"></span>Safe Mode Installation Instructions


By default, you will not be able to start the service in the Safe Mode. When you try to run sc start Te.Service, you'll get the following error: Error 1084: This service cannot be started in Safe Mode and this error is by (Windows) design.

To enable the TAEF service Safe Mode functionality, you need to:

-   Restart your computer in Safe Mode by pressing F8 before the Windows splash screen.
-   Click Start, click Run, type regedit, and then click OK.
-   Locate and then click the following registry subkey:
    -   HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\SafeBoot\\Minimal (for pure safe mode)
    -   HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\SafeBoot\\Network (for safe mode with networking)
-   On the Edit menu, point to New, click Key, and then type Te.Service.
-   Double-click Default, type Service in the Value data box, and then click OK.
-   Quit Registry Editor, and then restart your computer.
-   Open a command window with elevation privileges.
-   Now you should successfully start the service using sc start Te.Service

## <span id="Subscribing_to_Notifications"></span><span id="subscribing_to_notifications"></span><span id="SUBSCRIBING_TO_NOTIFICATIONS"></span>Subscribing to Notifications


When developing your server-running tests, you can subscribe for some server notifications in a way similar to the HandlerEx callback function. Currently, only the SERVICE\_CONTROL\_SESSIONCHANGE control code is supported.

To subscribe:

-   Define a callback function with a signature of the HandlerEx callback function.
-   Register this function using TAEF notification API
-   Unregister this function when you no longer want to receive notifications.
-   Link your code to Te.Common.lib

Example:

```cpp
    // define a call back function
    DWORD WINAPI HandlerEx(DWORD dwControl, DWORD dwEventType, LPVOID, LPVOID)
    {
        // Do some work here
        return 0;
    }

    // register the callback function to receive notifications
    TestNotification::RegisterHandler(HandlerEx));
```









