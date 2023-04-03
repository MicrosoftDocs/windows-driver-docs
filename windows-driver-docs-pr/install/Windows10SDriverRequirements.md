---
description: "Windows 10 in S mode Driver Requirements"
title: Windows 10 in S mode Driver Requirements
ms.date: 05/05/2017
---

# Windows 10 in S mode Driver Requirements

This section describes driver installation requirements and blocked components on Windows 10 S.  

## Driver Requirements

To install on Windows 10 in S mode, driver packages must meet the following requirements:

-   Driver packages must be digitally signed with a **Windows, WHQL, ELAM, or Store** certificate from the [Windows Hardware Developer Center Dashboard](https://aka.ms/DevCenterPortal).
-   Companion software must be signed with a [Microsoft Store Certificate](/windows/uwp/publish/the-app-certification-process).
-   Does not include an \*.exe, \*.zip, \*.msi or \*.cab in the driver package that extracts unsigned binaries.
-   Driver installs using only INF directives.
-   Driver does not call [blocked inbox components](#blocked-inbox-components).
-   Drivers does not include any user interface components, apps, or settings.  Instead, use Universal applications from the Microsoft Store, for example:
    *  [Hardware Support Apps](../devapps/hardware-support-app--hsa--steps-for-driver-developers.md)
    *  [UWP device apps](../devapps/meet-uwp-device-apps.md)
-   Driver and firmware servicing uses Windows Update and not an updater app.

Finally, we recommend using a Universal Windows driver where possible.  For more info, see:

-   [Getting Started with Universal Drivers](../develop/getting-started-with-windows-drivers.md)
-   [Validating Universal Drivers](../develop/validating-windows-drivers.md)

## Installation

* If you check the S compliance checkboxes when submitting a driver in the dashboard, the driver is delivered to both Windows 10 in S mode as well as desktop versions of Windows 10 that have the same HW ID. For more info about these dashboard options, see [Publish a driver to Windows Update](../dashboard/publish-a-driver-to-windows-update.md).
* If different driver packages are required for Windows 10 in S mode and desktop versions of Windows 10 that target the same HWID, set a greater **DriverVer** entry in the [INF Version Section](./inf-version-section.md) for the package that targets desktop versions of Windows 10.  For example, you might set a **DriverVer** of `05/24/2019,10.0.1.0` for the package targeting Windows 10 in S mode, and `05/24/2019,10.1.1.0` for the package targeting desktop versions of Windows 10.

## Troubleshooting installation

If you are targeting Windows 10 in S mode for both a base INF and an extension INF, but only the extension INF is installing on desktop versions of Windows 10, then either your installed driver is of greater rank, or your base driver was not published with the correct targeting.  (CHID may be different).    Check and compare your Shipping Label of the BASE driver and Extension driver.

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
-   infdefaultinstall.exe (new addition for Windows 10, version 1709)
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

> [!NOTE]
> To ensure your Windows app will operate correctly on devices that run Windows 10 in S mode, please review the [test guidance](/windows/uwp/porting/desktop-to-uwp-test-windows-s) for apps.
