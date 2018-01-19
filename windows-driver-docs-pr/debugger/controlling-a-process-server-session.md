---
title: Controlling a Process Server Session
description: Controlling a Process Server Session
ms.assetid: 4219b08a-d353-43dc-8640-96c504b8075b
keywords: ["process server, controlling a session"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Controlling a Process Server Session


## <span id="ddk_controlling_a_process_server_session_dbg"></span><span id="DDK_CONTROLLING_A_PROCESS_SERVER_SESSION_DBG"></span>


Once the remote session has been started, the smart client can be used as if it were debugging a target application on a single machine. All commands will behave as they would in this situation, except that paths are relative to the smart client's computer.

### <span id="using_windbg_as_a_smart_client"></span><span id="USING_WINDBG_AS_A_SMART_CLIENT"></span>Using WinDbg as a Smart Client

After WinDbg is started as a smart client for a user-mode process server, it will remain attached to the process server permanently. If the debugging session is ended, the [File | Attach to a Process](file---attach-to-a-process.md) menu command or the [**.tlist (List Process IDs)**](-tlist--list-process-ids-.md) command will display all processes running on the computer running the process server. WinDbg can attach to any of these processes.

The [File | Open Executable](file---open-executable.md) command cannot be used. A new process can only be spawned if it is included on the WinDbg command line.

In this situation, WinDbg will not be able to debug processes on the computer where it is running, nor will it be able to start a kernel debugging session.

### <span id="ending_the_session"></span><span id="ENDING_THE_SESSION"></span>Ending the Session

CDB or WinDbg can exit or end the debugging session in the normal fashion. See [Ending a Debugging Session in WinDbg](ending-a-debugging-session-in-windbg.md) for details. The process server will remain in operation and can be re-used as many times as desired. (It can also be used by for any number of simultaneous debugging sessions.)

The process server can be terminated from either computer. To terminate it from the smart client, use the [**.endpsrv (End Process Server)**](-endpsrv--end-process-server-.md) command. To terminate the process server from the computer it is running on, use Task Manager to end the dbgsrv.exe process.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Controlling%20a%20Process%20Server%20Session%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




