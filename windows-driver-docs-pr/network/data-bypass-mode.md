---
title: Data Bypass Mode
description: Data Bypass Mode
keywords:
- filter drivers WDK networking , data bypass mode
- NDIS filter drivers WDK , data bypass mode
- data bypass mode WDK networking
- bypass mode WDK networking
ms.date: 04/20/2017
---

# Data Bypass Mode





The filter driver *data bypass mode* can provide improved system performance. NDIS does not call *FilterXxx* functions that are bypassed. For example, if the send and receive services are not required for a given filter application, the filter driver can bypass the send and receive functions.

A filter driver specifies the default entry points, for functions that can be bypassed, during driver initialization when it calls the [**NdisFRegisterFilterDriver**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfregisterfilterdriver) function. The entry points are **NULL** for functions that are bypassed by default. For more information about initialization, see [Initializing a Filter Driver](initializing-a-filter-driver.md).

To change the bypass state at runtime, the driver must specify an entry point for the [*FilterSetModuleOptions*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_set_module_options) function during driver initialization. The driver can initialize an [**NDIS\_FILTER\_PARTIAL\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_filter_partial_characteristics) structure and pass the new characteristics to the [**NdisSetOptionalHandlers**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndissetoptionalhandlers) function from within the context of *FilterSetModuleOptions*.

NDIS calls the *FilterSetModuleOptions* function, if any, at the start of a restart operation. A filter driver can set bypass mode independently for each filter module. For more information, see [Starting a Filter Module](starting-a-filter-module.md).

Filter drivers can bypass the following optional *FilterXxx* functions that are specified in the [**NDIS\_FILTER\_DRIVER\_CHARACTERISTICS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_filter_driver_characteristics) structure:

[*FilterSendNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_send_net_buffer_lists)

[*FilterSendNetBufferListsComplete*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_send_net_buffer_lists_complete)

[*FilterCancelSendNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_cancel_send_net_buffer_lists)

[*FilterReturnNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_return_net_buffer_lists)

[*FilterReceiveNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_receive_net_buffer_lists)

To set a *FilterXxx* function to bypass mode, a filter driver specifies **NULL** for that function's entry point. However, if a driver calls any NDIS function that has an associated *FilterXxx* function, it must provide an entry point for that *FilterXxx* function. For example, if a driver calls the [**NdisFIndicateReceiveNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfindicatereceivenetbufferlists) function, it must provide a [*FilterReturnNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_return_net_buffer_lists) function.

If a filter driver specifies a [*FilterSendNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_send_net_buffer_lists) function and it queues send requests, it must also specify a [*FilterCancelSendNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_cancel_send_net_buffer_lists) function.

If a filter driver specifies a [*FilterReceiveNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_receive_net_buffer_lists) or [**FilterReturnNetBufferLists**](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_return_net_buffer_lists) function, the driver must also specify a [*FilterStatus*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_status) function.

To change its bypass mode settings at run time, a filter driver can call the [**NdisFRestartFilter**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfrestartfilter) function. **NdisFRestartFilter** schedules a pause operation that is followed by a restart operation for the specified filter module. When NDIS calls *FilterSetModuleOptions*, the filter driver can change the functions for that filter module by calling **NdisSetOptionalHandlers** and specifying a new set of entry points.

**Note**  Pause and restart could cause some network packets to be dropped on the transmit path, or receive path, or both. Network protocols that provide a reliable transport mechanism might retry the network I/O operation in the case of a lost packet, but other protocols that do not guarantee reliability do not retry the operation.

 

A filter driver can register additional optional functions that support optional driver services. The driver registers these optional services in the [*FilterSetOptions*](/windows-hardware/drivers/ddi/ndis/nc-ndis-set_options) function. For more information about these optional services, see [Configuring Optional Filter Driver Services](configuring-optional-filter-driver-services.md).

 

