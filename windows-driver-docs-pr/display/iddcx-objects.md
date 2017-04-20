---
title: IddCx Objects
description: IddCx uses the extensible UMDF object model to represent graphics objects, they are covered in following sections.
ms.assetid: B4D40C6B-DCEF-4661-9DF2-411326870014
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# IddCx Objects


IddCx uses the extensible UMDF object model to represent graphics objects, they are covered in following sections. The UMDF object model allows the driver specific storage to be associated with each IddCx (and hence UMDF) object, see UMDF Object Model for more information

## <span id="IDDCX_ADAPTER"></span><span id="iddcx_adapter"></span>IDDCX\_ADAPTER


This object represents a single logical display adapter created by the driver in a two stage process. First, it calls the [**IddCxAdapterInitAsync**](https://msdn.microsoft.com/library/windows/hardware/mt761916) callback function and the OS calls the driver's [EvtIddCxAdapterInitFinished](https://msdn.microsoft.com/library/windows/hardware/mt761860) DDI to complete the initialization.

In the simplest case, there is a one to one mapping between the UMDF device object created by the plug and play subsystem for the attached Indirect Display device and the **IDDCX\_ADAPTER** the driver creates. In more complex scenarios where a single Indirect Display dongle contains multiple plug and play devices (eg 2 USB device function), it is the responsibility of the driver to create only a single **IDDCX\_ADAPTER** object for the multiple UMDF device objects created, one for each Pnp device. The driver needs to consider the following in this scenario :

1. The **IDDCX\_ADAPTER** should only be created once all the devices that make up the Indirect Display solution have been started successfully
2. The driver has to pass a single **WDFDEVICE** when creating the adapter, so it requires logic to decide which UMDF device it will pass.
3. If any of the devices that make up the Indirect Display adapter have a hardware error, the driver should report all devices that make up the adapter as being in error.
The Indirect Display model does not have an explicit destroy adapter callback. Once the adapter initialization sequence has been completed successfully, the adapter is valid until the UMDF device passed at initialization time is stopped. When creating the adapter, the driver provides static adapter information about the Indirect Display Adapter.

## <span id="IDDCX_MONITOR"></span><span id="iddcx_monitor"></span>IDDCX\_MONITOR


This object represents a specific monitor connected to one of the connectors on the Indirect Display adapter.

The driver creates the monitor object in a two stage process. First, the driver calls the [**IddCxMonitorCreate**](https://msdn.microsoft.com/library/windows/hardware/mt761921) callback to create the **IDDCX\_MONITOR** object, then calls [**IddCxMonitorArrival**](https://msdn.microsoft.com/library/windows/hardware/mt761920) callback to complete the monitor arrival. When a monitor is unplugged, the driver calls the [**IddCxMonitorDeparture**](https://msdn.microsoft.com/library/windows/hardware/mt761922) callback to report the monitor has been unplugged, which will cause the **IDDCX\_MONITOR** object to be destroyed. Even if the same monitor is un-plugged then reconnected, the **IddCxMonitorDeparture**/**IddCxMonitorArrival** sequence needs to be called again. The **IDDCX\_MONITOR** is a child of the **IDDCX\_ADAPTER** object.

## <span id="IDDCX_SWAPCHAIN"></span><span id="iddcx_swapchain"></span>IDDCX\_SWAPCHAIN


This object represents a swapchain that will provide desktop images to display on a connected monitor. The swapchain has multiple buffers to allow the OS to compose the next desktop image in one buffer while the Indirect Display driver is accessing another buffer. The **IDDCX\_SWAPCHAIN** is a child of the **IDDCX\_MONITOR** so there will only be one assigned swapchain to a given monitor at any time. The OS creates and destroys the **IDDCX\_SWAPCHAIN** objects and assigns/unassigns them to monitors using the EvtIddCxMonitorAssignSwapChain and EvtIddCxMonitorUnassignSwapChain Ddi calls.

## <span id="IDDCX_OPMCTX"></span><span id="iddcx_opmctx"></span>IDDCX\_OPMCTX


This object represents an active OPM context from a single application OPM context that the application can use to control output protection on a single monitor. Multiple OPM contexts can be active on a given monitor at the same time. The OS calls the driver to create and destroy the OPM contexts using the driver's EvtIddCxMonitorOPMCreateProtectedOutput and EvtIddCxMonitorOPMDestroyProtectedOutput DDI calls.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20IddCx%20Objects%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




