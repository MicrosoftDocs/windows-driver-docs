---
title: NFC driver load order
description: When ACPI creates the device node to represent the NFCC, PnP matches against the NFC client driver-provided .inf and is installed for that device node.
ms.assetid: 8094B525-A4A1-42D2-8D1F-4B32D77418E3
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NFC driver load order


When ACPI creates the device node to represent the NFCC, PnP matches against the NFC client driver-provided .inf and is installed for that device node. The NFC client driver will, during its AddDevice routine, initialize the class extension, which will allow the Microsoft-provided NFC class extension (NfcCx.dll) to load and let itself setup any I/O queue handling it must implement for top portion of the NFC class extension driver. The following diagram illustrates the driver load mechanism.

![driver load order](images/driverloadsequence1.png)

 

 
## Related topics
[NFC device driver interface (DDI) overview](https://msdn.microsoft.com/library/windows/hardware/mt715815)  
[NFC class extension (CX) reference](https://msdn.microsoft.com/library/windows/hardware/dn905536)  

