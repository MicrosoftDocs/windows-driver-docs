---
title: Configuring Optional Filter Driver Services
description: Configuring Optional Filter Driver Services
keywords:
- filter drivers WDK networking , services
- NDIS filter drivers WDK , services
ms.date: 04/20/2017
---

# Configuring Optional Filter Driver Services





NDIS calls a filter driver's [*FilterSetOptions*](/windows-hardware/drivers/ddi/ndis/nc-ndis-set_options) function to configure optional filter driver services. NDIS calls *FilterSetOptions* within the context of the filter driver's call to the [**NdisFRegisterFilterDriver**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfregisterfilterdriver) function

*FilterSetOptions* registers the default entry points for optional *FilterXxx* functions that are required for optional services, and can allocate other driver resources. To register optional services, the filter driver calls the [**NdisSetOptionalHandlers**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndissetoptionalhandlers) function and passes a characteristics structure at the *OptionalHandlers* parameter.

There are no optional filter driver services in the current Windows version.

Filter drivers can also call **NdisSetOptionalHandlers** to set the some *FilterXxx* function entry points for a given filter module. For more information, see [Data Bypass Mode](data-bypass-mode.md).

If the filter driver calls **NdisSetOptionalHandlers** from *FilterRestart*, the configuration changes only affect the filter module that NDIS is restarting. The configuration of other filter modules is not affected.

 

