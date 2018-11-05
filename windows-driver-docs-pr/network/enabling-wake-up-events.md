---
title: Enabling Wake-Up Events
description: Enabling Wake-Up Events
ms.assetid: 48ed0f41-efa0-4040-8589-8d477c5ddd0e
keywords:
- wake-up capabilities WDK networking , enabling wake-up events
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Enabling Wake-Up Events





A protocol driver can send an [OID\_PNP\_ENABLE\_WAKE\_UP](https://msdn.microsoft.com/library/windows/hardware/ff569775) request to enable one or more of the network adapter's wake-up capabilities. NDIS does not immediately enable these wake-up capabilities. Instead, NDIS keeps track of the wake-up capabilities that are enabled by the protocol driver and, just before the miniport driver transitions to a sleeping state, sends an OID\_PNP\_ENABLE\_WAKE\_UP to the miniport driver to enable the appropriate wake-up events. After the miniport driver initializes the network adapter, or when it resumes from a low-power state, the miniport driver must disable any wake up methods that are set on the network adapter.

Before the miniport driver transitions to a low-power state (that is, before NDIS sends the miniport driver an OID\_PNP\_SET\_POWER request), NDIS sends the miniport driver an OID\_PNP\_ENABLE\_WAKE\_UP request to enable the network adapter's wake-up capabilities.

 

 





