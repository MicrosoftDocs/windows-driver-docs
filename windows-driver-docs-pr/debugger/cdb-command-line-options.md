---
title: CDB Command-Line Options
description: First-time users of CDB or NTSD should begin with the Debugging Using CDB and NTSD section.
ms.assetid: 34dbb695-19e4-4efc-83c7-3a94e5fcf269
keywords: ["CDB Command-Line Options Windows Debugging"]
ms.author: domars
ms.date: 08/01/2018
topic_type:
- apiref
api_name:
- CDB Command-Line Options
api_type:
- NA
ms.localizationpriority: medium
---

# CDB Command-Line Options


First-time users of CDB or NTSD should begin with the [Debugging Using CDB and NTSD](debugging-using-cdb-and-ntsd.md) section.

The CDB command line uses the following syntax:

```dbgcmd
cdb  [ -server ServerTransport | -remote ClientTransport ] 
[ -premote SmartClientTransport ] [-log{a|au|o|ou} LogFile]
[-2] [-d] [-ddefer] [-g] [-G] [-hd] [-lines] [-myob] [-bonc] 
[-n] [-o] [-s] [-v] [-w] [-cf "filename"] [-cfr "filename"] [-c "command"] 
[-robp] [-r BreakErrorLevel]  [-t PrintErrorLevel] 
[ -x{e|d|n|i} Exception ] [-x] [-clines lines] 
[-i ImagePath]  [-y SymbolPath] [-srcpath SourcePath] 
[-aExtension] [-failinc] [-noio] [-noinh] [-noshell] [-nosqm]
[-sdce] [-ses] [-sicv] [-sins] [-snc] [-snul] [-zp PageFile] 
[-sup] [-sflags 0xNumber] [-ee {masm|c++}]
[-e Event] [-pb] [-pd] [-pe] [-pr] [-pt Seconds] [-pv] 
[ -- | -p PID | -pn Name | -psn ServiceName | -z DumpFile | executable ] 
[-cimp] [-isd] [-kqm] [-pvr] [-version] [-vf] [-vf:<opts>] [-netsyms:{yes|no}]

cdb -iae 

cdb -iaec KeyString 

cdb -iu KeyString

cdb -QR Server 

cdb -wake pid 

cdb -?
```

The NTSD command-line syntax is identical to that of CDB:

```dbgcmd
ntsd  [ -server ServerTransport | -remote ClientTransport ] 
[ -premote SmartClientTransport ] [-log{a|au|o|ou} LogFile]
[-2] [-d] [-ddefer] [-g] [-G] [-hd] [-lines] [-myob] [-bonc] 
[-n] [-o] [-s] [-v] [-w] [-cf "filename"] [-cfr "filename"] [-c "command"] 
[-robp] [-r BreakErrorLevel]  [-t PrintErrorLevel] 
[ -x{e|d|n|i} Exception ] [-x] [-clines lines] 
[-i ImagePath]  [-y SymbolPath] [-srcpath SourcePath] 
[-aExtension] [-failinc] [-noio] [-noinh] [-noshell] [-nosqm]
[-sdce] [-ses] [-sicv] [-sins] [-snc] [-snul] [-zp PageFile] 
[-sup] [-sflags 0xNumber] [-ee {masm|c++}] 
[-e Event] [-pb] [-pd] [-pe] [-pr] [-pt Seconds] [-pv] 
[ -- | -p PID | -pn Name | -psn ServiceName | -z DumpFile | executable ] 
[-cimp] [-isd] [-kqm] [-pvr] [-version] [-vf] [-vf:<opts>] [-netsyms:{yes|no}]

ntsd -iae 

ntsd -iaec KeyString 

ntsd -iu KeyString

ntsd -QR Server 

ntsd -wake PID 

ntsd -?
```

The only difference between NTSD and CDB is that NTSD spawns a new console window while CDB inherits the window from which it was invoked. Since the **start** command can also be used to spawn a new console window, the following two constructions will give the same results:

```dbgcmd
start cdb [parameters]
ntsd [parameters]
```

