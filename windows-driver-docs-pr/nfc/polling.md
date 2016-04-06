---
title: NFC polling
description: NFC polling
ms.assetid: C6C531EC-59AA-4AF5-903E-A726C0E79E47
---

# NFC polling


Many NFP technologies (such as NFC) must poll in order to detect the presence of proximate devices and tags. When required, polling must be done in a power-efficient way and it must be done often enough that the NFP technology appears responsive to the user.

### Required Actions

If the NFP technology must poll, the polling MUST be done in hardware without waking any of the PC’s CPUs unless a proximate device or tag is detected. Also, the polling rate MUST be at least two times per second (every 500 ms). The recommended polling rate is 4-5 times per second.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnfpdrivers\nfpdrivers%5D:%20NFC%20polling%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




