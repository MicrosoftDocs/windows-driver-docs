---
title: Controlling a KD Connection Server Session
description: Controlling a KD Connection Server Session
ms.assetid: d927575f-f408-48d0-81f4-0711a09b0015
keywords: ["KD connection server, controlling a session"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Controlling%20a%20KD%20Connection%20Server%20Session%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




