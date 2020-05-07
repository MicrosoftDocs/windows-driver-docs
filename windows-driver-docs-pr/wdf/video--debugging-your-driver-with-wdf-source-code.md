---
title: Video Debugging your driver with WDF source code
description: This topic contains a video tutorial that shows how to debug your Windows Driver Frameworks (WDF) driver with full access to the WDF source code.
Search.SourceType: Video
ms.assetid: 735D71FC-0B35-4C79-8C0A-F3C762095C06
ms.date: 05/07/2020
ms.localizationpriority: medium
---

# Video: Debugging your driver with WDF source code


This topic contains a video tutorial that shows how to debug your Windows Driver Frameworks (WDF) driver with full access to the WDF source code.


>[!VIDEO https://www.microsoft.com/videoplayer/embed/2568bc8a-3f0b-4900-b659-aa5b22159f04]

 
Here is the step-by-step procedure followed in the video:
 

You can step freely into the framework code to get a full picture of what's going on internally, all without needing to download WDF source code, or figure out which build and framework version your target system is running. The debugger automatically downloads the correct code from GitHub.

Suppose you are using WinDbg to debug your WDF driver loaded on a Windows 10 machine, and the debugger is broken-in with framework code in the call stack. You can double-click on the WDF frame in the Call Stack view, and WinDbg will automatically download and open the relevant WDF source file at the matching line, fetched directly from our public Git repo. You can then step through the code, set breakpoints, and see exactly what's happening under the hood.


This feature supports target systems running public releases of Windows 10, Technical Preview build 10041 or later. These builds have private source indexed symbol files for KMDF (Wdf01000.sys) and UMDF (Wudfx02000.dll) available on the Microsoft Public Symbol Server. Note that source-level debugging of WDF code is only available in WinDbg, and not in the Visual Studio debugger.

## Quick Start

It is very simple to get started. You need to have a target machine with Windows 10 build 10041 or newer. Start a WinDbg kernel debug session to the target machine, break in, and follow these steps.

1. Set the default symbol path using .symfix. This sets the symbol path to point to the symbol server at https://msdl.microsoft.com/download/symbols.

`kd> .symfix`

2. Set the default source path using .srcfix. This sets the source path to srv*, which tells the debugger to retrieve source files from locations specified in the target modules' symbol files.

```
kd> .srcfix
Source search path is: SRV*
```

3. Reload symbols using .reload, and confirm that the Wdf01000.sys symbols (or Wudfx02000.dll for UMDF) are source-indexed. As shown in the output of !lmi below, the Wdf01000.sys PDB is source indexed. If yours is not, see the WinDbg Setup section below.

```
kd> .reload
...

kd> !lmi wdf01000.sys
Loaded Module Info: [wdf01000.sys] 
...
Load Report: private symbols & lines, source indexed 
C:\...\Wdf01000.pdb\...\Wdf01000.pdb
```

4. Now you're all set! An easy way to step through WDF source code is to set a break point on the framework's IRP dispatch routine, and then step through the rest of the code. Since a Windows system has many inbox KMDF drivers, WDF is always loaded and running, so this breakpoint will be hit right away (without needing to load your own driver).

```
kd> bp Wdf01000!FxDevice::DispatchWithLock
kd> g
Breakpoint 0 hit
Wdf01000!FxDevice::DispatchWithLock:
87131670 8bff mov edi,edi 
```

If this does not work, check out the WinDbg Setup steps below. 

## WinDbg Setup

If the above example did not work as expected, you may need to perform one or more of the instructions below.

### Enable Source Mode Debugging

Make sure [debugging in Source Mode](https://docs.microsoft.com/windows-hardware/drivers/debugger/debugging-in-source-mode) is enabled. Open the Debug menu and confirm that Source Mode is checked.


 
### Clear Stale Symbols Cache

If you previously debugged WDF drivers for the same Windows target, then you may be using the locally cached WDF symbols that were not source indexed. You can check this with the !lmi command:

```
kd> !lmi Wdf01000.sys
Loaded Module Info: [wdf01000.sys]
...
Load Report: private symbols & lines, not source indexed
C:\...\Wdf01000.pdb\...\Wdf01000.pdb
```

According to the Load Report above, Wdf01000.pdb is not source indexed. This means your local WinDbg symbols cache is stale. To fix this, unload the PDB from WinDbg, clear the local cache (your path may differ based on the !lmi output above), and reload the PDB:

```
kd> .reload /u Wdf01000.sys

CMD> del
C:\...\Wdf01000.pdb\...\Wdf01000.pdb

kd> .reload Wdf01000.sys
```

Now run !lmi to check again: the PDB should appear as source indexed and a source code window should pop up.

```
kd> !lmi Wdf01000.sys
Loaded Module Info: [wdf01000.sys]
...
Load Report: private symbols & lines, source indexed
C:\...\Wdf01000.pdb\...\Wdf01000.pdb 
```

You can use WDF source-level debugging not just for live debugging and analyzing crash dumps, but also for learning more about the framework internals by setting breakpoints on core functions like the IRP dispatcher and exploring the subsequent code paths.



