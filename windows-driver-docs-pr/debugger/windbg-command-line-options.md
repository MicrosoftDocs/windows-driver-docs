---
title: WinDbg Command-Line Options
description: First-time users of WinDbg should begin with the Debugging Using WinDbg section.
ms.assetid: bd169c73-0a46-41b5-bd7b-71adf7747069
keywords: ["WinDbg Command-Line Options Windows Debugging"]
ms.author: domars
ms.date: 08/10/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- WinDbg Command-Line Options
api_type:
- NA
ms.localizationpriority: medium
---

# WinDbg Command-Line Options


First-time users of WinDbg should begin with the [Debugging Using WinDbg](debugging-using-windbg.md) section.

The WinDbg command line uses the following syntax:

```dbgsyntax
windbg [ -server ServerTransport | -remote ClientTransport ] [-lsrcpath ]
   [ -premote SmartClientTransport ] [-?] [-ee {masm|c++}] 
   [-clines lines] [-b] [-d] [-aExtension]  
   [-failinc] [-g] [-G] [-hd] [-j] [-n] [-noshell] [-o] [-openPrivateDumpByHandle Handle]
   [-Q | -QY] [-QS | -QSY] [-robp] [-secure] [-ses] [-sdce] 
   [-sicv] [-sins] [-snc] [-snul] [-sup] [-sflags 0xNumber] 
   [-T Title] [-v] [-log{o|a} LogFile] [-noinh] 
   [-i ImagePath] [-y SymbolPath] [-srcpath SourcePath] 
   [-k [ConnectType] | -kl | -kx ExdiOptions] [-c "command"] 
   [-pb] [-pd] [-pe] [-pr] [-pt Seconds] [-pv]
   [-W Workspace] [-WF Filename] [-WX] [-zp PageFile] 
   [ -p PID | -pn Name | -psn ServiceName | -z DumpFile | executable ] 

windbg -I[S] 

windbg -IU KeyString

windbg -IA[S] 
```

Descriptions of the WinDbg command-line options follow. All command-line options are case-sensitive except for **-j**. The initial hyphen can be replaced with a forward-slash (/).

If the **-remote** or **-server** option is used, it must appear before any other options on the command line. If an *executable* is specified, it must appear last on the command line; any text after the *executable* name is passed to the executable program as its own command-line parameters.

## <span id="ddk_windbg_command_line_options_dbg"></span><span id="DDK_WINDBG_COMMAND_LINE_OPTIONS_DBG"></span>Parameters


<span id="_______-server_______ServerTransport______"></span><span id="_______-server_______servertransport______"></span><span id="_______-SERVER_______SERVERTRANSPORT______"></span> **-server** *ServerTransport*   
Creates a debugging server that can be accessed by other debuggers. For an explanation of the possible *ServerTransport* values, see [**Activating a Debugging Server**](activating-a-debugging-server.md). When this parameter is used, it must be the first parameters on the command line.

<span id="_______-remote_______ClientTransport______"></span><span id="_______-remote_______clienttransport______"></span><span id="_______-REMOTE_______CLIENTTRANSPORT______"></span> **-remote** *ClientTransport*   
Creates a debugging client, and connects to a debugging server that is already running. For an explanation of the possible *ClientTransport* values, see [**Activating a Debugging Client**](activating-a-debugging-client.md). When this parameter is used, it must be the first parameters on the command line.

<span id="_______-premote_______SmartClientTransport______"></span><span id="_______-premote_______smartclienttransport______"></span><span id="_______-PREMOTE_______SMARTCLIENTTRANSPORT______"></span> **-premote** *SmartClientTransport*   
Creates a smart client, and connects to a process server that is already running. For an explanation of the possible *SmartClientTransport* values, see [**Activating a Smart Client**](activating-a-smart-client.md).

<span id="_______-a________Extension______"></span><span id="_______-a________extension______"></span><span id="_______-A________EXTENSION______"></span> **-a** *Extension*   
Sets the default extension DLL. The default is kdextx86.dll or kdexts.dll. There must be no space after the "a", and the .dll file name extension must not be included. For details, and other methods of setting this default, see [Loading Debugger Extension DLLs](loading-debugger-extension-dlls.md).

<span id="_______-b______"></span><span id="_______-B______"></span> **-b**   
This option is no longer supported.

