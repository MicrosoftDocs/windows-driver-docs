---
title: Isochronous Synchronization Options for IEEE 1394 Devices
author: windows-driver-content
description: Isochronous Synchronization Options for IEEE 1394 Devices
MS-HAID:
- '1394-isoch\_ab4493be-72bf-4d38-b4b0-e24b377b81d7.xml'
- 'IEEE.isochronous\_synchronization\_options\_for\_ieee\_1394\_devices'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 27137890-09e7-45d5-b268-7e93c943b489
keywords: ["isochronous I/O WDK IEEE 1394 bus , synchronization", "synchronization WDK IEEE 1394 bus", "filtering WDK IEEE 1394 bus", "cycle time synchronization WDK IEEE 1394 bus", "buffers WDK IEEE 1394 bus"]
---

# Isochronous Synchronization Options for IEEE 1394 Devices


## <a href="" id="ddk-isochronous-synchronization-options-for-ieee-1394-devices-kg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5BIEEE\buses%5D:%20Isochronous%20Synchronization%20Options%20for%20IEEE%201394%20Devices%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


