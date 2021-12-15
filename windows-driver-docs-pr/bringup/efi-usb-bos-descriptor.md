---
title: EFI_USB_BOS_DESCRIPTOR
description: Provides information about the Binary Object Store (BOS) to the USB function driver.
ms.date: 08/20/2021
---

# EFI_USB_BOS_DESCRIPTOR

The **EFI_USB_BOS_DESCRIPTOR** structure provides information about the Binary Object Store (BOS) to the USB function driver.

## Syntax

```cpp
typedef struct
{
    UINT8   Length;
    UINT8   DescriptorType;
    UINT16  TotalLength;
    UINT8   NumDeviceCaps;
} EFI_USB_BOS_DESCRIPTOR;
```

## Members

**Length**  
The size of the descriptor.

**DescriptorType**  
The BOS descriptor type.

**TotalLength**  
The length of this descriptor and all of its sub descriptors.

**NumDeviceCaps**  
The number of separate device capability descriptors in the BOS.

## Requirements

**Header:** User generated
