---
title: Disabling NFP
description: A client can temporarily disable subscriptions, publications, and presence.
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 04/20/2017
---

# Disabling NFP


A client can temporarily disable subscriptions, publications, and presence.

Temporarily disabling subscriptions, publications, and presence is done by sending [**IOCTL\_NFP\_DISABLE**](/windows-hardware/drivers/ddi/nfpdev/ni-nfpdev-ioctl_nfp_disable) to the handle. This is useful when a client wants to disable the proximity functionality but keep the resources allocated to quickly re-enable them when needed.

 

 
## Related topics
[Near field communications (NFC) API reference](/windows-hardware/drivers/ddi/_nfpdrivers/)
