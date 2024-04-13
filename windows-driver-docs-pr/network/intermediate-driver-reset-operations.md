---
title: Intermediate Driver Reset Operations
description: Intermediate Driver Reset Operations
keywords:
- intermediate drivers WDK networking , reset operations
- NDIS intermediate drivers WDK , reset operations
- resetting intermediate drivers
ms.date: 04/20/2017
---

# Intermediate Driver Reset Operations





An intermediate driver must be prepared to handle the situation where its outstanding sends on a binding to an underlying driver can be dropped because the underlying NIC is reset.

An underlying driver typically resets a NIC because NDIS calls the miniport driver's [*MiniportResetEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_reset) function when NDIS times out queued sends or requests that are bound for the NIC. If an underlying NIC is reset, NDIS calls the [**ProtocolStatusEx**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_status_ex)(or [**ProtocolCoStatusEx**](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_co_status_ex)) function of each bound protocol and intermediate driver with a status of NDIS\_STATUS\_RESET\_START. When the miniport driver completes the reset, NDIS again calls *ProtocolStatusEx*(or *ProtocolCoStatusEx*) with a status of NDIS\_STATUS\_RESET\_END.

When a NIC is reset, if a bound intermediate driver has any transmit network data that is pending to that NIC, NDIS completes those network data back to the intermediate driver with an appropriate status. The intermediate driver must resubmit these network data again when the reset is completed.

When an intermediate driver receives a status of NDIS\_STATUS\_RESET\_START, it should:

-   Hold any network data ready to be transmitted until *ProtocolStatusEx* or *ProtocolCoStatusEx* receives an NDIS\_STATUS\_RESET\_END notification.

-   Hold any received network data that are ready to be indicated up to the next higher driver until *ProtocolStatusEx*(or *ProtocolCoStatusEx*) receives an NDIS\_STATUS\_RESET\_END notification.

-   Clean up any internal state it maintains for in-progress operations and NIC status.

After *ProtocolStatusEx*(or *ProtocolCoStatusEx*) receives NDIS\_STATUS\_RESET\_END, the intermediate driver can resume sending network data, making requests and making indications to higher-level drivers.

An intermediate driver does not provide a [*MiniportResetEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_reset) function.

 

