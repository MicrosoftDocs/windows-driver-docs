---
title: Determining Whether to Fail an Offload Request Because of 802.1Q Information
description: Determining Whether to Fail an Offload Request Because of 802.1Q Information
ms.assetid: 19eb2328-0ffa-4c40-bfab-6a5a3a3b4b7b
keywords:
- 802.1Q and 802.1p information WDK TCP chimney offload , failing requests
- failing requests for 802.1Q information WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Determining Whether to Fail an Offload Request Because of 802.1Q Information


\[The TCP chimney offload feature is deprecated and should not be used.\]




When the host stack makes an initiate offload request, one or more filter or intermediate drivers might be present between the host stack and the offload target. During the initiate offload request, a filter or intermediate driver might set the **VlanId** member of [**NEIGHBOR\_OFFLOAD\_STATE\_CONST**](https://msdn.microsoft.com/library/windows/hardware/ff568324) structure, the **UserPriority** member of the [**TCP\_OFFLOAD\_STATE\_CACHED**](https://msdn.microsoft.com/library/windows/hardware/ff570937) structure, or both.

When processing an initiate offload request in its [*MiniportInitiateOffload*](https://msdn.microsoft.com/library/windows/hardware/ff559393) function, an offload target must determine whether to fail the request based on the supplied 802.1Q information. The initiate offload request can request more VLAN tag resources than the offload target has available. If this situation occurs, the offload target must fail the initiate offload request by supplying a value of NDIS\_STATUS\_OFFLOAD\_VLAN\_TAG\_ENTRIES in the **Status** member of the [**NDIS\_MINIPORT\_OFFLOAD\_BLOCK\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff566469) structure that is associated with the neighbor state object. If offload target resources are available, the following algorithm applies:

-   If the interface VLAN identifier (the VLAN identifier that is read from the registry) is zero, the offload target must not fail the initiate offload request because of the neighbor **VlanId** for the TCP connection unless it has run out of VLAN identifier resources.

-   If one or more of the interface VLAN identifiers is nonzero, one or more VLANs are configured for the network interface.
    -   If the neighbor **VlanId** is zero, the offload target must not fail the initiate offload request because of the neighbor **VlanId** .
    -   If the neighbor **VlanId** is nonzero and matches one of the interface VLAN identifiers, the offload target must not fail the initiate offload request because of the neighbor **VlanId** unless it has run out of VLAN identifiers resources.
    -   If the neighbor **VlanId** is nonzero and does not match one of the interface VLAN identifiers, the offload target must fail the initiate offload request with the **Status** member set to NDIS\_STATUS\_VLAN\_MISMATCH.

 

 





