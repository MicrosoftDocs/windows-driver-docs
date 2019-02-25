---
title: CoNDIS WAN Is Less Complex
description: CoNDIS WAN Is Less Complex
ms.assetid: 750f321a-72c9-4d90-b02e-cbe5177dc2af
keywords:
- CoNDIS WAN drivers WDK networking , benefits
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# CoNDIS WAN Is Less Complex





CoNDIS defines objects that correspond to each of the logical entities that are involved in a connection. These entities include address families (AFs), virtual connections (VCs), service access points (SAPs), and parties.

In the CoNDIS environment, the system handles many of the complex TAPI requirements. Therefore, a CoNDIS WAN miniport driver or MCM does not have to handle as many TAPI OIDs as an NDIS WAN miniport driver. In addition, the CoNDIS WAN miniport driver or MCM is not required to handle the following status indications:

-   NDIS\_STATUS\_TAPI\_INDICATION

-   NDIS\_STATUS\_WAN\_LINE\_UP

-   NDIS\_STATUS\_WAN\_LINE\_DOWN

The separation of the call manager and miniport driver functions enables you to implement two simple drivers. The simplified drivers should be easier to maintain and debug than one large and complex driver.

 

 





