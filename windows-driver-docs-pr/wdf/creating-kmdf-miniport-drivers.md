---
title: Creating KMDF Miniport Drivers
description: Creating KMDF Miniport Drivers
ms.assetid: 3e01827b-fe1e-49ce-8072-9fc6c751fc01
keywords:
- miniport drivers WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating KMDF Miniport Drivers





Some miniport drivers can use Kernel-Mode Driver Framework, if the port/miniport architecture allows the miniport driver to communicate with other drivers by using WDM or framework interfaces. For example, [NDIS miniport drivers with a WDM lower edge](https://docs.microsoft.com/windows-hardware/drivers/network/ndis-miniport-drivers-with-a-wdm-lower-edge) can use the framework to implement the lower edge.

If you want your miniport driver to use the framework, the driver must:

-   Set the [**WdfDriverInitNoDispatchOverride**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdriver/ne-wdfdriver-_wdf_driver_init_flags) flag in the **DriverInitFlags** member of the driver's [**WDF\_DRIVER\_CONFIG**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdriver/ns-wdfdriver-_wdf_driver_config) structure before calling [**WdfDriverCreate**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdriver/nf-wdfdriver-wdfdrivercreate). Setting this flag enables the port driver, instead of the framework, to intercept I/O request packets (IRPs) that the I/O manager has directed to the driver.

-   Call [**WdfDeviceMiniportCreate**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfminiport/nf-wdfminiport-wdfdeviceminiportcreate) instead of [**WdfDeviceCreate**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreate) to create framework device objects for the miniport driver's devices. The miniport driver should call **WdfDeviceMiniportCreate** when its port driver informs it that a device is available.

-   Call [**WdfObjectDelete**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectdelete) to delete the device object that [**WdfDeviceMiniportCreate**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfminiport/nf-wdfminiport-wdfdeviceminiportcreate) creates, when the driver determines that the device has been removed. (Because the driver has set the [**WdfDriverInitNoDispatchOverride**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfdriver/ne-wdfdriver-_wdf_driver_init_flags) flag, the framework cannot determine when the device is removed and cannot delete the device object.)

-   Call [**WdfDriverMiniportUnload**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfminiport/nf-wdfminiport-wdfdriverminiportunload) when the port driver informs the miniport driver that it is about to be unloaded.

A miniport driver can use the framework only if the underlying device supports Plug and Play (PnP). Miniport drivers cannot use the framework's control device objects.

Restrictions apply to the device objects that the [**WdfDeviceMiniportCreate**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfminiport/nf-wdfminiport-wdfdeviceminiportcreate) method creates. For a list of these restrictions, see [**WdfDeviceMiniportCreate**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdfminiport/nf-wdfminiport-wdfdeviceminiportcreate).

 

 





