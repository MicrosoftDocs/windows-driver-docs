---
title: NFC CX Sequence Handling
description: Information about supporting non-standard NCI extensions by registering specific driver sequences exposed by the NFC CX.
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 01/11/2024
ms.topic: concept-article
---

# NFC CX Sequence handling

Most nonstandard NCI features and extensions that NFCC firmware from different vendors implement relate to chipset configuration, firmware download, and hardware tuning. The NFC client driver can support these nonstandard extensions by registering for specific driver sequences that the NFC CX exposes. The client driver registers for specific sequence handlers through the **NfcCxRegisterSequenceHandler** function. Typically, you register sequence handlers during initialization and invoke this function after **NfcCxDeviceInitialize**. Call **[NfcCxUnRegisterSequenceHandler](/windows-hardware/drivers/nfc/nfc-class-extension-quickstart/nf-nfccx-nfccxunregistersequencehandler)** to unregister these handlers during device shutdown. After the client driver's sequence handler callback is invoked, the NFC CX driver doesn't issue any NCI commands until the NFC client driver finishes its handling. These sequence handler callbacks are asynchronous, so the client can issue any number of I/O requests to the controller before notifying the NFC CX of its completion. NFC CX uses a watchdog timer mechanism to determine hung states. If the watchdog timer expires before the completion of sequence handler by the client, a bug check is triggered and the UMDF host process is terminated by the UMDF framework.

The following are the requirements for the NFC client driver in implementing any additional logic as part of the sequence handler:

- Any NCI commands sent by the NFC client when handling these sequences should ensure that the integrity of the current state as specified by the NFC CX is not violated. Therefore, NFC client must take care of this requirement to ensure proper functioning of the NFC device. As an example, when handling initialization complete sequence, the client driver should not issue NCI CORE_RESET_CMD to reset the chipset.
- The NFC client driver needs to ensure that NCI responses and notifications that the NCI commands it sends to the controller generate aren't sent to the NFC CX's **[NfcCxNciReadNotification](/windows-hardware/drivers/nfc/nfc-class-extension-quickstart/nf-nfccx-nfccxncireadnotification)** function. This requirement exists because otherwise the NFC CX NCI state machine gets out of sync with the commands it exchanges with the NFCC.

## Related topics

- [NFC device driver interface (DDI) overview](/windows-hardware/drivers/ddi/_nfpdrivers)
- [NFC class extension (CX) reference](/windows-hardware/drivers/nfc/nfc-class-extension-quickstart)
