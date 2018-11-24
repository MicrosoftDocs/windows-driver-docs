---
title: Debugging Device Installations with the Kernel Debugger (KD)
description: Debugging Device Installations with the Kernel Debugger (KD)
ms.assetid: 0967d375-2602-44d2-b4ac-8d1e112afc3f
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Debugging Device Installations with the Kernel Debugger (KD)


Starting with Windows Vista, when the Plug and Play (PnP) manager detects a new device in the system, the operating system starts the device installation host process (*DrvInst.exe*) to search for and install a driver for the device.

Because device installation occurs within this user-mode process, it is usually easiest to use a user-mode debugger as described in [Debugging Device Installations with a User-mode Debugger](debugging-device-installations-with-a-user-mode-debugger.md). In some cases, however, it might be helpful to use the kernel debugger (KD) to monitor the user-mode device installation process.

For example, by using KD while debugging the user-mode device installation, you can do the following:

-   Simultaneously debug a kernel-mode issue by using !devnode, !devobj, !drvobj, !irp, and other KD extensions.

-   Monitor other user-mode processes without managing multiple debuggers by using the KD extensions !process or .process /p.

For more information about KD and other debugging tools, see [Windows Debugging](https://msdn.microsoft.com/library/windows/hardware/ff551063).

The **DebugInstall** registry value specifies the type of device installation debugging support enabled on the system. For more information about this registry value, see [Enabling Support for Debugging Device Installations](enabling-support-for-debugging-device-installations.md).

When the **DebugInstall** registry value is set to 1, *DrvInst.exe* will first check that the kernel debugger is both enabled and currently attached before it breaks into the debugger. After this break is made, breakpoints can be set in the user-mode modules of the current process. For example:

```cpp
kd> .reload /user
kd> bp /p @$proc setupapi!SetupDiCallClassInstaller
```

This sets a breakpoint on the routine SETUPAPI!SetupDiCallClassInstaller for the current process only.

For the developer of a [driver package](driver-packages.md), it is usually most desirable to debug the actions of a class installer or co-installer DLL during the installation of a device. However, when *DrvInst.exe* breaks into the debugger, any class installer or co-installer DLLs from the driver package will not have been loaded. Although the user-mode debuggers support the ability to set a debugger exception when a user-mode module is loaded into the process with the "sx e ld" command, the kernel debugger only supports kernel-mode modules with that command.

The following code example shows how a "Debugger Command Program" monitors the loading of a specific class installer or co-installer into the current process. In this example, the debugger command program will set a breakpoint on the main entry point (CoInstallerProc) of the *Mycoinst.dll* co-installer:

```cpp
file: Z:\bpcoinst.txt

r $t1 = 0
!for_each_module .if ($spat("@#ModuleName", "mycoinst*") = 0) {r $t1 = 1}
.if (not @$t1 = 0) {.echo mycoinst is loaded, set bp on mycoinst!CoInstallerProc } .else {.echo mycoinst not loaded}
.if (not @$t1 = 0) {.reload mycoinst.dll}
.if (not @$t1 = 0) {bp[0x20] /p @$proc mycoinst!CoInstallerProc } .else {bc[0x20]}
```

When executed, the debugger command program will check the list of modules loaded into the current process for *Mycoinst.dll*. After this co-installer DLL is loaded, the debugger will set a breakpoint (with a well-known breakpoint ID) on the CoInstallerProc entry point function.

Starting from the debug break initiated by the *DrvInst.exe* host process, you should first set a breakpoint on the return address of the call where *DrvInst.exe* broke into the kernel debugger. This breakpoint will clear all breakpoints set during the device installation and continue execution:

```cpp
DRVINST.EXE: Entering debugger during PnP device installation.
Device instance = "X\Y\Z" ...

Break instruction exception - code 80000003 (first chance)
010117b7 cc               int     3

kd> bp[0x13] /p @$proc @$ra "bc *;g"
```

Next, you should set some breakpoints within the process to allow the commands in the debugger command program to execute at the appropriate time during device installation.

To make sure that the breakpoint for the class installer or co-installer DLL entry point is set before the function is invoked for device installation, the debugger command program should be executed anytime a new DLL is loaded into the current process, that is, after a call to LoadLibraryExW returns:

```cpp
kd> .reload
kd> bp[0x10] /p @$proc kernel32!LoadLibraryExW "gu;$$><Z:\\bpcoinst.txt;g"
```

Rather than executing the program on every LoadLibraryEx call within the process (bp\[0x10\]), the developer can restrict it to execute only when class installer and co-installer DLLs are loaded into the process. Because [**SetupDiCallClassInstaller**](https://msdn.microsoft.com/library/windows/hardware/ff550922) is the routine that invokes class installers and co-installers that are registered for a device, these DLLs will be loaded into the process during that call.

Because no assumptions should be made about when these DLLs will be unloaded from the *DrvInst.exe* host process, you must make sure the breakpoints can handle locating the DLL entry points during any calls that are made to **SetupDiCallClassInstaller** from the *DrvInst.exe* host process.

```cpp
kd> bd[0x10]
kd> bp[0x11] /p @$proc setupapi!SetupDiCallClassInstaller "be[0x10];bp[0x12] /p @$proc @$ra \"bd[0x10];bc[0x12];g\";g"
kd> g
```

The breakpoint to execute the debugger command program (bp\[0x10\]) is initially disabled. It is enabled whenever [**SetupDiCallClassInstaller**](https://msdn.microsoft.com/library/windows/hardware/ff550922) is invoked (bp\[0x11\]), and execution continues. The debugger command program (bp\[0x10\]) is again disabled when **SetupDiCallClassInstaller** returns by setting a breakpoint on the return address of that routine itself (bp\[0x12\]).

Be aware that the breakpoint that disables the debugger command program also clears itself and continues execution until [**SetupDiCallClassInstaller**](https://msdn.microsoft.com/library/windows/hardware/ff550922) is called again or until the installation program completes and all breakpoints are cleared (bp\[0x13\]).

When execution begins after the above breakpoints are set, the process will break on each call to mycoinst!CoInstallerProc. This allows you to debug the execution of the class installer or co-installer DLL during core device installation.

The default time period for an installation process to complete is 5 minutes. If the process does not complete within the given time period, the system assumes that the process has stopped responding, and it is terminated.

The default timeout restriction placed on device installations is still in effect while the process is being debugged through the kernel debugger. Because execution of all programs on the system is stopped while broken into the debugger, the amount of time taken by the installation process is tracked the same as it would be on a system that is not being debugged.

 

 





