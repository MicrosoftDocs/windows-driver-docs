---
title: (Process Status)
description: The pipe ( ) command displays status for the specified process, or for all processes that you are currently debugging.Do not confuse this command with the (System Status) command.
keywords: ["(Process Status) Windows Debugging"]
ms.date: 08/30/2023
topic_type:
- apiref
ms.topic: reference
api_name:
- (Process Status)
api_type:
- NA
---

# | (Process Status)

The pipe (**|**) command displays status for the specified process, or for all processes that you are currently debugging.

Do not confuse this command with the [**|| (System Status)**](----system-status-.md) command.

```dbgcmd
| Process
```

## Parameters

*Process*

Specifies the process to display. If you omit this parameter, all processes that you are debugging are displayed. For more information about the syntax, see [Process Syntax](process-syntax.md).

### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes|User mode only|
|Targets|Live, crash dump|
|Platforms|All|

### Additional Information

For more information and other methods of displaying or controlling processes and threads, see [Controlling Processes and Threads](controlling-processes-and-threads.md).

## Remarks

You can specify processes only in user mode.

You can add a process symbol before many commands. For more information about the meaning of a pipe (**|**) followed by a command, see the entry for the command itself.

Unless you enabled the debugging of child processes when you started the debugging session, there is only one process that is available to the debugger.

The following examples show you how to use this command. The following command displays all processes.

```dbgcmd
2:005> |
```

The following command also displays all processes.

```dbgcmd
2:005> |*
```

The following command displays the currently active process.

```dbgcmd
2:005> |.
```

The following command displays the process that originally caused the exception (or that the debugger originally attached to).

```dbgcmd
2:005> |#
```

The following command displays process number 2.

```dbgcmd
2:005> |2
```

The previous command displays the following output.

```dbgcmd
0:002> |
#  0 id: 224   name: myprog.exe 
   1 id: 228   name: onechild.exe 
 . 2 id: 22c   name: anotherchild.exe 
```

On the first line of this output, 0 is the decimal process number, 224 is the hexadecimal process ID, and *Myprog.exe* is the application name of the process. The period (.) before process 2 means that this process is the current process. The number sign (\#) before process 0 means that this process was the one that originally caused the exception or that the debugger attached to.
