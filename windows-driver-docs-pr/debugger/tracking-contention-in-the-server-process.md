---
title: Tracking Contention in the Server Process
description: Tracking Contention in the Server Process
ms.assetid: ef0c0294-a010-439b-82dd-25148e05a7f1
keywords: ["RPC debugging, tracking contention"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Tracking Contention in the Server Process


## <span id="ddk_tracking_contention_in_the_server_process_dbg"></span><span id="DDK_TRACKING_CONTENTION_IN_THE_SERVER_PROCESS_DBG"></span>


In order to service incoming requests, RPC will maintain a set of worker threads. Ideally, the number of threads will be small. However, this ideal situation has only been seen in lab environments, where the server manager routines are carefully tuned. In a real situation, the number of threads will vary depending on server workload, but it can be anywhere from 1 to 50.

If the number of worker threads is above 50, you may have excessive contention in the server process. Common causes of this are indiscriminate use of the heap, memory pressure, or serializing most activities in a server through a single critical section.

To see the number of threads in a given server process, use the [**!rpcexts.getthreadinfo**](-rpcexts-getthreadinfo.md) extension, or use DbgRpc with the **-t** switch. Supply the process ID (in the following example, 0xC4):

```console
D:\wmsg>dbgrpc -t -P c4
Searching for thread info ...
## PID  CELL ID   ST TID      LASTTIME
-----------------------------------
00c4 0000.0004 03 0000011c 000f164f
00c4 0000.0007 03 00000120 008a6290
00c4 0000.0015 03 0000018c 008a6236
00c4 0000.0026 03 00000264 0005c443
00c4 0000.002d 03 00000268 000265bb
00c4 0000.0030 03 0000026c 000f1d32
00c4 0000.0034 03 00000388 007251e9
```

In this case, there are only seven worker threads, which is reasonable.

If there are over 100 threads, a debugger should be attached to this process and the cause investigated.

**Note**   Running queries such as **dbgrpc -t** remotely is expensive to the server and the network. If you use this query in a script, you should make sure this command is not run too often.

 

 

 





