---
title: Overview of RPC Debugging
description: Overview of RPC Debugging
ms.assetid: 21db61fe-a4a1-45d3-9026-f58aecd3a3bc
keywords: ["RPC debugging, overview", "remote procedure call (RPC)"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Overview%20of%20RPC%20Debugging%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




