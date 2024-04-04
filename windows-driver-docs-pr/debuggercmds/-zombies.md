---
title: "!zombies (WinDbg)"
description: "The !zombies extension is obsolete."
keywords: ["!zombies Windows Debugging"]
ms.date: 04/02/2024
topic_type:
- apiref
ms.topic: reference
api_name:
- zombies
api_type:
- NA
---

# !zombies

The **!zombies** extension displays all dead ("zombie") processes or threads.

```dbgcmd
!zombies [Flags [RestartAddress]]
```

## Parameters

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Specifies what will be displayed. Possible values include:

<span id="1"></span>1  
Displays all zombie processes. (This is the default.)

<span id="2"></span>2  
Displays all zombie threads.

<span id="_______RestartAddress______"></span><span id="_______restartaddress______"></span><span id="_______RESTARTADDRESS______"></span> *RestartAddress*   
Specifies the hexadecimal address at which to begin the search. This is useful if the previous search was terminated prematurely. The default is zero.

## DLL

Windows XP and later - Unavailable

## Additional Information

This extension is obsolete.

To see a list of all processes and threads, use the [**!process**](-process.md) extension.

For general information about processes and threads in kernel mode, see [Changing Contexts](../debugger/changing-contexts.md). For more information about analyzing processes and threads, see *Microsoft Windows Internals*, by Mark Russinovich and David Solomon.

## Remarks

Zombie processes are dead processes that have not yet been removed from the process list. Zombie threads are analogous.
