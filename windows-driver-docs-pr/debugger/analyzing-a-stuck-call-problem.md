---
title: Analyzing a Stuck Call Problem
description: Analyzing a Stuck Call Problem
ms.assetid: e1a80cde-cf83-4a16-ae4b-5ddd5eb77b6d
keywords: ["RPC debugging, stuck call"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Analyzing a Stuck Call Problem


## <span id="ddk_analyzing_a_stuck_call_problem_dbg"></span><span id="DDK_ANALYZING_A_STUCK_CALL_PROBLEM_DBG"></span>


A common problem occurs when a process makes an RPC call, directly or indirectly, while holding a critical section or a resource. In this case, the RPC call goes to another process or machine and dispatches to the manager routine (server routine), which then hangs or takes too long. This causes the original caller to encounter a critical section time-out.

When examined through the debugger, RPC is on top of the stack of the thread owning the critical section, but it is not clear what it is waiting for.

Here is one example of such a stack. Many variations are possible.

```dbgcmd
0:002> ~1k
ChildEBP RetAddr
0068fba0 77e9e8eb ntdll!ZwWaitForSingleObject+0xb
0068fbc8 4efeff73 KERNEL32!WaitForSingleObjectEx+0x5a
0068fbe8 4eff0012 RPCRT4!UTIL_WaitForSyncIO+0x21
0068fc0c 4efe6e2b RPCRT4!UTIL_GetOverlappedResultEx+0x44
0068fc44 4ef973bf RPCRT4!WS_SyncRecv+0x12a
0068fc68 4ef98d5a RPCRT4!OSF_CCONNECTION__TransSendReceive+0xcb
0068fce4 4ef9b682 RPCRT4!OSF_CCONNECTION__SendFragment+0x297
0068fd38 4ef9a5a8 RPCRT4!OSF_CCALL__SendNextFragment+0x272
0068fd88 4ef9a9cb RPCRT4!OSF_CCALL__FastSendReceive+0x165
0068fda8 4ef9a7f8 RPCRT4!OSF_CCALL__SendReceiveHelper+0xed
0068fdd4 4ef946a7 RPCRT4!OSF_CCALL__SendReceive+0x37
0068fdf0 4efd56b3 RPCRT4!I_RpcSendReceive+0xc4
0068fe08 01002850 RPCRT4!NdrSendReceive+0x4f
0068ff40 01001f32 rtclnt+0x2850
0068ffb4 77e92ca8 rtclnt+0x1f32
0068ffec 00000000 KERNEL32!CreateFileA+0x11b
```

Here's how to troubleshoot this problem.

 **Troubleshooting a stuck call problem**

1.  Make sure the debugger is debugging the process that owns the stuck cell. (This is the process containing the client thread that is suspected of hanging in RPC.)

2.  Get the stack pointer of this thread. The stack will look like the one shown in the preceding example. In this example, the stack pointer is 0x0068FBA0.

3.  Get the call information for this thread. In order to do that, use the [**!rpcexts.rpcreadstack**](-rpcexts-rpcreadstack.md) extension with the thread stack pointer as its parameter, as follows:

    ```dbgcmd
    0:001> !rpcexts.rpcreadstack 68fba0
    CallID: 1
    IfStart: 19bb5061
    ProcNum: 0
            Protocol Sequence:      "ncacn_ip_tcp"  (Address: 00692ED8)
            NetworkAddress: ""      (Address: 00692F38)
            Endpoint:       "1120"  (Address: 00693988)
    ```

    The information displayed here will allow you to trace the call.

4.  The network address is empty, which indicates the local machine. The endpoint is 1120. You need to determine which process hosts this endpoint. This can be done by passing this endpoint number to the [**!rpcexts.getendpointinfo**](-rpcexts-getendpointinfo.md) extension, as follows:

    ```dbgcmd
    0:001> !rpcexts.getendpointinfo 1120
    Searching for endpoint info ...
    PID  CELL ID   ST PROTSEQ        ENDPOINT
    --------------------------------------------
    0278 0000.0001 01            TCP 1120
    ```

5.  From the preceding information, you can see that process 0x278 contains this endpoint. You can determine if this process knows anything about this call by using the [**!rpcexts.getcallinfo**](-rpcexts-getcallinfo.md) extension. This extension needs four parameters: *CallID*, *IfStart*, and *ProcNum* (which were found in step 3), and the *ProcessID* of 0x278:

    ```dbgcmd
    0:001> !rpcexts.getcallinfo 1 19bb5061 0 278
    Searching for call info ...
    PID  CELL ID   ST PNO IFSTART  TIDNUMBER CALLFLAG CALLID   LASTTIME CONN/CLN
    ----------------------------------------------------------------------------
    0278 0000.0004 02 000 19bb5061 0000.0002 00000001 00000001 00072c09 0000.0003
    ```

6.  The information in step 5 is useful, but somewhat abbreviated. The cell ID is given in the second column as 0000.0004. If you pass the process ID and this cell number to the [**!rpcexts.getdbgcell**](-rpcexts-getdbgcell.md) extension, you will see a more readable display of this cell:

    ```dbgcmd
    0:001> !rpcexts.getdbgcell 278 0.4
    Getting cell info ...
    Call
    Status: Dispatched
    Procedure Number: 0
    Interface UUID start (first DWORD only): 19BB5061
    Call ID: 0x1 (1)
    Servicing thread identifier: 0x0.2
    Call Flags: cached
    Last update time (in seconds since boot):470.25 (0x1D6.19)
    Owning connection identifier: 0x0.3
    ```

    This shows that the call is in state "dispatched", which means is has left the RPC Run-Time. The last update time is 470.25. You can learn the current time by using the [**!rpcexts.rpctime**](-rpcexts-rpctime.md) extension:

    ```dbgcmd
    0:001> !rpcexts.rpctime
    Current time is: 6003, 422
    ```

    This shows that the last contact with this call was approximately 5533 seconds ago, which is about 92 minutes. Thus, this must be a stuck call.

7.  As a last step before you attach a debugger to the server process, you can isolate the thread that should currently service the call by using the Servicing thread identifier. This is another cell number; it appeared in step 6 as "0x0.2". You can use it as follows:

    ```dbgcmd
    0:001> !rpcexts.getdbgcell 278 0.2
    Getting cell info ...
    Thread
    Status: Dispatched
    Thread ID: 0x1A4 (420)
    Last update time (in seconds since boot):470.25 (0x1D6.19)
    ```

    Now you know that you are looking for thread 0x1A4 in process 0x278.

It is possible that the thread was making another RPC call. If necessary, you can trace this call by repeating this procedure.

**Note**   This procedure shows how to find the server thread if you know the client thread. For an example of the reverse technique, see [Identifying the Caller From the Server Thread](identifying-the-caller-from-the-server-thread.md).

 

 

 





