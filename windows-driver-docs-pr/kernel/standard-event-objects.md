---
title: Standard Event Objects
description: Standard Event Objects
ms.assetid: 3c34c485-28b1-45d5-9e79-05dd2b26015e
keywords: ["event objects WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Standard Event Objects





The system provides several standard event objects. Drivers can use these event objects to be notified by the system whenever certain conditions occur. The following list contains the standard event objects:

<a href="" id="-kernelobjects-highmemorycondition"></a>**\\KernelObjects\\HighMemoryCondition**  
This event is set whenever the amount of free physical memory exceeds a system-defined amount. Drivers can wait for this event to be set as a signal to aggressively allocate memory.

<a href="" id="-kernelobjects-lowmemorycondition"></a>**\\KernelObjects\\LowMemoryCondition**  
This event is set whenever the amount of free physical memory falls below a system-defined amount. Drivers that have allocated large amounts of memory can wait for this event to be set as a signal to free unused memory.

For Microsoft Windows Server 2003 and later versions of Windows, drivers can also use the following additional standard event objects:

<a href="" id="-kernelobjects-highpagedpoolcondition"></a>**\\KernelObjects\\HighPagedPoolCondition**  
This event is set whenever the amount of free paged pool exceeds a system-defined amount. Drivers can wait for this event to be set as a signal to aggressively allocate memory from paged pool.

<a href="" id="-kernelobjects-lowpagedpoolcondition"></a>**\\KernelObjects\\LowPagedPoolCondition**  
This event is set whenever the amount of free paged pool falls below a system-defined amount. Drivers that have allocated large amounts of memory can wait for this event to be set as a signal to free unused memory from paged pool.

<a href="" id="-kernelobjects-highnonpagedpoolcondition"></a>**\\KernelObjects\\HighNonPagedPoolCondition**  
This event is set whenever the amount of free nonpaged pool exceeds a system-defined amount. Drivers can wait for this event to be set as a signal to aggressively allocate memory from nonpaged pool.

<a href="" id="-kernelobjects-lownonpagedpoolcondition"></a>**\\KernelObjects\\LowNonPagedPoolCondition**  
This event is set whenever the amount of free nonpaged pool falls below a system-defined amount. Drivers that have allocated large amounts of memory can wait for this event to be set as a signal to free unused memory from nonpaged pool.

For Windows Vista and later versions of Windows, drivers can also use the following additional standard event objects:

<a href="" id="-kernelobjects-lowcommitcondition"></a>**\\KernelObjects\\LowCommitCondition**  
This event is set when the operating system's [*commit charge*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-commit-charge) is low, relative to the [*current commit limit*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-current-commit-limit). In other words, memory usage is low and a lot of space is available in physical memory or paging files.

<a href="" id="-kernelobjects-highcommitcondition"></a>**\\KernelObjects\\HighCommitCondition**  
This event is set when the operating system's commit charge is high, relative to the current commit limit. In other words, memory usage is high and very little space is available in physical memory or paging files, but the operating system might be able to increase the size of its paging files.

<a href="" id="-kernelobjects-maximumcommitcondition"></a>**\\KernelObjects\\MaximumCommitCondition**  
This event is set when the operating system's commit charge is near the [*maximum commit limit*](https://msdn.microsoft.com/library/windows/hardware/ff556308#wdkgloss-maximum-commit-limit). In other words, memory usage is very high, very little space is available in physical memory or paging files, and the operating system cannot increase the size of its paging files. (A system administrator can always increase the size or number of paging files, without restarting the computer, if sufficient storage resources exist.)

Each of these events are notification events. They remain set as long as the triggering condition remains true.

To open a handle to any of these events, use the [**IoCreateNotificationEvent**](https://msdn.microsoft.com/library/windows/hardware/ff549039) routine. A driver that waits for any of these events should create a dedicated thread to do the waiting. The thread can wait for one or more of these events by calling either [**KeWaitForSingleObject**](https://msdn.microsoft.com/library/windows/hardware/ff553350) or [**KeWaitForMultipleObjects**](https://msdn.microsoft.com/library/windows/hardware/ff553324).

 

 




