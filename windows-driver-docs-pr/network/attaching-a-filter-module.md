---
title: Attaching a Filter Module
description: Attaching a Filter Module
ms.assetid: 4441383e-cc22-4fe1-9c46-28d405736daa
keywords:
- filter modules WDK networking , attaching
- attaching filter modules
- filter drivers WDK networking , attaching filter modules
- NDIS filter drivers WDK , attaching filter modules
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Attaching a Filter Module





To initiate the process of inserting a filter module into a driver stack, NDIS calls a filter driver's [*FilterAttach*](https://msdn.microsoft.com/library/windows/hardware/ff549905) function. At the start of execution in the *FilterAttach* function, the filter module enters the *Attaching* state. For more information about attaching a filter module to a driver stack, see [Starting a Driver Stack](starting-a-driver-stack.md).

A filter driver uses the handle, that NDIS passes at the *NdisFilterHandle* parameter of [*FilterAttach*](https://msdn.microsoft.com/library/windows/hardware/ff549905) in all future **NdisXxx** function calls that refer to this filter module. Such functions include status indications, send requests, receive indications, and OID requests.

While a filter module is in the *Attaching* state, the driver:

-   Creates a context area for the filter module and allocates buffer pools and other filter module-specific resources. For more information about buffer pools, see [Filter Driver Buffer Management](filter-driver-buffer-management.md).

-   Calls the [**NdisFSetAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff562619) function by using the *NdisFilterHandle* value that NDIS passed to [*FilterAttach*](https://msdn.microsoft.com/library/windows/hardware/ff549905). The *FilterModuleContext* parameter of **NdisFSetAttributes** specifies the filter driver's context area for this filter module. NDIS passes this context area to the filter driver's *FilterXxx* functions.

-   Optionally, reads configuration parameters for this filter module from the registry. For more information, see [Accessing Configuration Information for a Filter Driver](accessing-configuration-information-for-a-filter-driver.md).

-   If the preceding operations completed successfully, the filter module is in the *Paused* state.

-   If the preceding operations failed, the filter driver must release any resources that it allocated in the [*FilterAttach*](https://msdn.microsoft.com/library/windows/hardware/ff549905) function and return the filter module to the *Detached* state.

-   Returns NDIS\_STATUS\_SUCCESS or an appropriate failure code. If the driver returns a failure code, NDIS terminates the driver stack.

**Note**  The registry can contain a flag, which specifies that a filter module is optional. If an optional filter module does not attach, NDIS does not terminate the rest of the driver stack.

 

A filter driver cannot make send requests, indicate received data, make OID requests, or make status indications from the *Attaching* state. Send and receive operations are supported in the *Running* and *Pausing* states. OID requests and status indications are supported in the *Paused*, *Restarting*, *Running*, and *Pausing* states.

NDIS calls the [*FilterDetach*](https://msdn.microsoft.com/library/windows/hardware/ff549918) function to detach a filter module that NDIS attached with [*FilterAttach*](https://msdn.microsoft.com/library/windows/hardware/ff549905). For more information, see [Detaching a Filter Module](detaching-a-filter-module.md).

 

 





