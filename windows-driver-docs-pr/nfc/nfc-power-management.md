---
title: NFC power management
description: NFC power management
ms.assetid: 7B45730F-A49D-45E0-B314-0464141E3C8B
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NFC power management


The NFC driver shall intelligently manage the power state of the device. The following are general guidelines for IHVs that provide NFC drivers.

**Proximity power management.** If there are no active proximity publications, subscriptions, or smart card present/absent operations pending, or if the proximity radio state is disabled, then the NFC driver may deactivate the P2P and tag discovery portions of the discovery/polling loop.

**Secure element power management.** If no secure elements are exposed to readers through emulation, or if the secure element radio state is disabled, then the NFC driver may deactivate the card emulation portion of the discovery/polling loop.

**Overall power management.** If both proximity and card emulation operations are deactivated, then the NFC driver may power down the device completely by transitioning to a low power state (D3 state) using idle power management (when the system is in S0 state).

 

 
## Related topics
[NFC device driver interface (DDI) overview](https://msdn.microsoft.com/library/windows/hardware/mt715815)  


