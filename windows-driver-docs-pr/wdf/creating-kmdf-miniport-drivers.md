---
title: Creating KMDF Miniport Drivers
description: Creating KMDF Miniport Drivers
ms.assetid: 3e01827b-fe1e-49ce-8072-9fc6c751fc01
keywords: ["miniport drivers WDK KMDF"]
---

# Creating KMDF Miniport Drivers


## <a href="" id="ddk-using-windows-driver-framework-with-miniport-drivers-df"></a>


Some miniport drivers can use Kernel-Mode Driver Framework, if the port/miniport architecture allows the miniport driver to communicate with other drivers by using WDM or framework interfaces. For example, [NDIS miniport drivers with a WDM lower edge](https://msdn.microsoft.com/library/windows/hardware/ff565954) can use the framework to implement the lower edge.

If you want your miniport driver to use the framework, the driver must:

-   Set the [**WdfDriverInitNoDispatchOverride**](https://msdn.microsoft.com/library/windows/hardware/ff551303) flag in the **DriverInitFlags** member of the driver's [**WDF\_DRIVER\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff551300) structure before calling [**WdfDriverCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547175). Setting this flag enables the port driver, instead of the framework, to intercept I/O request packets (IRPs) that the I/O manager has directed to the driver.

-   Call [**WdfDeviceMiniportCreate**](https://msdn.microsoft.com/library/windows/hardware/ff546802) instead of [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926) to create framework device objects for the miniport driver's devices. The miniport driver should call **WdfDeviceMiniportCreate** when its port driver informs it that a device is available.

-   Call [**WdfObjectDelete**](https://msdn.microsoft.com/library/windows/hardware/ff548734) to delete the device object that [**WdfDeviceMiniportCreate**](https://msdn.microsoft.com/library/windows/hardware/ff546802) creates, when the driver determines that the device has been removed. (Because the driver has set the [**WdfDriverInitNoDispatchOverride**](https://msdn.microsoft.com/library/windows/hardware/ff551303) flag, the framework cannot determine when the device is removed and cannot delete the device object.)

-   Call [**WdfDriverMiniportUnload**](https://msdn.microsoft.com/library/windows/hardware/ff547193) when the port driver informs the miniport driver that it is about to be unloaded.

A miniport driver can use the framework only if the underlying device supports Plug and Play (PnP). Miniport drivers cannot use the framework's control device objects.

Restrictions apply to the device objects that the [**WdfDeviceMiniportCreate**](https://msdn.microsoft.com/library/windows/hardware/ff546802) method creates. For a list of these restrictions, see [**WdfDeviceMiniportCreate**](https://msdn.microsoft.com/library/windows/hardware/ff546802).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Creating%20KMDF%20Miniport%20Drivers%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




