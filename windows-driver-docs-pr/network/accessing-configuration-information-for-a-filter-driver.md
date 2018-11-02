---
title: Accessing Configuration Information for a Filter Driver
description: Accessing Configuration Information for a Filter Driver
ms.assetid: 7d6bd7d4-3c06-4fc3-874b-fb8369ac227e
keywords:
- filter drivers WDK networking , configuration information
- NDIS filter drivers WDK , configuration information
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Accessing Configuration Information for a Filter Driver





NDIS supports a set of functions that provide access to filter driver registry parameters. Filter drivers can access these parameters during the attach or restart operations or when they are processing a Plug and Play (PnP) notification. For more information about PnP notifications, see [Filter Module PnP Event Notifications](filter-module-pnp-event-notifications.md). For more information about attaching a filter module, see [Attaching a Filter Module](attaching-a-filter-module.md). For more information about restart operations, see [Starting a Filter Module](starting-a-filter-module.md).

Filter drivers call the [**NdisOpenConfigurationEx**](https://msdn.microsoft.com/library/windows/hardware/ff563717) function to access the registry settings. If a filter driver obtained the handle in the **NdisHandle** member of the [**NDIS\_CONFIGURATION\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff564866) structure by calling the [**NdisFRegisterFilterDriver**](https://msdn.microsoft.com/library/windows/hardware/ff562608) function, the **NdisOpenConfigurationEx** function provides a handle to the registry location where the filter driver's configuration parameters are stored. Filter drivers can use the configuration handle until they call the [**NdisFDeregisterFilterDriver**](https://msdn.microsoft.com/library/windows/hardware/ff561800) function.

If a filter driver obtained the handle in **NdisHandle** from the *NdisFilterHandle* parameter of the [*FilterAttach*](https://msdn.microsoft.com/library/windows/hardware/ff549905) function, [**NdisOpenConfigurationEx**](https://msdn.microsoft.com/library/windows/hardware/ff563717) provides a handle to the registry location where a filter module's configuration parameters are stored. The filter driver can use the configuration handle until NDIS detaches the filter module and the [*FilterDetach*](https://msdn.microsoft.com/library/windows/hardware/ff549918) function returns. If a monitoring filter driver specifies the NDIS\_CONFIG\_FLAG\_FILTER\_INSTANCE\_CONFIGURATION flag in the **Flags** member of the [**NDIS\_CONFIGURATION\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff564866) structure, the driver can access the filter module configuration for a specific filter module when there are multiple filter modules that are configured over the same miniport adapter. Modifying filter drivers must not use this flag.

After a driver is done accessing the configuration information, the driver must call the [**NdisCloseConfiguration**](https://msdn.microsoft.com/library/windows/hardware/ff561642) function to release the configuration handle and related resources.

 

 





