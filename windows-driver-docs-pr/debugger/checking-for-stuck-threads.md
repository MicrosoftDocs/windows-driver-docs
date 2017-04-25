---
title: Checking for Stuck Threads
description: Checking for Stuck Threads
ms.assetid: ffb1ff13-fc4c-4aaf-a8fe-b473b51b9db0
keywords: ["RPC debugging, stuck threads"]
---

# Checking for Stuck Threads


## <span id="ddk_checking_for_stuck_threads_dbg"></span><span id="DDK_CHECKING_FOR_STUCK_THREADS_DBG"></span>


RPC needs its worker threads available in order to perform normally. A common problem is that some component in the same process will deadlock while holding one of the global critical sections (for example, loader lock or heap lock). This will cause many threads to hang -- very possibly including some RPC worker threads.

If this occurs, the RPC server will not respond to the outside world. RPC calls to it will return RPC\_S\_SERVER\_UNAVAILABLE or RPC\_S\_SERVER\_TOO\_BUSY.

A similar problem can result if a faulty driver prevents IRPs from completing and reaching the RPC server.

If you suspect that one of these problems may be occurring, use DbgRpc with the **-t** switch (or use the [**!rpcexts.getthreadinfo**](https://msdn.microsoft.com/library/windows/hardware/ff564861) extension). The process ID should be used as a parameter. In the following example, assume the process ID is 0xC4:

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

The TID column gives the thread ID for each thread. The LASTTIME column contains the time stamp of the last change in state for each thread.

Whenever the server receives a request, at least one thread will change state, and its time stamp will be updated. Therefore, if an RPC request is made to the server and the request fails but none of the time stamps change, this indicates that the request is not actually reaching the RPC Run-Time. You should investigate the cause of this.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Checking%20for%20Stuck%20Threads%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




