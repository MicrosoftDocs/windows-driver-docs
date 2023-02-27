---
title: EFI_RNG_PROTOCOL
description: The EFI_RNG_PROTOCOL is used to obtain a Random Number Generation (RNG) value from an EFI driver.
ms.date: 02/24/2023
ms.topic: reference
---

# EFI_RNG_PROTOCOL

The EFI_RNG_PROTOCOL is used to obtain a Random Number Generation (RNG) value from an EFI driver.

## Syntax

```cpp
#define EFI_RNG_PROTOCOL_GUID \
  {0x3152bca5, 0xeade, 0x433d, 0x86, 0x2e, 0xc0, 0x1c, 0xdc, 0x29, 0x1f, 0x44};

typedef struct _EFI_RNG_PROTOCOL {
    EFI_RNG_GET_INFO    GetInfo;
    EFI_RNG_GET_RNG     GetRNG;
} EFI_RNG_PROTOCOL;
```

## Members

**GetInfo**  
Returns information about the RNG algorithms the driver supports. For more information, see [EFI_RNG_PROTOCOL.GetInfo](efi-rng-protocol-getinfo.md).

**GetRNG**  
Returns an RNG value using an optional RNG algorithm. For more information, see [EFI_RNG_PROTOCOL.GetRNG](efi-rng-protocol-getrng.md).

## Requirements

**Header:** User generated
