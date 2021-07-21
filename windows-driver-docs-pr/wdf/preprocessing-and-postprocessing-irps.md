---
title: Preprocessing and Postprocessing IRPs
description: Preprocessing and Postprocessing IRPs
keywords:
- preprocessing IRPs WDK KMDF
- postprocessing IRPs WDK KMDF
- WDM IRPs WDK KMDF , preprocessing and postprocessing
- IRPs WDK KMDF , preprocessing and postprocessing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Preprocessing and Postprocessing IRPs


\[Applies to KMDF only\]

If your driver must intercept an I/O request packet (IRP) before or after the framework handles the IRP, the driver can call [**WdfDeviceInitAssignWdmIrpPreprocessCallback**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitassignwdmirppreprocesscallback) to register an [*EvtDeviceWdmIrpPreprocess*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess) event callback function for a major I/O function code and, optionally, for specific minor I/O function codes that are associated with the major code. Subsequently, the framework calls the driver's *EvtDeviceWdmIrpPreprocess* callback function whenever the driver receives an IRP that contains a specified major and minor function code.

The [*EvtDeviceWdmIrpPreprocess*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess) callback function can do whatever is necessary to preprocess the IRP, and then it must call [**WdfDeviceWdmDispatchPreprocessedIrp**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicewdmdispatchpreprocessedirp) to return the IRP to the framework unless the driver is [handling an IRP that the framework does not support](handling-an-irp-that-the-framework-does-not-support.md).

After the driver calls [**WdfDeviceWdmDispatchPreprocessedIrp**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicewdmdispatchpreprocessedirp), the framework processes the IRP in the same way that it would have if the driver had not provided an [*EvtDeviceWdmIrpPreprocess*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess) callback function. If the IRP's I/O function code is one that the framework passes to drivers, the driver will receive the IRP again as a request object.

If the driver needs to postprocess the IRP after a lower-level driver completes the IRP, the driver's [*EvtDeviceWdmIrpPreprocess*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess) callback function can call [**IoSetCompletionRoutine**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetcompletionroutine) to set an [*IoCompletion*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routine before it calls [**WdfDeviceWdmDispatchPreprocessedIrp**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicewdmdispatchpreprocessedirp).

After your driver calls [**WdfDeviceInitAssignWdmIrpPreprocessCallback**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitassignwdmirppreprocesscallback), the framework causes the I/O manager to add an additional [I/O stack location](../kernel/i-o-stack-locations.md) to all IRPs so that the [*EvtDeviceWdmIrpPreprocess*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess) callback function can set an [*IoCompletion*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routine. The callback function must update the IRP's I/O stack location pointer before it calls [**WdfDeviceWdmDispatchPreprocessedIrp**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicewdmdispatchpreprocessedirp).

### Calling WdfDeviceWdmDispatchPreprocessedIrp

Because the I/O manager adds an additional I/O stack location to the IRP, the [*EvtDeviceWdmIrpPreprocess*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess) callback function must call [**IoSkipCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioskipcurrentirpstacklocation) or [**IoCopyCurrentIrpStackLocationToNext**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocopycurrentirpstacklocationtonext) (to set up the next I/O stack location in the IRP) before calling [**WdfDeviceWdmDispatchPreprocessedIrp**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicewdmdispatchpreprocessedirp).

If your driver is preprocessing an IRP, but not postprocessing the IRP, the driver does not need to set an [*IoCompletion*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routine for the IRP and can call [**IoSkipCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioskipcurrentirpstacklocation), as the following code example shows.

```cpp
NTSTATUS
  EvtDeviceMyIrpPreprocess(
    IN WDFDEVICE Device,
    IN OUT PIRP Irp
    )
{
//
// Perform IRP preprocessing operations here.
//
...
//
// Deliver the IRP back to the framework. 
//
IoSkipCurrentIrpStackLocation(Irp);
return WdfDeviceWdmDispatchPreprocessedIrp(Device, Irp);
}
```

If your driver is postprocessing the IRP, the driver must call [**IoCopyCurrentIrpStackLocationToNext**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocopycurrentirpstacklocationtonext), and then it must call [**IoSetCompletionRoutine**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetcompletionroutine) to set an [*IoCompletion*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routine for the IRP, as the following code example shows.

```cpp
NTSTATUS
  EvtDeviceMyIrpPreprocess(
    IN WDFDEVICE Device,
    IN OUT PIRP Irp
    )
{
//
// Perform IRP preprocessing operations here, if needed.
//
...
//
// Set a completion routine and deliver the IRP back to
// the framework. 
//
IoCopyCurrentIrpStackLocationToNext(Irp);
IoSetCompletionRoutine(
                       Irp,
                       MyIrpCompletionRoutine,
                       NULL,
                       TRUE,
                       TRUE,
                       TRUE
                      );
return WdfDeviceWdmDispatchPreprocessedIrp(Device, Irp);
}
```

Your driver must not call [**IoCopyCurrentIrpStackLocationToNext**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocopycurrentirpstacklocationtonext) (and therefore must not set an [*IoCompletion*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routine) if the device object handle that the driver's [*EvtDeviceWdmIrpPreprocess*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdfdevice_wdm_irp_preprocess) callback function receives represents a physical device object (PDO), and if the IRP's major function code is IRP\_MJ\_PNP or IRP\_MJ\_POWER. Otherwise, [Driver Verifier](../devtest/driver-verifier.md) will report an error.

For more information about when to call [**IoCopyCurrentIrpStackLocationToNext**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocopycurrentirpstacklocationtonext), [**IoSkipCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioskipcurrentirpstacklocation), and [**IoSetCompletionRoutine**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetcompletionroutine), see [Passing IRPs down the Driver Stack](../kernel/passing-irps-down-the-driver-stack.md).

 

