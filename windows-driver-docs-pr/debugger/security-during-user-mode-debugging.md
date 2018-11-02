---
title: Security During User-Mode Debugging
description: Security During User-Mode Debugging
ms.assetid: e198c29a-d793-4974-8ee3-f26679bd70b4
keywords: ["security considerations, user-mode debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Security During User-Mode Debugging


## <span id="ddk_security_during_user_mode_debugging_dbg"></span><span id="DDK_SECURITY_DURING_USER_MODE_DEBUGGING_DBG"></span>


When a user-mode debugger is active, it can effectively control any of the processes on the computer.

There are three possible ways in which security problems could arise during user-mode debugging:

-   If you use corrupt or destructive extension DLLs, they could cause your debugger to take unexpected actions, possibly affecting applications other than your target.

-   It is possible that corrupt or destructive symbol files could also cause your debugger to take unexpected actions, possibly affecting applications other than your target.

-   If you are running a remote debugging session, an unexpected client might attempt to link to your server. Or perhaps the client you are expecting might attempt to perform actions that you do not anticipate.

For suggestions on how to guard against unexpected remote connections, see [Security During Remote Debugging](security-during-remote-debugging.md). After a remote client has joined a user-mode debugging session, there is no way to restrict its access to processes on your computer.

If you are not performing remote debugging, you should still beware of bad symbol files and extension DLLs. do not load symbols or extensions that you distrust!

 

 





