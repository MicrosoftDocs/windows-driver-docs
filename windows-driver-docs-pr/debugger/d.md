---
title: D (Windows Debugger Glossary)
description: Glossary page - D
Robots: noindex, nofollow
ms.assetid: e4d53375-c82e-493b-9ccb-444c211fbc79
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# D


<span id="data_breakpoint"></span><span id="DATA_BREAKPOINT"></span>**data breakpoint**  
See processor breakpoint.

<span id="dbgeng_extension"></span><span id="DBGENG_EXTENSION"></span>**DbgEng extension**  
A debugger extension based on the prototypes in the dbgeng.h header file. These extensions use the debugger engine API to communicate with the debugger engine.

<span id="debug_build"></span><span id="DEBUG_BUILD"></span>**debug build**  
See Checked Build.

<span id="debuggee"></span><span id="DEBUGGEE"></span>**debuggee**  
See target.

<span id="debugger"></span><span id="DEBUGGER"></span>**debugger**  
A debugger engine application that uses the full functionality of the debugger engine. For example, WinDbg, CDB, NTSD, and KD are debuggers.

<span id="debugger_console"></span><span id="DEBUGGER_CONSOLE"></span>**debugger console**  
A fictional entity representing the source of the debugger engine input and the destination of its output. In reality, the debugger engine only uses input and output callbacks and has no notion of what is being used to implement them.

Typically, input is received from the Debugger Command window and output is sent to the same window. However, the input and output callbacks can provide many other sources of input and destinations for output, for example, remote connections, script files, and log files.

<span id="debugger_engine"></span><span id="DEBUGGER_ENGINE"></span>**debugger engine**  
A library for manipulating debugging targets. Its interface is based on the prototypes in the dbgeng.h file. It is used by debuggers, extensions, and debugger engine applications.

<span id="debugger_engine_api"></span><span id="DEBUGGER_ENGINE_API"></span>**debugger engine API**  
A powerful interface to control the behavior of the debugger engine. It may be used by debuggers, DbgEng extensions, and debugger engine applications. The prototypes for this interface are found in the dbgeng.h header file.

<span id="debugger_engine_application"></span><span id="DEBUGGER_ENGINE_APPLICATION"></span>**debugger engine application**  
A stand-alone application that uses the debugger engine API to control the debugger engine.

<span id="debugger_extension"></span><span id="DEBUGGER_EXTENSION"></span>**debugger extension**  
An external function that can run inside the debugger. Each extension is exported from a module known as an debugger extension DLL. The debugger engine invokes the debugger extension by calling its code within the DLL. Some debugger extensions ship with Debugging Tools for Windows. You can write your own extensions to automate any number of debugger features or to customize the output of the information accessible to the debugger.

Also referred to as an , or simply .

<span id="debugger_extension_dll"></span><span id="DEBUGGER_EXTENSION_DLL"></span>**debugger extension DLL**  
A DLL containing debugger extensions. When the debugger engine loads the DLL these extensions become available for use within the debugger.

<span id="debugger_extension_library"></span><span id="DEBUGGER_EXTENSION_LIBRARY"></span>**debugger extension library**  
See debugger extension DLL.

<span id="debugging_client"></span><span id="DEBUGGING_CLIENT"></span>**debugging client**  
An instance of the debugger engine acting as a proxy, sending debugger commands and I/O to the debugging server.

<span id="debugging_server"></span><span id="DEBUGGING_SERVER"></span>**debugging server**  
An instance of the debugger engine acting as a host, listening for connections from debugging clients.

<span id="debugging_session"></span><span id="DEBUGGING_SESSION"></span>**debugging session**  
The debugging session is the actual act of running a software debugging program, such as WinDbg, KD, or CDB, to debug a software component, system service, application, or operating system. The debugging session can also be run against a memory dump file for analysis.

A debugging session starts when a acquires a and lasts until all targets have been discarded.

<span id="default_exception_filter"></span><span id="DEFAULT_EXCEPTION_FILTER"></span>**default exception filter**  
The event filter which applies to exception events that do not match any other exception filters. The default exception filter is a specific exception filter.

<span id="dormant_mode"></span><span id="DORMANT_MODE"></span>**dormant mode**  
A state in which a debugger program is running, but without a target or active session.

<span id="downstream_store"></span><span id="DOWNSTREAM_STORE"></span>**downstream store**  
A cache of symbols created by a symbol server. Typically this cache is on your local machine, while the symbol store is located remotely. If you have a chain of symbol servers, the downstream store can be located on any computer downstream from the symbol store.

<span id="dump_file"></span><span id="DUMP_FILE"></span>**dump file**  
See crash dump file.

<span id="dump_target"></span><span id="DUMP_TARGET"></span>**dump target**  
A crash dump file that is being debugged.

 

 





