---
title: Deleting a Security Association from a NIC
description: Deleting a Security Association from a NIC
keywords:
- security associations WDK IPsec offload
- SAs WDK IPsec offload
- ESP-protected packets WDK IPsec offload , security associations
- AH-protected packets WDK IPsec offload , security associations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Deleting a Security Association from a NIC

\[The IPsec Task Offload feature is deprecated and should not be used.\]




If necessary, the TCP/IP transport can set [OID\_TCP\_TASK\_IPSEC\_DELETE\_SA](./oid-tcp-task-ipsec-delete-sa.md) to request that the miniport driver delete a security association (SA) from the NIC.

To create space for another SA on the NIC, the miniport driver can set the **SaDeleteReq** flag in the [**NDIS\_IPSEC\_OFFLOAD\_V1\_NET\_BUFFER\_LIST\_INFO**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_ipsec_offload_v1_net_buffer_list_info) structure for a receive packet. The TCP/IP transport subsequently issues OID\_TCP\_TASK\_IPSEC\_DELETE\_SA one time to delete the inbound security association (SA) over which the packet was received and another time to delete the outbound SA that corresponds to the deleted inbound SA. A NIC must not remove either of these SAs before it receives the corresponding OID\_TCP\_TASK\_IPSEC\_DELETE\_SA request. The miniport driver can set **SaDeleteReq** independently of the **CryptoDone** flag.
