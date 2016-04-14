---
title: NFP device interface
author: windows-driver-content
description: A client application communicates with the proximity device through a defined set of I/O control codes sent to an open handle.
ms.assetid: ED63FDCF-3253-4976-8571-82F4824923C5
keywords: ["NFC", "near field communications", "proximity", "near field proximity", "NFP"]
---

# NFP device interface


A client application communicates with the proximity device through a defined set of I/O control codes sent to an open handle.

## Publication and Subscription Handles


Each publication and each subscription is represented as an open handle to the driver. Therefore, M publications and N subscriptions would equate to M+N open handles to the driver. The Windows I/O Manager will enforce reasonable handle count limits on processes.

## Generic NULL File Name Handles


A generic file handle is opened for sending non-publication and non-subscription requests to the driver. This type of handle must be accepted. The client will use this handle to determine the Maximum Message Size and the Transmission Rate of the driver.

## IOCTL Support


The IOCTLs supporting the proximity device driver interface are defined in Nfpdev.h. The control codes are defined with the following attributes.

-   METHOD\_BUFFERED
-   FILE\_ANY\_ACCESS
-   FILE\_DEVICE\_NFP

Each publication and each subscription is manifested as its own open handle to the driver. Therefore, M publications and N subscriptions would equate to M+N open handles to the driver. The Windows I/O Manager will enforce reasonable handle count limits on processes.

The IOCTL codes are defined in the header Nfpdev.h

The security descriptor of the device is left as the OS or device class default.

## Reserved and Vendor IOCTL Codes


The following table describes the reserved and vender specific control code ranges.

| Type            | Range Start                               | Range End                                 |
|-----------------|-------------------------------------------|-------------------------------------------|
| Reserved        | `CTL_CODE(FILE_DEVICE_NFP, 0x0000, *, *)` | `CTL_CODE(FILE_DEVICE_NFP, 0x00FF, *, *)` |
| Vendor Specific | `CTL_CODE(FILE_DEVICE_NFP, 0x0100, *, *)` | `CTL_CODE(FILE_DEVICE_NFP, 0x01FF, *, *)` |

 

 

 
## Related topics
[NFC device driver interface (DDI) overview](https://msdn.microsoft.com/library/windows/hardware/mt715815)  
[Near field proximity DDI reference](https://msdn.microsoft.com/library/windows/hardware/jj866056)  

------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnfpdrivers\nfpdrivers%5D:%20NFP%20device%20interface%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")
