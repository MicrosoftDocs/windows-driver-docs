---
title: CoNDIS Client Registration
description: CoNDIS Client Registration
ms.assetid: 335dd117-f6c8-4416-8527-ff64c1a5f3ee
keywords:
- client registration WDK CoNDIS
- registering entry points
- entry points WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# CoNDIS Client Registration





CoNDIS clients initialize like other protocol drivers and also must register additional CoNDIS entry points. For general information about protocol driver initialization, see [Initializing a Protocol Driver](initializing-a-protocol-driver.md).

To register CoNDIS entry points for *ProtocolXxx* functions, CoNDIS clients call the [**NdisSetOptionalHandlers**](https://msdn.microsoft.com/library/windows/hardware/ff564550) function from the [*ProtocolSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff570269) function. In *ProtocolSetOptions*, all CoNDIS protocol drivers initialize an [**NDIS\_PROTOCOL\_CO\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff566817) structure and pass it at the *OptionalHandlers* parameter of **NdisSetOptionalHandlers**.

To specify entry points for a CoNDIS client, a protocol driver initializes an [**NDIS\_CO\_CLIENT\_OPTIONAL\_HANDLERS**](https://msdn.microsoft.com/library/windows/hardware/ff564884) structure and passes it at the *OptionalHandlers* parameter of **NdisSetOptionalHandlers**.

For more information about configuring optional protocol driver services, see [Configuring Optional Protocol Driver Services](configuring-optional-protocol-driver-services.md).

 

 





