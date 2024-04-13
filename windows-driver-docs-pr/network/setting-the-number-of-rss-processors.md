---
title: Setting the Number of RSS Processors
description: Setting the Number of RSS Processors
keywords:
- processors WDK RSS
- CPU configuration WDK RSS
ms.date: 09/21/2020
---

# Setting the Number of RSS Processors

Administrators should set the number of receive side scaling (RSS) processors to help the overall performance of a computer. 

Concurrent deferred procedure calls (DPCs) that are running on multiple CPUs enable distributed receive processing and remove the CPU bottleneck (for example, in high-speed NICs). However, multiple DPCs do create additional overhead. The interrupt and DPC processing overhead increases as more processors are used for RSS. Therefore, when RSS is active, the total CPU utilization across all CPUs increases. An administrator should select the number of CPUs that are used for RSS to avoid a situation where using RSS leaves less processing power for applications to use and does not improve network throughput.

> [!NOTE]
> Starting in Windows 8 and Windows Server 2012, administrators can control many aspects of Network Adapters by using PowerShell cmdlets. Directly editing the registry is now discouraged.

The PowerShell cmdlet for setting the number of RSS CPUs is [Set-NetAdapterRss](/powershell/module/netadapter/Set-NetAdapterRss). 

The primary difference between using **Set-NetAdapterRss** and using the **MaxNumRssCpus** registry keyword is that PowerShell cmdlets operate on a per-Network Adapter basis while **MaxNumRssCpus** is global, meaning it applies to all Network Adapters. Generally, working with each Network Adapter separately is recommended because it offers more flexibility, granularity, and understandability in giving each Network Adapter its own configuration. However, administrators might still use the global **MaxNumRssCpus** key if they would like to apply a configuration to all current and all future Network Adapters at the same time.

For a complete list of Network Adapter cmdlets, see [Network Adapter Cmdlets in Windows PowerShell](/powershell/module/netadapter/).

In Microsoft Windows Server 2003 with the Scalable Networking Pack, administrators can set the maximum number of RSS CPUs with the **MaxNumRssCpus** registry keyword in **HKEY\_LOCAL\_MACHINE\\\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters**. The **MaxNumRssCpus** value is a DWORD type and, if it is not present, NDIS uses the default value of 4.

In Windows Server 2008, administrators can set the maximum number of RSS CPUs with the **MaxNumRssCpus** registry keyword in **HKEY\_LOCAL\_MACHINE\\\\SYSTEM\\CurrentControlSet\\Services\\Ndis\\Parameters**. The **MaxNumRssCpus** value is a DWORD type and, if it is not present, NDIS uses the default value of 4. This registry keyword also applies to later versions of Windows Server.

To avoid complicated cases (and unrealistic cases that are not implemented in actual hardware) where the number of available hardware receive queues is less than the number of RSS CPUs, administrators must not set the **MaxNumRssCpus** value to a value that is greater than 16.

The actual number of CPUs that are used for RSS is also limited by the total number of core processors that remain after the RSS base CPU number has been configured. For example, if the administrator sets the maximum number of RSS CPUs on a quad-core computer system to 6, the networking driver stack uses, at most, 4 CPUs for RSS. If the administrator also sets the RSS base CPU number to 1, the networking driver stack uses at most 3 CPUs (CPU numbers 1, 2, and 3).

 The number of CPUs that the computer uses for RSS is static and does not change at run time. Therefore, any changes to the **MaxNumRssCpus** registry value require a restart to take effect.
