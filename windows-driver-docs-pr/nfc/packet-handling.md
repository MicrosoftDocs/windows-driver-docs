---
title: NCI Packet Handling
description: In some cases, the sequences defined by the NFC CX might not be sufficient for NFC client driver to add its custom logic.
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 01/11/2024
---

# NCI packet handling

In some cases, the sequences defined by the NFC CX might not be sufficient for NFC client driver to add its custom logic. In these cases, because all NCI packets are exchanged by the NFC CX with the NFC controller through the NFC client driver (which handles interfacing with the transport layer), this gives the NFC client driver the opportunity to inject additional NCI packets between standard NCI packets exchanged by the CX and NFCC. However, the NFC client driver must ensure the following requirements are satisfied if it utilizes this extensibility point in addition to the requirements (1) and (2) specified in the sequence extensibility section:

- When the exchange of these additional NCI packets are completed, the NFC client driver must send the response and notification associated with the NCI command sent by the NFC CX through the **[NfcCxNciReadNotification](/windows-hardware/drivers/ddi/nfccx/nf-nfccx-nfccxncireadnotification)** callback.

- Because per-channel flow control is performed in the NFC CX's logical channel management, the NFC client driver shouldn't perform any logic that would impact this. Therefore, it is recommended that the NFC client driver doesn't send any additional data packets on logical channels opened by CX without its knowledge.

## Related topics

- [NFC device driver interface (DDI) overview](/windows-hardware/drivers/ddi/index)
- [NFC class extension (CX) reference](/windows-hardware/drivers/ddi/index)
