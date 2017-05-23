---
title: Enabling RPC State Information
description: Enabling RPC State Information
ms.assetid: 8804d941-c241-44cb-8d91-05b94a875d94
keywords: ["RPC debugging, enabling RPC state information"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Enabling RPC State Information


## <span id="ddk_enabling_rpc_state_information_dbg"></span><span id="DDK_ENABLING_RPC_STATE_INFORMATION_DBG"></span>


Two different levels of RPC run-time state information can be gathered: **Server** information and **Full** information. This information gathering must be enabled before the debugger or DbgRpc can be used to analyze state information.

Only Windows XP and later versions of Windows support the gathering of RPC state information.

Gathering **Server** state information is very lightweight. It costs about 100 machine instructions per RPC call, resulting in no detectable load, even during performance tests. However, gathering this information does use memory (about 4KB per RPC server), so it is not recommended on a machine that is already experiencing memory pressure. **Server** information includes data about endpoints, threads, connection objects, and Server Call (SCALL) objects. This is sufficient to debug most RPC problems.

Gathering **Full** state information is more heavyweight. It includes all the information gathered at the **Server** level and, in addition, includes Client Call (CCALL) objects. **Full** state information is usually not needed.

To enable state information to be gathered on an individual machine, run the Group Policy Editor (Gpedit.msc). Under the Local Computer Policy, navigate to **Computer Configuration/Administrative Templates/System/Remote Procedure Call**. Under this node you will see the **RPC Troubleshooting State Information** item. When you edit its properties, you will see five possible states:

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None**  
No state information will be maintained. Unless your machine is experiencing memory pressure, this is not recommended.

<span id="Server"></span><span id="server"></span><span id="SERVER"></span>**Server**  
**Server** state information will be gathered. This is the recommended setting on a single computer.

<span id="Full"></span><span id="full"></span><span id="FULL"></span>**Full**  
**Full** state information will be gathered.

<span id="Auto1"></span><span id="auto1"></span><span id="AUTO1"></span>**Auto1**  
On a computer with less than 64 MB of RAM, this is the same as **None**. On a computer with at least 64 MB of RAM, this is the same as **Server**.

<span id="Auto2"></span><span id="auto2"></span><span id="AUTO2"></span>**Auto2**  
On a computer running Windows Server 2003 with less than 128 MB of RAM, or on any Windows XP computer, this is the same as **None**. On a Windows Server 2003 computer with at least 128 MB RAM, this is the same as **Server**.

This is the default.

If you want to simultaneously set these levels on a set of networked computers, use the Group Policy Editor to roll out a machine policy to the preferred set of machines. The policy engine will take care that the settings you want are propagated to the preferred set of machines. The **Auto1** and **Auto2** levels are especially useful in this case, because the operating system and amount of RAM on each computer may vary.

If the network includes computers running versions of Windows that are earlier than Windows XP, the settings will be ignored on those machines.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Enabling%20RPC%20State%20Information%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




