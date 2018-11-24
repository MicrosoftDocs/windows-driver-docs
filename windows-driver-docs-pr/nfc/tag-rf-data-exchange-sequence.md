---
title: Tag RF data exchange sequence
description: The following figures illustrate state sequences for StateRfDiscovered and StateRfDataXchg for various reader-writer protocols such as T1T, T2T, T3T, and ISO-DEP.
ms.assetid: F5911609-4531-44B3-9629-CD0A27D40324
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Tag RF data exchange sequence


The following figures illustrate the state sequences for StateRfDiscovered and StateRfDataXchg for various reader-writer protocols such as T1T, T2T, T3T, and ISO-DEP. The transition to StateRfDiscovered occurs after RF interface activation. In case of multiple remote endpoints or multiple protocols in StateRfDiscovery, the NFC CX selects a single end point and protocol. Preference of NFC-DEP over ISO-DEP is implemented in the NFC CX for improved interoperability in case bail option isn’t supported by the controller. StateRfDiscovered is a transitional state where the NFC CX performs an initial presence check before transitioning to StateRfDataXchg. For reader/writer mode, StateRfDataXchg is broken down into the following sequence of NDEF operations: check NDEF, read or write NDEF, followed by presence checks. The driver also executes additional operations like formatting, read-only, low-level tag operations in this state depending on the requests from the application layer. Note that the NFC CX supports the Frame-RF interface for all NCI-standard protocols (as well as ISO15693) with the exception of ISO-DEP. ISO-DEP RF interface must be supported by the NFC controller to support ISO-DEP protocol.

![t1t rf data exchange sequence](images/rfdataexchangesequence.png)

The following illustrates the T2T RF data exchange sequence:

![t2t rf data exchange sequence](images/t2trfdataexchangesequence.png)

The following illustrates the T3T RF data exchange sequence:

![t3t rf data exchange sequence](images/t3trfdataexchangesequence.png)

The following illustrates the ISO-DEP RF Data Exchange Sequence:

![iso-dep rf data exchange sequence](images/iso-dep-rfdataexchangesequence.png)

The NFC CX performs a presence check in StateRfDataXchg when there is no data to exchange with the remote RF endpoint. This is used to determine if the remote RF endpoint has moved out of range from the DH. As noted in the sequence diagram, the following commands are used for presence check for various tag types:

-   For NFC Forum Type 1 Tags, the NFC CX uses the Read Identification (RID) command, which returns the UID, to perform the presence check detection.

-   For NFC Forum Type 2 Tags, the NFC CX uses the READ block command, which returns the 16-byte block data, to perform the presence check detection.

-   For NFC Forum Type 3 Tags, the NFC CX uses the RF\_T3T\_POLLING\_CMD NCI command (SENSF) to perform the presence check detection.

-   For NFC Forum Type 4 Tags, the NFC CX uses an empty I-block exchange to perform the presence check detection.

 

 
## Related topics
[NFC device driver interface (DDI) overview](https://msdn.microsoft.com/library/windows/hardware/mt715815)  
[NFC class extension (CX) reference](https://msdn.microsoft.com/library/windows/hardware/dn905536)  
