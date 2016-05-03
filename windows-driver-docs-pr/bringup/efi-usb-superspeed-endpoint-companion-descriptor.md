---
title: EFI\_USB\_SUPERSPEED\_ENDPOINT\_COMPANION\_DESCRIPTOR
author: windows-driver-content
description: EFI\_USB\_SUPERSPEED\_ENDPOINT\_COMPANION\_DESCRIPTOR
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 5449A10A-17BC-40CB-A8FC-19F867CFC9D0
---

# EFI\_USB\_SUPERSPEED\_ENDPOINT\_COMPANION\_DESCRIPTOR


The **EFI\_USB\_SUPERSPEED\_ENDPOINT\_COMPANION\_DESCRIPTOR** structure provides the SuperSpeed Endpoint Companion descriptor to the USB function driver.

## Syntax


``` syntax
typedef struct
{
    UINT8          Length;
    UINT8          DescriptorType;
    UINT8          MaxBurst;
    union
    {
        UINT8      AsUchar;
        struct
        {
            UINT8  MaxStreams:5;
            UINT8  Reserved1:3;
        }          Bulk;
    }              Attributes;
    UINT16         BytesPerInterval;
} EFI_USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR;
```

## Members


<a href="" id="length"></a>**Length**  
The size of this descriptor in bytes.

<a href="" id="descriptortype"></a>**DescriptorType**  
Specifies the descriptor type. Must be set to SUPERSPEED\_USB\_ENDPOINT\_COMPANION.

<a href="" id="maxburst"></a>**MaxBurst**  
The maximum number of packets the endpoint can send or receive as part of a burst.

<a href="" id="asuchar"></a>**AsUchar**  
Specifies the length of the structures.

<a href="" id="maxstreams"></a>**MaxStreams**  
Specifies the maximum number of streams supported by the bulk endpoint.

<a href="" id="reserved1"></a>**Reserved1**  
Reserved. Do not use.

<a href="" id="bytesperinterval"></a>**BytesPerInterval**  
The total number of bytes this endpoint will transfer every service interval (SI).

## Requirements


**Header:** User generated

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20EFI_USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


