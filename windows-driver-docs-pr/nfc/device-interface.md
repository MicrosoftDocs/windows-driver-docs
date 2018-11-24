---
title: NFP device interface
description: A client application communicates with the proximity device through a defined set of I/O control codes sent to an open handle.
ms.assetid: ED63FDCF-3253-4976-8571-82F4824923C5
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 04/20/2017
ms.localizationpriority: medium
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

