---
title: EFI_USB_BOS_DESCRIPTOR
description: EFI_USB_BOS_DESCRIPTOR
ms.assetid: A12E3678-E5B6-4AB0-8F28-FCDA57C9D397
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_USB\_BOS\_DESCRIPTOR


The **EFI\_USB\_BOS\_DESCRIPTOR** structure provides information about the Binary Object Store (BOS) to the USB function driver.

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


<a href="" id="length"></a>**Length**  
The size of the descriptor.

<a href="" id="descriptortype"></a>**DescriptorType**  
The BOS descriptor type.

<a href="" id="totallength"></a>**TotalLength**  
The length of this descriptor and all of its sub descriptors.

<a href="" id="numdevicecaps"></a>**NumDeviceCaps**  
The number of separate device capability descriptors in the BOS.

## Requirements


**Header:** User generated

 

 




