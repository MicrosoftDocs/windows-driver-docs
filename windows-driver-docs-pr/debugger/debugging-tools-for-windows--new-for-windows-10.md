---
title: Debugging Tools for Windows New for Windows 10
description: For Windows 10, Debugging Tools for Windows includes these new features.
ms.assetid: DCF1222F-6A67-463E-8C31-B7753CAFFC20
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Debugging Tools for Windows: New for Windows 10


For Windows 10, Debugging Tools for Windows includes these new features.

## <span id="Windows_10__version_1703"></span><span id="windows_10__version_1703"></span><span id="WINDOWS_10__VERSION_1703"></span>Windows 10, version 1703


This section describes new debugging tools in Windows 10, version 1703.

-   Eight new JavaScript topics including [JavaScript Debugger Scripting](javascript-debugger-scripting.md)
-   Updates to the [**dx (Display Debugger Object Model Expression)**](dx--display-visualizer-variables-.md) command, to include new command capabilities.
-   New [**dtx (Display Type - Extended Debugger Object Model Information)**](dtx--display-type---extended-debugger-object-model-information-.md) command.
-   New [**!ioctldecode**](-ioctldecode.md) command.
-   Updated [Debugger Engine Reference](https://msdn.microsoft.com/library/windows/hardware/ff540540) to include additional interfaces and structures.
-   Updates to [Configuring tools.ini](configuring-tools-ini.md) to document additional options for the command line debuggers.
-   Published 75 previously undocumented stop codes in [Bug Check Code Reference](bug-check-code-reference2.md).
-   New [Supported Ethernet NICs for Network Kernel Debugging in Windows 10](supported-ethernet-nics-for-network-kernel-debugging-in-windows-10.md) topic.

## <span id="Windows_10__version_1607"></span><span id="windows_10__version_1607"></span><span id="WINDOWS_10__VERSION_1607"></span>Windows 10, version 1607


This section describes new debugging tools in Windows 10, version 1607.

-   New topic about [Debugging a UWP app using WinDbg](debugging-a-uwp-app-using-windbg.md).
-   Updates to the 30 most-viewed developer bug check topics in [Bug Check Code Reference](bug-check-code-reference2.md).

## <span id="Windows_10"></span><span id="windows_10"></span><span id="WINDOWS_10"></span>Windows 10


-   [**.settings (Set Debug Settings)**](-settings--set-debug-settings-.md) - New command that allows you to set, modify, display, load and save settings in the Debugger.Settings namespace.
-   [**dx (Display NatVis Expression)**](dx--display-visualizer-variables-.md) - Describes the new dx debugger command, which displays object information using the NatVis extension model and LINQ support.
-   New commands that work with the NatVis visualization files in the debugger environment.
    -   [**.nvlist (NatVis List)**](-nvlist--natvis-list-.md)
    -   [**.nvload (NatVis Load)**](-nvload--natvis-load-.md)
    -   [**.nvunload (NatVis Unload)**](-nvunload--natvis-unload-.md)
    -   [**.nvunloadall (NatVis Unload All)**](-nvunloadall--natvis-unload-all-.md)
-   [Bluetooth Extensions (Bthkd.dll)](bluetooh-extensions--bthkd-dll-.md)
-   [Storage Kernel Debugger Extensions](storage-kernel-debugger-extensions.md)
-   New Symproxy information including [SymProxy Automated Installation](symproxy-automated-installation.md). In addition the following topics are updated to cover new SymProxy functionality:
    -   [HTTP Symbol Stores](http-symbol-stores.md)
    -   [SymProxy](symproxy.md)
    -   [Installing SymProxy](installing-symproxy.md)
    -   [Configuring the Registry](configuring-the-registry.md)
    -   [Configuring IIS for SymProxy](configuring-iis-for-symproxy.md)
-   [**CDB Command-Line Options**](cdb-command-line-options.md) - Updated to include new command line options.
-   [**!analyze**](-analyze.md) - Updated to include information about using this extension with UMDF 2.15.
-   [**!wdfkd.wdfcrashdump**](-wdfkd-wdfcrashdump.md)- Updated to include information about using this extension with UMDF 2.15
-   [**!irp**](-irp.md) - Updated. Starting with Windows 10 the IRP major and minor code text is displayed in command output.
-   [Using Debugger Markup Language](debugger-markup-language-commands.md) - Updated to describe new right click behavior available in the Debugger Markup Language (DML).
-   [Crash dump analysis using the Windows debuggers (WinDbg)](crash-dump-files.md) - Performance has increased in taking a memory dump over KDNET.
-   [Debug Universal Drivers - Step by Step Lab (Echo Kernel-Mode)](debug-universal-drivers---step-by-step-lab--echo-kernel-mode-.md)- New step by step lab that shows how to use WinDbg to debug the sample KMDF echo driver.

 

 





