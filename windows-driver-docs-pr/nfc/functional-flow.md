---
title: Functional flow for Smart Card
description: A flowchart and short description of the hierarchical reading and writing of NDEF messages upon smart card discovery.
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Functional flow for Smart Card

Because the Smart Card is sharing the driver with NFP, when a smart card approaches, NDEF processing takes priority so that we give a chance for the higher level services to work on the NDEF message type before an application can communicate with the card.

![A flowchart describing the hierarchical reading and writing of NDEF messages upon smart card discovery.](images/smartcardfunctionalflow.png)

## Related topics

[NFC device driver interface (DDI) overview](/windows-hardware/drivers/ddi/_nfpdrivers)  
[Smart card DDI and command reference](/previous-versions/dn905601(v=vs.85))
