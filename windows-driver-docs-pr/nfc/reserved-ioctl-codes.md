---
title: Reserved IOCTL codes
author: windows-driver-content
ms.assetid: A2A67F8E-0A29-429E-935C-39368EFD9772
keywords: ["NFC", "near field communications", "proximity", "near field proximity", "NFP"]
description:
---

# Reserved IOCTL codes


All the following IOCTL codes are reserved, unless explicitly defined above; the driver MUST return STATUS\_INVALID\_DEVICE\_STATE from any of the following:

CTL\_CODE(FILE\_DEVICE\_NFP, 0x0000, \*, \*) through CTL\_CODE(FILE\_DEVICE\_NFP, 0x00FF, \*, \*)

The following IOCTLs MAY be used for IHV-specific functionality:

CTL\_CODE(FILE\_DEVICE\_NFP, 0x0100, \*, \*) through CTL\_CODE(FILE\_DEVICE\_NFP, 0x01FF, \*, \*)

 

 
## Related topics
[NFC device driver interface (DDI) overview](https://msdn.microsoft.com/library/windows/hardware/mt715815)  
[Near field proximity DDI reference](https://msdn.microsoft.com/library/windows/hardware/jj866056)  

------------------
