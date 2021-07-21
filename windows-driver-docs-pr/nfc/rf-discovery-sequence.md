---
title: RF discovery sequence
description: The following figure illustrates the sequence of NCI operations executed by NFC CX for starting discovery.
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

![A sequence diagram depicting the NCI operations executed by NFC CX for starting discovery.](images/staterfdiscoverysequence.png)

 

 
## Related topics
[NFC device driver interface (DDI) overview](/windows-hardware/drivers/ddi/index)  
[NFC class extension (CX) reference](/windows-hardware/drivers/ddi/index)
