---
title: EFI\_USB\_ENDPOINT\_TYPE
author: windows-driver-content
description: EFI\_USB\_ENDPOINT\_TYPE
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 5cdb0efc-2355-42e2-929b-df19257e35c1
---

# EFI\_USB\_ENDPOINT\_TYPE


The **EFI\_USB\_ENDPOINT\_TYPE** enumeration contains values used to indicate the type of endpoint.

## Syntax


``` syntax
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20EFI_USB_ENDPOINT_TYPE%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


