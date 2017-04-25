---
title: Tracking Contention in the Server Process
description: Tracking Contention in the Server Process
ms.assetid: ef0c0294-a010-439b-82dd-25148e05a7f1
keywords: ["RPC debugging, tracking contention"]
---

# Tracking Contention in the Server Process


## <span id="ddk_tracking_contention_in_the_server_process_dbg"></span><span id="DDK_TRACKING_CONTENTION_IN_THE_SERVER_PROCESS_DBG"></span>


In order to service incoming requests, RPC will maintain a set of worker threads. Ideally, the number of threads will be small. However, this ideal situation has only been seen in lab environments, where the server manager routines are carefully tuned. In a real situation, the number of threads will vary depending on server workload, but it can be anywhere from 1 to 50.

If the number of worker threads is above 50, you may have excessive contention in the server process. Common causes of this are indiscriminate use of the heap, memory pressure, or serializing most activities in a server through a single critical section.

To see the number of threads in a given server process, use the [**!rpcexts.getthreadinfo**](https://msdn.microsoft.com/library/windows/hardware/ff564861) extension, or use DbgRpc with the **-t** switch. Supply the process ID (in the following example, 0xC4):

```
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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Tracking%20Contention%20in%20the%20Server%20Process%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




