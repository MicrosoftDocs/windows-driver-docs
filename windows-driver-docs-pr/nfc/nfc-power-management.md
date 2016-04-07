---
title: NFC power management
author: windows-driver-content
description: NFC power management
ms.assetid: 7B45730F-A49D-45E0-B314-0464141E3C8B
keywords: ["NFC", "near field communications", "proximity", "near field proximity", "NFP"]
---

# NFC power management


The NFC driver shall intelligently manage the power state of the device. The following are general guidelines for IHVs that provide NFC drivers.

**Proximity power management.** If there are no active proximity publications, subscriptions, or smart card present/absent operations pending, or if the proximity radio state is disabled, then the NFC driver may deactivate the P2P and tag discovery portions of the discovery/polling loop.

**Secure element power management.** If no secure elements are exposed to readers through emulation, or if the secure element radio state is disabled, then the NFC driver may deactivate the card emulation portion of the discovery/polling loop.

**Overall power management.** If both proximity and card emulation operations are deactivated, then the NFC driver may power down the device completely by transitioning to a low power state (D3 state) using idle power management (when the system is in S0 state).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnfpdrivers\nfpdrivers%5D:%20NFC%20power%20management%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




