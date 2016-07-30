---
title: Functional flow
author: windows-driver-content
description: Because the Smart Card is sharing the driver with NFP, when a smart card approaches, NDEF processing takes priority so that we give a chance for the higher level services to work on the NDEF message type before an application can communicate with the card.
ms.assetid: 7B4B4902-FD16-4C9B-BB54-A1D6EFCAE9DB
keywords: ["NFC", "near field communications", "proximity", "near field proximity", "NFP"]
---

# Functional flow


Because the Smart Card is sharing the driver with NFP, when a smart card approaches, NDEF processing takes priority so that we give a chance for the higher level services to work on the NDEF message type before an application can communicate with the card.

![A flowchart describing the hierarchical reading and writing of NDEF messages upon smart card discovery.](images/smartcardfunctionalflow.png)

 

 
## Related topics
[NFC device driver interface (DDI) overview](https://msdn.microsoft.com/library/windows/hardware/mt715815)  
[Smart card DDI and command reference](https://msdn.microsoft.com/library/windows/hardware/dn905601)  

------------------
