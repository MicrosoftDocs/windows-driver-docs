---
title: Get RPC Cell Information
description: Get RPC Cell Information
ms.assetid: 7dd5e77e-914d-4b00-90c5-92705eebf436
keywords: ["RPC cell information"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Get RPC Cell Information


## <span id="ddk_get_rpc_cell_information_dbg"></span><span id="DDK_GET_RPC_CELL_INFORMATION_DBG"></span>


Detailed cell information is displayed by the **!rpcexts.getdbgcell** extension, or by DbgRpc when the **-l** switch is used.

The process ID of the process that contains the preferred cell must be specified, as well as the cell number.

In the following example, the process ID is 0x278, and the cell number is 0000.0002:

```
D:\wmsg>dbgrpc -l -P 278 -L 0.2
Getting cell info ...
Thread
Status: Dispatched
Thread ID: 0x1A4 (420)
Last update time (in seconds since boot):470.25 (0x1D6.19)
```

For details on the optional parameters, see [**DbgRpc Command-Line Options**](dbgrpc-command-line-options.md).

For a similar example using the RPC debugger extensions, see [**!rpcexts.getdbgcell**](-rpcexts-getdbgcell.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Get%20RPC%20Cell%20Information%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




