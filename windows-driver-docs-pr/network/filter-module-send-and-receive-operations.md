---
title: Filter Module Send and Receive Operations
description: Filter Module Send and Receive Operations
ms.assetid: 208f9af6-cde4-4801-9355-daa6633d7d0b
keywords:
- filter modules WDK networking , send operations
- filter modules WDK networking , receive operations
- filter drivers WDK networking , send operations
- NDIS filter drivers WDK , send operations
- filter drivers WDK networking , receive operations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Filter Module Send and Receive Operations





This section documents send and receive operations for NDIS 6.0 filter drivers. Filter drivers can initiate send requests and receive indications or filter the requests and indications of other drivers.

Filter modules are stacked over a miniport adapter. For more information about the driver stack, see [NDIS 6.0 Driver Stack](ndis-driver-stack.md).

The filter modules in the driver stack can filter all send requests and receive indications that are associated with the underlying adapter. This is true for all protocol bindings to an adapter. For more information about NDIS 6.0 send and receive operations, see [Send and Receive Operations](send-and-receive-operations.md).

Filter drivers do not provide direct support for legacy send and receive operations that are based on the [**NDIS\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/ff557086) structure. Instead, NDIS converts receive indications from legacy miniport drivers to [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structures. Also, NDIS handles the required conversions from send requests that are based on NET\_BUFFER structures to legacy send requests that are based on NDIS\_PACKET structures.

**Note**  A filter driver can change the send and receive *FliterXxx* functions for a filter module dynamically. For more information, see [Data Bypass Mode](data-bypass-mode.md).

 

The following topics provide additional information about filter driver send and receive operations:

[Filter Driver Buffer Management](filter-driver-buffer-management.md)

[Sending Data from a Filter Driver](sending-data-from-a-filter-driver.md)

[Canceling a Send Request in a Filter Driver](canceling-a-send-request-in-a-filter-driver.md)

[Receiving Data in a Filter Driver](receiving-data-in-a-filter-driver.md)

 

 





