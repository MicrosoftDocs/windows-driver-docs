---
title: Install the WDK using NuGet
description: Instructions to install the Windows Driver Kit (WDK) using the NuGet Package Manager in Visual Studio
keywords:
- Windows Driver Kit
- WDK
- drivers
- NuGet
- install
- download
ms.date: 05/24/2024
---

# Install the WDK using NuGet

This topic describes how to use NuGet to install the Windows Driver Kit on your computer. NuGet is a popular package manager, used for packaging and distributing software. For more information, see [What is NuGet?](/nuget/what-is-nuget/).

## Windows Drivers Kit Overview

Windows Driver Kit (WDK) is a software tool set used to develop, test and deploy Windows drivers. The content included in the WDK can be categorized into five unique types: Headers, Libraries, Samples, Tools and Templates.

The WDK is released in three different distributions, with different installation options.

**Windows Driver Kit (WDK)**: The WDK is available as a traditional msi based package. It requires Visual Studio to be installed and the WDK is installed to `%ProgramFiles(x86)%\Windows Kits\`. See [Download the Windows Driver Kit (WDK)](.\download-the-wdk.md) for information on downloading and installing the WDK.

**Enterprise Windows Drivers Kit (EWDK)**: This is shipped as a standalone ISO, which includes the command line compiler build tools, the SDK and the WDK. The EWDK is a standalone self-contained command-line environment. To get started, just mount the ISO and run LaunchBuildEnv. Visit [Download the Windows Driver Kit (WDK)](.\download-the-wdk.md) for details on how to download and use the EWDK.

**Windows Drivers Kit NuGet Package**: The WDK NuGet package consists of essential libraries, headers, DLL, tools and metadata used for building Windows drivers that can be shared and supported by modern CI/CD pipelines. The official release of the WDK NuGet package is now available on nuget.org. The latest release version is *10.0.26100.1*. For information on the latest release of the WDK, SDK and Visual Studio, see [Kit versioning](./download-the-wdk.md#kit-versioning).

Users can access and consume the NuGet packages directly from nuget.org from within Visual Studio. Using NuGet with the WDK provides a lightweight solution for WDK acquisition for developers who need always up to date tools for building modern hardware drivers. For more information, see [Install and manage packages in Visual Studio using the NuGet Package Manager](/nuget/consume-packages/install-use-packages-visual-studio/).

The WDK NuGet packages are also available on the NuGet website.

x64: <https://www.nuget.org/packages/Microsoft.Windows.WDK.x64/>

ARM64: <https://www.nuget.org/packages/Microsoft.Windows.WDK.ARM64>

## Install the latest WDK using NuGet - Step by Step

### Prerequisites

- X64/ARM64 PC with Windows 11 or newer.

### Step 1: Install Visual Studio 2022

Download and install Visual Studio 2022 Community, Professional, or Enterprise edition.

[Download Visual Studio Tools](https://visualstudio.microsoft.com/downloads/)

During the installation, select and install **Desktop development with C++**.

### Step 2: Prepare Visual Studio

The WDK requires Visual Studio 2022 with the **VS 2022 C++ build tools** and their corresponding **VS 2022 C++ Spectre-mitigated libs (Latest)** components for each architecture you intend to build drivers for.

1. Register and sign in with your credentials to Visual Studio.

1. Select and install the following VS individual components - *MSVC V143 - VS2022 C++ x64/x86 Spectre-mitigated libs (Latest)* and *MSVC V143 - VS2022 C++ ARM64 Spectre-mitigated libs (Latest)*

### Step 3: Install WDK Visual Studio extension

#### Option 1: Visual Studio Marketplace

In Visual Studio, select **Extensions**, **Manage Extensions** and then **Visual Studio Marketplace**. Search for "*Windows Driver Kit*", select and install the Windows Drivers Kit Visual Studio extension.

![screenshot of Visual Studio showing Visual Studio Marketplace extension](images/visual-studio-market-place.png)

#### Option 2: Download and install

Download and install the Windows Drivers Kit Visual Studio Extension using this link:

[Windows Driver Kit - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=DriverDeveloperKits-WDK.WDKVsix)

![screenshot of Windows Driver Kit Visual Studio extension (VSIX) install dialog](images/visual-studio-vsix-install-dialog.png)

## Getting Started - Use the WDK to develop a driver

Follow the following steps to acquire and install WDK NuGet package in Visual Studio.

1. Launch Visual Studio.

2. Create a new driver project, for example a "Kernel Mode Driver (KMDF)" C++ project.

3. Right Click the driver project solution file, and select **Manage NuGet packages**.

4. Click the drop down menu beside the package source and select `nuget.org`.

5. Search for "*WDK*".

6. Select `Microsoft.Windows.WDK.x64` or `Microsoft.Windows.WDK.ARM64` based on the platform architecture that you wish to develop for.

7. Leave other checkboxes set at their defaults.

8. Select **Install**.

![screenshot of Visual Studio NuGet packages being installation dialog](images/visual-studio-nuget-packages-install-dialog-solution.png)

9. The WDK takes dependencies on the SDK NuGet packages, and it will install the required packages.

10. Review and accept the license terms to complete the installation.

![screenshot of Visual Studio showing a list of three NuGet packages with links to license terms](images/visual-studio-nuget-packages-install-license-dialog.png)

11. Build and test your WDK driver solution.

> [!NOTE]
> Use of the dotnet command line doesn't work with WDK, and its use is not recommended.

## See also

[What is NuGet?](/nuget/what-is-nuget/)

[Use command-line parameters to install, update, and manage Visual Studio](/visualstudio/install/use-command-line-parameters-to-install-visual-studio)

[Download Visual Studio Tools](https://visualstudio.microsoft.com/downloads/)

### Related downloads

[Download current version of the WDK and Enterprise WDK manually](download-the-wdk.md)

[Download previous versions of the WDK manually](other-wdk-downloads.md)

[Download the Windows Debugging Tools (WinDbg)](./debugger/debugger-download-tools.md)
