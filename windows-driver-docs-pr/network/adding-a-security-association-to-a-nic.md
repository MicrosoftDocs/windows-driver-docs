---
title: Adding a Security Association to a NIC
description: Adding a Security Association to a NIC
ms.assetid: 524cc9f8-fe02-4192-85af-83813ae83d08
keywords:
- security associations WDK IPsec offload
- SAs WDK IPsec offload
- ESP-protected packets WDK IPsec offload , security associations
- AH-protected packets WDK IPsec offload , security associations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Adding a Security Association to a NIC

\[The IPsec Task Offload feature is deprecated and should not be used.\]




After the TCP/IP transport determines that a NIC can perform Internet protocol security (IPsec) operations (see [Reporting a NIC's IPsec Capabilities](reporting-a-nic-s-ipsec-capabilities.md)), the transport must request the NIC's miniport driver to add one or more inbound and outbound security associations (SAs) to the NIC before the transport can offload IPsec tasks to the NIC. To request that a miniport driver add one or more SAs to the NIC, the TCP/IP transport sets [OID\_TCP\_TASK\_IPSEC\_ADD\_SA](https://msdn.microsoft.com/library/windows/hardware/ff569808).

 

 





