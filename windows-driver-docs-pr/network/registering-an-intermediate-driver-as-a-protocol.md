---
title: Registering an Intermediate Driver as a Protocol
description: Registering an Intermediate Driver as a Protocol
ms.assetid: 79707f6b-0e31-46a8-a763-fa2669ce9635
keywords:
- registering intermediate drivers
- intermediate drivers WDK networking , registering
- NDIS intermediate drivers WDK , registering
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registering an Intermediate Driver as a Protocol





An intermediate driver registers its *ProtocolXxx* functions with NDIS in the context of its [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) function by calling [**NdisRegisterProtocolDriver**](https://msdn.microsoft.com/library/windows/hardware/ff564520).

Registering an intermediate driver as a protocol is nearly identical to registering as a protocol driver. For more information, see [Initializing a Protocol Driver](initializing-a-protocol-driver.md).

An intermediate driver with a connection-oriented lower edge must register as a connection-oriented client. A connection-oriented client uses the call-set-up and tear-down services of a call manager or integrated miniport call manager (MCM). A connection-oriented client also uses the send and receive capabilities of a connection-oriented miniport driver or an MCM to send and receive data. For more information, see [Connection-Oriented Operations Performed by Clients](connection-oriented-operations-performed-by-clients.md).

An intermediate driver might require other *ProtocolXxx* functions that are implementation specific. For information about registering optional *ProtocolXxx* functions, see [Configuring Optional Protocol Driver Services](configuring-optional-protocol-driver-services.md).

 

 





