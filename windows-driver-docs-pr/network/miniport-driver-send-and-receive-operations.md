---
title: Miniport Driver Send and Receive Operations
description: Miniport Driver Send and Receive Operations
keywords:
- miniport drivers WDK networking , sending data
- NDIS miniport drivers WDK , sending data
- miniport drivers WDK networking , receiving data
- NDIS miniport drivers WDK , receiving data
- sending data WDK networking
- receiving data WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Miniport Driver Send and Receive Operations





Miniport drivers handle send requests from overlying drivers and originate receive indications. In a single function call, NDIS miniport drivers can indicate a linked list with multiple received [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structures. Miniport drivers can handle send requests for lists of multiple NET\_BUFFER\_LIST structures with multiple [**NET\_BUFFER**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer) structures on each NET\_BUFFER\_LIST structure.

Miniport drivers must manage receive buffer pools. Most miniport drivers create pools that preallocate a single NET\_BUFFER structure with each NET\_BUFFER\_LIST structure.

The following topics provide more information about miniport driver buffer management, send operations, and receive operations:

[Miniport Driver Buffer Management](miniport-driver-buffer-management.md)

[Sending Data from a Miniport Driver](sending-data-from-a-miniport-driver.md)

[Canceling a Send Request in a Miniport Driver](canceling-a-send-request-in-a-miniport-driver.md)

[Indicating Received Data from a Miniport Driver](indicating-received-data-from-a-miniport-driver.md)

 

