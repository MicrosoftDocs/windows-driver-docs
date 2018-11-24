---
title: Disabling NFP
description: A client can temporarily disable subscriptions, publications, and presence.
ms.assetid: 94BE6D24-60AD-45BD-AF2D-388022114975
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Disabling NFP


A client can temporarily disable subscriptions, publications, and presence.

Temporarily disabling subscriptions, publications, and presence is done by sending [**IOCTL\_NFP\_DISABLE**](https://msdn.microsoft.com/library/windows/hardware/jj853315) to the handle. This is useful when a client wants to disable the proximity functionality but keep the resources allocated to quickly re-enable them when needed.

 

 
## Related topics
[NFC device driver interface (DDI) overview](https://msdn.microsoft.com/library/windows/hardware/mt715815)  
[Near field proximity DDI reference](https://msdn.microsoft.com/library/windows/hardware/jj866056)  

