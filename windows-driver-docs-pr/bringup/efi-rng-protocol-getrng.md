---
title: EFI_RNG_PROTOCOL.GetRNG
description: Retrieves a Random Number Generation (RNG) value.
ms.date: 03/23/2023
ms.topic: reference
---

# EFI_RNG_PROTOCOL.GetRNG

Retrieves a Random Number Generation (RNG) value.

## Syntax

```cpp
typedef EFI_STATUS (EFIAPI *EFI_RNG_GET_RNG) (
    IN  struct _EFI_RNG_PROTOCOL    *This,
    IN  EFI_RNG_ALGORITHM           *RNGAlgorithm, OPTIONAL
    IN  UINTN                       RNGValueLength,
    OUT UINT8                       *RNGValue
    );
```

## Parameters

*This*  
[in] A pointer to the [EFI_RNG_PROTOCOL](efi-rng-protocol.md) instance.

*RNGAlgorithm*  
[in] A pointer to the EFI_RNG_ALGORITHM which identifies the RNG algorithm to use. If this parameter is NULL, the default algorithm supported by the driver will be used.

*RNGValueLength*  
[in] The length, in bytes, of the buffer pointed to by *RNGValue*. The driver shall return exactly this many bytes.

*RNGValue*  
[out] Pointer to a buffer to fill with random bytes.

## Return value

Returns one of the following status codes.

| Status code | Description |
|--|--|
| EFI_SUCCESS | The function successfully returned an RNG value. |
| EFI_UNSUPPORTED | The algorithm specified by *RNGAlgorithm* is not supported by this driver. |
| EFI_DEVICE_ERROR | An RNG value could not be retrieved because of a hardware or firmware error. |
| EFI_NOT_READY | There is not enough entropy data available. |
| EFI_INVALID_PARAMETER | *RNGValue* is null or *RNGValueLength* is zero. |

## Requirements

**Header:** User generated
