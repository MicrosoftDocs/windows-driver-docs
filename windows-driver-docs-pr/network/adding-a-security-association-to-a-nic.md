---
title: Adding a Security Association to a NIC
description: Adding a Security Association to a NIC
keywords:
- security associations WDK IPsec offload
- SAs WDK IPsec offload
- ESP-protected packets WDK IPsec offload , security associations
- AH-protected packets WDK IPsec offload , security associations
ms.date: 04/20/2017
---

# Adding a Security Association to a NIC

\[The IPsec Task Offload feature is deprecated and should not be used.\]




After the TCP/IP transport determines that a NIC can perform Internet protocol security (IPsec) operations (see [Reporting a NIC's IPsec Capabilities](reporting-a-nic-s-ipsec-capabilities.md)), the transport must request the NIC's miniport driver to add one or more inbound and outbound security associations (SAs) to the NIC before the transport can offload IPsec tasks to the NIC. To request that a miniport driver add one or more SAs to the NIC, the TCP/IP transport sets [OID\_TCP\_TASK\_IPSEC\_ADD\_SA](./oid-tcp-task-ipsec-add-sa.md).

 

