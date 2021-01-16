---
title: Using Microsoft C Runtime with User-Mode Drivers and Desktop Apps
description: This topic provides information about distributing the C Runtime Libraries with applications and drivers for Windows 8 and Windows 8.1.
ms.date: 01/08/2021
ms.localizationpriority: medium
---

# Using the Microsoft C Runtime with User-Mode Drivers and Desktop Apps

> [!NOTE]
> This topic applies only to Windows Desktop drivers and not Windows Drivers. See [Getting Started with Windows Drivers](getting-started-with-windows-drivers.md) for information about this distinction.

If you are building applications or drivers for Windows 10, you only need to read this section. If you are using a version of Visual Studio earlier than Visual Studio 2015, skip this section and start with [Redistributing the C Runtime (applies to before Visual Studio 2015)](#redistributing-the-c-runtime-applies-to-before-visual-studio-2015).

Starting in Visual Studio 2015, the Universal C Runtime (UCRT) encompasses the C runtime. The other pieces required for a complete program (C/C++ Language Features, C++ Library) are provided by Visual Studio in the VC++ Redistributable. To avoid a runtime redistribution requirement, those pieces are statically linked.

> [!WARNING]
> When building a user-mode driver project in Visual Studio, if you set **PlatformToolset**  to `WindowsUserModeDriver10.0`, the toolset ignores any runtime library specified in the project and instead links statically against the VC++ Runtime and dynamically against the UCRT.  When using this toolset, this hybrid linking behavior cannot be reconfigured.

If you're not using the `WindowsUserModeDriver10.0` toolset, use the following procedure to make modifications (for example include another DLL):

1. Set to link statically in general: **Properties > C/C++ > Code Generation > Runtime Library = Multi-threaded (/MT)**
2. Remove the statically linked UCRT: **Properties > Linker > Input > Ignore Specific Default Libraries += libucrt.lib**
3. Add the dynamically linked UCRT: **Properties > Linker > Input > Additional Dependencies += ucrt.lib**, **Properties > Linker > Input > Ignore Specific Default Libraries += libucrt.lib**

## Redistributing the C Runtime (applies to before Visual Studio 2015)

> [!NOTE]
> All information below this point applies only to pre-2015. Prior to 2015, there were two separate versions of the C Runtime: the Visual C++ Runtime (VCRT, for example `msvcr120.dll`) and the legacy Windows CRT (`msvcrt.dll`).  

Visual Studio installs the latest version of the VCRT into the `System32` directory. If the file is not in this location, you can copy it directly into the build directory of your Visual C++ project.

If your user-mode driver or desktop application uses the VCRT, you must distribute the appropriate dynamic-link libraries. Use the Visual C++ Redistributable Package (`VCRedist_x86.exe`, `VCRedist_x64.exe`, `VCRedist_arm.exe`). Chain the redistributable package in with other binaries, and the redistributable package will receive automatic updates.

If you want to achieve isolation or avoid the dependency on the VC++ Redistributable, you can link statically to the CRT instead. 
While non-driver projects are usually able to copy the specific Visual C/C++ DLLs to the *application local folder* (where the application is installed) to avoid a dependency on the VC++ Redistributable, app-local deployment is not appropriate for a driver.

Do not copy individual CRT components to `System32` instead of using a redistributable package. This may cause the CRT not to be serviced automatically, and potentially to be overwritten.

The following special considerations apply for printer drivers:

-   These drivers should include the required CRT files in the INF, so the CRT files are copied to the driver store as part of the driver payload.
-   V4 print drivers cannot use a co-installer for setup, so the INF must copy relevant binaries of the C/C++ runtime library to the driver store. To do this, reference the appropriate files in the **\[COPY\_FILES\]** section of the driver package.
-   V3 print drivers should not use co-installers for setup, as they are not run during Point and Print connections. These drivers should reference the appropriate files in the **\[COPY\_FILES\]** section of the driver package.

The following is an example of how to include the CRT binaries in the **\[COPY\_FILES\]** section of an INF:

```inf
[COPY_FILES]
;CRT
Msvcr120.dll
; other files

* [SourceDisksFiles]
Msvcr120.dll = 2 
; other files

* [SourceDisksNames.amd64]
1 = %Location%,,,
2 = %Location%,,,"amd64"
```

For UMDF drivers:

-   Statically link your driver against the CRT to include the runtime in the binary. In this case, you do not need to redistribute the CRT.

## Linking your code with the C Runtime libraries (applies to before Visual Studio 2015)

To determine which DLLs you must redistribute with your application, collect a list of the DLLs that your application depends on. One way to collect the list is to run Dependency Walker (`depends.exe`).

For more information, see [Determining Which DLLs to Redistribute](/previous-versions/visualstudio/visual-studio-2013/8kche8ah(v=vs.120)) and [Choosing a Deployment Method](/previous-versions/visualstudio/visual-studio-2013/ms235316(v=vs.120)).

You cannot redistribute all of the files that are included in Visual Studio; you are only permitted to redistribute the files that are specified in [Redistributable Code for Visual Studio 2013 Preview and Visual Studio 2013 SDK Preview](https://go.microsoft.com/fwlink/p/?linkid=320999). Debug versions of applications and the various Visual C++ dynamic-link libraries are not redistributable.

The following libraries contain the C run-time library functions:

|Term|Description|
|--- |--- |
|Msvcr120.dll|C runtime|
|Msvcp120.dll|C++ runtime|
|Msvcr120d.dll|Debug version of C runtime - no redistribution allowed|
|Msvcp120d.dll|Debug version of C++ runtime - no redistribution allowed|

