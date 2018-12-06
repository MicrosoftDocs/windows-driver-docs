---
title: Reporting, Enabling, and Disabling a NIC's Ability to Parse UDP-ESP Packets
description: Reporting, Enabling, and Disabling a NIC's Ability to Parse UDP-ESP Packets
ms.assetid: 3a75c5b2-2d94-428e-9b2a-d760e14df552
keywords:
- UDP-encapsulated ESP packets WDK IPsec offload , parsing capabilities
- parsing capabilities WDK IPsec offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reporting, Enabling, and Disabling a NIC's Ability to Parse UDP-ESP Packets

\[The IPsec Task Offload feature is deprecated and should not be used.\]




A miniport driver specifies a NIC's Internet protocol security (IPsec) capabilities in an [**NDIS\_IPSEC\_OFFLOAD\_V1**](https://msdn.microsoft.com/library/windows/hardware/ff565796) structure. For more information, see [Reporting a NIC's IPsec Capabilities](reporting-a-nic-s-ipsec-capabilities.md).

The miniport reports the NIC's ability to parse incoming UDP-encapsulated ESP packets by setting one or more flags in the **Supported** . **Reserved** member of the NDIS\_IPSEC\_OFFLOAD\_V1 structure. The miniport driver can specify any or all of the four UDP-ESP encapsulation subtypes that are described in [UDP-ESP Encapsulation Types](udp-esp-encapsulation-types.md).

For information about enabling and disableing UDP ESP parsing capabilities, see [Enabling and Disabling TCP/IP Offload Services](enabling-and-disabling-task-offload-services.md).

 

 





