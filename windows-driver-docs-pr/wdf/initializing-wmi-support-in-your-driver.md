---
title: Initializing WMI Support in Your Driver
description: Initializing WMI Support in Your Driver
keywords:
- WMI WDK KMDF , initializing support
- provider instances WDK KMDF
- multiple provider instances WDK KMDF
- single provider instances WDK KMDF
- registering MOF resource names WDK KMDF
- MOF resource names WDK KMDF
- initializing WMI support WDK KMDF
ms.date: 04/20/2017
---

# Initializing WMI Support in Your Driver


\[Applies to KMDF only\]

To support WMI data blocks, a framework-based driver:

-   Registers the managed object format (MOF) resource names of any customized WMI data providers that are not defined in *Wmicore.mof*.

-   Creates one or more WMI instance objects to represent the data blocks it can read or write.

-   Optionally implements one or more event callback functions to supply the WMI data that the driver provides.

-   Register each WMI instance object to make it available to WMI clients.

To initialize its WMI support, a KMDF driver follows these steps, typically within its [*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) or [*EvtDeviceSelfManagedIoInit*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_init) callback:

1.  A driver that provides a MOF file to support customized WMI data providers must call the [**WdfDeviceAssignMofResourceName**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceassignmofresourcename) method to register a MOF resource name before the driver creates WMI provider objects that represent the data provider.

2.  Initialize a WMI provider configuration structure and optionally create a WMI provider object (WDFWMIPROVIDER).
3.  Initialize a WMI instance configuration structure and create a WMI instance object (WDFWMIINSTANCE).

The framework creates a WMI provider by default when a KMDF driver creates its first WMI instance. Therefore, if the driver requires only one WMI provider, it is not required to call the provider-creation method ([**WdfWmiProviderCreate**](/windows-hardware/drivers/ddi/wdfwmi/nf-wdfwmi-wdfwmiprovidercreate)). However, the driver must fill in the provider configuration structure because this structure supplies information about the provider that the framework uses when it creates the instance.

If your driver creates a single instance of each WMI data block that it supports, the driver calls [**WdfWmiInstanceCreate**](/windows-hardware/drivers/ddi/wdfwmi/nf-wdfwmi-wdfwmiinstancecreate), passing both a [**WDF\_WMI\_PROVIDER\_CONFIG**](/windows-hardware/drivers/ddi/wdfwmi/ns-wdfwmi-_wdf_wmi_provider_config) structure and a [**WDF\_WMI\_INSTANCE\_CONFIG**](/windows-hardware/drivers/ddi/wdfwmi/ns-wdfwmi-_wdf_wmi_instance_config) structure. This single call both configures the single framework-provided WMI provider object and creates a WMI instance object.

If your driver creates multiple instances of its WMI data blocks, the driver must call both [**WdfWmiProviderCreate**](/windows-hardware/drivers/ddi/wdfwmi/nf-wdfwmi-wdfwmiprovidercreate) and [**WdfWmiInstanceCreate**](/windows-hardware/drivers/ddi/wdfwmi/nf-wdfwmi-wdfwmiinstancecreate)

### <a href="" id="registering-provider-instances"></a> Registering Provider Instances

Before WMI clients can access your driver's WMI data blocks, the driver must register its provider instances with the system's WMI service. The driver can use either of the following techniques to register a provider instance:

-   Set the **Register** member of the provider instance's [**WDF\_WMI\_INSTANCE\_CONFIG**](/windows-hardware/drivers/ddi/wdfwmi/ns-wdfwmi-_wdf_wmi_instance_config) structure to **TRUE**.

    If your driver sets **Register** to **TRUE**, the framework automatically registers the instance the first time that the device enters its working (D0) state.

-   Call the [**WdfWmiInstanceRegister**](/windows-hardware/drivers/ddi/wdfwmi/nf-wdfwmi-wdfwmiinstanceregister) method.

    If your driver calls [**WdfWmiInstanceRegister**](/windows-hardware/drivers/ddi/wdfwmi/nf-wdfwmi-wdfwmiinstanceregister) after calling [**WdfWmiInstanceCreate**](/windows-hardware/drivers/ddi/wdfwmi/nf-wdfwmi-wdfwmiinstancecreate), the framework registers the instance after the device is in its working (D0) state.

The framework automatically deregisters each provider instance when the instance's device is removed (and before it calls the [*EvtDeviceSelfManagedIoCleanup*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_cleanup) event callback function). For information about the order in which the framework calls a driver's callback functions, see [PnP and Power Management Scenarios](pnp-and-power-management-scenarios.md).

Your driver can deregister an instance at any time by calling [**WdfWmiInstanceDeregister**](/windows-hardware/drivers/ddi/wdfwmi/nf-wdfwmi-wdfwmiinstancederegister).

 

