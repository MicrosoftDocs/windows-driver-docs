---
title: WAN-Specific Capabilities of CoNDIS WAN Drivers
description: WAN-Specific Capabilities of CoNDIS WAN Drivers
ms.assetid: c4e8e0ae-7dd5-4c4e-900a-b1f7e5eecb16
keywords:
- CoNDIS WAN drivers WDK networking , vs. non-WAN CoNDIS drivers
- non-WAN CoNDIS drivers WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WAN-Specific Capabilities of CoNDIS WAN Drivers





CoNDIS WAN drivers differ from a non-WAN CoNDIS drivers as follows:

-   CoNDIS WAN drivers that support TAPI services use the CO\_ADDRESS\_FAMILY\_TAPI\_PROXY address family.

-   CoNDIS WAN drivers support WAN-specific OIDs: [OID\_WAN\_PERMANENT\_ADDRESS](https://msdn.microsoft.com/library/windows/hardware/ff561220), [OID\_WAN\_CURRENT\_ADDRESS](https://msdn.microsoft.com/library/windows/hardware/ff561200), and [OID\_WAN\_MEDIUM\_SUBTYPE](https://msdn.microsoft.com/library/windows/hardware/ff561216).

-   CoNDIS WAN miniport drivers support a set of CoNDIS WAN OIDs to set and query operating characteristics. For more information about CoNDIS WAN OIDs, see [CoNDIS WAN Objects](https://msdn.microsoft.com/library/windows/hardware/ff545146).

-   CoNDIS WAN miniport drivers that provide TAPI services support a set of CoNDIS TAPI OIDs to set and query operating characteristics. For more information about CoNDIS TAPI OIDs, see [TAPI Extensions for Connection-Oriented NDIS](https://msdn.microsoft.com/library/windows/hardware/ff570924).

-   CoNDIS WAN miniport drivers support a set of WAN-specific status indications that denote changes in the status of a link. For more information about CoNDIS WAN miniport driver status indications, see [Indicating CoNDIS WAN Miniport Driver Status](indicating-condis-wan-miniport-driver-status.md).

-   CoNDIS WAN miniport drivers keep a WAN-specific set of statistics. The [OID\_WAN\_CO\_GET\_STATS\_INFO](https://msdn.microsoft.com/library/windows/hardware/ff569820) OID requests the miniport driver to return the statistics information.

-   CoNDIS WAN miniport drivers never attempt to loop back any packets; NDISWAN provides loop-back support.

 

 





