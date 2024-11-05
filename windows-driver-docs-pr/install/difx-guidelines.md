---
title: DIFx Guidelines
description: Starting in Windows 10 version 1607, the Driver Install Frameworks (DIFx) tools are deprecated and are no longer included in the WDK.
ms.date: 11/05/2024
---

# DIFx guidelines

Starting in Windows 10 version 1607, the Driver Install Frameworks (DIFx) tools (`Difxapi.dll`, `Difxapp.dll`, `Difxappa.dll`, and `DPInst.exe`) are deprecated and are no longer included in the WDK.

Instead, we recommend providing as a standalone [driver package](./driver-packages.md) that doesn't require an installer. This self-contained package adds its own settings or configuration that it needs to function correctly. A standalone driver package doesn't depend on an installer to modify system state that the driver package might require. Standalone driver packages are required to support distributing the driver package through Windows Update and adding the driver package to an offline image. We recommend publishing a standalone driver package to be delivered through Windows Update to systems that your hardware is plugged into. The first step to publishing the driver package on Windows Update is to submit your driver package to the [Windows Hardware Dev Center](https://partner.microsoft.com/dashboard).

If you choose to use DIFx anyway, you must use an older WDK to get the right tools. The following caveats apply:

- If your driver package specifies only **TargetOSVersion** values of Windows 8.1 or later, you can't use the DIFxApp MSI custom action (`Difxapp.dll` and `Difxappa.dll`) due to DIFxApp's dependency on **[GetVersionEx](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getversionexa)**, an API that changed starting in Windows 8.1. **TargetOSVersion** is specified in the [INF Manufacturer Section](inf-manufacturer-section.md). DIFxApp exposes MSI custom actions such as MsiProcessDrivers, MsiInstallDrivers, and MsiUninstallDrivers. If your driver package specifies **TargetOSVersion** values of Windows 8.1 or later, you can't use these custom actions in your MSI.

- Starting in Windows 8.1, applications that link to `Difxapi.dll` must contain an app manifest targeting the OS version on which the application is intended to run. This requirement is due to DIFxAPI's dependency on **[GetVersionEx](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getversionexa)**, an API that changed starting in Windows 8.1. For more on changes to **GetVersionEx** in Windows 8.1, see [Targeting your application for Windows](/windows/desktop/SysInfo/targeting-your-application-at-windows-8-1).

- If your driver package uses the ***BuildNumber*** part of **TargetOSVersion** (introduced in Windows 10, version 1607 (Build 14310 and later)), you can't use the DIFx tools with that driver package. The DIFx tools don't support BuildNumber targeting.

- Use DIFx version 2.1, which is available in the Windows 7 WDK through the Windows 10 Version 1511 WDK. Although a DIFx version of 2.1 was available in earlier versions of the WDK, it wasn't compatible with Windows 7 and later versions of Windows.

- The older WDKs only contain x86 and amd64 versions of the DIFx binaries. The DIFx binaries aren't available for other architectures.

Although it's no longer being updated, you can find API reference documentation for DIFx at [Difxapi.h](/previous-versions/windows/hardware/difxapi/). If you're using the DriverPackagePreinstall, DriverPackageInstall, and DriverPackageUninstall APIs, consider switching to **[DiInstallDriver](/windows/win32/api/newdev/nf-newdev-diinstalldriverw)** and **[DiUninstallDriver](/windows/win32/api/newdev/nf-newdev-diuninstalldriverw)**.

If you still need a custom installer to install your driver package, use either the [PnPUtil](../devtest/pnputil.md) command line tool or a custom installer that calls [driver installation functions](functions-that-simplify-driver-installation.md).

Similarly, if you need the custom installer to uninstall the driver package, use either [PnPUtil](../devtest/pnputil.md) or a custom installer that calls **[DiUninstallDriver](/windows/win32/api/newdev/nf-newdev-diuninstalldriverw)** or **[SetupUninstallOEMInf](/windows/win32/api/setupapi/nf-setupapi-setupuninstalloeminfw)**.
