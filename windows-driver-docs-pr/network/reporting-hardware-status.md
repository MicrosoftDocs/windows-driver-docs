---
title: Reporting Hardware Status
description: Reporting Hardware Status
keywords:
- WMI WDK networking , reporting hardware status
- miniport drivers WDK networking , hardware status
- NDIS miniport drivers WDK , hardware status
- hardware status WDK networking
- status information WDK NDIS miniport
ms.date: 04/20/2017
---

# Reporting Hardware Status





A connectionless miniport driver indicates changes in hardware status to upper layers by calling [**NdisMIndicateStatusEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatestatusex). A connection-oriented miniport driver indicates changes by calling [**NdisMCoIndicateStatusEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcoindicatestatusex).

**NdisM(Co)IndicateStatusEx** takes both a general status code and a buffer that contains media-specific information that further defines the reason for the status change. NDIS reports this status change to bound protocol drivers. NDIS does not interpret or otherwise intercept the status code.

The miniport driver can make one or more such calls. However, unlike earlier versions of NDIS, the miniport driver does not indicate that it has finished sending status. The protocol driver or configuration manager can log the status or take corrective action, as appropriate.

[**NdisMCoIndicateStatusEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismcoindicatestatusex) takes any valid NDIS\_STATUS\_*Xxx* value.

The miniport driver is responsible for indicating status codes that make sense to a protocol or higher level driver. A protocol driver ignores any status values in which it is not interested or that do not make sense in the context of its operations.

A miniport driver cannot indicate status in the context of its [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize), [*MiniportInterrupt*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_isr), [*MiniportHaltEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_halt), or [*MiniportShutdownEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_shutdown) function.

A miniport driver can also be interrogated by an upper layer driver or by NDIS about the miniport driver's hardware status. When the [*MiniportOidRequest*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_oid_request) function of a connectionless miniport driver or the [**MiniportCoOidRequest**](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_co_oid_request) function of a connection-oriented miniport driver receives OID\_GEN\_HARDWARE\_STATUS, it responds with any of the applicable status values that are defined in NDIS\_HARDWARE\_STATUS. These status values include:

-   **NdisHardwareStatusReady**

-   **NdisHardwareStatusInitializing**

-   **NdisHardwareStatusReset**

-   **NdisHardwareStatusClosing**

-   **NdisHardwareStatusNotReady**

The miniport driver can be queried so that NDIS can synchronize operations between layers of NDIS drivers--for example, by determining whether a NIC is ready to accept packets.

 

