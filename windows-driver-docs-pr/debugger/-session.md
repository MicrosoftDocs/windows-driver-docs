---
title: session
description: The session extension controls the session context. It can also display a list of all user sessions.
ms.assetid: c5f32bf0-59b5-4274-9271-1ad4913ffa1a
keywords: ["session Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- session
api_type:
- NA
ms.localizationpriority: medium
---

# !session


The **!session** extension controls the session context. It can also display a list of all user sessions.

Syntax

```dbgcmd
!session 
!session -s DefaultSession 
!session -?
```

## <span id="ddk__session_dbg"></span><span id="DDK__SESSION_DBG"></span>Parameters


<span id="_______-s_______DefaultSession______"></span><span id="_______-s_______defaultsession______"></span><span id="_______-S_______DEFAULTSESSION______"></span> **-s** **** *DefaultSession*   
Sets the [session context](changing-contexts.md#session-context) to the specified value. If *DefaultSession* is -1, the session context is set to the current session.

<span id="_______-_______"></span> **-?**   
Displays help for this extension in the Debugger Command window.

### <span id="DLL"></span><span id="dll"></span>DLL

Kdexts.dll

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about user sessions and the Session Manager (smss.exe), see *Microsoft Windows Internals*, by Mark Russinovich and David Solomon.

Remarks
-------

The **!session** extension is used to control the session context. Using **!session** with no parameters will display a list of active sessions on the target computer. Using **!session /s** *DefaultSession* will change the session context to the new default value.

When you set the session context, the process context is automatically changed to the active process for that session, and the [**.cache forcedecodeptes**](-cache--set-cache-size-.md) option is enabled so that session addresses are translated properly.

For more details and a list of all the session-related extensions that are affected by the session context, see [Changing Contexts](changing-contexts.md).

 

 





