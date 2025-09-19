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
ms.date: 10/01/2025
ms.topic: install-set-up-deploy
---

# Install the WDK using WinGet

You can use the Windows Package Manager (WinGet) tool to install or update the Windows Driver Kit on your computer. WinGet can also install the WDK's dependencies, such as Visual Studio and the Windows Software Development Kit. All of this can be done from the command line.

Refer to the [WinGet install documentation](/windows/package-manager/winget/#install-winget) if you need help with making sure that you have WinGet installed and configured correctly.

## Install the latest WDK step by step using WinGet

This step requires Visual Studio 2022 and the latest Windows SDK. For more info, see [Kit versioning](./download-the-wdk.md#kit-versioning).

### Step 1: Install Visual Studio 2022

The WDK requires Visual Studio 2022 with the **Desktop development with C++** workload installed, along with the **VS 2022 C++ build tools** and their corresponding **VS 2022 C++ Spectre-mitigated libs (Latest)** components for each architecture you intend to build drivers for.

You can use WinGet to install Visual Studio 2022 with all the workloads and components required for driver development. To do so, you need a Visual Studio installation configuration file. Create a `wdk.vsconfig` file with the following contents and take note of its location:

```json
{
  "version": "1.0",
  "components": [
    "Microsoft.Component.MSBuild",
    "Microsoft.VisualStudio.Component.CoreEditor",
    "Microsoft.VisualStudio.Component.NuGet",
    "Microsoft.VisualStudio.Component.Roslyn.Compiler",
    "Microsoft.VisualStudio.Component.TextTemplating",
    "Microsoft.VisualStudio.Component.VC.ASAN",
    "Microsoft.VisualStudio.Component.VC.ATL.ARM64.Spectre",
    "Microsoft.VisualStudio.Component.VC.ATL.ARM64",
    "Microsoft.VisualStudio.Component.VC.ATL.Spectre",
    "Microsoft.VisualStudio.Component.VC.ATL",
    "Microsoft.VisualStudio.Component.VC.ATLMFC.Spectre",
    "Microsoft.VisualStudio.Component.VC.ATLMFC",
    "Microsoft.VisualStudio.Component.VC.CoreIde",
    "Microsoft.VisualStudio.Component.VC.MFC.ARM64.Spectre",
    "Microsoft.VisualStudio.Component.VC.MFC.ARM64",
    "Microsoft.VisualStudio.Component.VC.Redist.14.Latest",
    "Microsoft.VisualStudio.Component.VC.Runtimes.ARM64.Spectre",
    "Microsoft.VisualStudio.Component.VC.Runtimes.ARM64EC.Spectre",
    "Microsoft.VisualStudio.Component.VC.Runtimes.x86.x64.Spectre",
    "Microsoft.VisualStudio.Component.VC.Tools.ARM64",
    "Microsoft.VisualStudio.Component.VC.Tools.ARM64EC",
    "Microsoft.VisualStudio.Component.VC.Tools.x86.x64",
    "Microsoft.VisualStudio.Component.Windows10SDK",
    "Microsoft.VisualStudio.ComponentGroup.NativeDesktop.Core",
    "Microsoft.VisualStudio.Workload.CoreEditor",
    "Microsoft.VisualStudio.Workload.NativeDesktop"
  ]
}
```

Depending on the edition you would like to install, you need to provide `winget` with a different set of installer parameters along with the path to the .vsconfig file you created to customize your installation.

> [!CAUTION]
> You must provide an absolute path to your *wdk.vsconfig* file in the following commands. Otherwise, WinGet might fail to install Visual Studio while still reporting success.

**Visual Studio Community 2022**:

```cmd
winget install --source winget --exact --id Microsoft.VisualStudio.2022.Community --override "--passive --config <vsconfig-folder>\wdk.vsconfig"
```

**Visual Studio Professional 2022**:

```cmd
winget install --source winget --exact --id Microsoft.VisualStudio.2022.Professional --override "--passive --config <vsconfig-folder>\wdk.vsconfig""
```

**Visual Studio Enterprise 2022**:

```cmd
winget install --source winget --exact --id Microsoft.VisualStudio.2022.Enterprise --override "--passive --config <vsconfig-folder>\wdk.vsconfig"
```

You can check Visual Studio documentation on [How to use WinGet to install or modify Visual Studio](/visualstudio/install/use-command-line-parameters-to-install-visual-studio#use-winget-to-install-or-modify-visual-studio) for more details.

### Step 2: Install Windows SDK and WDK

You can install both the Windows SDK and WDK from WinGet by running the following commands:

**Windows SDK**:

```cmd
winget install --source winget --exact --id Microsoft.WindowsSDK.10.0.26100 --log $env:USERPROFILE/Desktop/sdk-install.log
```

**Windows WDK**:

```cmd
winget install --source winget --exact --id Microsoft.WindowsWDK.10.0.26100 --log $env:USERPROFILE/Desktop/wdk-install.log
```

If you're using VS 17.11.0 or later, uncheck the install extension checkbox.

### Step 3: Install WDK Visual Studio extension

> [!NOTE]
> This section is only application when using VS earlier than 17.11.0 release. 

After installing the WDK from command line, you'll need to install the Windows Driver Kit Visual Studio extension separately to be able to build and test drivers. By default, the extension is located under `%ProgramFiles(x86)%\Windows Kits\10\Vsix\VS2022\10.0.26100.0\%PROCESSOR_ARCHITECTURE%\WDK.vsix`.

Using Command Prompt:

```cmd
for /f "usebackq tokens=*" %i in (`"%ProgramFiles(x86)%\Microsoft Visual Studio\Installer\vswhere.exe" -nologo -latest -products * -property enginePath`) do (
  "%i\VSIXInstaller.exe" "%ProgramFiles(x86)%\Windows Kits\10\Vsix\VS2022\10.0.26100.0\%PROCESSOR_ARCHITECTURE%\WDK.vsix"
)
```

Using PowerShell:

```powershell
& $(& "${env:ProgramFiles(x86)}\Microsoft Visual Studio\Installer\vswhere.exe" -nologo -latest -products * -property enginePath | Join-Path -ChildPath 'VSIXInstaller.exe') "${env:ProgramFiles(x86)}\Windows Kits\10\Vsix\VS2022\10.0.26100.0\${env:PROCESSOR_ARCHITECTURE}\WDK.vsix"
```

## Install a full driver development environment using a WinGet configuration file

By [using a WinGet Configuration file](/windows/package-manager/configuration/#use-a-winget-configuration-file-to-configure-your-machine), you can set up a new machine for driver development with minimal manual intervention.

A [configuration file](https://raw.githubusercontent.com/microsoft/Windows-driver-samples/main/configuration.dsc.yaml) for installing the Windows 11, version and its dependencies are provided for your convenience. This configuration sets up the following components:

- Visual Studio 2022 Community.
- Visual Studio required workflows and components for driver development.
- Windows 11, version 24H2 SDK.
- Windows 11, version 24H2 WDK.
- WDK Visual Studio Extension.

Configuration files work best when setting up a new machine. However, you can also use this configuration file on machines that already have some components installed. WinGet detects installed components and only installs the missing components.

> [!TIP]
> You can directly download and install the WDK configuration file using PowerShell. After [installing the latest version of WinGet](/windows/package-manager/winget/#install-winget), you can run the following commands:

```powershell
# Open a new PowerShell terminal if needed
powershell

# Download configuration file to install WDK with VS 2022 Community
Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/microsoft/Windows-driver-samples/main/configuration.dsc.yaml' -OutFile configuration.dsc.yaml

# Install VS, SDK, WDK and WDK VS extension using the configuration file
winget configure -f configuration.dsc.yaml
```

### Step 1: Set up WinGet

Make sure that you have WinGet version 1.6 or higher installed on the machine you would like to provision. You can do so by running `winget --version` on your terminal and checking that the output version number is `v1.6.2631` or greater. If not, or if the terminal throws an error telling that the command doesn't exist, you need to [install the latest version of WinGet](/windows/package-manager/winget/#install-winget) before proceeding.

### Step 2: Download the WDK Configuration file

The configuration description file can be downloaded from [here](https://raw.githubusercontent.com/microsoft/Windows-driver-samples/main/configuration.dsc.yaml). Save this file as `configuration.dsc.yml` and take note of its location.

> [!TIP]
> The provided configuration file installs the Community edition of Visual Studio 2022. If you need a different edition, you can edit `Microsoft.VisualStudio.2022.Community` and `Microsoft.VisualStudio.Product.Community` product IDs with different IDs for the edition you would like to install (for Professional: `Microsoft.VisualStudio.2022.Professional` and `Microsoft.VisualStudio.Product.Professional`; for Enterprise: `Microsoft.VisualStudio.2022.Enterprise` and `Microsoft.VisualStudio.Product.Enterprise`).

### Step 3A: Run WinGet configure to install WDK Configuration file

On a command line under the directory where the WDK configuration file was saved, run the following command to configure your machine using that file:

```cmd
winget configure -f configuration.dsc.yaml
```

### Step 3B: Use Dev Home to install WDK Configuration file

Alternatively, if you have [Dev Home](/windows/dev-home/) installed, you can use it to [configure your machine](/windows/dev-home/setup). To open the WDK configuration file that you downloaded, select **Machine configuration** from the sidebar, then **Set up development environment** > **Configuration file** on the main screen. After confirming that you would like to use that file to configure your machine, installation will proceed and, after it completes, you should have an environment ready for driver development.

## See also

- [Use the WinGet tool to install and manage applications](/windows/package-manager/winget/#install-winget)
- [WinGet Configuration](/windows/package-manager/configuration/): How to set up a machine using winget and a configuration file
- [Use command-line parameters to install, update, and manage Visual Studio](/visualstudio/install/use-command-line-parameters-to-install-visual-studio)
- [Windows 11 hardware requirements](/windows/whats-new/windows-11-requirements)

## Related downloads

- [Download current version of the WDK and Enterprise WDK manually](download-the-wdk.md)
- [Download previous versions of the WDK manually](other-wdk-downloads.md)
- [Download the Windows Assessment and Deployment Kit (Windows ADK)](/windows-hardware/get-started/adk-install)
- [Download the Windows HLK](/windows-hardware/test/hlk/windows-hardware-lab-kit)
- [Download the Windows Debugging Tools (WinDbg)](./debugger/debugger-download-tools.md)
- [Download Windows Symbol Packages](./debugger/debugger-download-symbols.md)
