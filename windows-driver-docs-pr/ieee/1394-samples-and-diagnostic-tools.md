---
title: 1394 Samples and Diagnostic Tools
description: 1394 Samples and Diagnostic Tools
MS-HAID:
- '1394api\_46afb449-6fac-4660-9113-ee829ca69fed.xml'
- 'IEEE.1394\_samples\_and\_diagnostic\_tools'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: e3ce71da-8c24-405b-b734-98a8c4f45e6b
keywords: ["IEEE 1394 WDK buses , samples", "1394 WDK buses , samples", "IEEE 1394 WDK buses , diagnostic tools", "1394 WDK buses , diagnostic tools", "sample drivers WDK IEEE 1394 bus"]
---

# 1394 Samples and Diagnostic Tools


The Windows Driver Kit (WDK) includes the source code for two sample kernel-mode drivers (*1394vdev.sys* and *1394diag.sys*) and diagnostic software that permits driver writers to communicate with the IEEE 1394 stack from user-mode.

The driver source code illustrates how drivers communicate with the upper edge of the IEEE 1394 stack. In addition to asynchronous and isochronous data transfers, the sample source code demonstrates the proper management of Plug and Play (PnP) and power management I/O Request Packets (IRPs).

The system enumerates *1394vdev.sys* and *1394diag.sys* differently. The 1394vdev.sys driver is a virtual diagnostic driver that the IEEE 1394 bus driver loads when it receives an IOCTL\_IEEE1394\_API\_REQUEST request. The *1394diag.sys* driver is a physical diagnostic device driver that the IEEE 1394 bus driver loads when an IEEE 1394 hardware device is plugged into the PC. *1394vdev.inf*, which is included in the WDK, loads both of these drivers.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5BIEEE\buses%5D:%201394%20Samples%20and%20Diagnostic%20Tools%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