Descriptions of the CDB and NTSD command-line options follow. Only the **-remote**, **-server**, **-g** and **-G** options are case-sensitive. The initial hyphen can be replaced with a forward-slash (/). Options that do not take any additional parameters can be concatenated -- so **cdb -o -d -G -g winmine** can be written as **cdb -odGg winmine**.

If the **-remote** or **-server** option is used, it must appear before any other options on the command line. If an *executable* is specified, it must appear last on the command line; any text after the *executable* name is passed to the executable program as its own command-line parameters.

## <span id="ddk_cdb_command_line_options_dbg"></span><span id="DDK_CDB_COMMAND_LINE_OPTIONS_DBG"></span>Parameters


<span id="_______-server_______ServerTransport______"></span><span id="_______-server_______servertransport______"></span><span id="_______-SERVER_______SERVERTRANSPORT______"></span> **-server** *ServerTransport*   
Creates a debugging server that can be accessed by other debuggers. For an explanation of the possible *ServerTransport* values, see [**Activating a Debugging Server**](activating-a-debugging-server.md). When this parameter is used, it must be the first parameters on the command line.

<span id="_______-remote_______ClientTransport______"></span><span id="_______-remote_______clienttransport______"></span><span id="_______-REMOTE_______CLIENTTRANSPORT______"></span> **-remote** *ClientTransport*   
Creates a debugging client, and connects to a debugging server that is already running. For an explanation of the possible *ClientTransport* values, see [**Activating a Debugging Client**](activating-a-debugging-client.md). When this parameter is used, it must be the first parameters on the command line.

<span id="_______-premote_______SmartClientTransport______"></span><span id="_______-premote_______smartclienttransport______"></span><span id="_______-PREMOTE_______SMARTCLIENTTRANSPORT______"></span> **-premote** *SmartClientTransport*   
Creates a smart client, and connects to a process server that is already running. For an explanation of the possible *SmartClientTransport* values, see [**Activating a Smart Client**](activating-a-smart-client.md).

<span id="_______-2______"></span> **-2**   
If the target application is a *console application*, this option causes it to live in a new console window. (The default is for a target console application to share the window with CDB or NTSD.)

<span id="_______--______"></span> **--**   
Debugs the Client Server Run-Time Subsystem (CSRSS). For details, see [Debugging CSRSS](debugging-csrss.md).

<span id="_______-a_______Extension______"></span><span id="_______-a_______extension______"></span><span id="_______-A_______EXTENSION______"></span> **-a** *Extension*   
Sets the default extension DLL. The default is *userexts*. There must be no space after the "a", and the .dll extension must not be included. For details, and other methods of setting this default, see [Loading Debugger Extension DLLs](loading-debugger-extension-dlls.md).

<span id="_______-bonc______"></span><span id="_______-BONC______"></span> **-bonc**   
If this option is specified, the debugger will break into the target as soon as the session begins. This is especially useful when connecting to a debugging server that might not be currently broken into the target.

<span id="_______-c_________command______________"></span><span id="_______-C_________COMMAND______________"></span> **-c "** *command* **"**   
Specifies the initial debugger command to run at start-up. This command must be surrounded with quotation marks. Multiple commands can be separated with semicolons. (If you have a long command list, it may be easier to put them in a script and then use the **-c** option with the [**$&lt;, $&gt;&lt;, $&gt;&lt;, $$&gt;&lt; (Run Script File)**](-----------------------a---run-script-file-.md) command.)

If you are starting a debugging client, this command must be intended for the debugging server. Client-specific commands such as **.lsrcpath** are not allowed.

<span id="_______-cf_________filename______________"></span><span id="_______-CF_________FILENAME______________"></span> **-cf "** *filename* **"**   
Specifies the path and name of a script file. This script file is executed as soon as the debugger is started. If *filename* contains spaces it must be enclosed in quotation marks. If the path is omitted, the current directory is assumed. If the **-cf** option is not used, the file ntsd.ini in the current directory is used as the script file. If the file does not exist, no error occurs. For details, see [Using Script Files](using-script-files.md).

