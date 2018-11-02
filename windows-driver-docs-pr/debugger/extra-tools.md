---
title: Tools Included in Debugging Tools for Windows
description: Debugging Tools for Windows includes several tools in addition to the debugging engine and the Debugging Environments. The tools are in the installation directory of Debugging Tools for Windows.
ms.assetid: f5d761b9-866e-4948-978e-e95f8aed8b21
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Tools Included in Debugging Tools for Windows


Debugging Tools for Windows includes several tools in addition to the debugging engine and the [Debugging Environments](debuggers-in-the-debugging-tools-for-windows-package.md). The tools are in the [installation directory](#installation-directories) of Debugging Tools for Windows.

## <span id="additional_tools_and_utilities"></span><span id="ADDITIONAL_TOOLS_AND_UTILITIES"></span>


<span id="ADPlus"></span><span id="adplus"></span><span id="ADPLUS"></span>[ADPlus](adplus.md)  
Automatically create memory dump files and log files with debug output from one or more processes.

<span id="DumpChk"></span><span id="dumpchk"></span><span id="DUMPCHK"></span>[DumpChk](dumpchk.md)  
Validate a memory dump file.

<span id="GFlags"></span><span id="gflags"></span><span id="GFLAGS"></span>[GFlags](gflags.md)  
Control registry keys and other settings.

<span id="Kill"></span><span id="kill"></span><span id="KILL"></span>[Kill](kill-tool.md)  
Terminate a process.

<span id="Logger_and_LogViewer"></span><span id="logger_and_logviewer"></span><span id="LOGGER_AND_LOGVIEWER"></span>[Logger and LogViewer](logger-and-logviewer.md)  
Record and display function calls and other actions of a program.

<span id="PLMDebug"></span><span id="plmdebug"></span><span id="PLMDEBUG"></span>[PLMDebug](plmdebug.md)  
Use the Windows debugger to debug Windows app, which run under Process Lifecycle Management (PLM). With PLMDebug, you can take manual control of suspending, resuming, and terminating a Windows app.

<span id="Remote_Tool"></span><span id="remote_tool"></span><span id="REMOTE_TOOL"></span>[Remote Tool](remote-tool.md)  
Remotely control any console program, including KD, CDB, and NTSD. See [Remote Debugging Through Remote.exe](remote-debugging-through-remote-exe.md).

<span id="TList"></span><span id="tlist"></span><span id="TLIST"></span>[TList](tlist.md)  
List all running processes.

<span id="UMDH"></span><span id="umdh"></span>[UMDH](umdh.md)  
Analyze heap allocations.

<span id="USBView"></span><span id="usbview"></span><span id="USBVIEW"></span>[USBView](usbview.md)  
Display USB host controllers and connected devices.

<span id="dbgrpc___dbgrpc.exe_"></span><span id="DBGRPC___DBGRPC.EXE_"></span>DbgRpc (Dbgrpc.exe)  
Display Microsoft Remote Procedure Call (RPC) state information. See [RPC Debugging](rpc-debugging.md) and [Using the DbgRpc Tool](using-the-dbgrpc-tool.md).

<span id="kdbgctrl___kernel_debugging_control__kdbgctrl.exe_"></span><span id="KDBGCTRL___KERNEL_DEBUGGING_CONTROL__KDBGCTRL.EXE_"></span>KDbgCtrl (Kernel Debugging Control, Kdbgctrl.exe)  
Control and configure the kernel debugging connection. See [Using KDbgCtrl](using-kdbgctrl.md).

<span id="SrcSrv"></span><span id="srcsrv"></span><span id="SRCSRV"></span>[SrcSrv](srcsrv.md)  
A source server that can be used to deliver source files while debugging.

<span id="SymSrv"></span><span id="symsrv"></span><span id="SYMSRV"></span>[SymSrv](symsrv.md)  
A symbol server that the debugger can use to connect to a symbol store.

<span id="SymProxy"></span><span id="symproxy"></span><span id="SYMPROXY"></span>[SymProxy](symproxy.md)  
Create a single HTTP symbol server on your network that all your debuggers can point to. This has the benefit of pointing to multiple symbol servers (both internal and external) with a single symbol path, handling all authentication, and increasing performance via symbol caching. Symproxy.dll is in the SymProxy folder in the [installation directory](#installation-directories).

<span id="SymChk"></span><span id="symchk"></span><span id="SYMCHK"></span>[SymChk](symchk.md)  
Compare executable files to symbol files to verify that the correct symbols are available.

<span id="SymStore"></span><span id="symstore"></span><span id="SYMSTORE"></span>[SymStore](symstore.md)  
Create a symbol store. See [Using SymStore](symstore.md).

<span id="AgeStore"></span><span id="agestore"></span><span id="AGESTORE"></span>[AgeStore](agestore.md)  
Removes old entries in the downstream store of a symbol server or a source server.

<span id="DBH"></span><span id="dbh"></span>[DBH](dbh.md)  
Display information about the contents of a symbol file.

<span id="PDBCopy"></span><span id="pdbcopy"></span><span id="PDBCOPY"></span>[PDBCopy](pdbcopy.md)  
Remove private symbol information from a symbol file, and control which public symbols are included in the file.

<span id="DbgSrv__"></span><span id="dbgsrv__"></span><span id="DBGSRV__"></span>DbgSrv   
A process server used for remote debugging. See [Process Servers (User Mode)](process-servers--user-mode-.md).

<span id="KdSrv"></span><span id="kdsrv"></span><span id="KDSRV"></span>KdSrv  
A KD connection server used for remote debugging.See [KD Connection Servers (Kernel Mode)](kd-connection-servers--kernel-mode-.md).

<span id="DbEngPrx"></span><span id="dbengprx"></span><span id="DBENGPRX"></span>DbEngPrx  
A repeater (small proxy server) used for remote debugging. See [Repeaters](repeaters.md).

<span id="breakin___breakin.exe_"></span><span id="BREAKIN___BREAKIN.EXE_"></span>Breakin (Breakin.exe)  
Causes a user-mode break to occur in a process. For help, open a Command Prompt window, navigate to the [installation directory](#installation-directories), and enter **breakin /?**.

<span id="list___file_list_utility___list.exe_"></span><span id="LIST___FILE_LIST_UTILITY___LIST.EXE_"></span>List (File List Utility) (List.exe)  
For help, open a Command Prompt window, navigate to the [installation directory](#installation-directories), and enter **list /?**.

<span id="rtlist___remote_task_list_viewer___rtlist.exe_"></span><span id="RTLIST___REMOTE_TASK_LIST_VIEWER___RTLIST.EXE_"></span>RTList (Remote Task List Viewer) (Rtlist.exe)  
List running processes via a DbgSrv process server. For help, open a Command Prompt window, navigate to the [installation directory](#installation-directories), and enter **rtlist /?**.

## <span id="installation-directories"></span><span id="INSTALLATION-DIRECTORIES"></span>Installation Directory


The default installation directory for 64 bit OS installs for the debugging tools is C:\\Program Files (x86)\\Windows Kits\\10\\Debuggers\\. If you have a 32-bit OS, you can find the Windows Kits folder under C:\\Program Files. To determine if you should use the 32 bit or 64 bit tools, see [Choosing the 32-Bit or 64-Bit Debugging Tools](choosing-a-32-bit-or-64-bit-debugger-package.md).

## <span id="related_topics"></span>Related topics


[Tools Related to Debugging Tools for Windows](tools-related-to-debugging-tools-for-windows.md)

 

 






