---
title: Displaying RPC State Information
description: Displaying RPC State Information
ms.assetid: 9931cf62-a7c2-4270-8664-a77a82207aa9
keywords: ["RPC debugging, displaying RPC state information"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Displaying RPC State Information


## <span id="ddk_displaying_rpc_state_information_dbg"></span><span id="DDK_DISPLAYING_RPC_STATE_INFORMATION_DBG"></span>


All RPC run-time state information is contained in cells. A cell is the smallest unit of information that can be viewed and updated individually. Both the DbgRpc tool and the RPC debugger extensions allow you to view the contents of any given cell or to run high-level queries.

Each key object in the RPC Run-Time will maintain one or more cells of information about its state. Each cell has a cell ID. When an object refers to another object, it does so by specifying that object's cell ID.

The key objects that the RPC Run-Time can maintain information about are endpoints, threads, connection objects, Server Call (SCALL) objects, and Client Call (CCALL) objects. Server Call objects are usually referred to simply as *call objects*.

The RPC state information queries produce the same information whether you are using the DbgRpc tool or the RPC debugger extensions. The following sections describe how queries are used in each vehicle:

[Using the RPC Debugger Extensions](using-the-rpc-debugger-extensions.md)

[Using the DbgRpc Tool](using-the-dbgrpc-tool.md)

The most basic query simply displays an individual cell:

[Get RPC Cell Information](get-rpc-cell-information.md)

The following high-level queries are also available:

[Get RPC Endpoint Information](get-rpc-endpoint-information.md)

[Get RPC Thread Information](get-rpc-thread-information.md)

[Get RPC Call Information](get-rpc-call-information.md)

[Get RPC Client Call Information](get-rpc-client-call-information.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Displaying%20RPC%20State%20Information%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




