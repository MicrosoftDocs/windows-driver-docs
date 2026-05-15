---
title: Install the WDK using WinGet
description: Instructions to install the Windows Driver Kit (WDK) using Windows Package Manager (WinGet)
keywords:
- Windows Driver Kit
- WDK
- drivers
- winget
- install
- download
ms.date: 05/08/2025
ms.topic: install-set-up-deploy
ai-usage: ai-assisted
---

# Install the WDK using WinGet

You can use the Windows Package Manager (WinGet) to install the Windows Driver Kit (WDK) and all of its dependencies from the command line. This article describes two approaches: using a WinGet configuration file to set up everything at once, or installing each component individually.

> [!NOTE]
> WinGet must be installed before you begin. See [Install WinGet](/windows/package-manager/winget/#install-winget) for setup instructions.

## Install a full driver development environment using a WinGet configuration file

Run the following command in PowerShell to install the WDK and all of its dependencies at once:

```powershell
winget configure -f 'https://raw.githubusercontent.com/microsoft/Windows-driver-samples/main/_wdk_utils/winget/configs/wdk-vscommunity.dsc.yaml'
```

This [configuration file](https://github.com/microsoft/Windows-driver-samples/blob/main/_wdk_utils/winget/configs/wdk-vscommunity.dsc.yaml) sets up the following components:

- Visual Studio Community
- Visual Studio workloads and components required for driver development
- Windows 11, version 26H1 SDK
- Windows 11, version 26H1 WDK

Configuration files work best when setting up a new machine. However, you can also use this on machines that already have some components installed — WinGet detects what's already there and only installs the missing ones.

> [!TIP]
> The provided configuration file installs the Community edition of Visual Studio. If you need a different edition, use the corresponding configuration file: `wdk-vsprofessional.dsc.yaml` for Professional or `wdk-vsenterprise.dsc.yaml` for Enterprise.

## Install each component individually

If you prefer to install components one at a time, follow the steps in this section. For the WDK to work properly, you need the following components:

- Visual Studio
- Visual Studio workloads and components required for driver development
- Windows 11, version 26H1 SDK
- Windows 11, version 26H1 WDK

### Visual Studio

Run the following commands in PowerShell to download a [`.vsconfig` file](https://github.com/microsoft/Windows-driver-samples/blob/main/_wdk_utils/winget/configs/wdk-desktop.vsconfig) and install Visual Studio Community with the required workloads and components for driver development:

```powershell
$cfg = "$PWD\wdk-desktop.vsconfig"
Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/microsoft/Windows-driver-samples/main/_wdk_utils/winget/configs/wdk-desktop.vsconfig' -OutFile $cfg
winget install Microsoft.VisualStudio.Community --override "--passive --config $cfg"
```

> [!NOTE]
> To install a different edition, change the `--id` value to `Microsoft.VisualStudio.Professional` or `Microsoft.VisualStudio.Enterprise`.

### Windows SDK

Run the following command in PowerShell to install the latest Windows SDK:

```powershell
winget install Microsoft.WindowsSDK.10.0.28000
```

### Windows WDK

Run the following command in PowerShell to install the latest WDK:

```powershell
winget install Microsoft.WindowsWDK.10.0.28000
```

## Use Dev Home to install the WDK configuration file

If you have [Dev Home](/windows/dev-home/) installed, you can use it to [configure your machine](/windows/dev-home/setup) instead of the command line. First, download the [configuration file](https://github.com/microsoft/Windows-driver-samples/blob/main/_wdk_utils/winget/configs/wdk-vscommunity.dsc.yaml).

Then, in Dev Home, select **Machine configuration** from the sidebar, then select **Set up development environment** > **Configuration file** on the main screen. After you confirm that you want to use the file to configure your machine, installation proceeds automatically. When it completes, your environment is ready for driver development.

## See also

- [Use the WinGet tool to install and manage applications](/windows/package-manager/winget/#install-winget)
- [WinGet Configuration](/windows/package-manager/configuration/): How to set up a machine using WinGet and a configuration file
- [Use command-line parameters to install, update, and manage Visual Studio](/visualstudio/install/use-command-line-parameters-to-install-visual-studio)
- [Windows 11 hardware requirements](/windows/whats-new/windows-11-requirements)

## Related downloads

- [Download current version of the WDK and Enterprise WDK manually](download-the-wdk.md)
- [Download previous versions of the WDK manually](other-wdk-downloads.md)
- [Download the Windows Assessment and Deployment Kit (Windows ADK)](/windows-hardware/get-started/adk-install)
- [Download the Windows HLK](/windows-hardware/test/hlk/windows-hardware-lab-kit)
- [Download the Windows Debugging Tools (WinDbg)](./debugger/debugger-download-tools.md)
- [Download Windows Symbol Packages](./debugger/debugger-download-symbols.md)
