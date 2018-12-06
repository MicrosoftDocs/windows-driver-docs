---
title: Initializing a TCP Chimney-Capable Intermediate Driver
description: Initializing a TCP Chimney-Capable Intermediate Driver
ms.assetid: dbe6226b-fa0f-4365-9044-488deedd27b6
keywords:
- intermediate drivers WDK TCP chimney offload , initializing
- initializing TCP chimney-capable intermediate drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Initializing a TCP Chimney-Capable Intermediate Driver


\[The TCP chimney offload feature is deprecated and should not be used.\]

A TCP chimney-capable intermediate driver follows the initialization sequence for an NDIS 6.0 intermediate driver. For more information about this sequence, see [Initializing an Intermediate Driver](initializing-an-intermediate-driver.md).

In addition to registering its base *MiniportXxx* and *ProtocolXxx* functions, a TCP chimney-capable intermediate driver must register *MiniportXxx* chimney functions and *ProtocolXxx* chimney functions, as described in the following topics:

[Registering an Intermediate Driver's MiniportXxx Chimney Functions](registering-an-intermediate-driver-s-miniportxxx-chimney-functions.md)

[Registering an Intermediate Driver's ProtocolXxx Chimney Functions](registering-an-intermediate-driver-s-protocolxxx-chimney-functions.md)

If an intermediate driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function returns NDIS\_STATUS\_SUCCESS, NDIS and the host stack query the operational characteristics of the offload target. For more information about this query, see [Querying and Setting an Intermediate Driver's TCP Chimney Offload Capabilities](querying-and-setting-an-intermediate-driver-s-tcp-chimney-offload-capa.md).

 

 





