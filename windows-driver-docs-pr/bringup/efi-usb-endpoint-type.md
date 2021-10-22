---
title: EFI_USB_ENDPOINT_TYPE
description: The EFI_USB_ENDPOINT_TYPE enumeration contains values used to indicate the type of endpoint.
ms.date: 08/20/2021
ms.localizationpriority: medium
---

# EFI_USB_ENDPOINT_TYPE

The **EFI_USB_ENDPOINT_TYPE** enumeration contains values used to indicate the type of endpoint.

## Syntax

```cpp
typedef enum _EFI_USB_ENDPOINT_TYPE{
  UsbEndpointControl = 0x00,
  UsbEndpointIsochronous = 0x01,
  UsbEndpointBulk = 0x02,
  UsbEndpointInterrupt = 0x03
} EFI_USB_ENDPOINT_TYPE;
```

## Constants

**UsbEndpointControl**  
Control transfer - command and status operations.

**UsbEndpointIsochronous**  
Isochronous transfer - continuous stream of time sensitive data with guaranteed bandwidth and bounded latency.

**UsbEndpointBulk**  
Bulk transfer - large amount data in bursts with no guarantee of bandwidth or minimum latency.

**UsbEndpointInterrupt**  
Interrupt transfer - non-periodic communication with guarantee of maximum latency.

## Requirements

**Header:** User generated
