---
title: Initialization sequence
description: The figure below illustrates a high-level set of NCI packets that are exchanged by the NFC CX and the NFCC during initialization.
ms.assetid: 4977E1D4-2546-4573-B555-FA87DB8A2168
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Initialization sequence


The figure below illustrates a high-level set of NCI packets that are exchanged by the NFC CX and the NFCC during initialization. Prior to start of the initialization, the NFC CX driver invokes the client driver’s Pre-Init sequence handler if one is registered. StateInit comprises the following high-level sequences: NCI reset, NCI initialization, standard NCI configuration of parameters, and RF Interface and RF Protocol mapping. Note, the NFC client driver can set the defaults of some of the NCI configuration parameters used during initialization through NFC CX interface functions such as [**NfcCxSetRfDiscoveryConfig**](https://msdn.microsoft.com/library/windows/hardware/dn905616) and [**NfcCxSetLlcpConfig**](https://msdn.microsoft.com/library/windows/hardware/dn905615). Following the completion of initialization, the initialize complete sequence handler is invoked. The next state after initialization is completed is StateRfIdle.

![initialization sequence](images/initializationsequence.png)

One of the key requirements for the proper functioning of the NFCC is handling firmware download operation from the NFC client driver. The NFC CX design is flexible enough to support multiple different designs for downloading firmware to the controller.

Some chipsets require NCI initialization for firmware versioning information to determine if a firmware download is required. For such designs, the state machine of the NFC CX and NFC client driver for accomplishing firmware download would appear as shown below. The BLUE states correspond to the states specified by the NFC CX, and the GRAY states correspond to the states in the NFC client driver. Post NCI initialization i.e. in initialization complete sequence handler, the client driver checks the current version from the CORE\_INIT\_RSP message, and determines if firmware download operation is required. If ‘No’ then normal state transition of NFC CX driver continues to the next state. If ‘Yes’ the client driver requests the NFC CX to perform a restart. On completion of shutdown, the NFC client driver can implement the firmware download.

![firmware download post-initialization](images/initializationsequence1.png)

Some NFCC firmware implementations have an out of band mechanism, i.e. outside the context of NCI, to determine if a firmware download is required. In such cases, when handling the pre-initialization sequence, the NFC client driver can implement its connector state to determine if a firmware download is required. If ‘Yes’ then the firmware download operations are carried out by the client driver. If ‘No’ i.e. firmware download isn’t required, then normal operation to the next state continues. The figure below shows the state machine handling for Firmware Download Pre-NCI initialization.

![firmware download pre-initialization](images/firmwaredownloadpreinitialization.png)

 

 
## Related topics
[NFC device driver interface (DDI) overview](https://msdn.microsoft.com/library/windows/hardware/mt715815)  
[NFC class extension (CX) reference](https://msdn.microsoft.com/library/windows/hardware/dn905536)  

