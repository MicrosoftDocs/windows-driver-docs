---
title: Reading the Registry in an NDIS 6.0 Miniport Driver
description: Reading the Registry in an NDIS 6.0 Miniport Driver
ms.assetid: e6b61d7e-ef69-4f18-aaa0-5792f7516fb4
keywords:
- reading registry WDK networking
- registry WDK networking
- miniport adapters WDK networking , reading registry
- adapters WDK networking , reading registry
- porting miniport drivers WDK networking , adapters
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reading the Registry in an NDIS 6.0 Miniport Driver





The [**NdisOpenConfigurationEx**](https://msdn.microsoft.com/library/windows/hardware/ff563717) function replaces the [**NdisOpenConfiguration**](https://msdn.microsoft.com/library/windows/hardware/ff553676) function. **NdisOpenConfigurationEx** receives as parameters an NDIS handle and a pointer to a configuration handle.

If the driver obtained the NDIS handle passed at *NdisHandle* by calling the [**NdisMRegisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563654) function, **NdisOpenConfigurationEx** provides a configuration handle to the registry location where the miniport driver's configuration parameters are stored.

If the driver obtained the handle passed at *NdisHandle* from the *MiniportAdapterHandle* parameter of the [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function, **NdisOpenConfigurationEx** provides a configuration handle to the registry location where a miniport adapter's configuration parameters are stored.

The miniport driver uses the configuration handle in subsequent calls to the [**NdisReadConfiguration**](https://msdn.microsoft.com/library/windows/hardware/ff564511) and [**NdisWriteConfiguration**](https://msdn.microsoft.com/library/windows/hardware/ff564659) functions. For more information, see [NDIS 6.0 Configuration Functions](ndis-configuration-functions.md).

 

 





