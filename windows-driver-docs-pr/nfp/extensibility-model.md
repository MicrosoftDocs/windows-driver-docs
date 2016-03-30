---
title: Extensibility Model
description: A primary purpose of the NFC class extension driver is to provide the client driver with the flexibility to add chipset-specific NCI proprietary extensions that aren’t covered by the NCI specification.
ms.assetid: 8CCCE7BF-595A-4F30-9924-B5BD45D6137F
---

# Extensibility Model


A primary purpose of the NFC class extension driver is to provide the client driver with the flexibility to add chipset-specific NCI proprietary extensions that aren’t covered by the NCI specification.

To accommodate this, the NFC class extension driver provides multiple extensibility points for the client driver to provide support for these NCI vendor extensions which includes but not limited to proprietary implementation of non-NCI-defined RF protocols, chipset-specific NCI commands to configure NFC controller for low power modes and other chipset-specific configuration of firmware parameters, and so on.

The NFC class extension driver provides three extensibility points for the NFC client driver:

-   [Sequence Handling](sequence-handling.md)
-   RF protocol and interface extensibility
-   NCI packet handling

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnfpdrivers\nfpdrivers%5D:%20Extensibility%20Model%20%20RELEASE:%20%283/30/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




