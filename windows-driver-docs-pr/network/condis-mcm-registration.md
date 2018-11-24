---
title: CoNDIS MCM Registration
description: CoNDIS MCM Registration
ms.assetid: 7dfb86c5-e7b6-4b9d-8f29-a6d247500c3e
keywords:
- MCMs WDK networking , registering CoNDIS miniport call managers
- miniport call managers WDK networking , registering CoNDIS miniport call managers
- registering miniport call managers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# CoNDIS MCM Registration





CoNDIS miniport call managers (MCMs) initialize like other miniport drivers and also must register additional CoNDIS entry points. For general information about miniport driver initialization, see [Initializing a Miniport Driver](initializing-a-miniport-driver.md).

To register CoNDIS entry points for *MiniportXxx* functions and *ProtocolXxx* functions, CoNDIS MCMs call the [**NdisSetOptionalHandlers**](https://msdn.microsoft.com/library/windows/hardware/ff564550) function from the [*MiniportSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff559443) function. In *MiniportSetOptions*, an MCM initializes an [**NDIS\_MINIPORT\_CO\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff565948) structure and passes it at the *OptionalHandlers* parameter of **NdisSetOptionalHandlers**.

To register call manager entry points, MCMs initialize an [**NDIS\_CO\_CALL\_MANAGER\_OPTIONAL\_HANDLERS**](https://msdn.microsoft.com/library/windows/hardware/ff564883) structure and pass it at the *OptionalHandlers* parameter of **NdisSetOptionalHandlers**.

For more information about configuring optional miniport driver services, see [Configuring Optional Miniport Driver Services](configuring-optional-miniport-driver-services.md).

 

 





