---
title: Enabling Postmortem Debugging
description: This topic covers how to enable postmortem debugging
ms.assetid: ae116b60-fed2-4e1d-98a8-9fe83f460c50
keywords: debugging. debug, Windbg, postmortem debugging, just-in-time debugging, JIT debugging, AeDebug registry key
ms.author: domars
ms.date: 09/17/2018
ms.localizationpriority: medium
---

# Enabling Postmortem Debugging


## <span id="ddk_enabling_postmortem_debugging_dbg"></span><span id="DDK_ENABLING_POSTMORTEM_DEBUGGING_DBG"></span>User Mode Exception Handling


**Exceptions and Breakpoints**

The most common application errors are called exceptions. These include access violations, division-by-zero errors, numerical overflows, CLR exceptions, and many other kinds of errors. Applications can also cause breakpoint interrupts. These occur when Windows is unable to run the application (for example, when a necessary module cannot be loaded) or when a breakpoint is encountered. Breakpoints can be inserted into the code by a debugger, or invoked through a function such as [**DebugBreak**](https://msdn.microsoft.com/library/windows/desktop/ms679297).

**Exception Handlers Precedence**

Based on configuration values and which debuggers are active, Windows handles user-mode errors in a variety of ways. The following sequence shows the precedence used for user mode error handling:

1.  If a user-mode debugger is currently attached to the faulting process, all errors will cause the target to break into this debugger.

    As long as the user-mode debugger is attached, no other error-handling methods will be used -- even if the [**gn (Go With Exception Not Handled)**](gn--gn--go-with-exception-not-handled-.md) command is used.

2.  If no user-mode debugger is attached and the executing code has its own exception handling routines (for example, **try - except**), this exception handling routine will attempt to deal with the error.

3.  If no user-mode debugger is attached, and Windows has an open kernel-debugging connection, and the error is a breakpoint interrupt, Windows will attempt to contact the kernel debugger.

    Kernel debugging connections must be opened during Windows' boot process. If you wish to prevent a user-mode interrupt from breaking into the kernel debugger, you can use the KDbgCtrl utility with the **-du** parameter. For details on how to configure kernel-debugging connections and how to use KDbgCtrl, see [Getting Set Up for Debugging](getting-set-up-for-debugging.md).

    In the kernel debugger, you can use [**gh (Go With Exception Handled)**](gh--go-with-exception-handled-.md) to disregard the error and continue running the target. You can use [**gn (Go With Exception Not Handled)**](gn--gn--go-with-exception-not-handled-.md) to bypass the kernel debugger and go on to step 4.

4.  If the conditions in steps 1, 2, and 3 do not apply, Windows will activate a debugging tool configured in the AeDebug registry values. Any program can be selected in advance as the tool to use in this situation. The chosen program is referred to as the *postmortem debugger*.

5.  If the conditions in steps 1, 2, and 3 do not apply, and there is no postmortem debugger registered, Windows Error Reporting (WER) displays a message and provides solutions if any are available. WER also writes a memory dump file if the appropriate values are set in the Registry. For more information, see [Using WER](https://go.microsoft.com/fwlink/p?LinkID=257799) and [Collecting User-Mode Dumps](https://go.microsoft.com/fwlink/p?LinkID=257798).

**DebugBreak Function**

If a postmortem debugger has been installed, you can deliberately break into the debugger from a user-mode application by calling the **DebugBreak** function.

## <span id="Specifying_a_Postmortem_Debugger"></span><span id="specifying_a_postmortem_debugger"></span><span id="SPECIFYING_A_POSTMORTEM_DEBUGGER"></span>Specifying a Postmortem Debugger


This section describes how to configure tools such as WinDbg as the postmortem debugger. Once configured, the postmortem debugger will be automatically started whenever an application crashes.

**Post Mortem Debugger Registry Keys**

Windows Error Reporting (WER) creates the postmortem debugger process using the values set in the AeDebug registry key.

**HKLM**\\**Software**\\**Microsoft**\\**Windows NT**\\**CurrentVersion**\\**AeDebug**

There are two primary registry values of interest, *Debugger* and *Auto*. The *Debugger* registry value specifies the command line for the postmortem debugger. The *Auto* registry value specifies if the postmortem debugger is automatically started, or if a confirmation message box is presented first.

<span id="Debugger__REG_SZ_"></span><span id="debugger__reg_sz_"></span><span id="DEBUGGER__REG_SZ_"></span>**Debugger (REG\_SZ)**  

This REG\_SZ value specifies the debugger that will handle postmortem debugging.

The full path to the debugger must be listed unless the debugger is located in a directory that is in the default path.

The command line is generated from the Debugger string via a printf style call that includes 3 parameters. Although the order is fixed, there is no requirement to use any or all of the available parameters.

DWORD (%ld) - Process ID of the target process.

DWORD (%ld) - Event Handle duplicated into the postmortem debugger process. If the postmortem debugger signals the event, WER will continue the target process without waiting for the postmortem debugger to terminate. The event should only be signaled if the issue has been resolved. If the postmortem debugger terminates without signaling the event, WER continues the collection of information about the target processes.

void\* (%p) - Address of a JIT\_DEBUG\_INFO structure allocated in the target process’s address space. The structure contains additional exception information and context.

<span id="Auto__REG_SZ_"></span><span id="auto__reg_sz_"></span><span id="AUTO__REG_SZ_"></span>**Auto (REG\_SZ)**
This REG\_SZ value is always either **0** or **1**.

If **Auto** is set to **0**, a confirmation message box is displayed prior to postmortem debugging process being started.

If **Auto** is set to **1**, the postmortem debugger is immediately created.

When you manually edit the registry, do so very carefully, because improper changes to the registry may not allow Windows to boot.

**Example Command Line Usage**

Many postmortem debuggers use a command line that includes -p and -e switches to indicate the parameters are a PID and Event (respectively). For example, installing WinDbg via `windbg.exe -I` creates the following values:

```console
Debugger = "<Path>\WinDbg -p %ld -e %ld -g"
Auto = 1
```

There is flexibility in how the WER %ld %ld %p parameters can be used. For example. there is no requirement to specify any switches around or between the WER parameters. For example, installing [Windows Sysinternals ProcDump](https://technet.microsoft.com/sysinternals/dd996900.aspx) using `procdump.exe -i` creates the following values with no switches between the WER %ld %ld %p parameters:

```console
Debugger = "<Path>\procdump.exe" -accepteula -j "c:\Dumps" %ld %ld %p
Auto = 1
```

**32 and 64 bit Debuggers**

On a 64-bit platform, the Debugger (REG\_SZ) and Auto (REG\_SZ) registry values are defined individually for 64-bit and 32-bit applications. An additional Windows on Windows (WOW) key is used to store the 32 bit application post mortem debugging values.

**HKLM**\\**Software**\\**Wow6432Node**\\**Microsoft**\\**Windows NT**\\**CurrentVersion**\\**AeDebug**

On a 64-bit platform, use a 32-bit post-mortem debugger for 32-bit processes and a 64-bit debugger for 64-bit processes. This avoids a 64-bit debugger focusing on the WOW64 threads, instead of the 32-bit threads, in a 32-bit process.

For many postmortem debuggers, including the Debugging Tools for Windows postmortem debuggers, this involves running the installation command twice; once with the x86 version and once with the x64 version. For example, to use WinDbg as the interactive postmortem debugger, the `windbg.exe -I` command would be run twice, once for each version.

64-bit Installation:

```console
C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\windbg.exe –I
```

This updates the registry key with these values.

```reg
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AeDebug
Debugger = "C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\windbg.exe" -p %ld -e %ld –g
```

32-bit Installation:

```console
C:\Program Files (x86)\Windows Kits\10\Debuggers\x86\windbg.exe –I
```

This updates the registry key with these values.

```reg
HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Windows NT\CurrentVersion\AeDebug
Debugger = "C:\Program Files (x86)\Windows Kits\10\Debuggers\x86\windbg.exe" -p %ld -e %ld –g
```

## <span id="Configuring"></span><span id="configuring"></span><span id="CONFIGURING"></span>Configuring Post Mortem Debuggers


### <span id="Debugging_Tools_for_Windows"></span><span id="debugging_tools_for_windows"></span><span id="DEBUGGING_TOOLS_FOR_WINDOWS"></span>Debugging Tools for Windows

The Debugging Tools for Windows debuggers all support being set as the postmortem debugger. The install command intends for the process to be debugged interactively.

**WinDbg**

To set the postmortem debugger to WinDbg, run `windbg -I`. (The `I` must be capitalized.) This command will display a success or failure message after it is used. To work with both 32 and 64 bit applications, run the command for the both the 64 and 32 debuggers.

```console
C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\windbg.exe –I
C:\Program Files (x86)\Windows Kits\10\Debuggers\x86\windbg.exe –I
```

This is how the AeDebug registry entry will be configured when `windbg -I` is run.

```console
Debugger = "<Path>\WinDbg -p %ld -e %ld -g"
Auto = 1
```

In the examples, *&lt;Path&gt;* is the directory where the debugger is located.

The -p and -e parameters pass the Process ID and Event, as discussed previously.

The **-g** passes the g (Go) command to WinDbg and continues execution from the current instruction.

**Note**  
There is a significant issue passing the g (Go) command. The issue with this approach, is that exceptions do not always repeat, typically, because of a transient condition that no longer exists when the code is restarted. For more information about this issue, see [**.jdinfo (Use JIT\_DEBUG\_INFO)**](-jdinfo--use-jit-debug-info-.md).

To avoid this issue, use .jdinfo or .dump /j. This approach allows the debugger to be in the context of the code failure of interest. For more information, see [Just In Time (JIT) Debugging](#jit) later in this topic.

 

**CDB**

To set the postmortem debugger to CDB, run **cdb -iae** (Install AeDebug) or **cdb -iaec** *KeyString* (Install AeDebug with Command).

```console
C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\cdb.exe -iae
C:\Program Files (x86)\Windows Kits\10\Debuggers\x86\cdb.exe -iae
```

When the **-iaec** parameter is used, *KeyString* specifies a string to be appended to the end of command line used to launch the postmortem debugger. If *KeyString* contains spaces, it must be enclosed in quotation marks.

```console
C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\cdb.exe -iaec [KeyString]
C:\Program Files (x86)\Windows Kits\10\Debuggers\x86\cdb.exe -iaec [KeyString]
```

This command display nothing if it succeeds, and an error message if it fails.

**NTSD**

To set the postmortem debugger to NTSD, run **ntsd -iae** (Install AeDebug) or **ntsd -iaec** *KeyString* (Install AeDebug with Command).

```console
C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\ntsd.exe -iae
C:\Program Files (x86)\Windows Kits\10\Debuggers\x86\ntsd.exe -iae
```

When the **-iaec** parameter is used, *KeyString* specifies a string to be appended to the end of command line used to launch the postmortem debugger. If *KeyString* contains spaces, it must be enclosed in quotation marks.

```console
C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\ntsd.exe -iaec [KeyString]
C:\Program Files (x86)\Windows Kits\10\Debuggers\x86\ntsd.exe -iaec [KeyString]
```

This command display nothing if it succeeds, and an error to a new console window on failure.

**Note**  Because the -p %ld -e %ld -g parameters always appear first on the command line of the postmortem debugger, you should not use the -iaec switch to specify the -server parameter because -server will not work unless it appears first on the command line. To install a postmortem debugger that includes this parameter, you must edit the registry manually.

 

### <span id="Visual_Studio_JIT_Debugger"></span><span id="visual_studio_jit_debugger"></span><span id="VISUAL_STUDIO_JIT_DEBUGGER"></span>Visual Studio JIT Debugger

If Visual Studio has been installed, vsjitdebugger.exe will be registered as the post mortem debugger. The Visual Studio JIT Debugger intends for the process to be debugged interactively.

```console
Debugger = "C:\WINDOWS\system32\vsjitdebugger.exe" -p %ld -e %ld
```

If Visual Studio is updated or re-installed, this entry will be re-written, overwriting any alternate values set.

### <span id="Window_Sysinternals_ProcDump"></span><span id="window_sysinternals_procdump"></span><span id="WINDOW_SYSINTERNALS_PROCDUMP"></span>Window Sysinternals ProcDump

The Windows Sysinternals ProcDump utility can also be used for postmortem dump capture. For more information about using and downloading ProcDump, see [ProcDump](https://technet.microsoft.com/sysinternals/dd996900.aspx) on TechNet.

Like the [**.dump**](-dump--create-dump-file-.md) WinDbg command, ProcDump is able to be capture a dump of the crash non-interactively. The capture may occur in any Windows system session.

ProcDump exits when the dump file capture completes, WER then reports the failure and the faulting process is terminated.

Use `procdump -i` to install procdump and -u to uninstall ProcDump for both the 32 and 64 bit post mortem debugging.

```console
<Path>\procdump.exe -i
```

The install and uninstall commands output the registry values modified on success, and the errors on failure.

The ProcDump command line options in the registry are set to:

```console
Debugger = <Path>\ProcDump.exe -accepteula -j "<DumpFolder>" %ld %ld %p
```

ProcDump uses all 3 parameters - PID, Event and JIT\_DEBUG\_INFO. For more information on the JIT\_DEBUG\_INFO parameter, see [Just In Time (JIT) Debugging](#jit) below.

The size of dump captured defaults to Mini (process/threads/handles/modules/address space) without a size option set, MiniPlus (Mini plus MEM\_PRIVATE pages) with -mp set, or Full (all memory - equivalent to ".dump /mA") with -ma set.

For systems with sufficient drive space, a Full (-ma) capture is recommended.

Use -ma with the -i option to specify an all memory capture. Optionally, provide a path for the dump files.

```console
<Path>\procdump.exe -ma -i c:\Dumps
```

For systems with limited drive space, a MiniPlus (-mp) capture is recommended.

```console
<Path>\procdump.exe -mp -i c:\Dumps
```

The folder to save the dump file to is optional. The default is the current folder. The folder should secured with an ACL that is equal or better than what is used for C:\\Windows\\Temp. For more information on managing security related to folders, see [Security During Postmortem Debugging](security-during-postmortem-debugging.md).

To uninstall ProcDump as the postmortem debugger, and restore the previous settings, use the -u (Uninstall) option.

```console
<Path>\procdump.exe -u
```

The install and uninstall commands set both the 64-bit and 32-bit values on 64-bit platforms.

ProcDump is a "packed" executable containing both the 32-bit and 64-bit version of application - as such, the same executable is used for both 32-bit and 64-bit. When ProcDump runs, it automatically switches the version, if the version running doesn't match the target process.

## <span id="JIT"></span><span id="jit"></span> Just In Time (JIT) Debugging


**Setting Context to the Faulting Application**

As discussed previously, it is very desirable to set the context to the exception that caused the crash using the JIT\_DEBUG\_INFO parameter. For more information about this, see [**.jdinfo (Use JIT\_DEBUG\_INFO)**](-jdinfo--use-jit-debug-info-.md).

**Debugging Tools for Windows**

This example shows how to edit the registry to run an initial command (-c) that uses the .jdinfo &lt;address&gt; command to display the additional exception information, and change the context to the location of the exception (similar to how .ecxr is used set the context to the exception record).

```console
Debugger = "<Path>\windbg.exe -p %ld -e %ld -c ".jdinfo 0x%p"
Auto = 1
```

The %p parameter is the address of a JIT\_DEBUG\_INFO structure in the target process’s address space. The %p parameter is pre-appended with 0x so that it is interpreted as a hex value. For more information, see [**.jdinfo (Use JIT\_DEBUG\_INFO)**](-jdinfo--use-jit-debug-info-.md).

To debug a mix of 32 and 64 bit apps, configure both the 32 and 64 bit registry keys (described above), setting the proper path to the location of the 64-bit and 32-bit WinDbg.exe.

**Creating a dump file using .dump**

To capture a dump file whenever a failure occurs that includes the JIT\_DEBUG\_INFO data, use .dump /j &lt;address&gt;.

```console
<Path>\windbg.exe -p %ld -e %ld -c ".dump /j %p /u <DumpPath>\AeDebug.dmp; qd"
```

Use the /u option to generate a unique filename to allow multiple dump files to be automatically created. For more information about the options see, [**.dump (Create Dump File)**](-dump--create-dump-file-.md).

The created dump will have the JITDEBUG\_INFO data stored as the default exception context. Instead of using .jdinfo to view the exception information and set the context, use .exr -1 to display the exception record and .ecxr to set the context. For more information see [**.exr (Display Exception Record)**](-exr--display-exception-record-.md) and [**.ecxr (Display Exception Context Record)**](-ecxr--display-exception-context-record-.md).

**Windows Error Reporting - q / qd**

The way the debug session ends determines if Windows Error Reporting reports the failure.

If the debug session is detached using qd prior to the closing of the debugger, WER will report the failure.

If the debug session is quit using q (or if the debugger is closed without detaching), WER will not report the failure.

Append *;q* or *;qd* to the end of the command string to invoke the desired behavior.

For example, to allow WER to report the failure after CDB captures a dump, configure this command string.

```console
<Path>\cdb.exe -p %ld -e %ld -c ".dump /j 0x%p /u c:\Dumps\AeDebug.dmp; qd"
```

This example would allow WER to report the failure after WinDbg captures a dump.

```console
<Path>\windbg.exe -p %ld -e %ld -c ".dump /j %p /u <DumpPath>\AeDebug.dmp; qd""
```

## <span id="security_vulnerabilities"></span><span id="SECURITY_VULNERABILITIES"></span>Security Vulnerabilities


If you are considering enabling postmortem debugging on a computer that you share with other people, see [Security During Postmortem Debugging](security-during-postmortem-debugging.md).

 

 





