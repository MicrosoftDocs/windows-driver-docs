---
title: NFC Class Extension Extensibility Model
description: The NFC class extension driver enables developers to add chipset-specific NCI proprietary extensions that aren't covered by the NCI specification.
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 01/11/2024
---

# NFC class extension extensibility model

A primary purpose of the NFC class extension driver is to provide the client driver with the flexibility to add chipset-specific NCI proprietary extensions that aren't covered by the NCI specification.

To accommodate this, the NFC class extension driver provides multiple extensibility points for the client driver to provide support for these NCI vendor extensions which includes but not limited to proprietary implementation of non-NCI-defined RF protocols, chipset-specific NCI commands to configure NFC controller for low power modes and other chipset-specific configuration of firmware parameters, and so on.

The NFC class extension driver provides three extensibility points for the NFC client driver:

- [Sequence Handling](sequence-handling.md)
- RF protocol and interface extensibility
- NCI packet handling

## Related topics

- [NFC device driver interface (DDI) overview](/windows-hardware/drivers/ddi/_nfpdrivers)
- [NFC class extension (CX) reference](/windows-hardware/drivers/ddi/nfccx)
