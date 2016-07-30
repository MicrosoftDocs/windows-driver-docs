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


