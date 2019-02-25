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

-   [**NfcCxDeviceInitConfig**](https://msdn.microsoft.com/library/windows/hardware/dn905610)
-   [**NfcCxDeviceInitialize**](https://msdn.microsoft.com/library/windows/hardware/dn905611)
-   [**NfcCxDeviceDeinitialize**](https://msdn.microsoft.com/library/windows/hardware/dn905609)
-   [**NfcCxHardwareEvent**](https://msdn.microsoft.com/library/windows/hardware/dn905612)
-   [**NfcCxNciReadNotification**](https://msdn.microsoft.com/library/windows/hardware/dn905613)
-   [**NfcCxSetRfDiscoveryConfig**](https://msdn.microsoft.com/library/windows/hardware/dn905616)
-   [**NfcCxSetLlcpConfig**](https://msdn.microsoft.com/library/windows/hardware/dn905615)
-   [**NfcCxRegisterSequenceHandler**](https://msdn.microsoft.com/library/windows/hardware/dn905614)
-   [**NfcCxUnRegisterSequenceHandler**](https://msdn.microsoft.com/library/windows/hardware/dn905617)

 

 
## Related topics
[NFC device driver interface (DDI) overview](https://msdn.microsoft.com/library/windows/hardware/mt715815)  
[NFC class extension (CX) reference](https://msdn.microsoft.com/library/windows/hardware/dn905536)  

