---
title: Get RPC Thread Information
description: Get RPC Thread Information
ms.assetid: 4cb8d11f-5b0a-4526-9f64-ee69fd15d1ba
keywords: ["RPC thread information"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Get RPC Thread Information


## <span id="ddk_get_rpc_thread_information_dbg"></span><span id="DDK_GET_RPC_THREAD_INFORMATION_DBG"></span>


Thread information is displayed by the **!rpcexts.getthreadinfo** extension, or by DbgRpc when the **-t** switch is used.

The PID of a process must be specified. You may specify a thread within that process as well. If the thread is omitted, all threads within that process will be displayed.

In the following example, the process ID is 0x278 and the thread ID is omitted:

```
D:\wmsg>dbgrpc -t -P 278
Searching for thread info ...
## PID  CELL ID   ST TID      LASTTIME
-----------------------------------
0278 0000.0002 01 000001a4 00072c09
0278 0000.0005 03 0000031c 00072bf5
```

For details on the optional parameters, see [**DbgRpc Command-Line Options**](dbgrpc-command-line-options.md).

For a similar example using the RPC debugger extensions, see [**!rpcexts.getthreadinfo**](-rpcexts-getthreadinfo.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Get%20RPC%20Thread%20Information%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




