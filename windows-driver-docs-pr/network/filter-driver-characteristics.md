---
title: Filter Driver Characteristics
description: Filter Driver Characteristics
ms.assetid: 95e302c1-687e-4a30-b3bc-9d272c688cba
keywords:
- filter drivers WDK networking , characteristics
- NDIS filter drivers WDK , characteristics
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Filter Driver Characteristics





Filter drivers have the following characteristics:

-   An instance of a filter driver is called a *filter module*. Filter modules are attached to an underlying miniport adapter. Multiple filter modules from the same filter driver or different filter drivers can be stacked over an adapter.

-   Overlying protocol drivers are not required to provide alternate functionality when filter modules are installed between such drivers and the underlying miniport drivers (otherwise stated, filter modules are transparent to overlying protocol drivers).

-   Because filter drivers do not implement virtual miniports like an intermediate driver, filter drivers are not associated with a device object. A miniport adapter with overlying filter modules functions as a modified version of the miniport adapter. For more information about the driver stack, see [NDIS 6.0 Driver Stack](ndis-driver-stack.md).

-   NDIS uses configuration information to attach the filter modules to the adapter in the correct driver stack order. For more information about the driver stack order of filter modules, see [INF File Settings for Filter Drivers](inf-file-settings-for-filter-drivers.md).

-   NDIS can dynamically insert or delete filter modules in the driver stack, or reconfigure the filter modules, without tearing down the entire stack. For more information, see [Modifying a Running Driver Stack](modifying-a-running-driver-stack.md).

-   Protocol drivers can obtain the list of filter modules in a driver stack when NDIS restarts the driver stack.

    For more information about the list of filter modules, see [**NDIS\_PROTOCOL\_RESTART\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566844).

-   Filter drivers can filter most communication to and from the underlying miniport adapter. Filter modules are not associated with any particular binding between overlying protocol drivers and the miniport adapter. For more information about the types of filtering services that a filter driver can provide, see [Filter Driver Services](filter-driver-services.md).

-   Filter drivers can select the services that are filtered and can be bypassed for the services that are not filtered. The selection of the services that are bypassed and the services that are filtered can be reconfigured dynamically. For more information, see [Data Bypass Mode](data-bypass-mode.md).

-   NDIS guarantees the availability of context space (see [NET\_BUFFER\_LIST\_CONTEXT structure](net-buffer-list-context-structure.md)) for filter drivers. Therefore, filter drivers are not required to include the code to copy buffers to obtain context space. For more information about how to manage buffers, see [Filter Driver Buffer Management](filter-driver-buffer-management.md).

 

 





