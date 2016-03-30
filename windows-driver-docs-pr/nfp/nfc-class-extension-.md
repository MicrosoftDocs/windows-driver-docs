---
title: NFC Class Extension
description: This section describes the interface between the NFC class extension (CX) and the NFC client driver.
ms.assetid: 64599C5E-7E72-4712-B733-24C078919B84
---

# NFC Class Extension


This section describes the interface between the NFC class extension (CX) and the NFC client driver. The NFC CX driver implements all NFC device driver interfaces and standard NFC protocols and formats based on the *NFC Forum NFC Controller Interface (NCI) Technical Specification*.

The NFC client driver is responsible for transport layer interfacing as well as support for any non-standard vendor-defined extensions for the optimized functioning of the NFC controller.

The NFC class extension driver implements all standard NFC Forum Tag (T1T, T2T, T3T, ISO-DEP) and P2P (LLCP and SNEP) protocols, and RF Management based on the NCI Core specification. The class extension driver implements all the Windows-defined device driver interfaces to interact with the NFC controller, Secure Elements, and Remote RF endpoints.

These topics describe the architecture and public interface between the NFC class extension driver supplied by Microsoft and the NFC client driver supplied by the corresponding chipset manufacturers. The NFC CX driver is designed to support NFC chipsets from various manufacturers, and enables manufacturers to implement non-NCI standard functionality in their NFC client driver for differentiation purposes.

The following are the Windows-defined NFC driver DDI that are implemented by the NFC CX driver:

-   Near Field Proximity DDI
-   NFC Secure Element Management DDI
-   Smart Card DDI for contactless smart card access
-   NFC Radio Management DDI
-   DTA DDI for NFC Forum certification

The following are the NFC Forum specifications implemented by the NFC CX driver:

-   NFC Controller Interface, NCI 1.0 Specification
-   NFC Data Exchange Format, NDEF
-   NFC Forum Type 1-4 Tag
-   Logical Link Control Protocol, LLCP 1.1 Specification
-   Simple NDEF Exchange Protocol, SNEP 1.0 Specification
-   ISO/IEC 15693

## In this section


-   [Glossary](glossary.md)
-   [Architecture](architecture.md)
-   [NFC Stack Architecture](nfc-stack-architecture.md)
-   [Driver Load Order](driver-load-order.md)
-   [Class Extension Interface](nfc-class-extension-interface.md)
-   [Class Extension State Machine](nfc-class-extension-state-machine.md)
-   [Extensibility Model](extensibility-model.md)
-   [Configurability](configurability.md)
-   [Error Handling](error-handling.md)
-   [Power States](power-states.md)
-   [NFC Client Driver Power Management Requirements](nfc-client-driver-power-management-requirements.md)
-   [Logging](logging.md)
-   [Persisted Data](persisted-data.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnfpdrivers\nfpdrivers%5D:%20NFC%20Class%20Extension%20%20%20RELEASE:%20%283/30/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




