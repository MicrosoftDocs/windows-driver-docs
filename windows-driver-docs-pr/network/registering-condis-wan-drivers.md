---
title: Registering CoNDIS WAN Drivers
description: Registering CoNDIS WAN Drivers
keywords:
- CoNDIS WAN drivers WDK networking , registering
- NdisMRegisterMiniportDriver
- registering CoNDIS WAN drivers
ms.date: 03/02/2023
---

# Registering CoNDIS WAN Drivers





A CoNDIS WAN miniport driver or MCM calls [**NdisMRegisterMiniportDriver**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismregisterminiportdriver) from its [**DriverEntry**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) function to register its standard *MiniportXxx* functions with NDIS. For more information about registering *MiniportXxx* functions, see [Initializing a Miniport Driver](initializing-a-miniport-driver.md).

A CoNDIS WAN call manager is an NDIS protocol driver. As such, a call manager calls [**NdisRegisterProtocolDriver**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisregisterprotocoldriver) to register its standard *ProtocolXxx* functions. For more information about registering an NDIS protocol driver, see [Initializing a Protocol Driver](initializing-a-protocol-driver.md). For information about other differences between call manager initialization and MCM initialization, see [Differences in Initialization](differences-in-initialization.md).

The call to **NdisMRegisterMiniportDriver** provides an NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS structure from the miniport driver. You must specify the correct NDIS version number. For more information about setting the NDIS version number, see [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_driver_characteristics).

CoNDIS WAN drivers must indicate NDIS version 5.0 or later.

NDIS 6.0 and later drivers must register CoNDIS callback functions as follows:

-   To register CoNDIS *ProtocolXxx* and *MiniportXxx* functions, all CoNDIS drivers must call the [**NdisSetOptionalHandlers**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndissetoptionalhandlers) function.

-   To register its CoNDIS *MiniportXxx* functions, a miniport driver or miniport call manager (MCM) must call the **NdisSetOptionalHandlers** function from its [*MiniportSetOptions*](/windows-hardware/drivers/ddi/ndis/nc-ndis-set_options) function and pass it an [**NDIS\_MINIPORT\_CO\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_co_characteristics) structure. To register call manager *ProtocolXxx* functions, MCMs also provide an [**NDIS\_CO\_CALL\_MANAGER\_OPTIONAL\_HANDLERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_co_call_manager_optional_handlers) structure.

-   To register its CoNDIS *ProtocolXxx* functions, a client or call managers must call the [**NdisSetOptionalHandlers**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndissetoptionalhandlers) function from its [*ProtocolSetOptions*](/windows-hardware/drivers/ddi/ndis/nc-ndis-set_options) function and must provide an [**NDIS\_PROTOCOL\_CO\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_protocol_co_characteristics) structure. Clients must also provide an [**NDIS\_CO\_CLIENT\_OPTIONAL\_HANDLERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_co_client_optional_handlers) structure and call managers must also provide an [**NDIS\_CO\_CALL\_MANAGER\_OPTIONAL\_HANDLERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_co_call_manager_optional_handlers) structure.

For more information about CoNDIS driver registration, see [CoNDIS Registration](condis-miniport-driver-registration.md).

.

 