<span id="_______-c_________command______________"></span><span id="_______-C_________COMMAND______________"></span> **-c "** *command* **"**   
Specifies the initial debugger command to run at start-up. This command must be enclosed in quotation marks. Multiple commands can be separated with semicolons. (If you have a long command list, it may be easier to put them in a script and then use the **-c** option with the [**$&lt;, $&gt;&lt;, $&gt;&lt;, $$&gt;&lt; (Run Script File)**](-----------------------a---run-script-file-.md) command.)

If you are starting a debugging client, this command must be intended for the debugging server. Client-specific commands, such as **.lsrcpath**, are not allowed.

<span id="_______-clines________lines______"></span><span id="_______-CLINES________LINES______"></span> **-clines** *lines*   
Sets the approximate number of commands in the command history which can be accessed during remote debugging. For details, and for other ways to change this number, see [Using Debugger Commands](using-debugger-commands.md).

<span id="_______-d______"></span><span id="_______-D______"></span> **-d**   
(Kernel mode only) After a reboot, the debugger will break into the target computer as soon as a kernel module is loaded. (This break is earlier than the break from the **-b** option.) See [Crashing and Rebooting the Target Computer](crashing-and-rebooting-the-target-computer.md) for details and for other methods of changing this status.

<span id="_______-ee__masm_c___"></span><span id="_______-EE__MASM_C___"></span> **-ee** {**masm**|**c++**}  
Sets the default expression evaluator. If **masm** is specified, MASM expression syntax will be used. If **c++** is specified, C++ expression syntax will be used. If the **-ee** option is omitted, MASM expression syntax is used as the default. See [Evaluating Expressions](evaluating-expressions.md) for details.

<span id="_______-failinc______"></span><span id="_______-FAILINC______"></span> **-failinc**   
Causes the debugger to ignore any questionable symbols. When debugging a user-mode or kernel-mode minidump file, this option will also prevent the debugger from loading any modules whose images can't be mapped. For details and for other methods of controlling this, see [SYMOPT\_EXACT\_SYMBOLS](symbol-options.md#symopt-exact-symbols).

<span id="_______-g______"></span><span id="_______-G______"></span> **-g**   
(User mode only) Ignores the initial breakpoint in target application. This option will cause the target application to continue running after it is started or WinDbg attaches to it, unless another breakpoint has been set. See [Initial Breakpoint](initial-breakpoint.md) for details.

<span id="_______-G______"></span><span id="_______-g______"></span> **-G**   
(User mode only) Ignores the final breakpoint at process termination. Typically, the debugging session ends during the image run-down process. This option will cause the debugging session to end immediately when the child terminates. This has the same effect as entering the command **sxd epr**. For more information, see [Controlling Exceptions and Events](controlling-exceptions-and-events.md).

<span id="_______-hd______"></span><span id="_______-HD______"></span> **-hd**   
(User mode only) Specifies that the debug heap should not be used.

<span id="_______-I_S_"></span><span id="_______-i_s_"></span> **-I**\[**S**\]  
Installs WinDbg as the postmortem debugger. For details, see [Enabling Postmortem Debugging](enabling-postmortem-debugging.md).

After this action is attempted, a success or failure message is displayed. If **S** is included, this procedure is done silently if it is successful; only failure messages are displayed.

The **-I** parameter must not be used with any other parameters. This command will not actually start WinDbg, although a WinDbg window may appear for a moment.

<span id="_______-IA_S_"></span><span id="_______-ia_s_"></span> **-IA**\[**S**\]  
Associates WinDbg with the file extensions .dmp, .mdmp, and .wew in the registry. After this action is attempted, a success or failure message is displayed. If **S** is included, this procedure is done silently if it is successful; only failure messages are displayed. After this association is made, double-clicking a file with one of these extensions will start WinDbg.

The **-IA** parameter must not be used with any other parameters. This command will not actually start WinDbg, although a WinDbg window may appear for a moment.

<span id="_______-IU________KeyString______"></span><span id="_______-iu________keystring______"></span><span id="_______-IU________KEYSTRING______"></span> **-IU** *KeyString*   
Registers debugger remoting as an URL type so that users can auto-launch a debugger remote client with an URL. *KeyString* has the format `remdbgeng://RemotingOption`. *RemotingOption* is a string that defines the transport protocol as defined in the topic [**Activating a Debugging Client**](activating-a-debugging-client.md). If this action succeeds, no message is displayed; if it fails, an error message is displayed.

The **-IU** parameter must not be used with any other parameters. Although a WinDbg window may appear for a moment, this command will not actually start WinDbg.

