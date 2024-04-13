---
title: CoNDIS Miniport Driver Registration
description: CoNDIS Miniport Driver Registration
keywords:
- miniport drivers WDK networking , CoNDIS
- NDIS miniport drivers WDK , CoNDIS
- registering miniport drivers
ms.date: 03/02/2023
---

# CoNDIS Miniport Driver Registration





CoNDIS miniport drivers initialize like other miniport drivers and also must register additional CoNDIS entry points. For general information about miniport driver initialization, see [Initializing a Miniport Driver](initializing-a-miniport-driver.md).

To register CoNDIS entry points for *MiniportXxx* functions, CoNDIS miniport drivers call the [**NdisSetOptionalHandlers**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndissetoptionalhandlers) function from the [*MiniportSetOptions*](/windows-hardware/drivers/ddi/ndis/nc-ndis-set_options) function. In *MiniportSetOptions*, the miniport driver initializes an [**NDIS\_MINIPORT\_CO\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_co_characteristics) structure and passes it at the *OptionalHandlers* parameter of **NdisSetOptionalHandlers**.

Miniport call managers (MCMs) also register *ProtocolXxx* functions in *MiniportSetOptions*. For more information about MCM driver registration, see [CoNDIS MCM Registration](condis-mcm-registration.md).

For more information about configuring optional miniport driver services, see [Configuring Optional Miniport Driver Services](configuring-optional-miniport-driver-services.md).

 

