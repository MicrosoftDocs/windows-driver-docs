---
title: Supporting WMI Data Blocks and Events in your Driver
description: Supporting WMI Data Blocks and Events in Your Driver
keywords:
- WMI WDK KMDF , data blocks
- WMI WDK KMDF , events
- read/write WMI data blocks WDK KMDF
- read-only WMI data blocks WDK KMDF
- events WDK KMDF , WMI
- tracing WDK KMDF
ms.date: 04/20/2017
---

# Supporting WMI Data Blocks and Events in Your Driver


\[Applies to KMDF only\]

Framework-based drivers support WMI data blocks by providing event callback functions. Drivers support WMI events by calling an object method that sends an event to WMI clients.

### <a href="" id="supporting-read-write-wmi-data-blocks"></a> Supporting Read/Write WMI Data Blocks

If the information in a WMI data block is both readable and writeable by WMI clients, the driver must provide an [*EvtWmiInstanceQueryInstance*](/windows-hardware/drivers/ddi/wdfwmi/nc-wdfwmi-evt_wdf_wmi_instance_query_instance) callback function that services a client's read requests, plus [*EvtWmiInstanceSetInstance*](/windows-hardware/drivers/ddi/wdfwmi/nc-wdfwmi-evt_wdf_wmi_instance_set_instance) or [*EvtWmiInstanceSetItem*](/windows-hardware/drivers/ddi/wdfwmi/nc-wdfwmi-evt_wdf_wmi_instance_set_item) callback functions (or both) that service a client's write requests.

If the data block contains methods that the driver executes at the client's request, the driver must also provide an [*EvtWmiInstanceExecuteMethod*](/windows-hardware/drivers/ddi/wdfwmi/nc-wdfwmi-evt_wdf_wmi_instance_execute_method) callback function.

If a WMI data block is write-only (that is, WMI clients can write information to the data block but cannot read the data block), the driver does not provide an [*EvtWmiInstanceQueryInstance*](/windows-hardware/drivers/ddi/wdfwmi/nc-wdfwmi-evt_wdf_wmi_instance_query_instance) callback function.

### <a href="" id="supporting-read-only-wmi-data-blocks"></a> Supporting Read-Only WMI Data Blocks

If the information in a WMI data block cannot be modified by a WMI client, the driver does not provide [*EvtWmiInstanceSetInstance*](/windows-hardware/drivers/ddi/wdfwmi/nc-wdfwmi-evt_wdf_wmi_instance_set_instance) or [*EvtWmiInstanceSetItem*](/windows-hardware/drivers/ddi/wdfwmi/nc-wdfwmi-evt_wdf_wmi_instance_set_item) callback functions. To support requests for the data block's information from WMI clients, the driver can do either of the following:

-   Provide an [*EvtWmiInstanceQueryInstance*](/windows-hardware/drivers/ddi/wdfwmi/nc-wdfwmi-evt_wdf_wmi_instance_query_instance) callback function to copy driver-supplied data into a WMI-supplied buffer.

-   Store the data block's information in the WMI instance object's [context space](framework-object-context-space.md), and set the **UseContextForQuery** member of the instance's [**WDF\_WMI\_INSTANCE\_CONFIG**](/windows-hardware/drivers/ddi/wdfwmi/ns-wdfwmi-_wdf_wmi_instance_config) structure to **TRUE**.

If the driver sets **UseContextForQuery** to **TRUE**, the framework copies the instance object's context space into a WMI-supplied buffer when a WMI client requests the instance's information. No *EvtWmiInstanceXxx* callbacks are required if the driver has only a single WMI instance that provides read-only, fixed-length data from its object context area.

If a read-only data block contains methods that the driver executes at the client's request, the driver can also provide an [*EvtWmiInstanceExecuteMethod*](/windows-hardware/drivers/ddi/wdfwmi/nc-wdfwmi-evt_wdf_wmi_instance_execute_method) callback function.

### Supporting Expensive WMI Data Blocks

If your driver collects relatively large amounts of dynamic data to support one of its WMI data blocks, the driver should do the following:

