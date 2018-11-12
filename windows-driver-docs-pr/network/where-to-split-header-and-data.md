---
title: Where to Split Header and Data
description: Where to Split Header and Data
ms.assetid: e302fcc1-5088-4f64-b454-5f20c69c0626
keywords:
- header-data split WDK , where to split
- Ethernet frame splitting WDK networking , where to split
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Where to Split Header and Data





The following are the only valid places where a header-data split provider can split an Ethernet frame:

-   [Beginning of upper-layer-protocol header](splitting-frames-at-the-beginning-of-the-upper-layer-protocol-headers.md).

-   [Beginning of UDP payload](splitting-frames-at-the-udp-payload.md).

-   [Beginning of TCP payload](splitting-frames-at-the-tcp-payload.md).

**Note**  These requirements apply only to header-data split providers. For more information about splitting frames in cases where header-data split is not used, see [Cases Where Header-Data Split Is Not Used](cases-where-header-data-split-is-not-used.md).

 

The following figure shows the major parts of the Ethernet frame and the valid split locations.

![diagram illustrating the format of the 802.11 mpdu frame encrypted through the wep algorithm](images/hdsplitframe.png)

 

 





