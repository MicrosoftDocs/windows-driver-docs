---
title: NFP Device Interface
description: A client application communicates with the proximity device through a defined set of I/O control codes sent to an open handle.
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 01/11/2024
---

# NFP device interface

A client application communicates with the proximity device through a defined set of I/O control codes sent to an open handle.

## Publication and Subscription Handles

Each publication and each subscription is represented as an open handle to the driver. Therefore, M publications and N subscriptions would equate to M+N open handles to the driver. The Windows I/O Manager will enforce reasonable handle count limits on processes.

## Generic NULL File Name Handles

A generic file handle is opened for sending non-publication and non-subscription requests to the driver. This type of handle must be accepted. The client will use this handle to determine the Maximum Message Size and the Transmission Rate of the driver.

## IOCTL Support

The IOCTLs supporting the proximity device driver interface are defined in Nfpdev.h. The control codes are defined with the following attributes.

- METHOD_BUFFERED
- FILE_ANY_ACCESS
- FILE_DEVICE_NFP

Each publication and each subscription is manifested as its own open handle to the driver. Therefore, M publications and N subscriptions would equate to M+N open handles to the driver. The Windows I/O Manager will enforce reasonable handle count limits on processes.

The IOCTL codes are defined in the header Nfpdev.h

The security descriptor of the device is left as the OS or device class default.

## Reserved and Vendor IOCTL Codes

The following table describes the reserved and vendor specific control code ranges.

| Type            | Range Start                               | Range End                                 |
|-----------------|-------------------------------------------|-------------------------------------------|
| Reserved        | `CTL_CODE(FILE_DEVICE_NFP, 0x0000, *, *)` | `CTL_CODE(FILE_DEVICE_NFP, 0x00FF, *, *)` |
| Vendor Specific | `CTL_CODE(FILE_DEVICE_NFP, 0x0100, *, *)` | `CTL_CODE(FILE_DEVICE_NFP, 0x01FF, *, *)` |

## Related topics

- [Near field communications (NFC) API reference](/windows-hardware/drivers/ddi/_nfpdrivers/)
