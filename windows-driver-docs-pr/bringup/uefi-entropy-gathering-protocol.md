---
title: UEFI entropy gathering protocol
description: The UEFI entropy gathering protocol is used to produce Random Number Generation (RNG) values in a well-known manner.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 616F178F-B4A0-4B8B-B71D-F7474738EA35
---

# UEFI entropy gathering protocol


The UEFI entropy gathering protocol is used to produce Random Number Generation (RNG) values in a well-known manner.

A UEFI RNG service that implements this protocol takes an optional input value that identifies an RNG algorithm and provides a RNG value based on the input value and internal state, including the state of its entropy sources. When a Deterministic Random Bit Generator (DRBG) is used on the output of the raw entropy source, its security level must be at least 256 bits.

For guidance about the standard methods of creating the RNG values used in this protocol, see [NIST SP 800-90A Recommendations for Random Number Generation using Deterministic Random Bit Generators]( http://go.microsoft.com/fwlink/p/?LinkId=523737).

## Protocol Interface


-   [EFI\_RNG\_SERVICE\_BINDING\_PROTOCOL](efi-rng-service-binding-protocol.md)

-   [EFI\_RNG\_PROTOCOL](efi-rng-protocol.md)

-   [**EFI\_RNG\_ALGORITHM\_LIST**](efi-rng-algorithm-list.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20UEFI%20entropy%20gathering%20protocol%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




