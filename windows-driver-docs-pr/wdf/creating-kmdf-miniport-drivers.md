---
title: Creating KMDF Miniport Drivers
description: Creating KMDF Miniport Drivers
keywords:
- miniport drivers WDK KMDF
ms.date: 04/20/2017
---

# Creating KMDF Miniport Drivers





Some miniport drivers can use Kernel-Mode Driver Framework, if the port/miniport architecture allows the miniport driver to communicate with other drivers by using WDM or framework interfaces. For example, [NDIS miniport drivers with a WDM lower edge](../network/ndis-miniport-drivers-with-a-wdm-lower-edge.md) can use the framework to implement the lower edge.

If you want your miniport driver to use the framework, the driver must:

-   Set the [**WdfDriverInitNoDispatchOverride**](/windows-hardware/drivers/ddi/wdfdriver/ne-wdfdriver-_wdf_driver_init_flags) flag in the **DriverInitFlags** member of the driver's [**WDF\_DRIVER\_CONFIG**](/windows-hardware/drivers/ddi/wdfdriver/ns-wdfdriver-_wdf_driver_config) structure before calling [**WdfDriverCreate**](/windows-hardware/drivers/ddi/wdfdriver/nf-wdfdriver-wdfdrivercreate). Setting this flag enables the port driver, instead of the framework, to intercept I/O request packets (IRPs) that the I/O manager has directed to the driver.

-   Call [**WdfDeviceMiniportCreate**](/windows-hardware/drivers/ddi/wdfminiport/nf-wdfminiport-wdfdeviceminiportcreate) instead of [**WdfDeviceCreate**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreate) to create framework device objects for the miniport driver's devices. The miniport driver should call **WdfDeviceMiniportCreate** when its port driver informs it that a device is available.

-   Call [**WdfObjectDelete**](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectdelete) to delete the device object that [**WdfDeviceMiniportCreate**](/windows-hardware/drivers/ddi/wdfminiport/nf-wdfminiport-wdfdeviceminiportcreate) creates, when the driver determines that the device has been removed. (Because the driver has set the [**WdfDriverInitNoDispatchOverride**](/windows-hardware/drivers/ddi/wdfdriver/ne-wdfdriver-_wdf_driver_init_flags) flag, the framework cannot determine when the device is removed and cannot delete the device object.)

-   Call [**WdfDriverMiniportUnload**](/windows-hardware/drivers/ddi/wdfminiport/nf-wdfminiport-wdfdriverminiportunload) when the port driver informs the miniport driver that it is about to be unloaded.

A miniport driver can use the framework only if the underlying device supports Plug and Play (PnP). Miniport drivers cannot use the framework's control device objects.

Restrictions apply to the device objects that the [**WdfDeviceMiniportCreate**](/windows-hardware/drivers/ddi/wdfminiport/nf-wdfminiport-wdfdeviceminiportcreate) method creates. For a list of these restrictions, see [**WdfDeviceMiniportCreate**](/windows-hardware/drivers/ddi/wdfminiport/nf-wdfminiport-wdfdeviceminiportcreate).

 

