---
title: session
description: The session extension controls the session context. It can also display a list of all user sessions.
ms.assetid: c5f32bf0-59b5-4274-9271-1ad4913ffa1a
keywords: ["session Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- session
api_type:
- NA
---

# !session


The **!session** extension controls the session context. It can also display a list of all user sessions.

Syntax

``` syntax
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!session%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




