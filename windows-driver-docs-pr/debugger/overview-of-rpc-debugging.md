---
title: Overview of RPC Debugging
description: Overview of RPC Debugging
ms.assetid: 21db61fe-a4a1-45d3-9026-f58aecd3a3bc
keywords: ["RPC debugging, overview", "remote procedure call (RPC)"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Overview of RPC Debugging


## <span id="ddk_overview_of_rpc_debugging_dbg"></span><span id="DDK_OVERVIEW_OF_RPC_DEBUGGING_DBG"></span>


Microsoft Remote Procedure Call (RPC) makes it easy to cross process and machine boundaries and carry data around. This network programming standard is one reason that networking with Microsoft Windows is so powerful.

However, because RPC hides network calls from individual processes, it obscures the details of the interactions between the computers. This can make it hard to be sure why threads are doing what they are doing -- or fail to do what they are supposed to do. As a result, debugging and troubleshooting RPC errors can be difficult. In addition, the vast majority of problems that appear to be RPC errors are actually configuration issues, or network connectivity issues, or other component issues.

Debugging Tools for Windows contains a tool called DbgRpc, as well as RPC-related debugger extensions. These can be used to analyze a variety of RPC problems on Windows XP and later versions of Windows.

These Windows versions can be configured to save RPC run-time state information. Different amounts of state information can be saved; this allows you to obtain the information you need without placing a significant burden on your computer. See [Enabling RPC State Information](enabling-rpc-state-information.md) for details.

This information can then be accessed through either the debugger or the DbgRpc tool. In each case, a collection of queries is available. See [Displaying RPC State Information](displaying-rpc-state-information.md) for details.

In many cases, you can troubleshoot a problem by using the techniques outlined in [Common RPC Debugging Techniques](common-rpc-debugging-techniques.md).

If you want to explore the mechanics of how this information is stored, or if you want to devise your own techniques for state information analysis, see [RPC State Information Internals](rpc-state-information-internals.md).

These tools and techniques do not work on Windows 2000.

 

 





