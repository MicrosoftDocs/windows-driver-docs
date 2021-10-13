---
title: NFP device identifiers
description: NFP device identifiers
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NFP device identifiers


The following are the device identifiers for NFP device drivers:

-   Device Interface Class
    -   GUID\_DEVINTERFACE\_NFP
    -   "{FB3842CD-9E2A-4F83-8FCC-4B0761139AE9}"
-   Device Class GUID
    -   “{5630831C-06C9-4856-B327-F5D32586E060}”
-   Device Class
    -   “Proximity”
    -   This is an OS-defined Device Class starting with Windows 8. Drivers that expose this interface must match this Device Class.
-   DEVPKEY\_NFP\_Capabilities
    -   0xFB3842CD, 0x9E2A, 0x4F83, 0x8F, 0xCC, 0x4B, 0x07, 0x61, 0x13, 0x9A, 0xE9, 0x02

If the device is advertised as NFC, the driver MUST populate DEVPKEY\_NFP\_Capabilities on the exposed GUID\_DEVINTERFACE\_NFP interface with a DEVPROP\_TYPE\_STRING\_LIST property containing one entry: “StandardNfc”.

 

 
## Related topics
[Near field communications (NFC) API reference](/windows-hardware/drivers/ddi/_nfpdrivers/)