<span id="_______-cfr_________filename______________"></span><span id="_______-CFR_________FILENAME______________"></span> **-cfr "** *filename* **"**   
Specifies the path and name of a script file. This script file is executed as soon as the debugger is started, and any time the target is restarted. If *filename* contains spaces it must be enclosed in quotation marks. If the path is omitted, the current directory is assumed. If the file does not exist, no error occurs. For details, see [Using Script Files](using-script-files.md).

<span id="_______-cimp______"></span><span id="_______-CIMP______"></span> **-cimp**   
Directs CDB/NTSD to start with a DbgSrv implicit command line instead of an explicit process to run. This option is the client side of dbgsrv -pc.

<span id="_______-clines________lines______"></span><span id="_______-CLINES________LINES______"></span> **-clines** *lines*   
Sets the approximate number of commands in the command history which can be accessed during remote debugging. For details, and for other ways to change this number, see [Using Debugger Commands](using-debugger-commands.md).

<span id="_______-d______"></span><span id="_______-D______"></span> **-d**   
Passes control of this debugger to the kernel debugger. If you are debugging CSRSS, this control redirection always is active, even if **-d** is not specified. (This option cannot be used during remote debugging -- use **-ddefer** instead.) See [Controlling the User-Mode Debugger from the Kernel Debugger](controlling-the-user-mode-debugger-from-the-kernel-debugger.md) for details. This option cannot be used in conjunction with either the **-ddefer** option or the **-noio** option.

**Note**  If you use WinDbg as the kernel debugger, many of the familiar features of WinDbg are not available in this scenario. For example, you cannot use the Locals window, the Disassembly window, or the Call Stack window, and you cannot step through source code. This is because WinDbg is only acting as a viewer for the debugger (NTSD or CDB) running on the target computer.

 

<span id="_______-ddefer______"></span><span id="_______-DDEFER______"></span> **-ddefer**   
Passes control of this debugger to the kernel debugger, unless a debugging client is connected. (This is a variation of **-d** that can be used from a debugging server.) See [Controlling the User-Mode Debugger from the Kernel Debugger](controlling-the-user-mode-debugger-from-the-kernel-debugger.md) for details. This option cannot be used in conjunction with either the **-d** option or the **-noio** option.

<span id="_______-e_______Event______"></span><span id="_______-e_______event______"></span><span id="_______-E_______EVENT______"></span> **-e** *Event*   
Signals the debugger that the specified event has occurred. This option is only used when starting the debugger programmatically.

<span id="_______-ee__masm_c___"></span><span id="_______-EE__MASM_C___"></span> **-ee** {**masm**|**c++**}  
Sets the default expression evaluator. If **masm** is specified, MASM expression syntax will be used. If **c++** is specified, C++ expression syntax will be used. If the **-ee** option is omitted, MASM expression syntax is used as the default. See [Evaluating Expressions](evaluating-expressions.md) for details.

<span id="_______-failinc______"></span><span id="_______-FAILINC______"></span> **-failinc**   
Causes the debugger to ignore any questionable symbols. When debugging a user-mode or kernel-mode minidump file, this option will also prevent the debugger from loading any modules whose images can't be mapped. For details and for other methods of controlling this, see [SYMOPT\_EXACT\_SYMBOLS](symbol-options.md#symopt-exact-symbols).

<span id="_______-g______"></span><span id="_______-G______"></span> **-g**   
Ignores the initial breakpoint in target application. This option will cause the target application to continue running after it is started or CDB attaches to it, unless another breakpoint has been set. See [Initial Breakpoint](initial-breakpoint.md) for details.

<span id="_______-G______"></span><span id="_______-g______"></span> **-G**   
Ignores the final breakpoint at process termination. By default, CDB stops during the image run-down process. This option will cause CDB to exit immediately when the child terminates. This has the same effect as entering the command **sxd epr**. For more information, see [Controlling Exceptions and Events](controlling-exceptions-and-events.md).

<span id="_______-hd______"></span><span id="_______-HD______"></span> **-hd**   
(Microsoft Windows XP and later) Specifies that the debug heap should not be used. See [Debugging a User-Mode Process Using CDB](debugging-a-user-mode-process-using-cdb.md) for details.

