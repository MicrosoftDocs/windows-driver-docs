---
title: NFC design guide
author: windows-driver-content
description: Windows exposes a rich set of experiences using NFC technology including the following platforms
ms.assetid: 26BFE25A-AC46-4634-8330-990DB447E55A
keywords: ["NFC", "near field communications", "proximity", "near field proximity", "NFP"]
---

# NFC design guide


Windows exposes a rich set of experiences using NFC technology including the following platforms:

-   Proximity Platform – Provides a platform to initiate peer-to-peer sharing of content between devices via NFC, focusing on Windows devices, as well as other NFC-compliant mobile devices as well as reading/write content to/from NFC forum compliant tags.
-   Wallet Platform – Provides the secure storage and transactional capabilities to power on-device payment scenarios, as well as brick-and-mortar payments and other NFC transactions.

To enable NFC support, Microsoft relies on IHVs to provide device drivers that implement the Device Driver Interface (DDI) defined in these topics.

Use the User-Mode Driver Framework (UMDF) 2.0 to write NFC drivers for Windows 10 for desktop editions (Home, Pro, Enterprise, and Education) and Windows 10 Mobile.

## Related topics


[Getting Started with UMDF](https://msdn.microsoft.com/library/windows/hardware/dn384105)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnfpdrivers\nfpdrivers%5D:%20NFC%20design%20guide%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





