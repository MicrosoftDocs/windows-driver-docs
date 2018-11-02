---
title: Displaying RPC State Information
description: Displaying RPC State Information
ms.assetid: 9931cf62-a7c2-4270-8664-a77a82207aa9
keywords: ["RPC debugging, displaying RPC state information"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
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

 

 





