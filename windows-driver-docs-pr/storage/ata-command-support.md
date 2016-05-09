---
title: ATA Command Support
description: ATA Command Support
ms.assetid: 98149A59-3435-4166-8250-EEFBA44DFD4C
---

# ATA Command Support


If a storage device supports the ATA command set, StorPort will send ATA commands directly to a target device using the ATA passthrough control codes. Device management applications can use the [**IOCTL\_ATA\_PASS\_THROUGH**](https://msdn.microsoft.com/library/windows/hardware/ff559309) and [**IOCTL\_ATA\_PASS\_THROUGH\_DIRECT**](https://msdn.microsoft.com/library/windows/hardware/ff559315) control codes for this purpose.

This section contains information about special requirements for issuing certain ATA command requests.

[Security Group Commands](security-group-commands.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20ATA%20Command%20Support%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




