---
title: DIFx Guidelines
description: DIFx Guidelines
ms.assetid: de34f810-0e90-4626-b84d-160ac61541ad
ms.date: 05/24/2018
ms.localizationpriority: medium
---

# DIFx Guidelines

Starting in Windows 10 Version 1607 (Redstone 1), the Driver Install Frameworks (DIFx) tools (`Difxapi.dll`, `Difxapp.dll`, `Difxappa.dll`, and `DPInst.exe`) are deprecated and are no longer included in the WDK.  Instead, we recommend providing your [driver pacakge](https://docs.microsoft.com/windows-hardware/drivers/install/driver-packages) as a standalone driver package that does not require an installer.  A standalone driver package is a driver package that is self contained and itself adds any settings or configuration required for the functioning of the driver package and the devices it installs on instead of an installer seperately modifying additional system state as part of adding the driver package to the system.  Standalone driver packages are required in order to have robust support of all driver package scenarios.  Ideally, you would publish this standalone driver package to be distributed through Windows Update.  To publish your driver to Windows Update, the first step is to submit your driver package to the [Windows Hardware Dev Center](https://partner.microsoft.com/dashboard).

If you choose to use DIFx anyway, you must use an older WDK which contains the tools and you should be aware of a couple caveats and best practices:

* If your driver package specifies only **TargetOSVersion** values of Windows 8.1 or later, you cannot use the DIFxApp MSI custom action due to DIFxApp's dependency on [**GetVersionEx**](https://docs.microsoft.com/windows/desktop/api/sysinfoapi/nf-sysinfoapi-getversionexa), an API that changed starting in Windows 8.1.  **TargetOSVersion** is specified in the [INF Manufacturer Section](inf-manufacturer-section.md). DIFxApp exposes MSI custom actions such as MsiProcessDrivers, MsiInstallDrivers, and MsiUninstallDrivers.  If your driver package specifies **TargetOSVersion** values of Windows 8.1 or later, you cannot use these custom actions in your MSI.
* Starting in Windows 8.1, applications that link to `Difxapi.dll` must contain an app manifest targeting the OS version on which the application is intended to run.  This is due to DIFxAPI's dependency on [**GetVersionEx**](https://docs.microsoft.com/windows/desktop/api/sysinfoapi/nf-sysinfoapi-getversionexa), an API that changed starting in Windows 8.1.  For more on changes to **GetVersionEx** in Windows 8.1, see [Targeting your application for Windows](https://docs.microsoft.com/windows/desktop/SysInfo/targeting-your-application-at-windows-8-1).
* If your driver package uses the ***BuildNumber*** part of **TargetOSVersion** (introduced in Windows 10, version 1607 (Build 14310 and later)), you cannot use the DIFx tools with that driver package.  The DIFx tools do not understand BuildNumber targeting.
* Use DIFx version 2.1, which is available in the Windows 7 WDK through the Windows 10 Version 1511 WDK.  Although a DIFx version of 2.1 was available in earlier versions of the WDK, it was not properly compatible with Windows 7 and later versions of Windows.

Although it's no longer being updated, you can find API reference documentation for DIFx at [Difxapi.h](https://docs.microsoft.com/previous-versions/windows/hardware/difxapi/).

If a custom installer is required to distribute your driver package, then the command line tool [PnPUtil](https://docs.microsoft.com/windows-hardware/drivers/devtest/pnputil) or a custom installer that uses [driver installation functions](setupapi-functions-that-simplify-driver-installation.md) can be used as part of an installation story. If the custom installer is required to also be able to remove the driver package from the system, then the command line tool [PnPUtil](https://docs.microsoft.com/windows-hardware/drivers/devtest/pnputil) or a custom installer that uses [DiUninstallDriver](https://docs.microsoft.com/windows/win32/api/newdev/nf-newdev-diuninstalldriverw) or [SetupUninstallOEMInf](https://docs.microsoft.com/windows/win32/api/setupapi/nf-setupapi-setupuninstalloeminfw) can be used as part of the uninstallation story.
