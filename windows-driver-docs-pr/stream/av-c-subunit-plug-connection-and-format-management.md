---
title: AV/C Subunit Plug Connection and Format Management
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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# AV/C Subunit Plug Connection and Format Management





The AV/C peer subunit driver stack provides functions for IEEE 1394 and AV/C subunit plug connection and format management. Kernel streaming (KS) pin format negotiation and pin connection mechanisms are translated to plug connections through *Avc.sys*. Some key aspects of this architecture include:

-   IEEE 1394 and AV/C subunit plug connections are represented as KS pin connections in DirectShow filter-graphs.

-   IEEE 1394 serial bus plugs (input and output plugs) are directly represented as KS pins only when there is no internal subunit plug connection capability. When this occurs, there is one pin per IEEE 1394 serial bus plug.

-   A medium globally unique identifier (GUID) represents IEEE 1394 serial bus connections. For more information about medium GUIDs, see [Mediums and Categories](mediums-and-categories.md).

-   Medium GUIDs for permanent internal AV/C unit and subunit connections are synthesized from the device-unique identifier and plug addresses.

-   There are new KSDATARANGE and KSDATAFORMAT extensions to use with AV/C connections.

The mediums and formats together help to determine whether a KS pin connection represents data to and from the computer over the IEEE 1394 serial bus or internal to a device.

 

 




