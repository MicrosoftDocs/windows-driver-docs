---
title: EFI\_USB\_SUPERSPEED\_INTERFACE\_INFO
description: EFI\_USB\_SUPERSPEED\_INTERFACE\_INFO
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 1B0C04D0-5254-4B9A-A94D-4FF1CEAD4627
---

# EFI\_USB\_SUPERSPEED\_INTERFACE\_INFO


The **EFI\_USB\_SUPERSPEED\_INTERFACE\_INFO** structure is used to define the supported USB SuperSpeed interface to the USB function driver.

## Syntax


``` syntax
typedef struct
{
    EFI_USB_INTERFACE_DESCRIPTOR            *InterfaceDescriptor;
    EFI_USB_SUPERSPEED_ENDPOINT_DESCRIPTOR  **EndpointDescriptorTable; 
} EFI_USB_SUPERSPEED_INTERFACE_INFO;
```

## Members


<a href="" id="interfacedescriptor"></a>**InterfaceDescriptor**  
An EFI\_USB\_INTERFACE\_DESCRIPTOR structure that describes the USB function interface.

<a href="" id="endpointdescriptortable"></a>**EndpointDescriptorTable**  
An [EFI\_USB\_SUPERSPEED\_ENDPOINT\_DESCRIPTOR](efi-usb-superspeed-endpoint-descriptor.md) structure that describes the USB SuperSpeed endpoints.

## Remarks


The **EFI\_USB\_INTERFACE\_DESCRIPTOR** structure is defined in the UEFI specification version 2.3 and later. For more information, visit the [UEFI.org](http://go.microsoft.com/fwlink/p/?linkid=109526) website.

## Requirements


**Header:** User generated

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20EFI_USB_SUPERSPEED_INTERFACE_INFO%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