-   Declare the data block to be "expensive" by setting the **WdfWmiProviderExpensive** flag in the **Flags** member of the WMI provider object's [**WDF\_WMI\_PROVIDER\_CONFIG**](/windows-hardware/drivers/ddi/wdfwmi/ns-wdfwmi-_wdf_wmi_provider_config) structure.

-   Provide an [*EvtWmiProviderFunctionControl*](/windows-hardware/drivers/ddi/wdfwmi/nc-wdfwmi-evt_wdf_wmi_provider_function_control) callback function that enables and disables data collection for the data block, or call [**WdfWmiProviderIsEnabled**](/windows-hardware/drivers/ddi/wdfwmi/nf-wdfwmi-wdfwmiproviderisenabled) to determine whether the driver should enable or disable data collection.

If your driver sets the **WdfWmiProviderExpensive** flag, the framework calls the [*EvtWmiProviderFunctionControl*](/windows-hardware/drivers/ddi/wdfwmi/nc-wdfwmi-evt_wdf_wmi_provider_function_control) callback function when a WMI client registers to access the data block. The callback function should enable the driver's ability to collect data. If all WMI clients remove their registrations for the data block, the framework calls the *EvtWmiProviderFunctionControl* callback function again so the driver can stop collecting data.

### Supporting WMI Events

A driver can use WMI events to notify WMI clients of exceptional conditions. (You should not use WMI events as an alternative to logging errors.) Like data items, WMI events are defined in WMI data blocks within managed object format (.mof) files.

WMI clients register for notification of WMI events. To send an event to registered WMI clients, your driver calls the [**WdfWmiInstanceFireEvent**](/windows-hardware/drivers/ddi/wdfwmi/nf-wdfwmi-wdfwmiinstancefireevent) method. This method allows the driver to optionally send event-specific data to the clients.

If the WMI data block that defines the event also contains WMI data items or method items, the driver provides appropriate WMI callback functions. If a data block defines an event but contains no data or method items, your driver must set the **WdfWmiProviderEventOnly** flag in the **Flags** member of the WMI provider object's [**WDF\_WMI\_PROVIDER\_CONFIG**](/windows-hardware/drivers/ddi/wdfwmi/ns-wdfwmi-_wdf_wmi_provider_config) structure.

The driver should call [**WdfWmiInstanceFireEvent**](/windows-hardware/drivers/ddi/wdfwmi/nf-wdfwmi-wdfwmiinstancefireevent) only if a WMI client has registered for event notification. The driver can determine if it should call **WdfWmiInstanceFireEvent** by either providing an [*EvtWmiProviderFunctionControl*](/windows-hardware/drivers/ddi/wdfwmi/nc-wdfwmi-evt_wdf_wmi_provider_function_control) callback function or calling [**WdfWmiProviderIsEnabled**](/windows-hardware/drivers/ddi/wdfwmi/nf-wdfwmi-wdfwmiproviderisenabled).

### Supporting WMI Event Tracing

Trace events are defined in .mof files, in the same manner as other WMI events. When your driver creates a WMI provider object for a trace event, it must set the **WdfWmiProviderTracing** flag in the **Flags** member of the provider object's [**WDF\_WMI\_PROVIDER\_CONFIG**](/windows-hardware/drivers/ddi/wdfwmi/ns-wdfwmi-_wdf_wmi_provider_config) structure.

After a provider instance has been registered, the driver can call [**WdfWmiProviderGetTracingHandle**](/windows-hardware/drivers/ddi/wdfwmi/nf-wdfwmi-wdfwmiprovidergettracinghandle) to obtain a tracing handle. The driver can use the tracing handle as input to the [**WmiTraceMessage**](/windows-hardware/drivers/ddi/wdm/nf-wdm-wmitracemessage) routine.

For more information about event tracing, see:

-   [WMI Event Tracing](../kernel/wmi-event-tracing.md)

-   [WPP Software Tracing](../devtest/wpp-software-tracing.md)

 

