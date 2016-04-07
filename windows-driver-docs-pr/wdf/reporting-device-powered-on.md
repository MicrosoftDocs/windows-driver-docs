---
title: Reporting Device Powered On When System Returns to S0
description: Reporting Device Powered On When System Returns to S0
ms.assetid: 35A48B37-8000-45DC-8E39-4B58ABE7DE68
---

# Reporting Device Powered On When System Returns to S0


\[Applies to KMDF only\]

When the system returns to its working (S0) state from a low-power state, the PnP manager sends a system set-power IRP ([**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744)) to return the device to its working (D0) state. WDF handles the system set-power IRP. However, because in the multi-component scenario the driver has directly registered with the power management framework (PoFx), the driver must call [**PoFxReportDevicePoweredOn**](https://msdn.microsoft.com/library/windows/hardware/hh439526) when the device has completed the transition to its fully on (D0) power state. The driver can accomplish this by registering a WDM preprocess routine to receive notification when a system set-power IRP arrives.

The driver can use the following procedure:

1.  Call [**WdfDeviceInitAssignWdmIrpPreprocessCallback**](https://msdn.microsoft.com/library/windows/hardware/ff546043) to register a [*EvtDeviceWdmIrpPreprocess*](https://msdn.microsoft.com/library/windows/hardware/ff540925) callback function for [**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744). In the callback, the driver sets a flag in its device extension to indicate that it needs to call [**PoFxReportDevicePoweredOn**](https://msdn.microsoft.com/library/windows/hardware/hh439526) from its next [*EvtDeviceD0Entry*](https://msdn.microsoft.com/library/windows/hardware/ff540848) callback.
2.  In [*EvtDeviceD0Entry*](https://msdn.microsoft.com/library/windows/hardware/ff540848), if the flag is set, the driver clears the flag and calls [**PoFxReportDevicePoweredOn**](https://msdn.microsoft.com/library/windows/hardware/hh439526).
3.  The driver also checks the flag in [*EvtDeviceSelfManagedIoFlush*](https://msdn.microsoft.com/library/windows/hardware/ff540901). If the flag is set, the device failed to return to D0 and the device has been removed. In this case, the driver calls [**PoFxReportDevicePoweredOn**](https://msdn.microsoft.com/library/windows/hardware/hh439526) and then unregisters with the power framework.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Reporting%20Device%20Powered%20On%20When%20System%20Returns%20to%20S0%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




