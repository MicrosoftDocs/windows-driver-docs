---
title: Checking for In-Progress Installations
description: Checking for In-Progress Installations
ms.assetid: 9630a22e-65df-41f1-bfaf-ef4df9ca8aed
keywords:
- in-progress installations WDK
- checking in-progress installations
- verifying in-progress installations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Checking for In-Progress Installations





Your [*device installation application*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-installation-application) should determine whether other installation activities are in progress before performing its installations. To make this determination, the device installation application should call [**CMP_WaitNoPendingInstallEvents**](https://msdn.microsoft.com/library/windows/hardware/ff537916), typically with a zero time-out value. If the return value from this function indicates other installation activities are pending (for example, the Found New Hardware Wizard might be active), the device installation application should exit.

To make your [*device installation application*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-installation-application) compatible with platforms that do not support **CMP_WaitNoPendingInstallEvents**, the application should include the following code:

```cpp
BOOL
IsDeviceInstallInProgress (VOID)
{
    HMODULE hModule;
    CMP_WAITNOPENDINGINSTALLEVENTS_PROC pCMP_WaitNoPendingInstallEvents;

    hModule = GetModuleHandle(TEXT("setupapi.dll"));
    if(!hModule)
    {
        // Should never happen since we&#39;re linked to SetupAPI, but...
        return FALSE;
    }

    pCMP_WaitNoPendingInstallEvents = 
        (CMP_WAITNOPENDINGINSTALLEVENTS_PROC)GetProcAddress(hModule,
                                             "CMP_WaitNoPendingInstallEvents");
    if(!pCMP_WaitNoPendingInstallEvents)
    {
        // We&#39;re running on a release of the operating system that doesn&#39;t supply this function.
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
        // We don&#39;t want to start right now.  Instead, our 
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

 

 





