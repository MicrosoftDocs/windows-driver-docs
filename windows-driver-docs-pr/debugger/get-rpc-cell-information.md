---
title: Get RPC Cell Information
description: Get RPC Cell Information
ms.assetid: 7dd5e77e-914d-4b00-90c5-92705eebf436
keywords: ["RPC cell information"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Get RPC Cell Information


## <span id="ddk_get_rpc_cell_information_dbg"></span><span id="DDK_GET_RPC_CELL_INFORMATION_DBG"></span>


Detailed cell information is displayed by the **!rpcexts.getdbgcell** extension, or by DbgRpc when the **-l** switch is used.

The process ID of the process that contains the preferred cell must be specified, as well as the cell number.

In the following example, the process ID is 0x278, and the cell number is 0000.0002:

```console
D:\wmsg>dbgrpc -l -P 278 -L 0.2
Getting cell info ...
Thread
Status: Dispatched
Thread ID: 0x1A4 (420)
Last update time (in seconds since boot):470.25 (0x1D6.19)
```

For details on the optional parameters, see [**DbgRpc Command-Line Options**](dbgrpc-command-line-options.md).

For a similar example using the RPC debugger extensions, see [**!rpcexts.getdbgcell**](-rpcexts-getdbgcell.md).

 

 





