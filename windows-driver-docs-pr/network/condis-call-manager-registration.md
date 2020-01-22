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

To register CoNDIS entry points for *ProtocolXxx* functions, call managers call the [**NdisSetOptionalHandlers**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nf-ndis-ndissetoptionalhandlers) function from the [*ProtocolSetOptions*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/nc-ndis-set_options) function. In *ProtocolSetOptions*, all CoNDIS protocol drivers initialize an [**NDIS\_PROTOCOL\_CO\_CHARACTERISTICS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_protocol_co_characteristics) structure and pass it at the *OptionalHandlers* parameter of **NdisSetOptionalHandlers**.

To specify entry points for a call manager, a protocol driver initializes an [**NDIS\_CO\_CALL\_MANAGER\_OPTIONAL\_HANDLERS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_co_call_manager_optional_handlers) structure and passes it at the *OptionalHandlers* parameter of **NdisSetOptionalHandlers**.

Miniport call managers (MCMs) also register call manager *ProtocolXxx* functions. For more information about MCM driver registration, see [CoNDIS MCM Registration](condis-mcm-registration.md).

For more information about configuring optional protocol driver services, see [Configuring Optional Protocol Driver Services](configuring-optional-protocol-driver-services.md).

 

 





