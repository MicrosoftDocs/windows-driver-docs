---
title: EFI_USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR
description: The EFI_USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR structure provides the SuperSpeed Endpoint Companion descriptor to the USB function driver.
ms.date: 02/24/2023
ms.topic: reference
---

# EFI_USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR

The **EFI_USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR** structure provides the SuperSpeed Endpoint Companion descriptor to the USB function driver.

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

**Length**
The size of this descriptor in bytes.

**DescriptorType**
Specifies the descriptor type. Must be set to SUPERSPEED_USB_ENDPOINT_COMPANION.

**MaxBurst**
The maximum number of packets the endpoint can send or receive as part of a burst.

**AsUchar**
Specifies the length of the structures.

**MaxStreams**
Specifies the maximum number of streams supported by the bulk endpoint.

**Reserved1**
Reserved. Do not use.

**BytesPerInterval**
The total number of bytes this endpoint will transfer every service interval (SI).

## Requirements

**Header:** User generated
