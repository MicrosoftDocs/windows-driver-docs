---
title: IddCx Objects
description: IddCx uses the extensible UMDF object model to represent graphics objects.
ms.date: 07/17/2020
keywords:
- Indirect display driver objects
- IDD objects
- Indirect display driver, UMDF objects
- IDD, UMDF objects
ms.localizationpriority: medium
---

# IddCx Objects

The [IddCx](/windows-hardware/drivers/ddi/iddcx/) (Indirect Display Driver Class eXtension) uses the extensible UMDF object model to represent the components of the indirect display device. The [UMDF](../wdf/getting-started-with-umdf-version-2.md) object model allows the driver-specific storage to be associated with each IddCx (and hence UMDF) object. See [UMDF Object Model](../wdf/umdf-objects-and-interfaces.md) for more information.

The order in which IDD objects are created is:

* The driver first creates an **IDDCX_ADAPTER** object.
* The driver then creates an **IDDCX_MONITOR** object.
* Once the **IDDCX_ADAPTER** and **IDDCX_MONITOR** objects are created, the OS creates **IDDCX_SWAPCHAIN** and **IDDCX_OPMCTX** objects and sends them to the driver.

The following sections provide more details about these objects.

## IDDCX_ADAPTER

This object represents a single logical display adapter created by the driver in a two stage process:

* The driver calls the [**IddCxAdapterInitAsync**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxadapterinitasync) callback function.
* The OS calls the driver's [*EvtIddCxAdapterInitFinished*](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_adapter_init_finished) DDI to complete the initialization.

The IDD model does not have an explicit destroy adapter callback. Once the adapter initialization sequence has been completed successfully, the adapter is valid until the UMDF device passed at initialization time is stopped. When creating the adapter, the driver provides static adapter information about the indirect display adapter.

### Handling multifunction devices

In the simplest case, there is a one-to-one mapping between the UMDF device object created by the plug and play subsystem for the attached indirect display device and the **IDDCX_ADAPTER** object that the indirect display driver (IDD) creates.

There can be more complex scenarios where a single indirect display dongle contains multiple plug and play devices. For example, an indirect display solution might have multiple PnP device functions such as a microphone (audio driver) and camera (video driver). In such situations, it is the IDD's responsibility to create a single **IDDCX_ADAPTER** object for the multiple UMDF device objects created for each PnP device. The driver needs to consider the following in this scenario:

* The **IDDCX_ADAPTER** should only be created once all the PnP devices that make up the indirect display solution have been started successfully.
* The driver must pass a single **WDFDEVICE** when creating the adapter, so it requires logic to decide which UMDF device it will pass.
* If any of the devices that make up the indirect display adapter have a hardware error, the driver should report all devices that make up the adapter as being in error.

## IDDCX_MONITOR

This object represents a specific monitor connected to one of the connectors on the indirect display adapter.

The driver creates the monitor object in a two stage process:

* It first calls the [**IddCxMonitorCreate**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxmonitorcreate) callback to create the **IDDCX_MONITOR** object.
* It then calls the [**IddCxMonitorArrival**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxmonitorarrival) callback to complete the monitor arrival.

When a monitor is unplugged, the driver calls the [**IddCxMonitorDeparture**](/windows-hardware/drivers/ddi/iddcx/nf-iddcx-iddcxmonitordeparture) callback to report the monitor has been unplugged, which causes the **IDDCX_MONITOR** object to be destroyed. Even if the same monitor is un-plugged then reconnected, the **IddCxMonitorDeparture**/**IddCxMonitorArrival** sequence needs to be called again.

The **IDDCX_MONITOR** is a child of the **IDDCX_ADAPTER** object.

## IDDCX_SWAPCHAIN

This object represents a [swapchain](/windows/win32/direct3d12/swap-chains) that will provide desktop images to display on a connected monitor. The swapchain has multiple buffers to allow the OS to compose the next desktop image in one buffer while the IDD is accessing another buffer. The **IDDCX_SWAPCHAIN** is a child of the **IDDCX_MONITOR** so there will only be one assigned swapchain to a given monitor at any time.

The OS creates and destroys the **IDDCX_SWAPCHAIN** objects and assigns/unassigns them to monitors using the [**EvtIddCxMonitorAssignSwapChain**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_monitor_assign_swapchain) and [**EvtIddCxMonitorUnassignSwapChain**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_monitor_unassign_swapchain) Ddi calls.

## IDDCX_OPMCTX

This object represents an active [Output Protection Manager](/windows/win32/medfound/output-protection-manager) (OPM) context from a single application OPM context that the application can use to control output protection on a single monitor. Multiple OPM contexts can be active on a given monitor at the same time. The OS calls the driver to create and destroy the OPM contexts using the driver's [**EvtIddCxMonitorOPMCreateProtectedOutput**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_monitor_opm_create_protected_output) and [**EvtIddCxMonitorOPMDestroyProtectedOutput**](/windows-hardware/drivers/ddi/iddcx/nc-iddcx-evt_idd_cx_monitor_opm_destroy_protected_output) DDI calls.
