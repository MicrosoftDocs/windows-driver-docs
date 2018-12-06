---
title: Debugging Device Installations with a User-mode Debugger
description: Debugging Device Installations with a User-mode Debugger
ms.assetid: 34427afb-3303-44ec-a3a7-72f247c5506d
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Debugging Device Installations with a User-mode Debugger


Starting with Windows Vista, when the Plug and Play (PnP) manager detects a new device in the system, the operating system starts the device installation host process (*DrvInst.exe*) to search for and install a driver for the device.

The most efficient way to debug the user-mode device installation host process is with a user-mode debugger, such as WinDbg or Visual Studio. Because the *DrvInst.exe* process would normally complete without any user interaction, Microsoft has added support to Windows Vista and later versions of Windows to allow the developer of a [driver package](driver-packages.md) to attach a debugger before the core stages of device installation are processed.

For more information about user-mode debuggers and other debugging tools, see [Windows Debugging](https://msdn.microsoft.com/library/windows/hardware/ff551063).

The **DebugInstall** registry value specifies the type of device installation debugging support that is enabled on the system. For more information about this registry value, see [Enabling Support for Debugging Device Installations](enabling-support-for-debugging-device-installations.md).

When the **DebugInstall** registry value is set to 2, *DrvInst.exe* will wait for a user-mode debugger to be attached to its process before it continues with the installation. After a debugger has been attached, the process will break into the debugger itself. A debugger should be attached and configured such that it will not initiate its own initial breakpoint in the target system that is being debugged.

For example, a debugger can be attached to *DrvInst.exe* by name:

```cpp
C:\>C:\Debuggers\WinDbg.exe -g -pn DrvInst.exe
```

Or, if a debugger is attached to the target system, the following debug information will be displayed:

```cpp
DRVINST.EXE: Waiting for debugger on Process ID = 3556 ......
```

This allows the debugger to be attached to the *DrvInst.exe* process by using its unique process ID:

```cpp
C:\>C:\Debuggers\WinDbg.exe -g -p 3556
```

After a user-mode debugger is attached to the *DrvInst.exe* process, the process will break into the debugger:

```cpp
Debugger detected!
DRVINST.EXE: Entering debugger during PnP device installation.
Device instance = "X\Y\Z" ...

(d48.5a0): Break instruction exception - code 80000003 (first chance)
eax=7ffde000 ebx=00000000 ecx=00000000 edx=77f745c0 esi=00000000 edi=00000000
eip=77f24584 esp=0105ff74 ebp=0105ffa0 iopl=0         nv up ei pl zr na po nc
cs=001b  ss=0023  ds=0023  es=0023  fs=003b  gs=0000             efl=00000246
ntdll!DbgBreakPoint:
77f24584 cc               int     3

0:000> |
.  0id: d48attachname: E:\Windows\system32\DrvInst.exe
```

Because the core stages of device installation have not been processed, any class installer or co-installer DLLs that are used for the device are not yet loaded.

If the module and function name for a breakpoint are known in advance, that name can be set as an unresolved breakpoint by using the "bu" debugger command. The following code example shows how to set an unresolved breakpoint for the main entry point (CoInstallerProc) of the *MyCoinst.dll* co-installer:

```cpp
0:000> bu mycoinst!CoInstallerProc
0:000> bl
 0 eu             0001 (0001) (mycoinst!CoInstallerProc)
```

When *MyCoinst.dll* co-installer is loaded and the breakpoint is reached:

```cpp
Breakpoint 0 hit
eax=00000001 ebx=00000000 ecx=00000152 edx=00000151 esi=01a57298 edi=00000002
eip=5bcf54f1 esp=0007e204 ebp=0007e580 iopl=0         nv up ei pl nz na pe nc
cs=001b  ss=0023  ds=0023  es=0023  fs=003b  gs=0000             efl=00000202
mycoinst!CoInstallerProc:
5bcf54f1 8bff             mov edi,edi
0:000> bl
 0 e 5bcf54f1     0001 (0001)  0:**** mycoinst!CoInstallerProc
```

A class installer or co-installer DLL should not predict when either, respectively, will be loaded or unloaded from the *DrvInst.exe* process. However, a breakpoint that is set by using "bu" will remain even if the module is unloaded.

Alternatively, the *DrvInst.exe* process might be allowed to execute up to the point where a specific class installer or co-installer DLL is loaded into the process by setting a debugger exception for the load event of that DLL:

```cpp
0:000> sxe ld mycoinst.dll
```

0:000&gt; g

After the module is loaded, breakpoints can be set within the DLL. For example:

```cpp
ModLoad: 5bcf0000 5bd05000   C:\WINDOWS\system32\mycoinst.dll
eax=00000000 ebx=00000000 ecx=011b0000 edx=7c90eb94 esi=00000000 edi=00000000
eip=7c90eb94 esp=0007da54 ebp=0007db48 iopl=0         nv up ei ng nz ac po nc
cs=001b  ss=0023  ds=0023  es=0023  fs=003b  gs=0000             efl=00000296
ntdll!KiFastSystemCallRet:
7c90eb94 c3               ret
0:000> .reload mycoinst.dll
0:000> x mycoinst!*InstallerProc*
5bcf54f1 mycoinst!CoInstallerProc (unsigned int, void *, struct _SP_DEVINFO_DATA *)

0:000> bu mycoinst!CoInstallerProc
0:000> bl
 0 e 3b0649d5     0001 (0001)  0:**** mycoinst!CoInstallerProc
0:000> sxd ld mycoinst.dll
0:000> g
Breakpoint 0 hit
eax=00000001 ebx=00000000 ecx=000001d4 edx=000001d3 esi=000bbac0 edi=00000002
eip=5bcf54f1 esp=0007e204 ebp=0007e580 iopl=0         nv up ei pl nz na pe nc
cs=001b  ss=0023  ds=0023  es=0023  fs=003b  gs=0000             efl=00000202
mycoinst!CoInstallerProc:
5bcf54f1 8bff             mov edi,edi
0:000> 
```

Because the breakpoint was set as an unresolved breakpoint (bu), it will remain set even if the module is unloaded.

The default time period for an installation process to complete is 5 minutes. If the process does not complete within the given time period, the system assumes that the process has hung (stopped responding), and the installation process is terminated.

If a user-mode debugger is attached to the target system during the device installation process, the system will not enforce this timeout period. This allows a [driver package](driver-packages.md) developer to spend the time needed to debug the installation process.

 

 