<span id="_______-i_______ImagePath______"></span><span id="_______-i_______imagepath______"></span><span id="_______-I_______IMAGEPATH______"></span> **-i** *ImagePath*   
Specifies the location of the executables that generated the fault. If the path contains spaces, it should be enclosed in quotation marks.

<span id="_______-iae______"></span><span id="_______-IAE______"></span> **-iae**   
Installs CDB as the postmortem debugger. For details, see [Enabling Postmortem Debugging](enabling-postmortem-debugging.md).

If this action succeeds, no message is displayed; if it fails, an error message is displayed.

The **-iae** parameter must not be used with any other parameters. This command will not actually start CDB.

<span id="_______-iaec_______KeyString______"></span><span id="_______-iaec_______keystring______"></span><span id="_______-IAEC_______KEYSTRING______"></span> **-iaec** *KeyString*   
Installs CDB as the postmortem debugger. The contents of *KeyString* will be appended to the end of the **AeDebug** registry key. If *KeyString* contains spaces, it must be enclosed in quotation marks. For details, see [Enabling Postmortem Debugging](enabling-postmortem-debugging.md).

If this action succeeds, no message is displayed; if it fails, an error message is displayed.

The **-iaec** parameter must not be used with any other parameters. This command will not actually start CDB.

<span id="_______-isd______"></span><span id="_______-ISD______"></span> **-isd**   
Turns on the CREATE\_IGNORE\_SYSTEM\_DEFAULT flag for any process creations.

<span id="_______-iu________KeyString______"></span><span id="_______-iu________keystring______"></span><span id="_______-IU________KEYSTRING______"></span> **-iu** *KeyString*   
Registers debugger remoting as an URL type so that users can auto-launch a debugger remote client with an URL. *KeyString* has the format `remdbgeng://RemotingOption`. *RemotingOption* is a string that defines the transport protocol as defined in the topic [**Activating a Debugging Client**](activating-a-debugging-client.md). If this action succeeds, no message is displayed; if it fails, an error message is displayed.

The **-iu** parameter must not be used with any other parameters. This command will not actually start CDB.

<span id="_______-kqm______"></span><span id="_______-KQM______"></span> **-kqm**   
Starts CDB/NTSD in quiet mode.

