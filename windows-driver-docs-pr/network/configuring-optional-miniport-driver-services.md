---
title: Configuring Optional Miniport Driver Services
description: Configuring Optional Miniport Driver Services
keywords:
- miniport drivers WDK networking , optional services
- NDIS miniport drivers WDK , optional services
- MiniportSetOptions
- characteristics structure WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Configuring Optional Miniport Driver Services





NDIS calls a miniport driver's [*MiniportSetOptions*](/windows-hardware/drivers/ddi/ndis/nc-ndis-set_options) function to allow the driver to configure optional services. NDIS calls *MiniportSetOptions* within the context of the miniport driver's call to the [**NdisMRegisterMiniportDriver**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismregisterminiportdriver) function.

*MiniportSetOptions* registers the default entry points for optional *MiniportXxx* functions and can allocate other driver resources. To register optional *MiniportXxx* functions, the miniport driver calls the [**NdisSetOptionalHandlers**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndissetoptionalhandlers) function and passes a characteristics structure at the *OptionalHandlers* parameter.

Starting with NDIS 6.0, the valid characteristics structures include the following:

[**NDIS\_MINIPORT\_CO\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_co_characteristics)

[**NDIS\_MINIPORT\_PNP\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_pnp_characteristics)

[**NDIS\_CO\_CALL\_MANAGER\_OPTIONAL\_HANDLERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_co_call_manager_optional_handlers)

[**NDIS\_PROVIDER\_CHIMNEY\_OFFLOAD\_GENERIC\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndischimney/ns-ndischimney-_ndis_provider_chimney_offload_generic_characteristics) (see [NDIS 6.0 TCP chimney offload documentation](full-tcp-offload.md))

[**NDIS\_PROVIDER\_CHIMNEY\_OFFLOAD\_TCP\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndischimney/ns-ndischimney-_ndis_provider_chimney_offload_tcp_characteristics) (see [NDIS 6.0 TCP chimney offload documentation](full-tcp-offload.md))

Starting with NDIS 6.30, the valid characteristics structures also include the following:

[**NDIS\_MINIPORT\_SS\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_ss_characteristics)

[**NDIS\_NDK\_PROVIDER\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndisndk/ns-ndisndk-_ndis_ndk_provider_characteristics)

 

