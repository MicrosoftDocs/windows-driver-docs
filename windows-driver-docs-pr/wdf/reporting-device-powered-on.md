---
title: Reporting Device Powered On When System Returns to S0
description: Reporting Device Powered On When System Returns to S0
ms.assetid: 35A48B37-8000-45DC-8E39-4B58ABE7DE68
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reporting Device Powered On When System Returns to S0


\[Applies to KMDF only\]

When the system returns to its working (S0) state from a low-power state, the PnP manager sends a system set-power IRP ([**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744)) to return the device to its working (D0) state. WDF handles the system set-power IRP. However, because in the multi-component scenario the driver has directly registered with the power management framework (PoFx), the driver must call [**PoFxReportDevicePoweredOn**](https://msdn.microsoft.com/library/windows/hardware/hh439526) when the device has completed the transition to its fully on (D0) power state. The driver can accomplish this by registering a WDM preprocess routine to receive notification when a system set-power IRP arrives.

The driver can use the following procedure:

1.  Call [**WdfDeviceInitAssignWdmIrpPreprocessCallback**](https://msdn.microsoft.com/library/windows/hardware/ff546043) to register a [*EvtDeviceWdmIrpPreprocess*](https://msdn.microsoft.com/library/windows/hardware/ff540925) callback function for [**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744). In the callback, the driver sets a flag in its device extension to indicate that it needs to call [**PoFxReportDevicePoweredOn**](https://msdn.microsoft.com/library/windows/hardware/hh439526) from its next [*EvtDeviceD0Entry*](https://msdn.microsoft.com/library/windows/hardware/ff540848) callback.
2.  In [*EvtDeviceD0Entry*](https://msdn.microsoft.com/library/windows/hardware/ff540848), if the flag is set, the driver clears the flag and calls [**PoFxReportDevicePoweredOn**](https://msdn.microsoft.com/library/windows/hardware/hh439526).
3.  The driver also checks the flag in [*EvtDeviceSelfManagedIoFlush*](https://msdn.microsoft.com/library/windows/hardware/ff540901). If the flag is set, the device failed to return to D0 and the device has been removed. In this case, the driver calls [**PoFxReportDevicePoweredOn**](https://msdn.microsoft.com/library/windows/hardware/hh439526) and then unregisters with the power framework.

 

 





