---
title: Reserved IOCTL codes
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
description: Information about reserved ioctl codes for NFC drivers, which must return STATUS_INVALID_DEVICE_STATE.
ms.date: 04/20/2017
---

# Reserved IOCTL codes


All the following IOCTL codes are reserved, unless explicitly defined above; the driver MUST return STATUS\_INVALID\_DEVICE\_STATE from any of the following:

CTL\_CODE(FILE\_DEVICE\_NFP, 0x0000, \*, \*) through CTL\_CODE(FILE\_DEVICE\_NFP, 0x00FF, \*, \*)

The following IOCTLs MAY be used for IHV-specific functionality:

CTL\_CODE(FILE\_DEVICE\_NFP, 0x0100, \*, \*) through CTL\_CODE(FILE\_DEVICE\_NFP, 0x01FF, \*, \*)

 

 
## Related topics
[Near field communications (NFC) API reference](/windows-hardware/drivers/ddi/_nfpdrivers/)
