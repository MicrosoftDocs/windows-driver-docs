---
title: Querying NDIS QoS Capabilities
description: Querying NDIS QoS Capabilities
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Querying NDIS QoS Capabilities


Overlying protocol and filter drivers can query the NDIS Quality of Service (QoS) capabilities of a network adapter in the following way:

-   The overlying driver can query the hardware NDIS QoS capabilities supported by the network adapter through an object identifier (OID) query request of [OID\_QOS\_HARDWARE\_CAPABILITIES](./oid-qos-hardware-capabilities.md).

-   The overlying driver can query the hardware NDIS QoS capabilities that are currently enabled on the network adapter through an OID query request of [OID\_QOS\_CURRENT\_CAPABILITIES](./oid-qos-current-capabilities.md).

NDIS handles these OID requests for the miniport driver. When the miniport driver registers the hardware and currently enabled NDIS QoS capabilities for the network adapter during network adapter initialization, NDIS caches this information. NDIS then returns this data when it handles the OID requests from an overlying driver.

For more information about how the miniport driver registers the NDIS QoS capabilities, see [Registering NDIS QoS Capabilities](registering-ndis-qos-capabilities.md).

 

