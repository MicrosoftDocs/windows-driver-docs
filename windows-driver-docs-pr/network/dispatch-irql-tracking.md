---
title: Dispatch IRQL Tracking
description: Dispatch IRQL Tracking
keywords:
- dispatch level flags WDK networking
- IRQLs WDK networking
- network drivers WDK , IRQLs
- current IRQLs WDK networking
- dispatch IRQL tracking WDK networking
ms.date: 04/20/2017
---

# Dispatch IRQL Tracking





To improve system performance, some NDIS functions (for example, the [*MiniportSendNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_send_net_buffer_lists) function) include a dispatch level flag that indicates the current IRQL. The proper use of the dispatch level flag can help to avoid unnecessary attempts to set the IRQL.

There are other flags that control other attributes, but the names for the dispatch level flags are:

NDIS\_SEND\_FLAGS\_DISPATCH\_LEVEL

NDIS\_SEND\_COMPLETE\_FLAGS\_DISPATCH\_LEVEL

NDIS\_RECEIVE\_FLAGS\_DISPATCH\_LEVEL

NDIS\_RETURN\_FLAGS\_DISPATCH\_LEVEL

NDIS\_RWL\_AT\_DISPATCH\_LEVEL

The caller must determine the dispatch level flag setting from the known current IRQL, not by testing the IRQL. For example, you know the IRQL because it is a fixed characteristic of the driver design, or the driver saved the current IRQL.

If the known current IRQL is DISPATCH\_LEVEL, the caller should set this flag. If the current IRQL is unknown, or the caller is not running at DISPATCH\_LEVEL, the caller should clear this flag. If the caller is NDIS, the called function should test this flag to avoid changing the IRQL.

Drivers should not test for the IRQL to determine the value for the dispatch level flag. Testing would defeat the purpose of the flag. If necessary, the called function can simply do the testing itself. How a driver determines that it should or should not set the flag is left to the design of the particular driver.

 

