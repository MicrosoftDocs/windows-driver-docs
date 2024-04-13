---
title: Configuring Optional Protocol Driver Services
description: Configuring Optional Protocol Driver Services
keywords:
- protocol drivers WDK networking , optional services
- NDIS protocol drivers WDK , optional services
ms.date: 04/20/2017
---

# Configuring Optional Protocol Driver Services





NDIS calls a protocol driver's [*ProtocolSetOptions*](/windows-hardware/drivers/ddi/ndis/nc-ndis-set_options) function to allow a protocol driver to configure optional services. NDIS calls *ProtocolSetOptions* within the context of the protocol driver's call to the [**NdisRegisterProtocolDriver**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisregisterprotocoldriver) function

*ProtocolSetOptions* registers default entry points for optional *ProtocolXxx* functions and can allocate other driver resources. To register optional *ProtocolXxx* functions, the protocol driver calls the [**NdisSetOptionalHandlers**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndissetoptionalhandlers) function and passes a characteristics structure at the *OptionalHandlers* parameter. In this case, the protocol driver passes the handle from the *NdisDriverHandle* parameter of *ProtocolSetOptions* at the *NdisHandle* parameter of **NdisSetOptionalHandlers**.

A protocol driver can also call **NdisSetOptionalHandlers** from the [*ProtocolBindAdapterEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_bind_adapter_ex) function or the [*ProtocolOpenAdapterCompleteEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_open_adapter_complete_ex) function after the protocol driver has a valid handle from the [**NdisOpenAdapterEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisopenadapterex) function. In this case, the protocol driver passes the handle from the *NdisBindingHandle* parameter of **NdisOpenAdapterEx** at the *NdisHandle* parameter of **NdisSetOptionalHandlers**.

In this case, the valid characteristics structures are:

[**NDIS\_PROTOCOL\_CO\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_protocol_co_characteristics)

[**NDIS\_CO\_CLIENT\_OPTIONAL\_HANDLERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_co_client_optional_handlers)

[**NDIS\_CO\_CALL\_MANAGER\_OPTIONAL\_HANDLERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_co_call_manager_optional_handlers)

NDIS\_CLIENT\_CHIMNEY\_OFFLOAD\_GENERIC\_CHARACTERISTICS (see [NDIS 6.0 TCP chimney offload documentation](full-tcp-offload.md))

NDIS\_CLIENT\_CHIMNEY\_OFFLOAD\_TCP\_CHARACTERISTICS (see [NDIS 6.0 TCP chimney offload documentation](full-tcp-offload.md))

 

