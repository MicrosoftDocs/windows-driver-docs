---
ms.assetid: ee46801a-4fa5-465a-aa81-5e76eb83d315
title: Building for OneCore
description: You can build a single binary that targets pre-Windows 10 and OneCore editions.
ms.date: 10/02/2018
ms.localizationpriority: medium
---

# Building for OneCore

When you use Visual Studio to build user-mode code for Windows 10, you can customize linker options to target specific versions of Windows.  Consider the following factors:

* Should the built binary run on only the most recent version of Windows?  Or should it run on earlier versions, such as Windows 7?  

* Does your project have any [UWP](https://docs.microsoft.com/windows/uwp/get-started/whats-a-uwp) dependencies?

For example, when you create a new UMDF v2 driver project, Visual Studio links to `OneCoreUAP.lib` by default.  This results in a binary that runs on the most recent version of Windows, and it permits addition of UWP functionality.

However, depending on your requirements, you might choose instead to link to `OneCore.lib`. The following table shows the scenarios applicable to each library:

|Library|Scenario|
|-|-|
|`OneCore.lib`|All editions of Windows 7 and later, no UWP support|
|`OneCoreUAP.lib`|Windows 7 and later, UWP editions (Desktop, IoT, HoloLens, but not Nano Server) of Windows 10|

>[!NOTE]
>To change linker options in Visual Studio, choose project properties and navigate to **Linker->Input->Additional Dependencies**.

A subset of Windows APIs compile cleanly but return runtime errors on non-Desktop OneCore editions (for example Mobile or IoT).

For example, the [**InstallApplication**](https://docs.microsoft.com/windows/desktop/api/appmgmt/nf-appmgmt-installapplication) function returns `ERROR_ NOT_SUPPORTED` on non-Desktop OneCore editions.  The [ApiValidator](validating-universal-drivers.md) tool also reports these problems. The next section describes how to fix them.

## Fixing ApiValidator errors by using [**IsApiSetImplemented**](https://docs.microsoft.com/windows/desktop/api/apiquery2/nf-apiquery2-isapisetimplemented)

If your code calls non-universal APIs, you might see the following [ApiValidator](validating-universal-drivers.md) errors:

* `Error: <Binary Name> has unsupported API call to <Module Name><Api Name>`
    
    If your app or base driver needs to run on Windows 10 as well as earlier versions of Windows, you must remove API calls in the above category.

* `Error: <Binary Name> has a dependency on <Module Name><Api Name> but is missing: IsApiSetImplemented("<contract-name-for-Module>)`
    
    API calls in the above category compile fine, but may not behave as expected at runtime, depending on the target operating system. To pass the U requirement of [DCHU](https://docs.microsoft.com/windows-hardware/drivers/develop/getting-started-with-universal-drivers#design-principles), wrap these calls with [**IsApiSetImplemented**](https://docs.microsoft.com/windows/desktop/api/apiquery2/nf-apiquery2-isapisetimplemented).

This enables you to compile your code with no errors.  Then at runtime, if the target machine does not have the needed API, [**IsApiSetImplemented**](https://docs.microsoft.com/windows/desktop/api/apiquery2/nf-apiquery2-isapisetimplemented) returns FALSE.

The following code samples illustrate how to do this.

## Code sample: Direct usage of API, without evaluating for existence

This code runs fine on versions of Windows earlier than Windows 10, but running it on a OneCore edition of Windows 10 results in WTSEnumerateSessions failure : 78 or ERROR_CALL_NOT_IMPLEMENTED 120 (0x78).

This code sample fails the U part of DCHU with the following [ApiValidator](validating-universal-drivers.md) errors:

```cpp
ApiValidation: Error: FlexLinkTest.exe has a dependency on 'wtsapi32.dll!WTSEnumerateSessionsW' but is missing: IsApiSetImplemented("ext-ms-win-session-wtsapi32-l1-1-0")
ApiValidation: Error: FlexLinkTest.exe has a dependency on 'wtsapi32.dll!WTSFreeMemory' but is missing: IsApiSetImplemented("ext-ms-win-session-wtsapi32-l1-1-0")
ApiValidation: NOT all binaries are Universal
```
Here's the code:

```cpp
#include <windows.h>
#include <stdio.h>
#include <Wtsapi32.h>

int __cdecl wmain(int /* argc */, PCWSTR /* argv */ [])
{
    PWTS_SESSION_INFO pInfo = {};
    DWORD count = 0;

    if (WTSEnumerateSessionsW(WTS_CURRENT_SERVER_HANDLE, 0, 1, &pInfo, &count))
    {
        wprintf(L"SessionCount = %d\n", count);

        for (ULONG i = 0; i < count; i++)
        {
            PWTS_SESSION_INFO pCurInfo = &pInfo[i];
            wprintf(L"    %s: ID = %d, state = %d\n", pCurInfo->pWinStationName, pCurInfo->SessionId, pCurInfo->State);
        }

        WTSFreeMemory(pInfo);
    }
    else
    {
        wprintf(L"WTSEnumerateSessions failure : %x\n", GetLastError());
    } 

    return 0;
}
```

## Code sample: Direct usage of API, after evaluating for existence

This sample shows how to call [**IsApiSetImplemented**](https://docs.microsoft.com/windows/desktop/api/apiquery2/nf-apiquery2-isapisetimplemented). This sample passes the U part of DCHU with the following [ApiValidator](validating-universal-drivers.md) output:

```cpp
ApiValidation: All binaries are Universal
```

Here's the code:

```cpp
#include <windows.h>
#include <stdio.h>
#include <Wtsapi32.h>

int __cdecl wmain(int /* argc */, PCWSTR /* argv */ [])
{
    PWTS_SESSION_INFO pInfo = {};
    DWORD count = 0;

    if (!IsApiSetImplemented("ext-ms-win-session-wtsapi32-l1-1-0"))
    {
        wprintf(L"IsApiSetImplemented on ext-ms-win-session-wtsapi32-l1-1-0 returns FALSE\n");
    }
    else
    {
        if (WTSEnumerateSessionsW(WTS_CURRENT_SERVER_HANDLE, 0, 1, &pInfo, &count))
        {
            wprintf(L"SessionCount = %d\n", count);

            for (ULONG i = 0; i < count; i++)
            {
                PWTS_SESSION_INFO pCurInfo = &pInfo[i];
                wprintf(L"    %s: ID = %d, state = %d\n", pCurInfo->pWinStationName, pCurInfo->SessionId, pCurInfo->State);
            }

            WTSFreeMemory(pInfo);
        }
        else
        {
            wprintf(L"WTSEnumerateSessions failure : %x\n", GetLastError());
        }
    }

    return 0;
}
```

## Recommended actions

* Review the linker options above and update your Visual Studio project accordingly.
* Use the [ApiValidator](validating-universal-drivers.md) tool in the WDK.  This tool runs automatically when you build a driver in Visual Studio.
* Use runtime testing to verify that your user-mode code runs as you expect on non-Desktop OneCore editions.  Note that stubbed APIs may generate different error codes.

## See Also

* [Validating Universal Windows drivers](https://docs.microsoft.com/windows-hardware/drivers/develop/validating-universal-drivers)
* [OneCore](https://docs.microsoft.com/windows-hardware/get-started/what-s-new-in-windows)

<!--API BOILERPLATE: Compiles using OneCore.lib but returns ERROR_CALL_NOT_IMPLEMENTED on non-Desktop OneCore editions.-->
