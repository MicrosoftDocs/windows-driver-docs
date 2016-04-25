---
title: EFI\_RNG\_PROTOCOL
description: The EFI\_RNG\_PROTOCOL is used to obtain a Random Number Generation (RNG) value from an EFI driver.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 927E2C40-973B-49AB-ACD5-2A3532827D74
---

# EFI\_RNG\_PROTOCOL


The EFI\_RNG\_PROTOCOL is used to obtain a Random Number Generation (RNG) value from an EFI driver.

## Syntax


``` syntax
#define EFI_RNG_PROTOCOL_GUID \
  {0x3152bca5, 0xeade, 0x433d, 0x86, 0x2e, 0xc0, 0x1c, 0xdc, 0x29, 0x1f, 0x44};

typedef struct _EFI_RNG_PROTOCOL {
    EFI_RNG_GET_INFO    GetInfo;
    EFI_RNG_GET_RNG     GetRNG;
} EFI_RNG_PROTOCOL;
```

## Members


<a href="" id="getinfo"></a>**GetInfo**  
Returns information about the RNG algorithms the driver supports. For more information, see [EFI\_RNG\_PROTOCOL.GetInfo](efi-rng-protocol-getinfo.md).

<a href="" id="getrng"></a>**GetRNG**  
Returns an RNG value using an optional RNG algorithm. For more information, see [EFI\_RNG\_PROTOCOL.GetRNG](efi-rng-protocol-getrng.md).

## Requirements


**Header:** User generated

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20EFI_RNG_PROTOCOL%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




