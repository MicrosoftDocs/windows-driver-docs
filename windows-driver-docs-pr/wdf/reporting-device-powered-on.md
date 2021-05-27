---
title: Reporting Device Powered On When System Returns to S0
description: Reporting Device Powered On When System Returns to S0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reporting Device Powered On When System Returns to S0


\[Applies to KMDF only\]

When the system returns to its working (S0) state from a low-power state, the PnP manager sends a system set-power IRP ([**IRP\_MN\_SET\_POWER**](../kernel/irp-mn-set-power.md)) to return the device to its working (D0) state. WDF handles the system set-power IRP. However, because in the multi-component scenario the driver has directly registered with the power management framework (PoFx), the driver must call [**PoFxReportDevicePoweredOn**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxreportdevicepoweredon) when the device has completed the transition to its fully on (D0) power state. The driver can accomplish this by registering a WDM preprocess routine to receive notification when a system set-power IRP arrives.

The driver can use the following procedure:

1.  Call [**WdfDeviceInitAssignWdmIrpPreprocessCallback**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitassignwdmirppreprocesscallback) to register a [*EvtDeviceWdmIrpPreprocess*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess) callback function for [**IRP\_MN\_SET\_POWER**](../kernel/irp-mn-set-power.md). In the callback, the driver sets a flag in its device extension to indicate that it needs to call [**PoFxReportDevicePoweredOn**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxreportdevicepoweredon) from its next [*EvtDeviceD0Entry*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_entry) callback.
2.  In [*EvtDeviceD0Entry*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_entry), if the flag is set, the driver clears the flag and calls [**PoFxReportDevicePoweredOn**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxreportdevicepoweredon).
3.  The driver also checks the flag in [*EvtDeviceSelfManagedIoFlush*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_flush). If the flag is set, the device failed to return to D0 and the device has been removed. In this case, the driver calls [**PoFxReportDevicePoweredOn**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pofxreportdevicepoweredon) and then unregisters with the power framework.

 

