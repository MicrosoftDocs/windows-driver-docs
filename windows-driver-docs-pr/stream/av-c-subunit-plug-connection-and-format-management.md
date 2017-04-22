---
title: AV/C Subunit Plug Connection and Format Management
author: windows-driver-content
description: AV/C Subunit Plug Connection and Format Management
ms.assetid: c80641d5-3108-4dbc-91b9-7ed295434b97
keywords:
- plug connections WDK AV/C
- subunit support WDK AV/C
- AV/C WDK , plug connections
- peer subunit driver stacks WDK AV/C
- KS pin connections WDK AV/C
- pin connections WDK AV/C
- formats WDK AV/C
- pin formats WDK AV/C
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# AV/C Subunit Plug Connection and Format Management


## <a href="" id="ddk-av-c-subunit-plug-connection-and-format-management-ksg"></a>


The AV/C peer subunit driver stack provides functions for IEEE 1394 and AV/C subunit plug connection and format management. Kernel streaming (KS) pin format negotiation and pin connection mechanisms are translated to plug connections through *Avc.sys*. Some key aspects of this architecture include:

-   IEEE 1394 and AV/C subunit plug connections are represented as KS pin connections in DirectShow filter-graphs.

-   IEEE 1394 serial bus plugs (input and output plugs) are directly represented as KS pins only when there is no internal subunit plug connection capability. When this occurs, there is one pin per IEEE 1394 serial bus plug.

-   A medium globally unique identifier (GUID) represents IEEE 1394 serial bus connections. For more information about medium GUIDs, see [Mediums and Categories](mediums-and-categories.md).

-   Medium GUIDs for permanent internal AV/C unit and subunit connections are synthesized from the device-unique identifier and plug addresses.

-   There are new KSDATARANGE and KSDATAFORMAT extensions to use with AV/C connections.

The mediums and formats together help to determine whether a KS pin connection represents data to and from the computer over the IEEE 1394 serial bus or internal to a device.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20AV/C%20Subunit%20Plug%20Connection%20and%20Format%20Management%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


