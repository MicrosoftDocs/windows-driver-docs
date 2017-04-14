---
title: Introducing Threats to a BDA Minidriver
author: windows-driver-content
description: Introducing Threats to a BDA Minidriver
ms.assetid: 5dabf93a-9a85-4791-958c-59c8e0a99cf4
keywords: ["Broadcast Driver Architecture WDK AVStream , security", "BDA WDK AVStream , security", "security WDK BDA"]
---

# Introducing Threats to a BDA Minidriver


## <a href="" id="ddk-introducing-threats-to-a-bda-minidriver-ksg"></a>


The following paths can possibly introduce BDA minidriver threats:

1.  Signal transport stream.

2.  Special-purpose IOCTLs.

3.  Direct WDM dispatch routines.

The following diagram shows how BDA minidriver threats can be introduced:

![diagram illustrating how bda minidriver threats can be introduced](images/bdathret.png)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Introducing%20Threats%20to%20a%20BDA%20Minidriver%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


