---
title: "!session (WinDbg)"
description: "The !session extension controls the session context. It can also display a list of all user sessions."
keywords: ["!session Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- session
api_type:
- NA
---

# !session

The **!session** extension controls the session context. It can also display a list of all user sessions.

Syntax

```dbgcmd
!session 
!session -s DefaultSession 
!session -?
```

## Parameters

<span id="_______-s_______DefaultSession______"></span><span id="_______-s_______defaultsession______"></span><span id="_______-S_______DEFAULTSESSION______"></span> **-s** **** *DefaultSession*   
Sets the [session context](../debugger/changing-contexts.md#session-context) to the specified value. If *DefaultSession* is -1, the session context is set to the current session.

<span id="_______-_______"></span> **-?**   
Displays help for this extension in the Debugger Command window.

## DLL

Kdexts.dll

## Additional Information

For information about user sessions and the Session Manager (smss.exe), see *Microsoft Windows Internals*, by Mark Russinovich and David Solomon.

## Remarks

The **!session** extension is used to control the session context. Using **!session** with no parameters will display a list of active sessions on the target computer. Using **!session /s** *DefaultSession* will change the session context to the new default value.

When you set the session context, the process context is automatically changed to the active process for that session, and the [**.cache forcedecodeptes**](-cache--set-cache-size-.md) option is enabled so that session addresses are translated properly.

For more details and a list of all the session-related extensions that are affected by the session context, see [Changing Contexts](../debugger/changing-contexts.md).
