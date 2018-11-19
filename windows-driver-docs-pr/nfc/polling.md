---
title: NFC polling
description: NFC polling
ms.assetid: C6C531EC-59AA-4AF5-903E-A726C0E79E47
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NFC polling


Many NFP technologies (such as NFC) must poll in order to detect the presence of proximate devices and tags. When required, polling must be done in a power-efficient way and it must be done often enough that the NFP technology appears responsive to the user.

### Required Actions

If the NFP technology must poll, the polling MUST be done in hardware without waking any of the PC’s CPUs unless a proximate device or tag is detected. Also, the polling rate MUST be at least two times per second (every 500 ms). The recommended polling rate is 4-5 times per second.

 

 
## Related topics
[NFC device driver interface (DDI) overview](https://msdn.microsoft.com/library/windows/hardware/mt715815)  
 

