---
title: Set the Number of RSS Processors for Improved Performance
description: Learn how to set the number of receive side scaling (RSS) processors to optimize network performance. Improve throughput and efficiency—read more.
ms.date: 05/22/2025
ms.topic: concept-article
---

# Set the number of RSS processors

Set the number of receive side scaling (RSS) processors to optimize your computer’s network performance. This article explains how setting RSS processors improves throughput and efficiency.

Concurrent deferred procedure calls (DPCs) running on multiple CPUs let you distribute receive processing and remove the CPU bottleneck (for example, in high-speed NICs). However, using multiple DPCs creates additional overhead. Interrupt and DPC processing overhead increases as you use more processors for RSS. When RSS is active, total CPU utilization across all CPUs increases. Select the number of CPUs for RSS to avoid using too much processing power for RSS and not improving network throughput.

> [!NOTE]
> Starting in Windows 8 and Windows Server 2012, administrators can control many aspects of Network Adapters by using PowerShell cmdlets. Directly editing the registry is now discouraged.

## Differences between PowerShell and registry configuration

The PowerShell cmdlet for setting the number of RSS CPUs is [Set-NetAdapterRss](/powershell/module/netadapter/Set-NetAdapterRss).

Use the [Set-NetAdapterRss](/powershell/module/netadapter/Set-NetAdapterRss) PowerShell cmdlet to set the number of RSS CPUs.

The main difference between using **Set-NetAdapterRss** and the **MaxNumRssCpus** registry keyword is that PowerShell cmdlets work on each network adapter, while **MaxNumRssCpus** is global and applies to all network adapters. Setting each network adapter separately gives you more flexibility, granularity, and makes configurations easier to understand. You can use the global **MaxNumRssCpus** key if you want to apply a configuration to all current and future network adapters at the same time.

For a complete list of Network Adapter cmdlets, see [Network Adapter Cmdlets in Windows PowerShell](/powershell/module/netadapter/).

## Registry settings for RSS processors

In Microsoft Windows Server 2003 with the Scalable Networking Pack, set the maximum number of RSS CPUs with the **MaxNumRssCpus** registry keyword in **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters**. The **MaxNumRssCpus** value is a DWORD type. If it's not present, NDIS uses the default value of 4.

In Windows Server 2008, set the maximum number of RSS CPUs with the **MaxNumRssCpus** registry keyword in **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Ndis\\Parameters**. The **MaxNumRssCpus** value is a DWORD type. If it's not present, NDIS uses the default value of 4. This registry keyword also applies to later versions of Windows Server.

## Best practices for configuring RSS processors

To avoid complicated and unrealistic cases where the number of available hardware receive queues is less than the number of RSS CPUs, don't set the **MaxNumRssCpus** value higher than 16.

The number of CPUs used for RSS is also limited by the total number of core processors left after you set the RSS base CPU number. For example, if you set the maximum number of RSS CPUs on a quad-core computer to 6, the networking driver stack uses at most 4 CPUs for RSS. If you also set the RSS base CPU number to 1, the networking driver stack uses at most 3 CPUs (CPU numbers 1, 2, and 3).

The number of CPUs the computer uses for RSS is static and doesn't change at run time. If you change the **MaxNumRssCpus** registry value, restart the computer for the change to take effect.
