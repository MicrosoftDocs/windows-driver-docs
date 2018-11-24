---
title: EFI_USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR
description: EFI_USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR
ms.assetid: 5449A10A-17BC-40CB-A8FC-19F867CFC9D0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_USB\_SUPERSPEED\_ENDPOINT\_COMPANION\_DESCRIPTOR


The **EFI\_USB\_SUPERSPEED\_ENDPOINT\_COMPANION\_DESCRIPTOR** structure provides the SuperSpeed Endpoint Companion descriptor to the USB function driver.

## Syntax


```cpp
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

 

 




