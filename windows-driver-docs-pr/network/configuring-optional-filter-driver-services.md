---
title: Configuring Optional Filter Driver Services
description: Configuring Optional Filter Driver Services
ms.assetid: 698e1b2a-de1a-435a-bc30-0d27d9e15e19
keywords:
- filter drivers WDK networking , services
- NDIS filter drivers WDK , services
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Configuring Optional Filter Driver Services





NDIS calls a filter driver's [*FilterSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff549972) function to configure optional filter driver services. NDIS calls *FilterSetOptions* within the context of the filter driver's call to the [**NdisFRegisterFilterDriver**](https://msdn.microsoft.com/library/windows/hardware/ff562608) function

*FilterSetOptions* registers the default entry points for optional *FilterXxx* functions that are required for optional services, and can allocate other driver resources. To register optional services, the filter driver calls the [**NdisSetOptionalHandlers**](https://msdn.microsoft.com/library/windows/hardware/ff564550) function and passes a characteristics structure at the *OptionalHandlers* parameter.

There are no optional filter driver services in the current Windows version.

Filter drivers can also call **NdisSetOptionalHandlers** to set the some *FilterXxx* function entry points for a given filter module. For more information, see [Data Bypass Mode](data-bypass-mode.md).

If the filter driver calls **NdisSetOptionalHandlers** from *FilterRestart*, the configuration changes only affect the filter module that NDIS is restarting. The configuration of other filter modules is not affected.

 

 





