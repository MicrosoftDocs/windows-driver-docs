---
title: Controlling a KD Connection Server Session
description: Controlling a KD Connection Server Session
ms.assetid: d927575f-f408-48d0-81f4-0711a09b0015
keywords: ["KD connection server, controlling a session"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Controlling a KD Connection Server Session


## <span id="ddk_controlling_a_kd_connection_server_session_dbg"></span><span id="DDK_CONTROLLING_A_KD_CONNECTION_SERVER_SESSION_DBG"></span>


Once the remote session has been started, the smart client can be used as if it were debugging the target computer from the computer where the KD connection server is running. All commands will behave as they would in this situation, except that paths are relative to the smart client's computer.

### <span id="using_windbg_as_a_smart_client"></span><span id="USING_WINDBG_AS_A_SMART_CLIENT"></span>Using WinDbg as a Smart Client

After WinDbg is started as a smart client for a KD connection server, you can use the [Debug | Stop Debugging](debug---stop-debugging.md) command to end the debugging session. At that point, WinDbg will enter dormant mode and will no longer be connected to the KD connection server. All subsequent debugging will be done on the computer where WinDbg is running. You cannot reattach to the KD connection serve by using [File | Kernel Debug](file---kernel-debug.md) -- this can only be done from the command line.

### <span id="ending_the_session"></span><span id="ENDING_THE_SESSION"></span>Ending the Session

KD or WinDbg can exit or end the debugging session in the normal fashion. See [Ending a Debugging Session in WinDbg](ending-a-debugging-session-in-windbg.md)

for details. The KD connection server will remain in operation and can be re-used as many times as desired. (It can also be used by for any number of simultaneous debugging sessions.)

The KD connection server can be terminated from either computer. To terminate it from the smart client, use the [**.endpsrv (End Process Server)**](-endpsrv--end-process-server-.md) command. To terminate the KD connection server from the computer it is running on, use Task Manager to end the kdsrv.exe process.

 

 





