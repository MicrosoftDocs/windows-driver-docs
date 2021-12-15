---
title: NFC polling
description: NFC polling
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 04/20/2017
---

# NFC polling


Many NFP technologies (such as NFC) must poll in order to detect the presence of proximate devices and tags. When required, polling must be done in a power-efficient way and it must be done often enough that the NFP technology appears responsive to the user.

### Required Actions

If the NFP technology must poll, the polling MUST be done in hardware without waking any of the PC’s CPUs unless a proximate device or tag is detected. Also, the polling rate MUST be at least two times per second (every 500 ms). The recommended polling rate is 4-5 times per second.

 

 
## Related topics
[NFC device driver interface (DDI) overview](/windows-hardware/drivers/ddi/index)  
