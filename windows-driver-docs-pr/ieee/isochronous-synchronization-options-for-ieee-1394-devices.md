---
title: Isochronous Synchronization Options for IEEE 1394 Devices
description: Isochronous Synchronization Options for IEEE 1394 Devices
ms.assetid: 27137890-09e7-45d5-b268-7e93c943b489
keywords:
- isochronous I/O WDK IEEE 1394 bus , synchronization
- synchronization WDK IEEE 1394 bus
- filtering WDK IEEE 1394 bus
- cycle time synchronization WDK IEEE 1394 bus
- buffers WDK IEEE 1394 bus
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Isochronous Synchronization Options for IEEE 1394 Devices





The IEEE 1394 driver stack supports certain types of synchronization and filtering during [**REQUEST\_ISOCH\_LISTEN**](https://msdn.microsoft.com/library/windows/hardware/ff537655) and [**REQUEST\_ISOCH\_TALK**](https://msdn.microsoft.com/library/windows/hardware/ff537660) operations.

A driver can initiate filtering by setting the DESCRIPTOR\_SYNCH\_ON\_SY or DESCRIPTOR\_SYNCH\_ON\_TAG flag in the **fulFlags** member of a buffer's [**ISOCH\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff537401) structure. Beginning with the data that is destined for that buffer, the bus driver removes all packets from the data stream that do not have Sy or Tag values that match the Sy or Tag values indicated in the isoch descriptor. This filtering continues with the buffers that follow, even if neither one of the DESCRIPTOR\_SYNCH\_ON\_SY and DESCRIPTOR\_SYNCH\_ON\_TAG flags are set in the isoch descriptors of those buffers.

If, in addition to setting the DESCRIPTOR\_SYNCH\_ON\_SY or DESCRIPTOR\_SYNCH\_ON\_TAG flags, the client driver also sets the DESCRIPTOR\_USE\_SY\_TAG\_IN\_FIRST flag, the bus driver will use the Sy or Tag value that is provided by the client driver in the isoch descriptor to synchronize the data flow. In this case, the bus driver discards all data packets until it receives one whose Sy or Tag value matches the value that is indicated in the isoch descriptor. Upon finding a match, the bus driver ceases discarding packets and resumes forwarding *all* packets to the client driver.

If the host controller supports it, a client driver can use cycle times to synchronize an isochronous data stream. A "cycle time" in this context is defined by the [**CYCLE\_TIME**](https://msdn.microsoft.com/library/windows/hardware/ff537067) structure. It includes a second count, **CL\_SecondCount**, that wraps every 128 seconds, a cycle count, **CL\_CycleCount**, that indicates the number of isochronous cycles that have elapsed within the current second, and a clock-ticks count, **CL\_CycleOffset**, that indicates the number of IEEE 1394 bus clock ticks that have elapsed within the current cycle.

A client can either initiate a synchronization operation in a particular buffer, or it can synchronize the entire data stream on a certain cycle time.

To initiate a synchronization operation in a particular buffer, the client driver must set the DESCRIPTOR\_SYNCH\_ON\_TIME flag in the **fulFlags** member of an isoch descriptor for that buffer. It must also initialize the **CycleTime** member of the descriptor with the cycle time that will be used to synchronize the data stream. After the bus driver examines the isoch descriptor, it will initiate the synchronization operation using the indicated cycle time. The bus driver discards all packets that do not have the indicated cycle time, and resumes delivering packets once it finds a packet with the correct cycle time.

To synchronize the entire data stream on a certain cycle time, client drivers must configure a channel, so that all requests that are initiated on the channel will automatically synchronize the data stream using the indicated cycle time. This provides an alternative to triggering the synchronization based on the cycle time settings of a particular isoch descriptor. To configure a channel in this manner, the client driver must take two steps:

1.  When the client allocates a resource handle for the channel with a [**REQUEST\_ISOCH\_ALLOCATE\_RESOURCES**](https://msdn.microsoft.com/library/windows/hardware/ff537649) request, it must set the RESOURCE\_SYNCH\_ON\_TIME flag in the **fulFlags** member of the IRB.

2.  When the client requests a listen or talk operation on a channel, it specifies the cycle time that will be used to synchronize the data stream in the **StartTime** member of the IRB. For more information about listen and talk requests, see [**REQUEST\_ISOCH\_LISTEN**](https://msdn.microsoft.com/library/windows/hardware/ff537655) and [**REQUEST\_ISOCH\_TALK**](https://msdn.microsoft.com/library/windows/hardware/ff537660).

To determine if the host controller supports synchronization on cycle times, the client driver should send a [**REQUEST\_GET\_LOCAL\_HOST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff537644) request to the bus driver, with the **nLevel** member of the IRB set to 2. The bus driver returns a [**GET\_LOCAL\_HOST\_INFO2**](https://msdn.microsoft.com/library/windows/hardware/ff537147) structure in response to this request. If the bus driver sets the HOST\_INFO\_SUPPORTS\_START\_ON\_CYCLE flag in the **HostCapabilities** member of GET\_LOCAL\_HOST\_INFO2, this indicates that the host controller supports the synchronization of isochronous operations using cycle times.

 

 




