---
title: UEFI entropy gathering protocol
description: The UEFI entropy gathering protocol is used to produce Random Number Generation (RNG) values in a well-known manner.
ms.date: 03/23/2023
---

# UEFI entropy gathering protocol

The UEFI entropy gathering protocol is used to produce Random Number Generation (RNG) values in a well-known manner.

A UEFI RNG service that implements this protocol takes an optional input value that identifies an RNG algorithm and provides a RNG value based on the input value and internal state, including the state of its entropy sources. When a Deterministic Random Bit Generator (DRBG) is used on the output of the raw entropy source, its security level must be at least 256 bits.

For guidance about the standard methods of creating the RNG values used in this protocol, see [NIST SP 800-90A Rev. 1 - Recommendations for Random Number Generation using Deterministic Random Bit Generators](https://csrc.nist.gov/publications/detail/sp/800-90a/rev-1/final).

## Protocol Interface

[EFI_RNG_SERVICE_BINDING_PROTOCOL](efi-rng-service-binding-protocol.md)

[EFI_RNG_PROTOCOL](efi-rng-protocol.md)

[EFI_RNG_ALGORITHM_LIST](efi-rng-algorithm-list.md)
