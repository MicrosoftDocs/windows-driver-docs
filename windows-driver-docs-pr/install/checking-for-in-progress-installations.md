---
title: How a Device Installation Application Checks for In-Progress Device Installations
description: How a Device Installation Application determines whether other device installation activities are in progress before performing its installations.
keywords:
- in-progress installations WDK
- checking in-progress installations
- verifying in-progress installations
ms.custom: contperf-fy22q3
ms.date: 03/08/2022
---

# How a Device Installation Application checks for in-progress device installations

Your *device installation application* should determine whether other device installation activities are in progress before performing its installations. To make this determination, the device installation application should call [**CMP_WaitNoPendingInstallEvents**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_waitnopendinginstallevents), typically with a zero time-out value. If the return value from this function indicates other installation activities are pending (for example, the Found New Hardware Wizard might be active), the device installation application should exit.

To make your *device installation application* compatible with platforms that do not support **CMP_WaitNoPendingInstallEvents**, the application should include the following code:

```cpp
BOOL
IsDeviceInstallInProgress (VOID)
{
    HMODULE hModule;
    CMP_WAITNOPENDINGINSTALLEVENTS_PROC pCMP_WaitNoPendingInstallEvents;

    hModule = GetModuleHandle(TEXT("setupapi.dll"));
    if(!hModule)
    {
        // Should never happen since we're linked to SetupAPI, but...
        return FALSE;
    }

    pCMP_WaitNoPendingInstallEvents =
        (CMP_WAITNOPENDINGINSTALLEVENTS_PROC)GetProcAddress(hModule,
                                             "CMP_WaitNoPendingInstallEvents");
    if(!pCMP_WaitNoPendingInstallEvents)
    {
        // We're running on a release of the operating system that doesn't supply this function.
        // Trust the operating system to suppress AutoRun when appropriate.
        return FALSE;
    }
    return (pCMP_WaitNoPendingInstallEvents(0) == WAIT_TIMEOUT);
}

int
__cdecl
_tmain(IN int argc, IN PTCHAR argv[])
{
    if(IsDeviceInstallInProgress()) {
        //
        // We don't want to start right now.  Instead, our
        // device co-installer will invoke this application
        // (if necessary) during finish-install processing.
        //
        return -1;
    }
    .
    .
}
```

Use of this code is based on the premise that if a platform does not support **CMP_WaitNoPendingInstallEvents**, the platform does not start AutoRun if installation activities are in progress.

For a sample usage of this code, see the toaster installation package under the *src\\general\\toaster* subdirectory of the Windows Driver Kit (WDK).
