---
title: Bug Check 0x4D NO_PAGES_AVAILABLE
description: The NO_PAGES_AVAILABLE bug check has a value of 0x0000004D. This indicates that no free pages are available to continue operations.
keywords: ["Bug Check 0x4D NO_PAGES_AVAILABLE", "NO_PAGES_AVAILABLE"]
ms.date: 12/27/2018
topic_type:
- apiref
api_name:
- NO_PAGES_AVAILABLE
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x4D: NO\_PAGES\_AVAILABLE


The NO\_PAGES\_AVAILABLE bug check has a value of 0x0000004D. This indicates that no free pages are available to continue operations.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## NO\_PAGES\_AVAILABLE Parameters

|Parameter|Description|
|--- |--- |
|1|The total number of dirty pages|
|2|The number of dirty pages destined for the page file|
|3|The size of the nonpaged pool available at the time the bug check occurred|
|4|The most recent modified write error status.|


## Cause

To see general memory statistics, use the [**!vm 3**](-vm.md) extension.

This bug check can occur for any of the following reasons:

-   A driver has blocked, deadlocking the modified or mapped page writers. Examples of this include mutex deadlocks or accesses to paged out memory in file system drivers or filter drivers. This indicates a driver bug.

    If Parameter 1 or Parameter 2 is large, then this is a possibility. Use [**!vm 3**](-vm.md).

-   A storage driver is not processing requests. Examples of this are stranded queues and non-responding drives. This indicates a driver bug.

    If Parameter 1 or Parameter 2 is large, then this is a possibility. Use [**!vm 8**](-vm.md), followed by [**!process 0 7**](-process.md).

-   A high-priority realtime thread has starved the balance set manager from trimming pages from the working set, or starved the modified page writer from writing them out. This indicates a bug in the component that created this thread.

    This situation is difficult to analyze. Try using [**!ready**](-ready.md). Try also [**!process 0 7**](-process.md) to list all threads and see if any have accumulated excessive kernel time as well as what their current priorities are. Such processes may have blocked out the memory management threads from making pages available.

-  Not enough pool is available for the storage stack to write out modified pages. This indicates a driver bug.

    If Parameter 3 is small, then this is a possibility. Use [**!vm**](-vm.md) and [**!poolused 2**](-poolused.md).

If the problem cannot be found, then try booting with a kernel debugger attached from the beginning, and monitor the situation.

 

 




