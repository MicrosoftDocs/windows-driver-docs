---
title: Reading the Registry in an NDIS 6.0 Protocol Driver
description: Reading the Registry in an NDIS 6.0 Protocol Driver
ms.assetid: ef6d9a77-b804-4ba3-b791-25ad3e9ff4da
keywords:
- NdisOpenConfiguration
- NdisOpenConfigurationEx
- registry WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reading the Registry in an NDIS 6.0 Protocol Driver





In NDIS 6.0, the [**NdisOpenConfigurationEx**](https://msdn.microsoft.com/library/windows/hardware/ff563717) function replaces the [**NdisOpenConfiguration**](https://msdn.microsoft.com/library/windows/hardware/ff553676) function. **NdisOpenConfigurationEx** receives, as parameters, an NDIS handle and a pointer to a configuration handle.

If the driver obtained the NDIS handle passed at *NdisHandle* by calling the [**NdisRegisterProtocolDriver**](https://msdn.microsoft.com/library/windows/hardware/ff564520) function, **NdisOpenConfigurationEx** provides a configuration handle to the registry location where the protocol driver's configuration parameters are stored.

If the driver obtained the handle from the pointer at the *BindParameters* parameter of the [*ProtocolBindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570220) function, **NdisOpenConfigurationEx** provides a configuration handle to the registry location where the underlying miniport adapter configuration parameters are stored.

The protocol driver uses the configuration handle in subsequent calls to the [**NdisReadConfiguration**](https://msdn.microsoft.com/library/windows/hardware/ff564511) and [**NdisWriteConfiguration**](https://msdn.microsoft.com/library/windows/hardware/ff564659) functions. For more information about configuration functions, see [NDIS 6.0 Configuration Functions](ndis-configuration-functions.md).

 

 





