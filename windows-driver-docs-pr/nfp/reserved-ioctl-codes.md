---
title: Reserved IOCTL Codes
ms.assetid: A2A67F8E-0A29-429E-935C-39368EFD9772
description: 
---

# Reserved IOCTL Codes


All the following IOCTL codes are reserved, unless explicitly defined above; the driver MUST return STATUS\_INVALID\_DEVICE\_STATE from any of the following:

CTL\_CODE(FILE\_DEVICE\_NFP, 0x0000, \*, \*) through CTL\_CODE(FILE\_DEVICE\_NFP, 0x00FF, \*, \*)

The following IOCTLs MAY be used for IHV-specific functionality:

CTL\_CODE(FILE\_DEVICE\_NFP, 0x0100, \*, \*) through CTL\_CODE(FILE\_DEVICE\_NFP, 0x01FF, \*, \*)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnfpdrivers\nfpdrivers%5D:%20Reserved%20IOCTL%20Codes%20%20RELEASE:%20%283/30/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




