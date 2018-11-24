---
title: Intermediate Driver Network Data Management
description: Intermediate Driver Network Data Management
ms.assetid: 12f708b9-32f2-470c-bc4d-7c1b0c1012b1
keywords:
- intermediate drivers WDK networking , network data management
- NDIS intermediate drivers WDK , network data management
- network data management WDK NDIS intermediate
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Intermediate Driver Network Data Management





An intermediate driver receives [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures with one or more associated MDLs from a higher-level driver to send over the network. The intermediate driver can pass the data through to the underlying driver by calling [**NdisSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff564535) if the driver has a connectionless lower edge, or by calling [**NdisCoSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff561728) if the driver has a connection-oriented lower edge. Alternatively, the intermediate driver can take some actions to modify either the contents of the chained buffers or the ordering or timing of the incoming data relative to other transmissions.

Depending on the purpose of the intermediate driver, such a driver can repackage buffers that are chained to incoming NET\_BUFFER\_LIST structures. For example, an intermediate driver repackages network data in the following circumstances:

-   The intermediate driver receives a larger data buffer from an overlying protocol driver than can be sent in a single buffer over the underlying medium. Consequently, the intermediate driver must divide the incoming data into smaller buffers.

-   The intermediate driver changes the length or content of the network data by compressing or encrypting the data before forwarding each send to the underlying driver.

For information about creating network data management, see [Protocol Driver Buffer Management](protocol-driver-buffer-management.md).

NDIS provides interfaces to clone and fragment [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures. For more information about cloning and fragmenting structures, see [Derived NET\_BUFFER\_LIST Structures](derived-net-buffer-list-structures.md).

NET\_BUFFER\_LIST structures can be allocated as needed, at driver initialization time, or in the [*ProtocolBindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570220) function. An intermediate driver developer can, if necessary and for performance reasons, allocate a number of structures at initialization time so that [**ProtocolReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff570267) has preallocated resources into which to copy incoming data for indicating to a higher-level driver, and so that [*MiniportSendNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff559440) has available [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures (and possibly buffers) to pass incoming send network data on to the next lower driver.

If an intermediate driver copies send data or received data to a new buffer or buffers, and the length of actual data in the last buffer is less than the allocated length of the buffer, the intermediate driver can call **NdisAdjustMdlLength** to adjust the buffer to the actual length of the data.

An intermediate driver with a connectionless lower edge always receives incoming data from an underlying miniport adapter from its [**ProtocolReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff570267) function.

An intermediate driver with a connection-oriented lower edge always receives incoming data from an underlying miniport adapter from its [**ProtocolCoReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff570256) function.

 

 





