---
title: Using Microsoft C Runtime with User-Mode Drivers and Desktop Apps
description: This topic provides information about distributing the C Runtime Libraries with applications and drivers for Windows 8 and Windows 8.1.
ms.date: 01/08/2021
ms.localizationpriority: medium
---

# Using the Microsoft C Runtime with User-Mode Drivers and Desktop Apps

> [!NOTE]
> This topic applies only to Windows Desktop drivers and not Windows Drivers. See [Getting Started with Windows Drivers](getting-started-with-windows-drivers.md) for information about this distinction.

This topic provides information about distributing the C Runtime Libraries with applications and drivers for Windows 8 and Windows 8.1. It provides guidelines for user-mode driver and desktop application writers to compile their code, and package it for redistribution with the necessary C Runtime libraries.

## <span id="The_C_runtime_libraries__CRT__are_no_longer_shipped_as_a_Windows_shared_component"></span><span id="the_c_runtime_libraries__crt__are_no_longer_shipped_as_a_windows_shared_component"></span><span id="THE_C_RUNTIME_LIBRARIES__CRT__ARE_NO_LONGER_SHIPPED_AS_A_WINDOWS_SHARED_COMPONENT"></span>The C runtime libraries (CRT) are no longer shipped as a Windows shared component


In the past, Microsoft distributed the C runtime libraries (CRT) as a Window shared system component. In previous versions of the WDK, you could link your code with the Windows System version of the CRT when you built your driver or traditional Windows app. With the release of Windows 8, the C Runtime libraries are no longer considered a system component, and you must ship a redistributable version of the CRT with your user-mode driver or desktop application. This topic discusses the reasons for this change, the new components of the C Runtime, and strategies for building your desktop app or driver and redistributing the CRT.

## <span id="Why_did_Microsoft_make_this_change_"></span><span id="why_did_microsoft_make_this_change_"></span><span id="WHY_DID_MICROSOFT_MAKE_THIS_CHANGE_"></span>Why did Microsoft make this change?


There are now two separate versions of the C Runtime. One is an internal Windows component, and the other is for use by application and driver developers and ships with Visual Studio. The primary reasons for this change are for consistency and to support servicing of the CRT for customers.

In the past, applications were sometimes linked to versions of the CRT on computers that did not have the correct versions of the CRT DLL installed. Using a common public version of the CRT will help eliminate this problem.

In addition, servicing the CRT can be complex. The Visual C team plans to ship periodic updates of the CRT included with Visual Studio. By using the recommended redistribution strategies, you can easily pick up these changes for your application. Also, you will not have to worry about a change in the Windows System version of the CRT breaking your application.

The msvcrt.dll is now a system component owned and built by Windows. It is intended for use only by system-level components. The files msvcr110.dll (Visual Studio 2012) or msvcr120.dll (Microsoft Visual Studio 2013) are the new public versions of the CRT and are for use by Desktop application and user-mode driver developers.

Visual Studio installs the latest version of the VCRT into the `System32` directory. If the file is not in this location, you can copy it directly into the build directory of your Visual C++ project.

If your user-mode driver or desktop application uses the VCRT, you must distribute the appropriate dynamic-link libraries. Use the Visual C++ Redistributable Package (`VCRedist_x86.exe`, `VCRedist_x64.exe`, `VCRedist_arm.exe`). Chain the redistributable package in with other binaries, and the redistributable package will receive automatic updates.

## <span id="Redistributing_the_C_Runtime_"></span><span id="redistributing_the_c_runtime_"></span><span id="REDISTRIBUTING_THE_C_RUNTIME_"></span>Redistributing the C Runtime

Do not copy individual CRT components to `System32` instead of using a redistributable package. This may cause the CRT not to be serviced automatically, and potentially to be overwritten.

The following special considerations apply for printer drivers:

The Visual C/C++ Redistributable Package (VCRedist\_\*.exe ) is serviced as an application. If your installation includes the redistributable package, the latest version is installed in System32 upon initial setup, and updates are enabled using the Microsoft Update service, as a complete package. All components of the Visual C/C++ Redistributable Package are updated as a single unit.

If you copied individual CRT components to System32, without using redistributable package, these would not be serviced automatically, and may be overwritten accidentally.

A potential problem exists if a driver copies CRT components to System32 and another program runs the redistributable package, the version installed by the driver will be overwritten. The opposite case is also a potential problem. If a program ran redistributable package and a driver copies an earlier version of CRT components into System32, this might break the application. The INF installation process simply checks the version number of the library to install against the one already in System32, and overwrites it if they are different.

## <span id="Recommended_Strategies"></span><span id="recommended_strategies"></span><span id="RECOMMENDED_STRATEGIES"></span>Recommended Strategies


Use the following strategies when redistributing the C/C++ run time components with your drivers and applications.

For applications installed under Program Files:

-   Use the Visual C++ Redistributable Package (VCRedist\_x86.exe, VCRedist\_x64.exe, VCRedist\_arm.exe), which deploys the CRT under System32. In this case, the redistributable package can be updated automatically.
-   Alternatively, install the DLL(s) to the application local directory (copied directly to the directory where the application is installed), or link statically to the CRT. In this case, the CRT would need to be serviced manually.

For printer drivers:

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

## <span id="Linking_your_code_with_the_C_Runtime_libraries"></span><span id="linking_your_code_with_the_c_runtime_libraries"></span><span id="LINKING_YOUR_CODE_WITH_THE_C_RUNTIME_LIBRARIES"></span>Linking your code with the C Runtime libraries

To determine which DLLs you must redistribute with your application, collect a list of the DLLs that your application depends on. One way to collect the list is to run Dependency Walker (`depends.exe`).

For more information, see [Determining Which DLLs to Redistribute](/previous-versions/visualstudio/visual-studio-2013/8kche8ah(v=vs.120)) and [Choosing a Deployment Method](/previous-versions/visualstudio/visual-studio-2013/ms235316(v=vs.120)).


To determine which DLLs you must redistribute with your application, you should collect a list of the DLLs that your application depends on. One way to collect the list is to run Dependency Walker (depends.exe).

When you have the list of dependencies, compare it to the list of files described in [Redistributable Code for Visual Studio 2013 Preview and Visual Studio 2013 SDK Preview](https://go.microsoft.com/fwlink/p/?linkid=320999). For more information, see [Determining Which DLLs to Redistribute](/previous-versions/visualstudio/visual-studio-2013/8kche8ah(v=vs.120)) and [Choosing a Deployment Method](/previous-versions/visualstudio/visual-studio-2013/ms235316(v=vs.120)).

You cannot redistribute all of the files that are included in Visual Studio; you are only permitted to redistribute the files that are specified in [Redistributable Code for Visual Studio 2013 Preview and Visual Studio 2013 SDK Preview](https://go.microsoft.com/fwlink/p/?linkid=320999). Debug versions of applications and the various Visual C++ dynamic-link libraries are not redistributable.

The following libraries contain the C run-time library functions:

|Term|Description|
|--- |--- |
|Msvcr120.dll|C runtime|
|Msvcp120.dll|C++ runtime|
|Msvcr120d.dll|Debug version of C runtime - no redistribution allowed|
|Msvcp120d.dll|Debug version of C++ runtime - no redistribution allowed|

