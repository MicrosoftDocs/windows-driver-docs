---
title: Get RPC Thread Information
description: Get RPC Thread Information
ms.assetid: 4cb8d11f-5b0a-4526-9f64-ee69fd15d1ba
keywords: ["RPC thread information"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Get RPC Thread Information


## <span id="ddk_get_rpc_thread_information_dbg"></span><span id="DDK_GET_RPC_THREAD_INFORMATION_DBG"></span>


Thread information is displayed by the **!rpcexts.getthreadinfo** extension, or by DbgRpc when the **-t** switch is used.

The PID of a process must be specified. You may specify a thread within that process as well. If the thread is omitted, all threads within that process will be displayed.

In the following example, the process ID is 0x278 and the thread ID is omitted:

```console
D:\wmsg>dbgrpc -t -P 278
Searching for thread info ...
## PID  CELL ID   ST TID      LASTTIME
-----------------------------------
0278 0000.0002 01 000001a4 00072c09
0278 0000.0005 03 0000031c 00072bf5
```

For details on the optional parameters, see [**DbgRpc Command-Line Options**](dbgrpc-command-line-options.md).

For a similar example using the RPC debugger extensions, see [**!rpcexts.getthreadinfo**](-rpcexts-getthreadinfo.md).

 

 





