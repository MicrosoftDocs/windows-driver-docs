---
title: "WinDbg - Command-Line Startup Options"
description: "This section covers the command-line startup options for WinDbg, the debugger for Windows."
keywords: ["Command line startup options", "WinDbg", "Menu", "Windows Debugging"]
ms.date: 09/11/2019
ms.topic: reference
---

# WinDbg: Command-line startup options

:::image type="content" source="images/windbgx-preview-logo.png" alt-text="WinDbg logo with a magnifying glass inspecting bits.":::

## Start WinDbg

After WinDbg is installed, WinDbgX.exe is available to run from any directory location.

## Command-line startup options

```dbgsyntax
WinDbgX [options]
```

The following tables summarize the available command-line options.

#### General options

|     Option      |                                                                          Description                                                                          |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `-c  command`  | Runs a command line after the debugger is attached. Enclose this command in quotation marks. Separate multiple commands with semicolons. |
| `-v`               | Enables verbose output in the debugger.                                                            |
| `-T Title`       | Sets the window title.                                                                     |
| `-logo LogFile`  | Opens log. Begins logging information to a log file. If the file exists, it's overwritten.                                |
| `-loga LogFile`  | Appends log. Begins logging information to a log file. If the file exists, it's appended.                               |
| `-e EventHandle` | Signals the event with the specific handle after the next exception in a target.                                         |
|       `-?`         | Displays a summary of commands available.                                                           |

#### Kernel options

|       Option       |                                                                      Description                                                                      |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| `-k \[ConnectType\]` | Starts a kernel debugging session. If `-k` is used without any `ConnectType` options following it, it must be the final entry on the command line. |
|        `-kqm`        | Starts kernel debugging in quiet mode.                                                                |
|        `-kl`         | Starts a kernel debugging session on the same machine as the debugger.                                         |
| `-kx ExdiOptions`  | Starts a kernel debugging session by using an EXDI driver. For more information about EXDI, see [Configure the EXDI debugger transport](../debugger/configuring-the-exdi-debugger-transport.md). |
|         `-I`         | Breaks into the target computer as soon as a kernel module is loaded after a reboot                         |

#### User mode options

Option | Description
|------ | -----------|
`-o` | Debugs all processes started by the target application (child processes).
`-g` | Ignores the initial breakpoint in target application.
`-G` |Ignores the final breakpoint in target application.
`-pv` | Specifies that the debugger should attach to the target process noninvasively.
`-hd` | Specifies that the debug heap shouldn't be used.
`-cimp` | Specifies that any processes created use an implicit command line set by the server instead of a user-specified command-line string from the client.

#### Target options

| Option                     |                 Description                                                                                                                                  |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `-remote ClientTransport`  | Connects to a debugging server that's already running. For an explanation of the possible `ClientTransport` values, see [Activate a debugging client](../debugger/activating-a-debugging-client.md). When this parameter is used, it must be the first parameters on the command line. |
| `-server ServerTransport`  | Creates a debugging server that other debuggers can access. For an explanation of the possible `ServerTransport` values, see [Activate a debugging server](../debugger/activating-a-debugging-server.md).              |
| `-premote SmartClientTransport`   | Creates a smart client and connects to a process server that's already running. For an explanation of the possible `SmartClientTransport` values, see [Activate a smart client](../debugger/activating-a-smart-client.md). |
| `-p PID`               | Specifies the decimal process ID to be debugged.                                                                                                              |
| `-tid TID`             | Specifies the thread ID of a thread to be resumed when the debugging session is started.                                                                      |
| `-psn ServiceName`     | Specifies the name of the service contained in the process to be debugged. Used to debug a process that's already running.                           |
| `-pn ProcessName`      | Specifies the name of the process to be debugged.                                                                                                             |
| `-z DumpFile`          | Specifies the name of a crash dump file to debug. If the path and file name contain spaces, surround them with quotation marks.                       |
| `-debugArch x86 -or- amd64`    | Overrides the autodetect behavior and sets the target bitness for the debugger.                                                                           |
| `-loadSession`           | Loads a saved session configuration file.                                                                                                                      |
| `-setupFirewallRules`    | Configures the required firewall rules on the local system to allow kernel debugging by using KDNET.                                                                         |
| `-openPrivateDumpByHandle Handle` | *Microsoft internal use only*. Specifies the handle of a crash dump file to debug.                                                                 |
| `-benchmarkStartup`      | *Microsoft internal use only*. Runs a startup benchmark and appends the result to a file.                                                                                                    |

#### Symbol options

Option | Description
|------ | -----------|
`-y SymbolPath` | Specifies the symbol path to use. Separate multiple paths with a semicolon (;). If the path contains spaces, enclose it in quotation marks. For more information and for other ways to change this path, see [Symbol path](../debugger/symbol-path.md).
`-n`              | Addresses noisy symbol load. Enables verbose output from symbol handler.
`-i *ImagePath`  | Sets the image search path to use.
`-sdce`           | Causes the debugger to display "File access error" messages during symbol load.
`-ses`            | Causes the debugger to perform a strict evaluation of all symbol files and ignore any questionable symbols.
`-sicv`           | Causes the symbol handler to ignore the CV record.
`-sins`           | Causes the debugger to ignore the symbol path and executable image path environment variables.
`-snc`            | Causes the debugger to turn off C++ translation.
`-snul`           | Disables automatic symbol loading for unqualified names.
`-sup`           | Causes the symbol handler to search the public symbol table during every symbol search.
`-sflags`         | Sets all the symbol handler options at once.

#### Source path options

 Option   | Description
|-------- | -----------|
`-srcpath`  | Specifies the source path to use on the debugging server.
`-lsrcpath` | Specifies the source path to use on the local client.

If you're in a local debugger session, `srcpath` and `lsrcpath` are effectively the same. (Your "server" is your local session.) For remote debugging, there are situations where you might want to set these options to different values. For more information about remote debugging, see [Remote debugging](../debugger/remote-debugging.md).

#### Exception handling

Option | Description
|------ | -----------|
`-x`   |   Enables second-chance handling only for access violation exceptions.
`-xe Exception`  |   Enables first-chance exception handling for the specified exception.
`-xd Exception` |   Enables second-chance exception handling for the specified exception.
`-xn Exception` |   Disables first-chance and second-chance handling for the specific exception, and displays only a message on the console.
`-xi Exception` |   Ignores the specific exception. Disables first-chance handling and second-chance handling. Doesn't output anything to the console.

For a list of exceptions that you can specify, see [Event definitions and defaults](./../debugger/controlling-exceptions-and-events.md#event-definitions-and-defaults).

#### Postmortem

Option  | Description
|------ | -----------|
`-I`     | Sets WinDbg as the default postmortem debugger for the system.
`-IS`    | Sets WinDbg as the default postmortem debugger for the system silently. Only errors are reported.

#### Deprecated options

Option | Description
|------ | -----------|
`-Q`   | Deprecated command-line option.
`-QY`  | Deprecated command-line option.
`-QS`  | Deprecated command-line option.
`-QSY` | Deprecated command-line option.
`-WX`  | Deprecated command-line option.

For general information on the startup parameters, see [WinDbg command-line options](../debugger/windbg-command-line-options.md).

You can use `-?` to list the supported command-line options.

:::image type="content" source="images/windbgx-start-up-options.png" alt-text="Screenshot of WinDbgX command-line help output displaying various options.":::

## Related content

- [WinDbg features](../debugger/debugging-using-windbg-preview.md)