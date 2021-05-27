---
title: CoNDIS MCM Registration
description: CoNDIS MCM Registration
keywords:
- MCMs WDK networking , registering CoNDIS miniport call managers
- miniport call managers WDK networking , registering CoNDIS miniport call managers
- registering miniport call managers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# CoNDIS MCM Registration





CoNDIS miniport call managers (MCMs) initialize like other miniport drivers and also must register additional CoNDIS entry points. For general information about miniport driver initialization, see [Initializing a Miniport Driver](initializing-a-miniport-driver.md).

To register CoNDIS entry points for *MiniportXxx* functions and *ProtocolXxx* functions, CoNDIS MCMs call the [**NdisSetOptionalHandlers**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndissetoptionalhandlers) function from the [*MiniportSetOptions*](/windows-hardware/drivers/ddi/ndis/nc-ndis-set_options) function. In *MiniportSetOptions*, an MCM initializes an [**NDIS\_MINIPORT\_CO\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_co_characteristics) structure and passes it at the *OptionalHandlers* parameter of **NdisSetOptionalHandlers**.

To register call manager entry points, MCMs initialize an [**NDIS\_CO\_CALL\_MANAGER\_OPTIONAL\_HANDLERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_co_call_manager_optional_handlers) structure and pass it at the *OptionalHandlers* parameter of **NdisSetOptionalHandlers**.

For more information about configuring optional miniport driver services, see [Configuring Optional Miniport Driver Services](configuring-optional-miniport-driver-services.md).

 

