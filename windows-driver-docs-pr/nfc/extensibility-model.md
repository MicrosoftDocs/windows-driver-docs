---
title: NFC class extension extensibility model
description: The NFC class extension driver enables developers to add chipset-specific NCI proprietary extensions that aren’t covered by the NCI specification.
ms.assetid: 8CCCE7BF-595A-4F30-9924-B5BD45D6137F
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NFC class extension extensibility model


A primary purpose of the NFC class extension driver is to provide the client driver with the flexibility to add chipset-specific NCI proprietary extensions that aren’t covered by the NCI specification.

To accommodate this, the NFC class extension driver provides multiple extensibility points for the client driver to provide support for these NCI vendor extensions which includes but not limited to proprietary implementation of non-NCI-defined RF protocols, chipset-specific NCI commands to configure NFC controller for low power modes and other chipset-specific configuration of firmware parameters, and so on.

The NFC class extension driver provides three extensibility points for the NFC client driver:

-   [Sequence Handling](sequence-handling.md)
-   RF protocol and interface extensibility
-   NCI packet handling

 

 
## Related topics
[NFC device driver interface (DDI) overview](https://msdn.microsoft.com/library/windows/hardware/mt715815)  
[NFC class extension (CX) reference](https://msdn.microsoft.com/library/windows/hardware/dn905536)  
