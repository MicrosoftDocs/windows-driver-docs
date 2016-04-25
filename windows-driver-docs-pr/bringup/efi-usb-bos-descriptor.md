---
title: EFI\_USB\_BOS\_DESCRIPTOR
description: EFI\_USB\_BOS\_DESCRIPTOR
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: A12E3678-E5B6-4AB0-8F28-FCDA57C9D397
---

# EFI\_USB\_BOS\_DESCRIPTOR


The **EFI\_USB\_BOS\_DESCRIPTOR** structure provides information about the Binary Object Store (BOS) to the USB function driver.

## Syntax


``` syntax
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20EFI_USB_BOS_DESCRIPTOR%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




