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
ms.date: 09/27/2023
---

# Install the WDK using WinGet

You can use the Windows Package Manager (WinGet) tool to install or update the Windows Driver Kit on your machine, along with its dependencies such as Visual Studio and the Windows Software Development Kit, from command line.

Refer to the [WinGet install documentation](/windows/package-manager/winget/#install-winget) if you need help making sure that you have WinGet installed and configured correctly.

## Install the latest WDK step by step using WinGet

The latest version of the WDK is 22621, which targets Windows 11, version 22H2. It requires Visual Studio 2022 and Windows 11, version 22H2 SDK (22621).

### Step 1: Install Visual Studio 2022

The WDK requires Visual Studio 2022 with the **Desktop development with C++** workload installed, along with the **VS 2022 C++ build tools** and their corresponding **VS 2022 C++ Spectre-mitigated libs (Latest)** components for each architecture you intend to build drivers for.

You can use WinGet to install Visual Studio 2022 with all the workloads and components required for driver development. To do so, you need a Visual Studio installation configuration file. Create a `wdk.vsconfig` file with the following contents and take note of its location:

```json
{
  "version": "1.0",
  "components": [
    "Microsoft.Component.MSBuild",
    "Microsoft.VisualStudio.Component.CoreEditor",
    "Microsoft.VisualStudio.Component.NuGet.BuildTools",
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
    "Microsoft.VisualStudio.Component.VC.MFC.ARM64"
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
    "Microsoft.VisualStudio.Workload.NativeDesktop",
  ]
}
```

Depending on the edition you would like to install, you will need to provide `winget` with a different set of installer parameters along with the path to the .vsconfig file you have just created to customize your installation.

**Visual Studio Community 2022**:
```
winget install --source winget --exact --id Microsoft.VisualStudio.2022.Community --override "--passive --config <vsconfig-folder>\wdk.vsconfig"
```
**Visual Studio Professional 2022**:
```
winget install --source winget --exact --id Microsoft.VisualStudio.2022.Professional --override "--passive --config <vsconfig-folder>\wdk.vsconfig""
```
**Visual Studio Enterprise 2022**:
```
winget install --source winget --exact --id Microsoft.VisualStudio.2022.Enterprise --override "--passive --config <vsconfig-folder>\wdk.vsconfig"
```

You can check Visual Studio documentation on [How to use WinGet to install or modify Visual Studio](/visualstudio/install/use-command-line-parameters-to-install-visual-studio?view=vs-2022#use-winget-to-install-or-modify-visual-studio) for more details.

### Step 2: Install Windows 11, version 22H2 SDK and WDK

You can install both the Windows SDK and WDK from WinGet by running the following commands:

**Windows SDK**:
```
winget install --source winget --exact --id Microsoft.WindowsSDK.10.0.22621
```
**Windows WDK**:
```
winget install --source winget --exact --id Microsoft.WindowsWDK.10.0.22621
```

### Step 3: Install WDK Visual Studio extension

After installing the WDK from command line, you will need to install the Windows Driver Kit Visual Studio extension separately to be able to build and test drivers. By default, the extension is located under `%ProgramFiles(x86)%\Windows Kits\10\Vsix\VS2022\10.0.22621.0\WDK.vsix`.

Using Command Prompt:
```
for /f "usebackq tokens=*" %i in (`"%ProgramFiles(x86)%\Microsoft Visual Studio\Installer\vswhere.exe" -nologo -latest -products * -property enginePath`) do (
  "%i\VSIXInstaller.exe" "%ProgramFiles(x86)%\Windows Kits\10\Vsix\VS2022\10.0.22621.0\WDK.vsix"
)
```

Using PowerShell:
```powershell
& $(& "${env:ProgramFiles(x86)}\Microsoft Visual Studio\Installer\vswhere.exe" -nologo -latest -products * -property enginePath | Join-Path -ChildPath 'VSIXInstaller.exe') "${env:ProgramFiles(x86)}\Windows Kits\10\Vsix\VS2022\10.0.22621.0\WDK.vsix"
```

## Install other WDK versions using WinGet

You can install multiple kits for different Windows versions from WinGet.

> [!NOTE]
> For versions 22000 (targeting Windows 11, version 21H2) and older, you need to install an older version of Visual Studio. See [Other WDK downloads > Step 1: Install Visual Studio](other-wdk-downloads.md#step-1-install-visual-studio) to find the required Visual Studio version for the WDK version you would like to install.

You can search for other available kit versions using the `winget search` command.

**Windows SDK**:
```
winget search --source winget --id Microsoft.WindowsSDK
```
**Windows WDK**:
```
winget search --source winget --id Microsoft.WindowsWDK
```

Each command will return a table with all the available SDK/WDK versions in WinGet. For example, when looking for all the available WDK versions, a table like this will be shown:
```
Name                                        Id                              Version        Source
--------------------------------------------------------------------------------------------------
Windows Driver Kit - Windows 10.1.22000.1   Microsoft.WindowsWDK.10.0.22000 10.1.22000.1   winget
Windows Driver Kit                          Microsoft.WindowsWDK.10.0.19041 10.1.19041.685 winget
Windows Driver Kit - Windows 10.0.22621.382 Microsoft.WindowsWDK.10.0.22621 10.1.22621.382 winget
```

You can then install your required combination of kits for a specific `<kit-version>` using `winget install`:

**Windows SDK**:
```
winget install --source winget --exact --id Microsoft.WindowsSDK.10.0.<kit-version>
```
**Windows WDK**:
```
winget install --source winget --exact --id Microsoft.WindowsWDK.10.0.<kit-version>
```

> [!NOTE]
> If the Windows Driver Kit version you are looking for is not available in WinGet, you will need to download and install it separately by going to the [Other WDK downloads](./other-wdk-downloads.md) site.

Unless you have the WDK Visual Studio extension from a newer WDK installed already, you will need to install it manually. It's located by default under `%ProgramFiles(x86)%\Windows Kits\10\Vsix\<vs-version>\10.0.<kit-version>.0\WDK.vsix` for kit versions 22621 and newer, or `%ProgramFiles(x86)%\Windows Kits\10\Vsix\<vs-version>\WDK.vsix` for kit versions 22000 and older.

Locate first the folder for the `<vs-version>` that you will be using (`VS2022` for versions 22621 and newer, `VS2019` for versions 18362 thru 22000). If that folder contains multiple versioned folders, locate the folder inside with the latest version number. Take note of this location as `<wdk-vsix-folder>` if you want to install the extension from command line.

Using Command Prompt:
```
for /f "usebackq tokens=*" %i in (`"%ProgramFiles(x86)%\Microsoft Visual Studio\Installer\vswhere.exe" -nologo -latest -products * -property enginePath`) do (
  "%i\VSIXInstaller.exe" "<wdk-vsix-folder>\WDK.vsix"
)
```

Using PowerShell:
```powershell
& $(& "${env:ProgramFiles(x86)}\Microsoft Visual Studio\Installer\vswhere.exe" -nologo -latest -products * -property enginePath | Join-Path -ChildPath 'VSIXInstaller.exe') "<wdk-vsix-folder>\WDK.vsix"
```

## Install a full driver development environment using a WinGet configuration file

By [using a WinGet Configuration file](/windows/package-manager/configuration/#use-a-winget-configuration-file-to-configure-your-machine), you can set up a new machine for driver development with minimal manual intervention.

A [configuration file](https://raw.githubusercontent.com/microsoft/Windows-driver-samples/main/configuration.dsc.yaml) for installing the Windows 11, version 22H2 WDK and its dependencies is provided for your convenience. This configuration will set up the following components:

* Visual Studio 2022 Community.
* Visual Studio required workflows and components for driver development.
* Windows 11, version 22H2 SDK.
* Windows 11, version 22H2 WDK.
* WDK Visual Studio Extension.

Although using a configuration description file works better for provisioning a new machine, you can use it even if you have some of the components installed already and WinGet will attempt to only install the missing components.

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

Make sure that you have WinGet version 1.6 or higher installed on the machine you would like to provision. You can do so by running `winget --version` on your terminal and checking that the output version number is `v1.6.2631` or greater. If not, or if the terminal throws an error telling that the command does not exist, you will need to [install the latest version of WinGet](/windows/package-manager/winget/#install-winget) before proceeding.

### Step 2: Download the WDK Configuration file

The configuration description file can be downloaded from [here](https://raw.githubusercontent.com/microsoft/Windows-driver-samples/main/configuration.dsc.yaml). Save this file as `configuration.dsc.yml` and take note of its location.

> [!TIP]
> The provided configuration file will install the Community edition of Visual Studio 2022. If you need a different edition, you can edit `Microsoft.VisualStudio.2022.Community` and `Microsoft.VisualStudio.Product.Community` product IDs with different IDs for the edition you would like to install (for Professional: `Microsoft.VisualStudio.2022.Professional` and `Microsoft.VisualStudio.Product.Professional`; for Enterprise: `Microsoft.VisualStudio.2022.Enterprise` and `Microsoft.VisualStudio.Product.Enterprise`).

### Step 3A: Run WinGet configure to install WDK Configuration file

On a command line under the directory where the WDK configuration file was saved, run the following command to configure your machine using that file:

```
winget configure -f configuration.dsc.yaml
```

### Step 3B: Use Dev Home to install WDK Configuration file

Alternatively, if you have [Dev Home](/windows/dev-home/) installed, you can use it to [configure your machine](https://learn.microsoft.com/en-us/windows/dev-home/setup). Select "Machine configuration" from the sidebar, then "Set up development environment" > "Configuration file" on the main screen to open the WDK configuration file that you have downloaded. After confirming that you would like to use that file to configure your machine, installation will proceed and, after it completes, you should have an environment ready for driver development.

## See also

* [Use the WinGet tool to install and manage applications](/windows/package-manager/winget/#install-winget)
* [WinGet Configuration](/windows/package-manager/configuration/): How to set up a machine using winget and a configuration file
* [Use command-line parameters to install, update, and manage Visual Studio](/visualstudio/install/use-command-line-parameters-to-install-visual-studio)
* [Windows 11 hardware requirements](/windows/whats-new/windows-11-requirements)

## Related downloads

* [Download current version of the WDK and Enterprise WDK manually](download-the-wdk.md)
* [Download previous versions of the WDK manually](other-wdk-downloads.md)
* [Download the Windows Assessment and Deployment Kit (Windows ADK)](/windows-hardware/get-started/adk-install)
* [Download the Windows HLK](/windows-hardware/test/hlk/windows-hardware-lab-kit)
* [Download the Windows Debugging Tools (WinDbg)](./debugger/debugger-download-tools.md)
* [Download Windows Symbol Packages](./debugger/debugger-download-symbols.md)