<span id="_______-i_______ImagePath______"></span><span id="_______-i_______imagepath______"></span><span id="_______-I_______IMAGEPATH______"></span> **-i** *ImagePath*   
Specifies the location of the executables that generated the fault. If the path contains spaces, it should be enclosed in quotation marks.

<span id="_______-j______"></span><span id="_______-J______"></span> **-j**   
Allow journaling.

<span id="_______-k__ConnectType_"></span><span id="_______-k__connecttype_"></span><span id="_______-K__CONNECTTYPE_"></span> **-k** \[*ConnectType*\]  
(Kernel mode only) Starts a kernel debugging session. For details, see [Live Kernel-Mode Debugging Using WinDbg](performing-kernel-mode-debugging-using-windbg.md). If **-k** is used without any *ConnectType* options following it, it must be the final entry on the command line.

<span id="_______-kl______"></span><span id="_______-KL______"></span> **-kl**   
(Kernel mode only) Starts a kernel debugging session on the same machine as the debugger.

<span id="_______-kx_______ExdiOptions______"></span><span id="_______-kx_______exdioptions______"></span><span id="_______-KX_______EXDIOPTIONS______"></span> **-kx** *ExdiOptions*   
(Kernel mode only) Starts a kernel debugging session using an EXDI driver. EXDI drivers are not described in this documentation. If you have an EXDI interface to your hardware probe or hardware simulator, please contact Microsoft for debugging information.

<span id="_______-log_o_a__LogFile"></span><span id="_______-log_o_a__logfile"></span><span id="_______-LOG_O_A__LOGFILE"></span> **-log**{**o**|**a**} *LogFile*  
Begins logging information to a log file. If the specified log file already exists, it will be overwritten if **-logo** is used. If **loga** is used, the output will be appended to the file. For more details, see [Keeping a Log File in WinDbg](keeping-a-log-file-in-windbg.md).

<span id="_______-lsrcpath______"></span><span id="_______-LSRCPATH______"></span> **-lsrcpath**   
Sets the local source path for a remote client. This option must follow **-remote** on the command line.

