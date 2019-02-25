---
title: Querying NDIS QoS Capabilities
description: Querying NDIS QoS Capabilities
ms.assetid: 00A2EFCD-CD90-446C-B588-EC66E3E730B2
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Querying NDIS QoS Capabilities


Overlying protocol and filter drivers can query the NDIS Quality of Service (QoS) capabilities of a network adapter in the following way:

-   The overlying driver can query the hardware NDIS QoS capabilities supported by the network adapter through an object identifier (OID) query request of [OID\_QOS\_HARDWARE\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/hh451828).

-   The overlying driver can query the hardware NDIS QoS capabilities that are currently enabled on the network adapter through an OID query request of [OID\_QOS\_CURRENT\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/hh451827).

NDIS handles these OID requests for the miniport driver. When the miniport driver registers the hardware and currently enabled NDIS QoS capabilities for the network adapter during network adapter initialization, NDIS caches this information. NDIS then returns this data when it handles the OID requests from an overlying driver.

For more information about how the miniport driver registers the NDIS QoS capabilities, see [Registering NDIS QoS Capabilities](registering-ndis-qos-capabilities.md).

 

 





