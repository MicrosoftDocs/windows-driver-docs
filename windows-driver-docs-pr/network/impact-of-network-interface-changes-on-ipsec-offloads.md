---
title: Impact of Network Interface Changes on IPsec Offloads
description: Impact of Network Interface Changes on IPsec Offloads
keywords:
- ESP-protected packets WDK IPsec offload , routing interface changed
- AH-protected packets WDK IPsec offload , routing interface changed
- ESP-protected packets WDK IPsec offload , NIC removed and
- AH-protected packets WDK IPsec offload , NIC removed and
ms.date: 04/20/2017
---

# Impact of Network Interface Changes on IPsec Offloads

\[The IPsec Task Offload feature is deprecated and should not be used.\]




The following events in the network interface affect the offloading of Internet protocol security (IPsec) tasks:

-   A NIC is removed.

    Before a NIC to which tasks are being offloaded is removed from the system, its miniport driver should delete all security associations (SAs) from the NIC. The miniport driver does not have to request that the TCP/IP transport delete the SAs.

-   A routing interface is changed.

    When network traffic is routed through a new interface, the TCP/IP stack temporarily performs IPsec tasks until it has added the appropriate SAs to the NIC that is used in the new interface. The TCP/IP stack adds an SA to a NIC by issuing [OID\_TCP\_TASK\_IPSEC\_ADD\_SA](./oid-tcp-task-ipsec-add-sa.md). After the SAs on the NIC that is used for the old interface expire, the TCP/IP transport issues [OID\_TCP\_TASK\_IPSEC\_DELETE\_SA](./oid-tcp-task-ipsec-delete-sa.md) as many times as necessary to request that the NIC's miniport driver delete the SAs from the NIC.

 

