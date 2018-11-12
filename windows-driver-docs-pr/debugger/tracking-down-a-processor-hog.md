---
title: Tracking Down a Processor Hog
description: Tracking Down a Processor Hog
ms.assetid: 8ecd000d-34e6-4471-a040-b50627915a20
keywords: ["processor hog", "hogging a processor", "starving applications"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Tracking Down a Processor Hog


## <span id="ddk_tracking_down_a_processor_hog_dbg"></span><span id="DDK_TRACKING_DOWN_A_PROCESSOR_HOG_DBG"></span>


If one application is consuming ("hogging") all the processor's attention, other processes will end up "starving" and unable to run.

Use the following procedure to correct a bug of this sort.

**Debugging an application that is using all the CPU cycles**

1.  **Identify which application is causing this problem:** Use **Task Manager** or **Perfmon** to find which process is using 99% or 100% of the processor's cycles. This may tell you the offending thread as well.

2.  Attach WinDbg, KD, or CDB to this process.

3.  **Identify which thread is causing the problem:** Break into the offending application. Use the [**!runaway 3**](-runaway.md) extension to take a "snapshot" of where all the CPU time is going. Use [**g (Go)**](g--go-.md) and wait a few seconds. Then break in and use **!runaway 3** again.

    ```dbgcmd
    0:002> !runaway 3
     User Mode Time
     Thread    Time
     4e0        0:12:16.0312
     268        0:00:00.0000
     22c        0:00:00.0000
     Kernel Mode Time
     Thread    Time
     4e0        0:00:05.0312
     268        0:00:00.0000
     22c        0:00:00.0000

    0:002> g

    0:001> !runaway 3
     User Mode Time
     Thread    Time
     4e0        0:12:37.0609
     3d4        0:00:00.0000
     22c        0:00:00.0000
     Kernel Mode Time
     Thread    Time
     4e0        0:00:07.0421
     3d4        0:00:00.0000
     22c        0:00:00.0000
    ```

    Compare the two sets of numbers and look for the thread whose user-mode time or kernel-mode time has increased the most. Because **!runaway** sorts by descending CPU time, the offending thread is usually the one at the top of the list. In this case, thread 0x4E0 is causing the problem.

4.  Use the [**~ (Thread Status)**](---thread-status-.md) and [**~s (Set Current Thread)**](-s--set-current-thread-.md) commands to make this the current thread:
    ```dbgcmd
    0:001> ~
       0  Id: 3f4.3d4 Suspend: 1 Teb: 7ffde000 Unfrozen
    .  1  Id: 3f4.22c Suspend: 1 Teb: 7ffdd000 Unfrozen
     2  Id: 3f4.4e0 Suspend: 1 Teb: 7ffdc000 Unfrozen

    0:001> ~2s
    ```

5.  Use [**kb (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) to obtain a stack trace of this thread:
    ```dbgcmd
    0:002> kb
    FramePtr  RetAddr   Param1   Param2   Param3   Function Name
    0b4ffc74  77f6c600  000000c8.00000000 77fa5ad0 BuggyProgram!CreateMsgFile+0x1b
    0b4ffce4  01836060  0184f440 00000001 0b4ffe20 BuggyProgram!OpenDestFileStream+0xb3
    0b4ffd20  01843eba  02b5b920 00000102 02b1e0e0 BuggyProgram!SaveMsgToDestFolder+0xb3
    0b4ffe20  01855924  0b4ffef0 00145970 0b4ffef0 BuggyProgram!DispatchToConn+0xa4
    0b4ffe5c  77e112e6  01843e16 0b4ffef0 0b4fff34 RPCRT4!DispatchToStubInC+0x34
    0b4ffeb0  77e11215  0b4ffef0 00000000 0b4fff34 RPCRT4!?DispatchToStubWorker@RPC_INTERFACE@@AAEJPAU_RPC_MESSAGE@@IPAJ@Z+0xb0
    0b4ffed0  77e1a3b1  0b4ffef0 00000000 0b4fff34 RPCRT4!?DispatchToStub@RPC_INTERFACE@@QAEJPAU_RPC_MESSAGE@Z+0x41
    0b4fff40  77e181e4  02b1e0b0 00000074 0b4fff90 RPCRT4!?ReceiveOriginalCall@OSF_SCONNECTION@Z+0x14b
    0b4fff60  77e1a5df  02b1e0b0 00000074 00149210 RPCRT4!?DispatchPacket@OSF_SCONNECTION@+0x91
    0b4fff90  77e1ac1c  77e15eaf 00149210 0b4fffec RPCRT4!?ReceiveLotsaCalls@OSF_ADDRESS@@QAEXXZ+0x76
    ```

6.  Set a breakpoint on the return address of the currently-running function. In this case, the return address is shown on the first line as 0x77F6C600. The return address is equivalent to the function offset shown on the second line (**BuggyProgram!OpenDestFileStream+0xB3**). If no symbols are available for the application, the function name may not appear. Use the [**g (Go)**](g--go-.md) command to execute until this return address is reached, using either the symbolic or hexadecimal address:
    ```dbgcmd
    0:002> g BuggyProgram!OpenDestFileStream+0xb3
    ```

7.  If this breakpoint is hit, repeat the process. For example, suppose this breakpoint is hit. The following steps should be taken:

    ```dbgcmd
    0:002> kb
    FramePtr  RetAddr   Param1   Param2   Param3   Function Name
    0b4ffce4  01836060  0184f440 00000001 0b4ffe20 BuggyProgram!OpenDestFileStream+0xb3
    0b4ffd20  01843eba  02b5b920 00000102 02b1e0e0 BuggyProgram!SaveMsgToDestFolder+0xb3
    0b4ffe20  01855924  0b4ffef0 00145970 0b4ffef0 BuggyProgram!DispatchToConn+0xa4
    0b4ffe5c  77e112e6  01843e16 0b4ffef0 0b4fff34 RPCRT4!DispatchToStubInC+0x34
    0b4ffeb0  77e11215  0b4ffef0 00000000 0b4fff34 RPCRT4!?DispatchToStubWorker@RPC_INTERFACE@@AAEJPAU_RPC_MESSAGE@@IPAJ@Z+0xb0
    0b4ffed0  77e1a3b1  0b4ffef0 00000000 0b4fff34 RPCRT4!?DispatchToStub@RPC_INTERFACE@@QAEJPAU_RPC_MESSAGE@Z+0x41
    0b4fff40  77e181e4  02b1e0b0 00000074 0b4fff90 RPCRT4!?ReceiveOriginalCall@OSF_SCONNECTION@Z+0x14b
    0b4fff60  77e1a5df  02b1e0b0 00000074 00149210 RPCRT4!?DispatchPacket@OSF_SCONNECTION@+0x91
    0b4fff90  77e1ac1c  77e15eaf 00149210 0b4fffec RPCRT4!?ReceiveLotsaCalls@OSF_ADDRESS@@QAEXXZ+0x76

    0:002> g BuggyProgram!SaveMsgToDestFolder+0xb3
    ```

    If this is hit, continue with:

    ```dbgcmd
    0:002> kb
    FramePtr  RetAddr   Param1   Param2   Param3   Function Name
    0b4ffd20  01843eba  02b5b920 00000102 02b1e0e0 BuggyProgram!SaveMsgToDestFolder+0xb3
    0b4ffe20  01855924  0b4ffef0 00145970 0b4ffef0 BuggyProgram!DispatchToConn+0xa4
    0b4ffe5c  77e112e6  01843e16 0b4ffef0 0b4fff34 RPCRT4!DispatchToStubInC+0x34
    0b4ffeb0  77e11215  0b4ffef0 00000000 0b4fff34 RPCRT4!?DispatchToStubWorker@RPC_INTERFACE@@AAEJPAU_RPC_MESSAGE@@IPAJ@Z+0xb0
    0b4ffed0  77e1a3b1  0b4ffef0 00000000 0b4fff34 RPCRT4!?DispatchToStub@RPC_INTERFACE@@QAEJPAU_RPC_MESSAGE@Z+0x41
    0b4fff40  77e181e4  02b1e0b0 00000074 0b4fff90 RPCRT4!?ReceiveOriginalCall@OSF_SCONNECTION@Z+0x14b
    0b4fff60  77e1a5df  02b1e0b0 00000074 00149210 RPCRT4!?DispatchPacket@OSF_SCONNECTION@+0x91
    0b4fff90  77e1ac1c  77e15eaf 00149210 0b4fffec RPCRT4!?ReceiveLotsaCalls@OSF_ADDRESS@@QAEXXZ+0x76

    0:002> g BuggyProgram!DispatchToConn+0xa4
    ```

8.  Finally you will find a breakpoint that is not hit. In this case, you should assume that the last **g** command set the target running and it did not break. This means that the **SaveMsgToDestFolder()** function will never return.

9.  Break into the thread again and set a breakpoint on **BuggyProgram!SaveMsgToDestFolder+0xB3** with the [**bp (Set Breakpoint)**](bp--bu--bm--set-breakpoint-.md) command. Then use the **g** command repeatedly. If this breakpoint hits immediately, regardless of how many times you have executed the target, it is very likely that you have identified the offending function:
    ```dbgcmd
    0:002> bp BuggyProgram!SaveMsgToDestFolder+0xb3

    0:002> g 

    0:002> g 
    ```

10. Use the [**p (Step)**](p--step-.md) command to proceed through the function until you identify the place where the looping sequence of instructions are. You can then analyze the application's source code to identify the cause of the spinning thread. The cause will usually turn out to be a problem in the logic of a **while**, **do-while**, **goto**, or **for** loop.

 

 





