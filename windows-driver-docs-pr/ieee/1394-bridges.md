---
title: 1394 Bridges
author: windows-driver-content
description: 1394 Bridges
MS-HAID:
- '1394-design\_b2027068-c43e-41d7-9600-f2fc60182fdc.xml'
- 'IEEE.1394\_bridges'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 208cceaa-dd26-46f9-b015-723c5940b02b
keywords: ["IEEE 1394 WDK buses , bridges", "1394 WDK buses , bridges", "bridges WDK IEEE 1394 bus", "1394 bridges WDK IEEE 1394 bus"]
---

# 1394 Bridges


## <a href="" id="ddk-bridges-kg"></a>


The 1394 base stack (*ohci1394.sys* and *1394bus.sys*) does not support 1394 bridge devices or bridging between multiple 1394 buses. This is because the 1394 base stack does not allow multiple bus numbers. It uses the bus number 0x3FF for all bus operations. This is the agreed standard for local bus numbers, as defined by the IEEE 1394-1995 specification.

Since bridges require that the operating system support multiple bus numbers in order to function properly, Microsoft does not guarantee that 1394 devices attached to a bridge will work.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5BIEEE\buses%5D:%201394%20Bridges%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


