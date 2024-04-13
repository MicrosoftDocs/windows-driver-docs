---
title: NFC Driver Load Order
description: When ACPI creates the device node to represent the NFCC, PnP matches against the NFC client driver-provided .inf and is installed for that device node.
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 01/11/2024
---

# NFC driver load order

When ACPI creates the device node to represent the NFCC, PnP matches against the NFC client driver-provided .inf and is installed for that device node. The NFC client driver will, during its AddDevice routine, initialize the class extension, which will allow the Microsoft-provided NFC class extension (NfcCx.dll) to load and let itself setup any I/O queue handling it must implement for top portion of the NFC class extension driver. The following diagram illustrates the driver load mechanism.

![driver load order.](images/driverloadsequence1.png)

## Related topics

- [NFC device driver interface (DDI) overview](/windows-hardware/drivers/ddi/index)
- [NFC class extension (CX) reference](/windows-hardware/drivers/ddi/index)
