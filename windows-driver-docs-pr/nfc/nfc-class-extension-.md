---
title: NFC class extension
description: This section describes the interface between the NFC class extension (CX) and the NFC client driver.
ms.assetid: 64599C5E-7E72-4712-B733-24C078919B84
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
- CX
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NFC class extension (CX) design guide


This section describes the interface between the NFC class extension (CX) and the NFC client driver. The NFC CX driver implements all NFC device driver interfaces and standard NFC protocols and formats based on the *NFC Forum NFC Controller Interface (NCI) Technical Specification*.

The NFC client driver is responsible for transport layer interfacing as well as support for any non-standard vendor-defined extensions for the optimized functioning of the NFC controller.

The NFC class extension driver implements all standard NFC Forum Tag (T1T, T2T, T3T, ISO-DEP) and P2P (LLCP and SNEP) protocols, and RF Management based on the NCI Core specification. The class extension driver implements all the Windows-defined device driver interfaces to interact with the NFC controller, Secure Elements, and Remote RF endpoints.

These topics describe the architecture and public interface between the NFC class extension driver supplied by Microsoft and the NFC client driver supplied by the corresponding chipset manufacturers. The NFC CX driver is designed to support NFC chipsets from various manufacturers, and enables manufacturers to implement non-NCI standard functionality in their NFC client driver for differentiation purposes.

## NFC driver DDI
The following are the Windows-defined NFC driver DDI that are implemented by the NFC CX driver:

-   [Near Field Proximity DDI](https://msdn.microsoft.com/library/windows/hardware/jj866056)
-   [NFC Secure Element Management DDI](https://msdn.microsoft.com/library/windows/hardware/dn905485)
-   [Smart Card DDI for contactless smart card access](https://msdn.microsoft.com/library/windows/hardware/dn905601)
-   [NFC Radio Management DDI](https://msdn.microsoft.com/library/windows/hardware/dn905577)
-   DTA DDI for NFC Forum certification

## NFC forum specifications
The following are the NFC Forum specifications implemented by the NFC CX driver:  

-   NFC Controller Interface, NCI 1.0 Specification
-   NFC Data Exchange Format, NDEF
-   NFC Forum Type 1-4 Tag
-   Logical Link Control Protocol, LLCP 1.1 Specification
-   Simple NDEF Exchange Protocol, SNEP 1.0 Specification
-   ISO/IEC 15693

## Supported NFC smart cards and tags
The following are the NFC smart cards and tags supported by the NFC CX driver:  

-   MIFARE Classic family
-   MIFARE Ultralight family
-   MIFARE DESFire family
-   FeliCa family
-   Jewel/Topaz family
-   Generic ISO 15693 tags
-   Thinfilm NFC Barcode (Kovio)



## In this section


-   [Glossary](glossary.md)
-   [Architecture](architecture.md)
-   [NFC stack architecture](nfc-stack-architecture.md)
-   [Driver load order](driver-load-order.md)
-   [Class extension interface](nfc-class-extension-interface.md)
-   [Class extension state machine](nfc-class-extension-state-machine.md)
-   [Extensibility model](extensibility-model.md)
-   [Configurability](configurability.md)
-   [Error handling](error-handling.md)
-   [Power sates](power-states.md)
-   [NFC client driver power management requirements](nfc-client-driver-power-management-requirements.md)
-   [Logging](logging.md)
-   [Persisted data](persisted-data.md)

 

 
## Related topics
[NFC device driver interface (DDI) overview](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/_nfpdrivers/)  
[NFC class extension (CX) reference](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/nfccx/)  
