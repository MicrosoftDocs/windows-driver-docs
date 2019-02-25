---
title: Reporting a NIC's IPsec Offload Version 2 Capabilities
description: Reporting a NIC's IPsec Offload Version 2 Capabilities
ms.assetid: 0ce5c42d-5c0c-4dfa-8a9f-a80c8924201d
keywords:
- IPsecOV2 WDK TCP/IP transport , capabilities
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reporting a NIC's IPsec Offload Version 2 Capabilities

\[The IPsec Task Offload feature is deprecated and should not be used.\]




To specify IPsec offload version 2 (IPsecOV2) capabilities, an NDIS 6.1 and later miniport driver specifies the current or default configuration of a NIC in an [**NDIS\_IPSEC\_OFFLOAD\_V2**](https://msdn.microsoft.com/library/windows/hardware/ff565808) structure. Miniport drivers must include the default IPsecOV2 configuration in the [**NDIS\_MINIPORT\_ADAPTER\_OFFLOAD\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565930) structure. Miniport drivers call the [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) function from the [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function and pass in the information in NDIS\_MINIPORT\_ADAPTER\_OFFLOAD\_ATTRIBUTES.

Miniport drivers must report changes in the IPsecOV2 capabilities, if any, in the [**NDIS\_STATUS\_TASK\_OFFLOAD\_CURRENT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff567424) status indication.

**Note**  NDIS provides a direct OID request interface for NDIS 6.1 and later drivers. The [direct OID request path](https://msdn.microsoft.com/library/windows/hardware/ff564736) supports OID requests that are queried or set frequently.

 

In response to a query of [OID\_TCP\_OFFLOAD\_CURRENT\_CONFIG](https://msdn.microsoft.com/library/windows/hardware/ff569805), NDIS includes the NDIS\_IPSEC\_OFFLOAD\_V2 structure in the [**NDIS\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff566599) structure that NDIS returns in the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure. NDIS uses the information that the miniport driver provided.

 

 





