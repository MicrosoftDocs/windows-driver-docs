---
title: KD Command-Line Options
description: First-time users of KD should begin with the Debugging Using KD and NTKD section.
ms.assetid: 76c11b45-8469-4f27-840d-06477d8922b8
keywords: ["KD Command-Line Options Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- KD Command-Line Options
api_type:
- NA
ms.localizationpriority: medium
---

# KD Command-Line Options


First-time users of KD should begin with the [Debugging Using KD and NTKD](debugging-using-kd-and-ntkd.md) section.

The KD command line uses the following syntax.

```dbgcmd
kd [ -server ServerTransport | -remote ClientTransport ] 
   [-b | -x] [-d] [-bonc] [-m] [-myob] [-lines] [-n] [-r] [-s] 
   [-v] [-clines lines] [-failinc] [-noio] [-noshell] 
   [-secure] [-sdce] [-ses] [-sicv] [-sins] [-snc] [-snul]
   [-sup] [-sflags 0xNumber] [-log{a|au|o|ou} LogFile] 
   [-aExtension] [-zp PageFile] 
   [-i ImagePath] [-y SymbolPath]  [-srcpath SourcePath] 
   [-k ConnectType | -kl | -kqm | -kx ExdiOptions] [-ee {masm|c++}] 
   [-z DumpFile] [-cf "filename"] [-cfr "filename"] [-c "command"] 
   [-t PrintErrorLevel] [-version] 

kd -iu KeyString

kd -QR Server 

kd -wake PID 

kd -?
```

Descriptions of the KD command-line options follow. Only the **-remote** and **-server** options are case-sensitive. The initial hyphen can be replaced with a forward-slash (/). Options which do not take any additional parameters can be concatenated -- so **kd -r -n -v** can be written as **kd -rnv**.

If the **-remote** or **-server** option is used, it must appear before any other options on the command line.

## <span id="ddk_kd_command_line_options_dbg"></span><span id="DDK_KD_COMMAND_LINE_OPTIONS_DBG"></span>Parameters


<span id="_______-server_______ServerTransport______"></span><span id="_______-server_______servertransport______"></span><span id="_______-SERVER_______SERVERTRANSPORT______"></span> **-server** *ServerTransport*   
Creates a debugging server that can be accessed by other debuggers. For an explanation of the possible *ServerTransport*, see [**Activating a Debugging Server**](activating-a-debugging-server.md). When this parameter is used, it must be the first parameters on the command line.

<span id="_______-remote_______ClientTransport______"></span><span id="_______-remote_______clienttransport______"></span><span id="_______-REMOTE_______CLIENTTRANSPORT______"></span> **-remote** *ClientTransport*   
Creates a debugging client, and connects to a debugging server that is already running. For an explanation of the possible *ClientTransport* values, see [**Activating a Debugging Client**](activating-a-debugging-client.md). When this parameter is used, it must be the first parameters on the command line.

<span id="_______-a________Extension______"></span><span id="_______-a________extension______"></span><span id="_______-A________EXTENSION______"></span> **-a** *Extension*   
Sets the default extension DLL. The default is kdextx86.dll or kdexts.dll. There must be no space after the "a", and the .dll file name extension must not be included. For details, and other methods of setting this default, see [Loading Debugger Extension DLLs](loading-debugger-extension-dlls.md).

<span id="_______-b______"></span><span id="_______-B______"></span> **-b**   
This option no longer supported.

<span id="_______-bonc______"></span><span id="_______-BONC______"></span> **-bonc**   
If this option is specified, the debugger will break into the target as soon as the session begins. This is especially useful when connecting to a debugging server that might not be currently broken into the target.

<span id="_______-c__command_______"></span><span id="_______-C__COMMAND_______"></span> **-c "**<em>command</em>**"**   
Specifies the initial debugger command to run at start-up. This command must be surrounded with quotation marks. Multiple commands can be separated with semicolons. (If you have a long command list, it may be easier to put them in a script and then use the **-c** option with the [**$&lt;, $&gt;&lt;, $&gt;&lt;, $$&gt;&lt; (Run Script File)**](-----------------------a---run-script-file-.md) command.)

If you are starting a debugging client, this command must be intended for the debugging server. Client-specific commands, such as **.lsrcpath**, are not allowed.

<span id="_______-cf__filename_______"></span><span id="_______-CF__FILENAME_______"></span> **-cf "**<em>filename</em>**"**   
Specifies the path and name of a script file. This script file is executed as soon as the debugger is started. If *filename* contains spaces it must be enclosed in quotation marks. If the path is omitted, the current directory is assumed. If the -cf option is not used, the file ntsd.ini in the current directory is used as the script file. If the file does not exist, no error occurs. For details, see [Using Script Files](using-script-files.md).

<span id="_______-cfr__filename_______"></span><span id="_______-CFR__FILENAME_______"></span> **-cfr "**<em>filename</em>**"**   
Specifies the path and name of a script file. This script file is executed as soon as the debugger is started, and any time the target is restarted. If *filename* contains spaces it must be enclosed in quotation marks. If the path is omitted, the current directory is assumed. If the file does not exist, no error occurs. For details, see [Using Script Files](using-script-files.md).

<span id="_______-clines________lines______"></span><span id="_______-CLINES________LINES______"></span> **-clines** *lines*   
Sets the approximate number of commands in the command history which can be accessed during remote debugging. For details, and for other ways to change this number, see [Using Debugger Commands](using-debugger-commands.md).

<span id="_______-d______"></span><span id="_______-D______"></span> **-d**   
After a reboot, the debugger will break into the target computer as soon as a kernel module is loaded. (This break is earlier than the break from the **-b** option.) See [Crashing and Rebooting the Target Computer](crashing-and-rebooting-the-target-computer.md) for details and for other methods of changing this status.

<span id="_______-ee__masm_c___"></span><span id="_______-EE__MASM_C___"></span> **-ee** {**masm**|**c++**}  
Sets the default expression evaluator. If **masm** is specified, MASM expression syntax will be used. If **c++** is specified, C++ expression syntax will be used. If the **-ee** option is omitted, MASM expression syntax is used as the default. See [Evaluating Expressions](evaluating-expressions.md) for details.

<span id="_______-failinc______"></span><span id="_______-FAILINC______"></span> **-failinc**   
Causes the debugger to ignore any questionable symbols. When debugging a user-mode or kernel-mode minidump file, this option will also prevent the debugger from loading any modules whose images can't be mapped. For details and for other methods of controlling this, see [SYMOPT\_EXACT\_SYMBOLS](symbol-options.md#symopt-exact-symbols).

<span id="_______-i_______ImagePath______"></span><span id="_______-i_______imagepath______"></span><span id="_______-I_______IMAGEPATH______"></span> **-i** *ImagePath*   
Specifies the location of the executables that generated the fault. If the path contains spaces, it should be enclosed in quotation marks.

<span id="_______-iu________KeyString______"></span><span id="_______-iu________keystring______"></span><span id="_______-IU________KEYSTRING______"></span> **-iu** *KeyString*   
Registers debugger remoting as an URL type so that users can auto-launch a debugger remote client with an URL. *KeyString* has the format `remdbgeng://RemotingOption`. *RemotingOption* is a string that defines the transport protocol as defined in the topic [**Activating a Debugging Client**](activating-a-debugging-client.md). If this action succeeds, no message is displayed; if it fails, an error message is displayed.

The **-iu** parameter must not be used with any other parameters. This command will not actually start KD.

<span id="_______-k_______ConnectType______"></span><span id="_______-k_______connecttype______"></span><span id="_______-K_______CONNECTTYPE______"></span> **-k** *ConnectType*   
Tells the debugger how to connect to the target. For details, see [Debugging Using KD and NTKD](debugging-using-kd-and-ntkd.md).

<span id="_______-kl______"></span><span id="_______-KL______"></span> **-kl**   
(Windows XP and later) Starts a kernel debugging session on the same machine as the debugger.

<span id="_______-kqm______"></span><span id="_______-KQM______"></span> **-kqm**   
Starts KD in quiet mode.

<span id="_______-kx_______ExdiOptions______"></span><span id="_______-kx_______exdioptions______"></span><span id="_______-KX_______EXDIOPTIONS______"></span> **-kx** *ExdiOptions*   
Starts a kernel debugging session using an EXDI driver. EXDI drivers are not described in this documentation. If you have an EXDI interface to your hardware probe or hardware simulator, please contact Microsoft for debugging information.

<span id="_______-lines______"></span><span id="_______-LINES______"></span> **-lines**   
Enables source line debugging. If this option is omitted, the [**.lines (Toggle Source Line Support)**](-lines--toggle-source-line-support-.md) command will have to be used before source debugging will be allowed. For other methods of controlling this, see [SYMOPT\_LOAD\_LINES](symbol-options.md#symopt-load-lines).

<span id="_______-log_a_au_o_ou__LogFile"></span><span id="_______-log_a_au_o_ou__logfile"></span><span id="_______-LOG_A_AU_O_OU__LOGFILE"></span> **-log**{**a|au|o|ou**} *LogFile*  
Begins logging information to a log file. If *LogFile* already exists, it will be overwritten if **-logo** is used, or output will be appended to the file if **-loga** is used. The **-logau** and **-logou** options operate similar to **-loga** and **-logo** respectively, except that the log file is a Unicode file. For more details, see [Keeping a Log File in KD](keeping-a-log-file-in-kd.md).

<span id="_______-m______"></span><span id="_______-M______"></span> **-m**   
Indicates that the serial port is connected to a modem. Instructs the debugger to watch for the carrier-detect signal.

<span id="_______-myob______"></span><span id="_______-MYOB______"></span> **-myob**   
If there is a version mismatch with dbghelp.dll, the debugger will continue to run. (Without the **-myob** switch, this is considered a fatal error.)

A secondary effect of this option is that the warning that normally appears when breaking into the target computer is suppressed.

<span id="_______-n______"></span><span id="_______-N______"></span> **-n**   
*Noisy symbol load*: Enables verbose output from symbol handler. For details and for other methods of controlling this, see [SYMOPT\_DEBUG](symbol-options.md#symopt-debug).

<span id="_______-noio______"></span><span id="_______-NOIO______"></span> **-noio**   
Prevents the debugging server from being used for input or output. Input will only be accepted from the debugging client (plus any initial command or command script specified by the **-c** command-line option).

All output will be directed to the debugging client. For more details, see [**Activating a Debugging Server**](activating-a-debugging-server.md).

<span id="_______-noshell______"></span><span id="_______-NOSHELL______"></span> **-noshell**   
Prohibits all **.shell** commands. This prohibition will last as long as the debugger is running, even if a new debugging session is begun. For details, and for other ways to disable shell commands, see [Using Shell Commands](using-shell-commands.md).

<span id="_______-QR_______Server______"></span><span id="_______-qr_______server______"></span><span id="_______-QR_______SERVER______"></span> **-QR** *Server*   
Lists all debugging servers running on the specified network server. The double backslash (**\\\\**) preceding *Server* is optional. See [**Searching for Debugging Servers**](searching-for-debugging-servers.md) for details.

The **-QR** parameter must not be used with any other parameters. This command will not actually start KD.

<span id="_______-r______"></span><span id="_______-R______"></span> **-r**   
Displays registers.

<span id="_______-s______"></span><span id="_______-S______"></span> **-s**   
Disables lazy symbol loading. This will slow down process startup. For details and for other methods of controlling this, see [SYMOPT\_DEFERRED\_LOADS](symbol-options.md#symopt-deferred-loads).

<span id="_______-sdce______"></span><span id="_______-SDCE______"></span> **-sdce**   
Causes the debugger to display **File access error** dialog boxes during symbol load. For details and for other methods of controlling this, see [SYMOPT\_FAIL\_CRITICAL\_ERRORS](symbol-options.md#symopt-fail-critical-errors).

<span id="_______-secure______"></span><span id="_______-SECURE______"></span> **-secure**   
Activates [Secure Mode](secure-mode.md).

<span id="_______-ses______"></span><span id="_______-SES______"></span> **-ses**   
Causes the debugger to perform a strict evaluation of all symbol files and ignore any questionable symbols. For details and for other methods of controlling this, see [SYMOPT\_EXACT\_SYMBOLS](symbol-options.md#symopt-exact-symbols).

<span id="_______-sflags_0xNumber"></span><span id="_______-sflags_0xnumber"></span><span id="_______-SFLAGS_0XNUMBER"></span> **-sflags 0x***Number*  
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

<span id="_______-t________PrintErrorLevel______"></span><span id="_______-t________printerrorlevel______"></span><span id="_______-T________PRINTERRORLEVEL______"></span> **-t** *PrintErrorLevel*   
Specifies the error level that will cause the debugger to display an error message. This is a decimal number equal to 0, 1, 2, or 3. The values are described as follows:

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
Generates verbose messages for loads, deferred loads, and unloads.

<span id="_______-version______"></span><span id="_______-VERSION______"></span> **-version**   
Prints the debugger version string.

<span id="_______-wake_______PID______"></span><span id="_______-wake_______pid______"></span><span id="_______-WAKE_______PID______"></span> **-wake** *PID*   
Causes sleep mode to end for the user-mode debugger whose process ID is specified by *PID*. This command must be issued on the target machine during sleep mode. See [Controlling the User-Mode Debugger from the Kernel Debugger](controlling-the-user-mode-debugger-from-the-kernel-debugger.md) for details.

The **-wake** parameter must not be used with any other parameters. This command will not actually start KD.

<span id="_______-x______"></span><span id="_______-X______"></span> **-x**   
Causes the debugger to break in when an exception first occurs, rather than letting the application or module that caused the exception deal with it. (Same as **-b**, except with an initial **eb nt!NtGlobalFlag 9;g** command.)

<span id="_______-y_______SymbolPath______"></span><span id="_______-y_______symbolpath______"></span><span id="_______-Y_______SYMBOLPATH______"></span> **-y** *SymbolPath*   
Specifies the symbol search path. Separate multiple paths with a semicolon (**;**). If the path contains spaces, it should be enclosed in quotation marks. For details, and for other ways to change this path, see [Symbol Path](symbol-path.md).

<span id="_______-z_______DumpFile______"></span><span id="_______-z_______dumpfile______"></span><span id="_______-Z_______DUMPFILE______"></span> **-z** *DumpFile*   
Specifies the name of a crash dump file to debug. If the path and file name contain spaces, this must be surrounded by quotation marks. It is possible to open several dump files at once by including multiple **-z** options, each followed by a different *DumpFile* value. For details, see [Analyzing a Kernel-Mode Dump File with KD](analyzing-a-kernel-mode-dump-file-with-kd.md).

<span id="_______-zp_______PageFile______"></span><span id="_______-zp_______pagefile______"></span><span id="_______-ZP_______PAGEFILE______"></span> **-zp** *PageFile*   
Specifies the name of a modified page file. This is useful if you are debugging a dump file and want to use the [**.pagein (Page In Memory)**](-pagein--page-in-memory-.md) command. You cannot use **-zp** with a standard Windows page file—only specially-modified page files can be used.

<span id="_______-_______"></span> **-?**   
Displays command-line help text.

KD will automatically detect the platform on which the target is running. You do not need to specify the target on the KD command line. The older syntax (using the name *I386KD* or *IA64KD*) is obsolete.

 

 





