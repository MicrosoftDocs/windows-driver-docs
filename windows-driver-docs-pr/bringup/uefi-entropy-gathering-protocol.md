---
title: UEFI entropy gathering protocol
description: The UEFI entropy gathering protocol is used to produce Random Number Generation (RNG) values in a well-known manner.
ms.assetid: 616F178F-B4A0-4B8B-B71D-F7474738EA35
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# UEFI entropy gathering protocol


The UEFI entropy gathering protocol is used to produce Random Number Generation (RNG) values in a well-known manner.

A UEFI RNG service that implements this protocol takes an optional input value that identifies an RNG algorithm and provides a RNG value based on the input value and internal state, including the state of its entropy sources. When a Deterministic Random Bit Generator (DRBG) is used on the output of the raw entropy source, its security level must be at least 256 bits.

For guidance about the standard methods of creating the RNG values used in this protocol, see [NIST SP 800-90A Recommendations for Random Number Generation using Deterministic Random Bit Generators]( http://go.microsoft.com/fwlink/p/?LinkId=523737).

## Protocol Interface


-   [EFI\_RNG\_SERVICE\_BINDING\_PROTOCOL](efi-rng-service-binding-protocol.md)

-   [EFI\_RNG\_PROTOCOL](efi-rng-protocol.md)

-   [**EFI\_RNG\_ALGORITHM\_LIST**](efi-rng-algorithm-list.md)

 

 




