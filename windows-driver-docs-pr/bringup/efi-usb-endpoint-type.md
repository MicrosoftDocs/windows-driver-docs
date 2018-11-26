---
title: EFI_USB_ENDPOINT_TYPE
description: EFI_USB_ENDPOINT_TYPE
ms.assetid: 5cdb0efc-2355-42e2-929b-df19257e35c1
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_USB\_ENDPOINT\_TYPE


The **EFI\_USB\_ENDPOINT\_TYPE** enumeration contains values used to indicate the type of endpoint.

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


<a href="" id="usbendpointcontrol"></a>**UsbEndpointControl**  
Control transfer - command and status operations.

<a href="" id="usbendpointisochronous"></a>**UsbEndpointIsochronous**  
Isochronous transfe - continuous stream of time sensitive data with guaranteed bandwidth and bounded latency.

<a href="" id="usbendpointbulk"></a>**UsbEndpointBulk**  
Bulk transfer - large amount data in bursts with no guarantee of bandwidth or minimum latency.

<a href="" id="usbendpointinterrupt"></a>**UsbEndpointInterrupt**  
Interrupt transfer - non-periodic communication with guarantee of maximum latency.

## Requirements


**Header:** User generated

 

 