<span id="_______-n______"></span><span id="_______-N______"></span> **-n**   
*Noisy symbol load*: Enables verbose output from symbol handler. For details and for other methods of controlling this, see [SYMOPT\_DEBUG](symbol-options.md#symopt-debug).

<span id="_______-noinh______"></span><span id="_______-NOINH______"></span> **-noinh**   
(User mode only) Prevents processes created by the debugger from inheriting handles from the debugger. For other methods of controlling this, see [Debugging a User-Mode Process Using WinDbg](debugging-a-user-mode-process-using-windbg.md).

<span id="_______-noprio______"></span><span id="_______-NOPRIO______"></span> **-noprio**   
Prevents any priority change. This parameter will prevent WinDbg from taking priority for CPU time while active.

<span id="_______-noshell______"></span><span id="_______-NOSHELL______"></span> **-noshell**   
Prohibits all **.shell** commands. This prohibition will last as long as the debugger is running, even if a new debugging session is begun. For details, and for other ways to disable shell commands, see [Using Shell Commands](using-shell-commands.md).

<span id="_______-o______"></span><span id="_______-O______"></span> **-o**   
(User mode only) Debugs all processes launched by the target application (child processes). By default, processes created by the one you are debugging will run as they normally do.

<span id="_______-openPrivateDumpByHandle______"></span><span id="_______-OPENPRIVATEDUMPBYHANDLE______"></span> **-openPrivateDumpByHandle** *Handle*   
Specifies the handle of a crash dump file to debug.

<span id="_______-p_______PID______"></span><span id="_______-p_______pid______"></span><span id="_______-P_______PID______"></span> **-p** *PID*   
Specifies the decimal process ID to be debugged. This is used to debug a process that is already running.

<span id="_______-pb______"></span><span id="_______-PB______"></span> **-pb**   
(User mode only) Prevents the debugger from requesting an initial break-in when attaching to a target process. This can be useful if the application is already suspended, or if you wish to avoid creating a break-in thread in the target.

<span id="_______-pd______"></span><span id="_______-PD______"></span> **-pd**   
(User mode only) Causes the target application not to be terminated at the end of the debugging session. See [Ending a Debugging Session in WinDbg](ending-a-debugging-session-in-windbg.md) for details.

<span id="_______-pe______"></span><span id="_______-PE______"></span> **-pe**   
(User mode only) Indicates that the target application is already being debugged. See [Re-attaching to the Target Application](reattaching-to-the-target-application.md) for details.

<span id="_______-pn_______Name______"></span><span id="_______-pn_______name______"></span><span id="_______-PN_______NAME______"></span> **-pn** *Name*   
Specifies the name of the process to be debugged. (This name must be unique.) This is used to debug a process that is already running.

<span id="_______-pr______"></span><span id="_______-PR______"></span> **-pr**   
(User mode only) Causes the debugger to start the target process running when it attaches to it. This can be useful if the application is already suspended and you wish it to resume execution.

<span id="_______-psn_______ServiceName______"></span><span id="_______-psn_______servicename______"></span><span id="_______-PSN_______SERVICENAME______"></span> **-psn** *ServiceName*   
Specifies the name of a service contained in the process to be debugged. This is used to debug a process that is already running.

<span id="_______-pt_______Seconds______"></span><span id="_______-pt_______seconds______"></span><span id="_______-PT_______SECONDS______"></span> **-pt** *Seconds*   
Specifies the break timeout, in seconds. The default is 30. See [Controlling the Target](controlling-the-target.md) for details.

<span id="_______-pv______"></span><span id="_______-PV______"></span> **-pv**   
(User mode only) Specifies that the debugger should attach to the target process noninvasively. For details, see [Noninvasive Debugging (User Mode)](noninvasive-debugging--user-mode-.md).

<span id="_______-Q______"></span><span id="_______-q______"></span> **-Q**   
Suppresses the "Save Workspace?" dialog box. Workspaces are not automatically saved. See [Using Workspaces](using-workspaces.md) for details.

<span id="_______-QS______"></span><span id="_______-qs______"></span> **-QS**   
Suppresses the "Reload Source?" dialog box. Source files are not automatically reloaded.

<span id="_______-QSY______"></span><span id="_______-qsy______"></span> **-QSY**   
Suppresses the "Reload Source?" dialog box and automatically reloads source files.

<span id="_______-QY______"></span><span id="_______-qy______"></span> **-QY**   
Suppresses the "Save Workspace?" dialog box and automatically saves workspaces. See [Using Workspaces](using-workspaces.md) for details.

<span id="_______-robp______"></span><span id="_______-ROBP______"></span> **-robp**   
This allows CDB to set a breakpoint on a read-only memory page. (The default is for such an operation to fail.)

<span id="_______-sdce______"></span><span id="_______-SDCE______"></span> **-sdce**   
Causes the debugger to display **File access error** messages during symbol load. For details and for other methods of controlling this, see [SYMOPT\_FAIL\_CRITICAL\_ERRORS](symbol-options.md#symopt-fail-critical-errors).

<span id="_______-secure______"></span><span id="_______-SECURE______"></span> **-secure**   
Activates [Secure Mode](secure-mode.md).

<span id="_______-ses______"></span><span id="_______-SES______"></span> **-ses**   
Causes the debugger to perform a strict evaluation of all symbol files and ignore any questionable symbols. For details and for other methods of controlling this, see [SYMOPT\_EXACT\_SYMBOLS](symbol-options.md#symopt-exact-symbols).

<span id="_______-sflags_0x________Number______"></span><span id="_______-sflags_0x________number______"></span><span id="_______-SFLAGS_0X________NUMBER______"></span> **-sflags 0x** *Number*   
Sets all the symbol handler options at once. *Number* should be a hexadecimal number prefixed with **0x** -- a decimal without the **0x** is permitted, but the symbol options are binary flags and therefore hexadecimal is recommended. This option should be used with care, since it will override all the symbol handler defaults. For details, see [Setting Symbol Options](symbol-options.md).

<span id="_______-sicv______"></span><span id="_______-SICV______"></span> **-sicv**   
Causes the symbol handler to ignore the CV record. For details and for other methods of controlling this, see [SYMOPT\_IGNORE\_CVREC](symbol-options.md#symopt-ignore-cvrec).

<span id="_______-sins______"></span><span id="_______-SINS______"></span> **-sins**   
Causes the debugger to ignore the symbol path and executable image path environment variables. For details, see [SYMOPT\_IGNORE\_NT\_SYMPATH](symbol-options.md#symopt-ignore-nt-sympath).

<span id="_______-snc______"></span><span id="_______-SNC______"></span> **-snc**   
Causes the debugger to turn off C++ translation. For details and for other methods of controlling this, see [SYMOPT\_NO\_CPP](symbol-options.md#symopt-no-cpp).

<span id="_______-snul______"></span><span id="_______-SNUL______"></span> **-snul**   
Disables automatic symbol loading for unqualified names. For details and for other methods of controlling this, see [SYMOPT\_NO\_UNQUALIFIED\_LOADS](symbol-options.md#symopt-no-unqualified-loads).

<span id="_______-srcpath_______SourcePath______"></span><span id="_______-srcpath_______sourcepath______"></span><span id="_______-SRCPATH_______SOURCEPATH______"></span> **-srcpath** *SourcePath*   
Specifies the source file search path. Separate multiple paths with a semicolon (**;**). If the path contains spaces, it should be enclosed in quotation marks. For details, and for other ways to change this path, see [Source Path](source-path.md).

<span id="_______-sup______"></span><span id="_______-SUP______"></span> **-sup**   
Causes the symbol handler to search the public symbol table during every symbol search. For details and for other methods of controlling this, see [SYMOPT\_AUTO\_PUBLICS](symbol-options.md#symopt-auto-publics).

<span id="_______-T_______Title______"></span><span id="_______-t_______title______"></span><span id="_______-T_______TITLE______"></span> **-T** *Title*   
Sets WinDbg window title.

<span id="_______-v______"></span><span id="_______-V______"></span> **-v**   
Enables verbose output from debugger.

<span id="_______-W_______Workspace______"></span><span id="_______-w_______workspace______"></span><span id="_______-W_______WORKSPACE______"></span> **-W** *Workspace*   
Loads the given named workspace. If the workspace name contains spaces, enclose it in quotation marks. If no workspace of this name exists, you will be given the option of creating a new workspace with this name or abandoning the load attempt. For details, see [Using Workspaces](using-workspaces.md).

<span id="_______-WF_______Filename______"></span><span id="_______-wf_______filename______"></span><span id="_______-WF_______FILENAME______"></span> **-WF** *Filename*   
Loads the workspace from the given file. *Filename* should include the file and the extension (usually .wew). If the workspace name contains spaces, enclose it in quotation marks. If no workspace file with this name exists, you will be given the option of creating a new workspace file with this name or abandoning the load attempt. For details, see [Using Workspaces](using-workspaces.md).

<span id="_______-WX______"></span><span id="_______-wx______"></span> **-WX**   
Disables automatic workspace loading. For details, see [Using Workspaces](using-workspaces.md).

<span id="_______-y_______SymbolPath______"></span><span id="_______-y_______symbolpath______"></span><span id="_______-Y_______SYMBOLPATH______"></span> **-y** *SymbolPath*   
Specifies the symbol search path. Separate multiple paths with a semicolon (**;**). If the path contains spaces, it should be enclosed in quotation marks. For details, and for other ways to change this path, see [Symbol Path](symbol-path.md).

<span id="_______-z_______DumpFile______"></span><span id="_______-z_______dumpfile______"></span><span id="_______-Z_______DUMPFILE______"></span> **-z** *DumpFile*   
Specifies the name of a crash dump file to debug. If the path and file name contain spaces, this must be surrounded by quotation marks. It is possible to open several dump files at once by including multiple **-z** options, each followed by a different *DumpFile* value. For details, see [Analyzing a User-Mode Dump File](analyzing-a-user-mode-dump-file.md) or [Analyzing a Kernel-Mode Dump File with WinDbg](analyzing-a-kernel-mode-dump-file-with-windbg.md).

<span id="_______-zp_______PageFile______"></span><span id="_______-zp_______pagefile______"></span><span id="_______-ZP_______PAGEFILE______"></span> **-zp** *PageFile*   
Specifies the name of a modified page file. This is useful if you are debugging a dump file and want to use the [**.pagein (Page In Memory)**](-pagein--page-in-memory-.md) command. You cannot use **-zp** with a standard Windows page file -- only specially-modified page files can be used.

<span id="_______executable______"></span><span id="_______EXECUTABLE______"></span> *executable*   
Specifies the command line of an executable process. This is used to launch a new process and debug it. This has to be the final item on the command line. All text after the executable name is passed to the executable as its argument string. For details, see [Debugging a User-Mode Process Using WinDbg](debugging-a-user-mode-process-using-windbg.md).

<span id="_______-_______"></span> **-?**   
Pops up this HTML Help window.

When you are running the debugger from the command line, specify arguments for the target application after application's file name. For instance:

```dbgcmd
windbg myexe arg1 arg2
```

 

 





