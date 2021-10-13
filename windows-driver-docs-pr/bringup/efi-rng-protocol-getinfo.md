---
title: EFI_RNG_PROTOCOL.GetInfo
description: Returns information about the RNG algorithms supported by a driver that implements EFI_RNG_PROTOCOL.
ms.date: 08/20/2021
ms.localizationpriority: medium
---

# EFI_RNG_PROTOCOL.GetInfo

Returns information about the RNG algorithms supported by a driver that implements EFI_RNG_PROTOCOL.

## Syntax

```cpp
typedef
EFI_STATUS
(EFIAPI *EFI_RNG_GET_INFO) (
    IN  struct _EFI_RNG_PROTOCOL    *This,
    IN  OUT UINTN                   *RNGAlgorithmListSize,
    OUT EFI_RNG_ALGORITHM           *RNGAlgorithmList
    );
```

## Parameters

*This*  
[in] A pointer to the [EFI_RNG_PROTOCOL](efi-rng-protocol.md) instance.

*RNGAlgorithmListSize*  
[in, out] The number of algorithms in *RNGAlgorithmList*.

*RNGAlgorithmList*  
[out] A pointer to a list of [EFI_RNG_ALGORITHM](efi-display-power-state.md) values that represent RNG algorithms. Each algorithm is `sizeof(EFI_GUID)` bytes long.

## Remarks

A driver that implements EFI_RNG_PROTOCOL can support one or more RNG algorithms.

The value returned by the *RNGAlgorithmList* parameter must not change across multiple calls to the same driver. The first algorithm in the list is the default algorithm for the driver.

The list of algorithms is allocated by this function using EFI_BOOT_SERVICES-&gt;AllocatePool(), and it is the caller's responsibility to free this list by using EFI_BOOT_SERVICES-&gt;FreePool().

## Return value

Returns one of the following status codes.

| Status code | Description |
|--|--|
| EFI_SUCCESS | The function successfully retrieved the list of RNG algorithms. |
| EFI_UNSUPPORTED | The service is not supported by this driver. |
| EFI_DEVICE_ERROR | The list of RNG algorithms could not be retrieved because of a hardware or firmware error. |
| EFI_OUT_OF_RESOURCES | The driver is unable to allocate memory for the *RNGAlgorithmList* parameter. |

## Requirements

**Header:** User generated
