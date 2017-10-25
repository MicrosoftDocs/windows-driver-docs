---
title: Windows 10 S Driver Requirements
ms.author: windowsdriverdev
ms.date: 05/05/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Windows 10 S Driver Requirements

This section describes driver installation requirements and blocked components on Windows 10 S.  

## Driver Requirements

To install on Windows 10 S, driver packages must meet the following requirements:

-   Driver packages must be digitally signed with a **Windows, WHQL, ELAM, or Store** certificate from the [Windows Hardware Developer Center Dashboard](https://aka.ms/DevCenterPortal).
-   Companion software must be signed with a [Windows Store Certificate](https://docs.microsoft.com/windows/uwp/publish/the-app-certification-process).
-   Does not include an \*.exe, \*.zip, \*.msi or \*.cab in the driver package that extracts unsigned binaries.
-   Driver installs using only INF directives.
-   Driver does not call [blocked inbox components](#blocked-inbox-components).
-   Drivers does not include any user interface components, apps, or settings.  Instead, use Universal applications from the Windows Store, for example:
    *  [Hardware Support Apps](https://docs.microsoft.com/windows-hardware/drivers/devapps/hardware-access-for-universal-windows-platform-apps)
    *  [Windows Store Device Apps](https://docs.microsoft.com/windows-hardware/drivers/devapps/meet-windows-store-device-apps)
    *  [Centennial Apps](https://developer.microsoft.com/windows/bridges/desktop)
-   Driver and firmware servicing uses Windows Update and not an updater app.

Finally, we recommend using a Universal Windows driver where possible.  For more info, see:

-   [Getting Started with Universal Drivers](https://docs.microsoft.com/windows-hardware/drivers/develop/getting-started-with-universal-drivers)
-   [Validating Universal Drivers](https://docs.microsoft.com/windows-hardware/drivers/develop/validating-universal-drivers)

## Blocked inbox components

The following components are blocked from executing on Windows 10 S:

-   bash.exe
-   cdb.exe
-   cmd.exe
-   cscript.exe
-   csi.exe
-   dnx.exe
-   fsi.exe
-   hh.exe
-   infdefaultinstall.exe (new addition for Fall Creators update)
-   kd.exe
-   lxssmanager.exe
-   msbuild.exe
-   mshta.exe
-   ntsd.exe
-   powershell.exe
-   powershell_ise.exe
-   rcsi.exe
-   reg.exe
-   regedit.exe  
-   regedt32.exe
-   regini.exe
-   syskey.exe
-   wbemtest.exe
-   windbg.exe
-   wmic.exe
-   wscript.exe
-   wsl.exe

> [!NEXT]
> To ensure your Windows app will operate correctly on devices that run Windows 10 S, please review the [test guidance](https://docs.microsoft.com/en-us/windows/uwp/porting/desktop-to-uwp-test-windows-s) for apps. 
