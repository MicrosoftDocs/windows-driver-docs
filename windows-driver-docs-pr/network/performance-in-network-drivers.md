---
title: Performance in network drivers
description: This section describes techniques to improve performance in network drivers
ms.assetid: 7EA23AA6-7673-4D88-91CA-BDDD8FBB2A4F
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Performance in Network Drivers


-   [Minimizing send and receive path length](#minimizing-send-and-receive-path-length)
-   [Partitioning data and code to minimize sharing across processors](#partitioning-data-and-code-to-minimize-sharing-across-processors)
-   [Avoiding false sharing](#avoiding-false-sharing)
-   [Using locking mechanisms properly](#using-locking-mechanisms-properly)
-   [Using 64-bit DMA](#using-64-bit-dma)
-   [Ensuring proper buffer alignment](#ensuring-proper-buffer-alignment)
-   [Using Scatter-Gather DMA](#using-scatter-gather-dma)
-   [Supporting Receive Side Throttle](#supporting-receive-side-throttle)

## Minimizing send and receive path length


Although the send and receive paths differ from driver to driver, there are some general rules for performance optimizations:

-   Optimize for the common paths. The Kernprof.exe tool is provided with the developer and IDW builds of Windows that extracts the needed information. The developer should look at the routines that consume the most CPU cycles and attempt to reduce the frequency of these routines being called or the time spent in these routines.

-   Reduce time spent in DPC so that the network adapter driver does not use excessive system resources, which would cause overall system performance to suffer.

-   Make sure that debugging code is not compiled into the final released version of the driver; this avoids executing excess code.

## Partitioning data and code to minimize sharing across processors


Partitioning is needed to minimize shared data and code across processors. Partitioning helps reduce system bus utilization and improves the effectiveness of processor cache. To minimize sharing, driver writers should consider the following:

-   Implement the driver as a deserialized miniport as described in [Deserialized NDIS Miniport Drivers](deserialized-ndis-miniport-drivers.md).

-   Use per-processor data structures to reduce global and shared data access. This allows you to keep statistic counters without synchronization, which reduces the code path length and increases performance. For vital statistics, have per-processor counters that are added together at query time. If you must have a global counter, use interlocked operations instead of spin locks to manipulate the counter. See Using Locking Mechanisms Properly below for information about how to avoid using spin locks.

    To facilitate this, [**KeGetCurrentProcessorNumberEx**](https://msdn.microsoft.com/library/windows/hardware/ff552076) can be used to determine the current processor. To determine the number of processors when allocating per-processor data structures, [**KeQueryGroupAffinity**](https://msdn.microsoft.com/library/windows/hardware/ff553007) can be used.

    The total number of bits set in the affinity mask indicates the number of active processors in the system. Drivers should not assume that all the set bits in the mask will be contiguous because the processors might not be consecutively numbered in the future releases of the operating system. The number of processors in an SMP machine is a zero-based value.

    If your driver maintains per-processor data, you can use the [**KeQueryGroupAffinity**](https://msdn.microsoft.com/library/windows/hardware/ff553007) function to reduce cache-line contention.

## Avoiding false sharing


False sharing occurs when processors request shared variables that are independent from each other. However, because the variables are on the same cache line, they are shared among the processors. In such situations, the cache line will travel back and forth between processors for every access to any of the variables in it, causing an increase in cache flushes and reloads. This increases the system bus utilization and reduces overall system performance.

To avoid false sharing, align important data structures (such as spin locks, buffer queue headers, singly linked lists) to cache-line boundaries by using [**NdisGetSharedDataAlignment**](https://msdn.microsoft.com/library/windows/hardware/ff562671).

## Using locking mechanisms properly


Spin locks can reduce performance if not used properly. Drivers should minimize their use of spin locks by using interlocked operations wherever possible. However, in some cases, a spin lock might be the best choice for some purposes. For example, if a driver acquires a spin lock while handling the reference count for the number of packets that have not been indicated back to the driver, it is not necessary to use an interlocked operation. For more information, see [Synchronization and Notification in Network Drivers](synchronization-and-notification-in-network-drivers.md).

Here are some tips for using locking mechanisms effectively:

-   Use NDIS singly-linked list functions such as the following for managing resource pools:

    [**NdisInitializeSListHead**](https://msdn.microsoft.com/library/windows/hardware/ff562739)

    [**NdisInterlockedPushEntrySList**](https://msdn.microsoft.com/library/windows/hardware/ff562764)

    [**NdisInterlockedPopEntrySList**](https://msdn.microsoft.com/library/windows/hardware/ff562760)

    [**NdisQueryDepthSList**](https://msdn.microsoft.com/library/windows/hardware/ff563753)

-   If you need to use spin locks, use them to only protect data, not code. Don't use one lock to protect all data used in common paths. For example, separate the data used in the send and receive paths into two data structures so that when the send path needs to lock its data, the receive path is not affected.

-   If you are using spin locks and the path is already at DPC level, use the [**NdisDprAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff561749) and [**NdisDprReleaseSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff561753) functions to avoid extra code when acquiring and releasing the locks.

-   To minimize the number of spin lock acquires and releases, use these NDIS RWLock functions:

    [**NdisAllocateRWLock**](https://msdn.microsoft.com/library/windows/hardware/ff561615)

    [**NdisAcquireRWLockRead**](https://msdn.microsoft.com/library/windows/hardware/ff560697)

    [**NdisAcquireRWLockWrite**](https://msdn.microsoft.com/library/windows/hardware/ff560698)

    [**NdisReleaseRWLock**](https://msdn.microsoft.com/library/windows/hardware/ff564523)

## Using 64-bit DMA


64-Bit DMA If the network adapter supports 64-bit DMA, steps must be taken to avoid extra copies for addresses above the 4 GB range. When the driver calls [**NdisMRegisterScatterGatherDma**](https://msdn.microsoft.com/library/windows/hardware/ff563659), the **NDIS\_SG\_DMA\_64\_BIT\_ADDRESS** flag must be set in the *Flags* parameter.

## Ensuring proper buffer alignment


Buffer alignment on a cache-line boundary improves performance when copying data from one buffer to another. Most network adapter receive buffers are properly aligned when they are first allocated, but the user data that must eventually be copied into the application buffer is misaligned due to the header space consumed. In the case of TCP data (the most common scenario), the shift due to the TCP, IP and Ethernet headers results in a shift of 0x36 bytes. To resolve this problem, we recommend that drivers allocate a slightly larger buffer and insert packet data at an offset of 0xA bytes. This will ensure that, after the buffers are shifted by 0x36 bytes for the header, the user data is properly aligned. For more information about cache-line boundaries, see the Remarks section for [**NdisMAllocateSharedMemory**](https://msdn.microsoft.com/library/windows/hardware/ff562782).

## Using Scatter-Gather DMA


[NDIS Scatter/Gather DMA](ndis-scatter-gather-dma.md) provides the hardware with support to transfer data to and from noncontiguous ranges of physical memory. Scatter-Gather DMA uses a [**SCATTER\_GATHER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff563664) structure, which includes an array of **SCATTER\_GATHER\_ELEMENT** structures and the number of elements in the array. This structure is retrieved from the packet descriptor passed to the driver's send function. Each element of the array provides the length and starting physical address of a physically contiguous Scatter-Gather region. The driver uses the length and address information for transferring the data.

Using the Scatter-Gather routines for DMA operations can improve utilization of system resources by not locking these resources down statically, as would occur if map registers were used. For more information, see [NDIS Scatter/Gather DMA](ndis-scatter-gather-dma.md).

If the network adapter supports TCP Segmentation Offload (Large Send Offload), then the driver will need to pass in the maximum buffer size it can get from TCP/IP into the *MaximumPhysicalMapping* parameter within [**NdisMRegisterScatterGatherDma**](https://msdn.microsoft.com/library/windows/hardware/ff563659) function. This will guarantee that the driver has enough map registers to build the Scatter-Gather list and eliminate any possible buffer allocations and copying. For more information, see these topics:

- [Determining Task Offload Capabilities](determining-task-offload-capabilities.md)
- [Offloading the Segmentation of Large TCP Packets](offloading-the-segmentation-of-large-tcp-packets.md)

## Supporting Receive Side Throttle


To minimize disruptions during media playback in multimedia applications, NDIS 6.20 and later drivers must support Receive Side Throttle (RST) in processing receive interrupts. For more information, see:

[Receive Side Throttle in NDIS 6.20](receive-side-throttle-in-ndis-6-20.md)
"Send and Receive Code Paths" in [Summary of Changes Required to Port a Miniport Driver to NDIS 6.20](summary-of-changes-required-to-port-a-miniport-driver-to-ndis-6-20.md)
 

 





