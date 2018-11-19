---
title: Reserving Processors for Applications
description: Reserving Processors for Applications
ms.assetid: e09790e9-29a7-4ff6-a122-b4bd99de8bc7
keywords:
- CPU configuration WDK RSS
- reserving processors for applications WDK RSS
- processors WDK RSS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reserving Processors for Applications





The receive side scaling (RSS) interface enables an administrator to reserve a set of processors for applications to use. The administrator can reserve a set of processors starting at logical CPU number 0 and ending at a specified CPU number. The RSS *base CPU number* is the CPU number of the first CPU that RSS can use. RSS cannot use the CPUs that are numbered below the base CPU number. For example, on a quad-core system with hyper-threading turned off, if base CPU number is set to 1, processors 1, 2, and 3 can be used for RSS.

NDIS uses the default value of 0 for base CPU number, but an administrator can change this value. The RSS interface does not permit the administrator to reserve a non-contiguous, arbitrary subset of CPUs for applications to use.

In Microsoft Windows Server 2003 with the Scalable Networking Pack, administrators can set the base CPU number with the **RssBaseCpu** registry keyword in **HKEY\_LOCAL\_MACHINE\\\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters**. The **RssBaseCpu** value is a DWORD type and, if it is not present, NDIS uses the default value of 0.

In Windows Server 2008, administrators can set the base CPU number with the **RssBaseCpu** registry keyword in **HKEY\_LOCAL\_MACHINE\\\\SYSTEM\\CurrentControlSet\\Services\\NDIS\\Parameters**. The **RssBaseCpu** value is a DWORD type and, if it is not present, NDIS uses the default value of 0. This registry keyword also applies to later versions of Windows Server.

**Note** Starting in Windows 8 and Windows Server 2012, administrators can control many aspects of Network Adapters by using PowerShell cmdlets. Directly editing the registry is now discouraged.

The PowerShell cmdlet for reserving RSS CPUs is [Set-NetAdapterRss](https://technet.microsoft.com/library/jj130863). The primary difference between using **Set-NetAdapterRss** and using **RssBaseCpu** is that PowerShell cmdlets operate on a per-Network Adapter basis while **RssBaseCpu** is global, meaning it applies to all Network Adapters. Generally, working with each Network Adapter separately is recommended because it offers more flexibility, granularity, and understandability in giving each Network Adapter its own configuration. However, administrators might still use the global **RssBaseCpu** key if they would like to apply a configuration to all current and all future Network Adapters at the same time.

For a complete list of Network Adapter cmdlets, see [Network Adapter Cmdlets in Windows PowerShell](https://technet.microsoft.com/library/jj134956).

 

 





