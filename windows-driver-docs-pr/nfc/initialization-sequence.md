---
title: Initialization Sequence
description: The figure below illustrates a high-level set of NCI packets that are exchanged by the NFC CX and the NFCC during initialization.
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 01/11/2024
ms.topic: concept-article
---

# Initialization sequence

The following diagram shows a high-level set of NCI packets that the NFC CX and the NFCC exchange during initialization. Before the initialization starts, the NFC CX driver calls the client driver's Pre-Init sequence handler if the client driver registers one. `StateInit` includes the following high-level sequences: NCI reset, NCI initialization, standard NCI configuration of parameters, and RF Interface and RF Protocol mapping. The NFC client driver can set the defaults for some of the NCI configuration parameters that the initialization process uses through NFC CX interface functions such as **NfcCxSetRfDiscoveryConfig** and **NfcCxSetLlcpConfig**. When initialization finishes, the initialize complete sequence handler is called. The next state after initialization finishes is `StateRfIdle`.

![initialization sequence.](images/initializationsequence.png)

One of the key requirements for the proper functioning of the NFCC is handling firmware download operation from the NFC client driver. The NFC CX design is flexible enough to support multiple different designs for downloading firmware to the controller.

Some chipsets require NCI initialization for firmware versioning information to determine if a firmware download is required. For such designs, the state machine of the NFC CX and NFC client driver for accomplishing firmware download would appear as shown below. The BLUE states correspond to the states specified by the NFC CX, and the GRAY states correspond to the states in the NFC client driver. Post NCI initialization i.e. in initialization complete sequence handler, the client driver checks the current version from the CORE_INIT_RSP message, and determines if firmware download operation is required. If 'No' then normal state transition of NFC CX driver continues to the next state. If 'Yes' the client driver requests the NFC CX to perform a restart. On completion of shutdown, the NFC client driver can implement the firmware download.

![firmware download post-initialization.](images/initializationsequence1.png)

Some NFCC firmware implementations have an out of band mechanism, i.e. outside the context of NCI, to determine if a firmware download is required. In such cases, when handling the pre-initialization sequence, the NFC client driver can implement its connector state to determine if a firmware download is required. If 'Yes' then the firmware download operations are carried out by the client driver. If 'No' i.e. firmware download isn't required, then normal operation to the next state continues. The figure below shows the state machine handling for Firmware Download Pre-NCI initialization.

![firmware download pre-initialization.](images/firmwaredownloadpreinitialization.png)

## Related topics

- [NFC device driver interface (DDI) overview](/windows-hardware/drivers/ddi/_nfpdrivers)
- [NFC class extension (CX) design guide](/windows-hardware/drivers/nfc/nfc-class-extension-)
