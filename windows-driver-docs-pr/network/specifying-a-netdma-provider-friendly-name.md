---
title: Specifying a NetDMA Provider Friendly Name
description: Specifying a NetDMA Provider Friendly Name
ms.assetid: fe39f3e6-6e01-4342-8845-847846a2c8e5
keywords:
- NetDMA provider friendly names WDK networking
- friendly names WDK NetDMA
- NetDMA 2.0 WDK networking , friendly names
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Specifying a NetDMA Provider Friendly Name


**Note**  The NetDMA interface is not supported in Windows 8 and later.

 

## <a href="" id="ddk-specifying-a-netdma-provider-friendly-name-ng"></a>


For improved manageability and testing, NetDMA 2.0 providers and later must provide a friendly name for the provider in the **FriendlyName** member of the [**NET\_DMA\_PROVIDER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff568738) structure.

 

 





