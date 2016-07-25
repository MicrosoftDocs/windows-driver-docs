---
title: Checking for In-Progress Installations
description: Checking for In-Progress Installations
ms.assetid: 9630a22e-65df-41f1-bfaf-ef4df9ca8aed
keywords: ["in-progress installations WDK", "checking in-progress installations", "verifying in-progress installations"]
---

# Checking for In-Progress Installations


## <a href="" id="ddk-checking-for-in-progress-installations-dg"></a>


Your [*device installation application*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-installation-application) should determine whether other installation activities are in progress before performing its installations. To make this determination, the device installation application should call [**CMP\_WaitNoPendingInstallEvents**](https://msdn.microsoft.com/library/windows/hardware/ff537916), typically with a zero time-out value. If the return value from this function indicates other installation activities are pending (for example, the Found New Hardware Wizard might be active), the device installation application should exit.

To make your [*device installation application*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-installation-application) compatible with platforms that do not support **CMP\_WaitNoPendingInstallEvents**, the application should include the following code:

```
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

Use of this code is based on the premise that if a platform does not support **CMP\_WaitNoPendingInstallEvents**, the platform does not start AutoRun if installation activities are in progress.

For a sample usage of this code, see the toaster installation package under the *src\\general\\toaster* subdirectory of the Windows Driver Kit (WDK).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Checking%20for%20In-Progress%20Installations%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