<span id="_______-lines______"></span><span id="_______-LINES______"></span> **-lines**   
Enables source line debugging. If this option is omitted, the [**.lines (Toggle Source Line Support)**](-lines--toggle-source-line-support-.md) command will have to be used before source debugging will be allowed. For other methods of controlling this, see [SYMOPT\_LOAD\_LINES](symbol-options.md#symopt-load-lines).

<span id="_______-log_a_au_o_ou__LogFile"></span><span id="_______-log_a_au_o_ou__logfile"></span><span id="_______-LOG_A_AU_O_OU__LOGFILE"></span> **-log**{**a|au|o|ou**} *LogFile*  
Begins logging information to a log file. If the specified file already exists, it will be overwritten if **-logo** is used, or output will be appended to the file if -loga is used. The **-logau** and **-logou** options operate similar to **-loga** and **-logo** respectively, except that the log file is a Unicode file. For more details, see [Keeping a Log File in CDB](keeping-a-log-file-in-cdb.md).

<span id="_______-myob______"></span><span id="_______-MYOB______"></span> **-myob**   
If there is a version mismatch with dbghelp.dll, the debugger will continue to run. (Without the **-myob** switch, this is considered a fatal error.)

<span id="_______-n______"></span><span id="_______-N______"></span> **-n**   
*Noisy symbol load*: Enables verbose output from the symbol handler. For details and for other methods of controlling this, see [SYMOPT\_DEBUG](symbol-options.md#symopt-debug).

<span id="_______-netsyms__yes_no_______"></span><span id="_______-NETSYMS__YES_NO_______"></span> **-netsyms {yes|no}**   
Allow or disallow loading symbols from a network path.

<span id="_______-noinh______"></span><span id="_______-NOINH______"></span> **-noinh**   
Prevents processes created by the debugger from inheriting handles from the debugger. For other methods of controlling this, see [Debugging a User-Mode Process Using CDB](debugging-a-user-mode-process-using-cdb.md).

<span id="_______-noio______"></span><span id="_______-NOIO______"></span> **-noio**   
Prevents the debugging server from being used for input or output. Input will only be accepted from the debugging client (plus any initial command or command script specified by the **-c** command-line option).

All output will be directed to the debugging client. If NTSD is used for the server, no console window will be created at all. For more details, see [**Activating a Debugging Server**](activating-a-debugging-server.md). This option cannot be used in conjunction with either the **-d** option or the **-ddefer** option.

<span id="_______-noshell______"></span><span id="_______-NOSHELL______"></span> **-noshell**   
Prohibits all **.shell** commands. This prohibition will last as long as the debugger is running, even if a new debugging session is begun. For details, and for other ways to disable **.shell** commands, see [Using Shell Commands](using-shell-commands.md).

<span id="_______-nosqm______"></span><span id="_______-NOSQM______"></span> **-nosqm**   
Disables telemetry data collection and upload.

<span id="_______-o______"></span><span id="_______-O______"></span> **-o**   
Debugs all processes launched by the target application (child processes). By default, processes created by the one you are debugging will run as they normally do. For other methods of controlling this, see [Debugging a User-Mode Process Using CDB](debugging-a-user-mode-process-using-cdb.md).

<span id="_______-p_______PID______"></span><span id="_______-p_______pid______"></span><span id="_______-P_______PID______"></span> **-p** *PID*   
Specifies the decimal process ID to be debugged. This is used to debug a process that is already running. For details, see [Debugging a User-Mode Process Using CDB](debugging-a-user-mode-process-using-cdb.md).

<span id="_______-pb______"></span><span id="_______-PB______"></span> **-pb**   
(Windows XP and later) Prevents the debugger from requesting an initial break-in when attaching to a target process. This can be useful if the application is already suspended, or if you wish to avoid creating a break-in thread in the target.

<span id="_______-pd______"></span><span id="_______-PD______"></span> **-pd**   
(Windows XP and later) Causes the target application not to be terminated at the end of the debugging session. See [Ending a Debugging Session in CDB](ending-a-debugging-session-in-cdb.md) for details.

<span id="_______-pe______"></span><span id="_______-PE______"></span> **-pe**   
(Windows XP and later) Indicates that the target application is already being debugged. See [Re-attaching to the Target Application](reattaching-to-the-target-application.md) for details.

<span id="_______-pn_______Name______"></span><span id="_______-pn_______name______"></span><span id="_______-PN_______NAME______"></span> **-pn** *Name*   
Specifies the name of the process to be debugged. (This name must be unique.) This is used to debug a process that is already running.

<span id="_______-pr______"></span><span id="_______-PR______"></span> **-pr**   
(Windows XP and later) Causes the debugger to start the target process running when it attaches to it. This can be useful if the application is already suspended and you wish it to resume execution.

<span id="_______-psn_______ServiceName______"></span><span id="_______-psn_______servicename______"></span><span id="_______-PSN_______SERVICENAME______"></span> **-psn** *ServiceName*   
Specifies the name of a service contained in the process to be debugged. This is used to debug a process that is already running.

<span id="_______-pt_______Seconds______"></span><span id="_______-pt_______seconds______"></span><span id="_______-PT_______SECONDS______"></span> **-pt** *Seconds*   
Specifies the break time-out, in seconds. The default is 30. See [Controlling the Target](controlling-the-target.md) for details.

<span id="_______-pv______"></span><span id="_______-PV______"></span> **-pv**   
Specifies that the debugger should attach to the target process noninvasively. For details, see [Noninvasive Debugging (User Mode)](noninvasive-debugging--user-mode-.md).

<span id="_______-pvr______"></span><span id="_______-PVR______"></span> **-pvr**   
Works like **-pv** except that the target process is not suspended.

<span id="_______-QR_______Server______"></span><span id="_______-qr_______server______"></span><span id="_______-QR_______SERVER______"></span> **-QR** *Server*   
Lists all debugging servers running on the specified network server. The double backslash (\\\) preceding *Server* is optional. See [**Searching for Debugging Servers**](searching-for-debugging-servers.md) for details.

The **-QR** parameter cannot be used with any other parameters. This command will not actually start CDB.

<span id="_______-r________BreakErrorLevel______"></span><span id="_______-r________breakerrorlevel______"></span><span id="_______-R________BREAKERRORLEVEL______"></span> **-r** *BreakErrorLevel*   
Specifies the error level that will cause the target to break into the debugger. This is a decimal number equal to 0, 1, 2, or 3. Possible values are as follows:

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Constant</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0</p></td>
<td align="left"><p>NONE</p></td>
<td align="left"><p>Do not break on any errors.</p></td>
</tr>
<tr class="even">
<td align="left"><p>1</p></td>
<td align="left"><p>ERROR</p></td>
<td align="left"><p>Break on ERROR level debugging events.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>2</p></td>
<td align="left"><p>MINORERROR</p></td>
<td align="left"><p>Break on MINORERROR and ERROR level debugging events.</p></td>
</tr>
<tr class="even">
<td align="left"><p>3</p></td>
<td align="left"><p>WARNING</p></td>
<td align="left"><p>Break on WARNING, MINORERROR, and ERROR level debugging events.</p></td>
</tr>
</tbody>
</table>

 

This error level only has meaning in checked builds of Microsoft Windows. The default value is 1.

<span id="_______-robp______"></span><span id="_______-ROBP______"></span> **-robp**   
This allows CDB to set a breakpoint on a read-only memory page. (The default is for such an operation to fail.)

<span id="_______-s______"></span><span id="_______-S______"></span> **-s**   
Disables lazy symbol loading. This will slow down process startup. For details and for other methods of controlling this, see [SYMOPT\_DEFERRED\_LOADS](symbol-options.md#symopt-deferred-loads).

<span id="_______-sdce______"></span><span id="_______-SDCE______"></span> **-sdce**   
Causes the debugger to display **File access error** dialog boxes during symbol load. For details and for other methods of controlling this, see [SYMOPT\_FAIL\_CRITICAL\_ERRORS](symbol-options.md#symopt-fail-critical-errors).

<span id="_______-ses______"></span><span id="_______-SES______"></span> **-ses**   
Causes the debugger to perform a strict evaluation of all symbol files and ignore any questionable symbols. For details and for other methods of controlling this, see [SYMOPT\_EXACT\_SYMBOLS](symbol-options.md#symopt-exact-symbols).

<span id="_______-sflags_0x_______Number______"></span><span id="_______-sflags_0x_______number______"></span><span id="_______-SFLAGS_0X_______NUMBER______"></span> **-sflags 0x** *Number*   
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
Specifies the source file search path. Separate multiple paths with a semicolon (;). If the path contains spaces, it should be enclosed in quotation marks. For details, and for other ways to change this path, see [Source Path](source-path.md).

<span id="_______-sup______"></span><span id="_______-SUP______"></span> **-sup**   
Causes the symbol handler to search the public symbol table during every symbol search. For details and for other methods of controlling this, see [SYMOPT\_AUTO\_PUBLICS](symbol-options.md#symopt-auto-publics).

<span id="_______-t________PrintErrorLevel______"></span><span id="_______-t________printerrorlevel______"></span><span id="_______-T________PRINTERRORLEVEL______"></span> **-t** *PrintErrorLevel*   
Specifies the error level that will cause the debugger to display an error message. This is a decimal number equal to 0, 1, 2, or 3. Possible values are as follows:

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Constant</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0</p></td>
<td align="left"><p>NONE</p></td>
<td align="left"><p>Do not display any errors.</p></td>
</tr>
<tr class="even">
<td align="left"><p>1</p></td>
<td align="left"><p>ERROR</p></td>
<td align="left"><p>Display ERROR level debugging events.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>2</p></td>
<td align="left"><p>MINORERROR</p></td>
<td align="left"><p>Display MINORERROR and ERROR level debugging events.</p></td>
</tr>
<tr class="even">
<td align="left"><p>3</p></td>
<td align="left"><p>WARNING</p></td>
<td align="left"><p>Display WARNING, MINORERROR, and ERROR level debugging events.</p></td>
</tr>
</tbody>
</table>

 

This error level only has meaning in checked builds of Microsoft Windows. The default value is 1.

<span id="_______-v______"></span><span id="_______-V______"></span> **-v**   
Enables verbose output from the debugger.

<span id="_______-version______"></span><span id="_______-VERSION______"></span> **-version**   
Prints the debugger version string.

<span id="_______-vf______"></span><span id="_______-VF______"></span> **-vf**   
Enables default ApplicationVerifier settings.

<span id="_______-vf________opts_"></span><span id="_______-VF________OPTS_"></span> **-vf:** *&lt;opts&gt;*  
Enables given ApplicationVerifier settings.

<span id="_______-w______"></span><span id="_______-W______"></span> **-w**   
Specifies to debug 16-bit applications in a separate VDM.

<span id="_______-wake_______PID______"></span><span id="_______-wake_______pid______"></span><span id="_______-WAKE_______PID______"></span> **-wake** *PID*   
Causes sleep mode to end for the user-mode debugger whose process ID is specified by *PID*. This command must be issued on the target machine during sleep mode. See [Controlling the User-Mode Debugger from the Kernel Debugger](controlling-the-user-mode-debugger-from-the-kernel-debugger.md) for details.

The **-wake** parameter should not be used with any other parameters. This command will not actually start CDB.

<span id="_______-x_e_d_n_i__Exception"></span><span id="_______-x_e_d_n_i__exception"></span><span id="_______-X_E_D_N_I__EXCEPTION"></span> **-x**{**e**|**d**|**n**|**i**} *Exception*  
Controls the debugger's behavior when the specified event occurs. The *Exception* can be either an exception number or an event code. You can specify this option multiple times to control different events. See [Controlling Exceptions and Events](controlling-exceptions-and-events.md) for details and for other methods of controlling these settings.

<span id="_______-x______"></span><span id="_______-X______"></span> **-x**   
Disables first-chance break on access violation exceptions. The second occurrence of an access violation will break into the debugger. This is the same as **-xd av**.

<span id="_______-y_______SymbolPath______"></span><span id="_______-y_______symbolpath______"></span><span id="_______-Y_______SYMBOLPATH______"></span> **-y** *SymbolPath*   
Specifies the symbol search path. Separate multiple paths with a semicolon (;). If the path contains spaces, it should be enclosed in quotation marks. For details, and for other ways to change this path, see [Symbol Path](symbol-path.md).

<span id="_______-z_______DumpFile______"></span><span id="_______-z_______dumpfile______"></span><span id="_______-Z_______DUMPFILE______"></span> **-z** *DumpFile*   
Specifies the name of a crash dump file to debug. If the path and file name contain spaces, this must be surrounded by quotation marks. It is possible to open several dump files at once by including multiple **-z** options, each followed by a different *DumpFile* value. For details, see [Analyzing a User-Mode Dump File](analyzing-a-user-mode-dump-file.md).

<span id="_______-zp_______PageFile______"></span><span id="_______-zp_______pagefile______"></span><span id="_______-ZP_______PAGEFILE______"></span> **-zp** *PageFile*   
Specifies the name of a modified page file. This is useful if you are debugging a dump file and want to use the [**.pagein (Page In Memory)**](-pagein--page-in-memory-.md) command. You cannot use **-zp** with a standard Windows page file -- only specially-modified page files can be used.

<span id="_______executable______"></span><span id="_______EXECUTABLE______"></span> *executable*   
Specifies the command line of an executable process. This is used to launch a new process and debug it. This has to be the final item on the command line. All text after the executable name is passed to the executable as its argument string.

<span id="_______-_______"></span> **-?**   
Displays command-line help text.

When you are starting the debugger from **Start | Run** or from a Command Prompt window, specify arguments for the target application after the application's file name. For instance:

```dbgcmd
cdb myexe arg1arg2
```

 

 





