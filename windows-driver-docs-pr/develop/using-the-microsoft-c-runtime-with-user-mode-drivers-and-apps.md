---
title: Using Microsoft C Runtime with User-Mode Drivers and Desktop Apps
description: This topic provides information about distributing the C Runtime Libraries with applications and drivers for Windows 8 and Windows 8.1.
ms.date: 01/08/2021
ms.topic: how-to
---

# Using the Microsoft C Runtime with User-Mode Drivers and Desktop Apps

If you are building applications or drivers for Windows 10 or Windows 11, you only need to read this section. If you are using a version of Visual Studio earlier than Visual Studio 2015, skip this section and start with [Redistributing the C Runtime (applies to before Visual Studio 2015)](#redistributing-the-c-runtime-applies-to-before-visual-studio-2015).

Starting with Visual Studio 2015, the C++ runtime pieces required for a complete program (C/C++ Language Features, C++ Library) are provided by Visual Studio in the VC++ Runtime. To avoid a runtime redistribution requirement, only *static linking* must be used for drivers created with Visual Studio 2015 or later, MSVC v14.x toolset.

> [!NOTE]
> When building a user-mode driver project in Visual Studio, if you set **PlatformToolset** to `WindowsUserModeDriver10.0`, the toolset ignores any runtime library specified in the project and instead links statically against the VC++ Runtime and dynamically against the UCRT.  When using this toolset, this hybrid linking behavior cannot be reconfigured.

If you're not using the `WindowsUserModeDriver10.0` toolset, use the following procedure to make modifications (for example include another DLL) and ensure the required MSVC C++ runtime pieces are statically linked:

1. Set to link statically in general: **Properties > C/C++ > Code Generation > Runtime Library = Multi-threaded (/MT)**
2. Remove the statically linked UCRT: **Properties > Linker > Input > Ignore Specific Default Libraries += libucrt.lib**
3. Add the dynamically linked UCRT: **Properties > Linker > Input > Additional Dependencies += ucrt.lib**, **Properties > Linker > Input > Ignore Specific Default Libraries += libucrt.lib**


## Redistributing the C Runtime (applies to before Visual Studio 2015)

> [!NOTE]
> All information below this point applies only to Visual Studio 2013 or earlier. Please note, all such versions are no longer supported. More information about the support lifecycle of Visual Studio can be found at the [Visual Studio Product Lifecycle and Servicing page](https://learn.microsoft.com/en-us/visualstudio/releases/2026/servicing-vs#support-for-older-versions)

Prior to VS 2015, there were two separate versions of the C Runtime: the Visual C++ Runtime (MSVC CRT, for example `msvcr120.dll`) and the legacy Windows CRT (`msvcrt.dll`).  

Visual Studio installed the latest version of the MSVC CRT into the `System32` directory. If the file is not in this location, you can copy it directly into the build directory of your Visual C++ project.

If your user-mode driver or desktop application uses the MSV CRT, you must distribute the appropriate dynamic-link libraries. Use the Visual C++ Redistributable Package (`VCRedist_x86.exe`, `VCRedist_x64.exe`, `VCRedist_arm.exe`). Chain the redistributable package in with other binaries, and the redistributable package will receive automatic updates.

If you want to achieve isolation or avoid the dependency on the VC++ Redistributable, you should link statically to the CRT instead. 
While non-driver projects are usually able to copy the specific Visual C/C++ DLLs to the *application local folder* (where the application is installed) to avoid a dependency on the VC++ Redistributable, app-local deployment is not appropriate for a driver.

Do not copy individual CRT components to `System32` instead of using a redistributable package. This may cause the CRT not to be serviced automatically, and potentially to be overwritten.

> [!WARNING]
Printer drivers built with Visual Studio 2013 or earlier may have included the required MSVC CRT files in the INF file sections, so required files are copied to the driver store as part of the driver payload. However, starting with Visual Studio 2015, printer driver must not include any MSVC CRT files as part of their inf files. Instead, they must link statically to the MSVC CRT as outlined in the [Using the Microsoft C Runtime with User-Mode Drivers and Desktop Apps)](#using-the-microsoft-c-runtime-with-user-mode-drivers-and-desktop=apps) section.

