---
title: NFC class extension interface
description: The NFC CX interface is based on the UMDF class extension model.
ms.assetid: 400043BE-4C16-40C7-B0EB-BA223F882F21
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NFC class extension interface


The NFC CX interface is based on the UMDF class extension model. The NFC CX interface enables the NFC client to offload the class implementation to the Microsoft-provided class extension that implements the NFC CX interface, while allowing the client driver to perform transport-specific initialization and I/O handling, as well as serve as the host for all vendor-specific functionality required for the NFC controller.

The NFC CX interface includes the following methods:

-   [**NfcCxDeviceInitConfig**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/nfccx/nf-nfccx-nfccxdeviceinitconfig)
-   [**NfcCxDeviceInitialize**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/nfccx/nf-nfccx-nfccxdeviceinitialize)
-   [**NfcCxDeviceDeinitialize**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/nfccx/nf-nfccx-nfccxdevicedeinitialize)
-   [**NfcCxHardwareEvent**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/nfccx/nf-nfccx-nfccxhardwareevent)
-   [**NfcCxNciReadNotification**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/nfccx/nf-nfccx-nfccxncireadnotification)
-   [**NfcCxSetRfDiscoveryConfig**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/nfccx/nf-nfccx-nfccxsetrfdiscoveryconfig)
-   [**NfcCxSetLlcpConfig**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/nfccx/nf-nfccx-nfccxsetllcpconfig)
-   [**NfcCxRegisterSequenceHandler**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/nfccx/nf-nfccx-nfccxregistersequencehandler)
-   [**NfcCxUnRegisterSequenceHandler**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/nfccx/nf-nfccx-nfccxunregistersequencehandler)

 

 
## Related topics
[NFC device driver interface (DDI) overview](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/index)  
[NFC class extension (CX) reference](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/index)  

