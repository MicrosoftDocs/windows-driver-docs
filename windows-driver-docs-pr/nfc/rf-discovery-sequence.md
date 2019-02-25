---
title: RF discovery sequence
description: The following figure illustrates the sequence of NCI operations executed by NFC CX for starting discovery.
ms.assetid: 392F8A06-262D-4CF9-B510-C3FE86291026
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# RF discovery sequence


The following figure illustrates the sequence of NCI operations executed by NFC CX for starting discovery. The StateRfDiscovery entered from StateRfIdle triggers the start RF discovery sequence. The main set of operations performed in this state is configuration of RF discovery parameters, optional configuration for listen mode routing table, and enabling discovery through the RF discover NCI command. An NFC client driver can use SequencePreRfDiscStart to add non-standard NCI commands to optimize the discovery process.

![A sequence diagram depicting the NCI operations executed by NFC CX for starting discovery](images/staterfdiscoverysequence.png)

 

 
## Related topics
[NFC device driver interface (DDI) overview](https://msdn.microsoft.com/library/windows/hardware/mt715815)  
[NFC class extension (CX) reference](https://msdn.microsoft.com/library/windows/hardware/dn905536)  

