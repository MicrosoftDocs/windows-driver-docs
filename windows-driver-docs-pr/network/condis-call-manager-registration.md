---
title: CoNDIS Call Manager Registration
description: CoNDIS Call Manager Registration
ms.assetid: 63cde3d1-122c-4411-91b6-97e97bdd2df3
keywords:
- call managers WDK networking , CoNDIS
- registering call managers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# CoNDIS Call Manager Registration





CoNDIS stand-alone call managers initialize like other protocol drivers and also must register additional CoNDIS entry points. For general information about protocol driver initialization, see [Initializing a Protocol Driver](initializing-a-protocol-driver.md).

To register CoNDIS entry points for *ProtocolXxx* functions, call managers call the [**NdisSetOptionalHandlers**](https://msdn.microsoft.com/library/windows/hardware/ff564550) function from the [*ProtocolSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff570269) function. In *ProtocolSetOptions*, all CoNDIS protocol drivers initialize an [**NDIS\_PROTOCOL\_CO\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff566817) structure and pass it at the *OptionalHandlers* parameter of **NdisSetOptionalHandlers**.

To specify entry points for a call manager, a protocol driver initializes an [**NDIS\_CO\_CALL\_MANAGER\_OPTIONAL\_HANDLERS**](https://msdn.microsoft.com/library/windows/hardware/ff564883) structure and passes it at the *OptionalHandlers* parameter of **NdisSetOptionalHandlers**.

Miniport call managers (MCMs) also register call manager *ProtocolXxx* functions. For more information about MCM driver registration, see [CoNDIS MCM Registration](condis-mcm-registration.md).

For more information about configuring optional protocol driver services, see [Configuring Optional Protocol Driver Services](configuring-optional-protocol-driver-services.md).

 

 





