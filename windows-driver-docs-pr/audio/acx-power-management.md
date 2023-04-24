---
title: ACX power management
description: This topic provides a summary of the ACX power management
ms.date: 04/19/2023
ms.localizationpriority: medium
---

# ACX power management

>[!IMPORTANT]
> Some information relates to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

This topic discusses ACX power management. For information about ACX  device enumeration, startup and shutdown, and device rebalance, see [ACX device enumeration](acx-device-enumeration.md). For a general overview of ACX, see [ACX audio class extensions overview](acx-audio-class-extensions-overview.md).

ACX leverages the WDF KMDF PnP power behavior. For more  information about KMDF power management sequences, see [PnP and Power Management Callback Sequences](../wdf/pnp-and-power-management-callback-sequences.md).

## ACX device enumeration and startup for static audio devices

To learn about how ACX startup works, the following scenario will be described.

## ACX device surprise removal

The WDF framework can call the [EvtDeviceSurpriseRemoval](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_surprise_removal) at any time, i.e., this callback is not serialized with the power down sequence. The WDF driver should not take any action on receiving this callback except for taking note that the device was surprise removed.

The power down surprise removal callback sequence is identical to the power down Dx and remove cases, WDF doesn’t invoke the following callbacks on the surprise removal path:

- EvtDeviceArmWakeFrom*
- EvtIoStop (purge power-managed queues's)
- EvtDeviceSelfManagedIoFlush (flush I/O buffers)

For more information, see [PnP and Power Management Callback Sequences](../wdf/pnp-and-power-management-callback-sequences.md).

## ACX circuit power-up and startup

A "dynamic" AcxCircuit can be added at any time. The driver creates a new child PDO device and associates the new AcxCircuit when handling the WDF PrepareHardware callback for this PDO device. The lifetime of a "dynamic' circuit is not bound to the lifetime of the FDO.

A "static" AcxCircuit can only be added when the driver is handling the WDF PrepareHardware callback for its FDO device. The lifetime of a "static" circuit is bound to the lifetime of the FDO.

An ACX driver can also create AcxFactoryCircuit objects (circuit providers) during power up sequence. An AcxFactoryCircuit object uses dynamic circuit creation for adding ACXCIRCUITS when requested by ACX. This feature is very useful when building composite endpoints, i.e., audio endpoint made up of two or more ACXCIRCUITs linked together.

The ACX Circuit defines the following callbacks which are invoked during the AcxCircuit / Audio Endpoint initialization:

[EvtAcxCircuitPrepareHardware](/windows-hardware/drivers/ddi/acxcircuit/nc-acxcircuit-evt_acx_circuit_prepare_hardware): ACX invokes this callback just after WDF delivers its WDF prepare hardware callback. It gives an opportunity to the driver to do any 'prepare-hardware' specific to the circuit. This call is serialized by ACX. Device is not in D0 when this call is invoked.

[EvtAcxCircuitPowerUp](/windows-hardware/drivers/ddi/acxcircuit/nc-acxcircuit-evt_acx_circuit_power_up): ACX invokes this callback just after coming back from Dx. This call is serialized by ACX. Device is in D0.

For composite endpoints AcxCircuits can optionally register for these callbacks:
[EvtAcxCircuitCompositeCircuitInitialize](/windows-hardware/drivers/ddi/acxcircuit/nc-acxcircuit-evt_acx_circuit_composite_circuit_initialize), invoked the first time ACX detects that this ACXCIRCUIT is visible, i.e., the associated device went in D0 and made this circuit visible to entities external to its own stack. The circuit's audio interfaces are still in the OFF state.

[EvtAcxCircuitCompositeInitialize](/windows-hardware/drivers/ddi/acxcircuit/nc-acxcircuit-evt_acx_circuit_composite_initialize), invoked each time ACX is finishing up the init of a composite endpoint. After this callback ACX turns on the audio interfaces of this circuit.

[EvtAcxCircuitCompositeDeinitialize](/windows-hardware/drivers/ddi/acxcircuit/nc-acxcircuit-evt_acx_circuit_composite_deinitialize), invoked each time ACX is tearing down a composite endpoint. Drivers may not receive this callback if its own stack has been surprise-removed, or unable to process I/O.

If present, stream instances are restored to their pre-power down states.

## ACX circuit power-down and removal

A "dynamic" AcxCircuit can be removed at any time by invalidating and removing the device object associated with the circuit. The associated circuit can be removed / detached from the removed device when the driver handles the WDF PrepareHardware/ReleaseHardware callbacks for this PDO device. The lifetime of a "dynamic" circuit is not bound to the lifetime of the FDO.

A "static" AcxCircuit can only be removed when the driver is handling the WDF PrepareHardware/ReleaseHardware callbacks for its FDO device. The lifetime of a "static" circuit is bound to the lifetime of the FDO.

The driver can remove an AcxFactoryCircuit (circuit provider) in its  the WDF PrepareHardware/ReleaseHardware callbacks. Removing an AcxFactoryCircuit has the effect of removing all its associated "dynamic" AcxCircuit(s). AcxCircuit(s) can also be removed when the ACX manager tells a circuit factory to remove a specific circuit, or when the ACX manager closes its AcxFactoryCircuit handles - in this scenario ACX closes all the circuits associated with that handle.

The [ACX_CIRCUIT_PNPPOWER_CALLBACKS structure](/windows-hardware/drivers/ddi/acxcircuit/ns-acxcircuit-acx_circuit_pnppower_callbacks) describes the following callbacks that can be used by an ACX driver.

[EvtAcxCircuitPowerDown](/windows-hardware/drivers/ddi/acxcircuit/nc-acxcircuit-evt_acx_circuit_power_down): ACX invokes this callback just before going in Sx/Dx/Stop/Removal/SurpriseRemoval and when the driver removes the circuit. This call is serialized by ACX. Device is in D0, although keep in mind that the device could be Surprise Removed at any time (which means the associated hardware is gone).

[EvtAcxCircuitReleaseHardware](/windows-hardware/drivers/ddi/acxcircuit/nc-acxcircuit-evt_acx_circuit_release_hardware): ACX invokes this callback just before WDF delivers its WDF release hardware callback. It gives an opportunity to the driver to do any cleanup while the circuit is still alive. This call is serialized by ACX. Device is not in D0 when this call is invoked.

[EvtWdfObjectContextCleanup](/windows-hardware/drivers/ddi/wdfobject/nc-wdfobject-evt_wdf_object_context_cleanup): WDF invokes this callback when the WDF/ACX object is deleted. This call is synchronous with the deletion of the WDF object call. Device may not be in D0 when this call is invoked. The callback is running at Passive level.

[EvtWdfObjectContextDestory](/windows-hardware/drivers/ddi/wdfobject/nc-wdfobject-evt_wdf_object_context_destroy): WDF invokes this callback after the last ref on this object goes away. This call is asynchronous with the deletion of the WDF object call. Device may not be in D0 when this call is invoked. This callback is invoked only after the last reference on the object goes away. The callback is running at <= DPC level. The exact IRQL depends on the IRQL of the thread releasing the last ref.

## ACX device idle management

ACX leverages the WDF idle management infrastructure. ACX drivers uses the following WDF DDIs to enable idle management:

[WdfDeviceAssignS0IdleSettings](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceassigns0idlesettings): this call specifies the type of idle timeout and idle management. The ACX driver is free to use the appropriate setting for its device.

[WdfDeviceStopIdle](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicestopidle): this call prevents the device from idling. Note that his call doesn’t block Sx requests. That is, the device goes in Dx independently of the number of active power references when the system goes to a lower power state.

[WdfDeviceResumeIdle](/windows-hardware/drivers/ddi//wdfdevice/nf-wdfdevice-wdfdeviceresumeidle): this call allows the device to restart its idle timeout.

In a multi-stack/circuit scenario, different stacks may have different idle timeouts. This is because of the different power settings/requirements of each stack, so different idle timeouts are appropriate.

### Power management framework (PoFx) and driver-managed idle timeout

Note that WDF does not directly support Fx device/component states. To use these states, the driver must use driver-managed idle timeout. For more information about the use of Fx device component states and driver-managed idle timeout, see the following topics.

- [Component-Level Power Management](../kernel/component-level-power-management.md)
- [Supporting Multiple-Component Devices with Single or Multiple Functional Power State](../wdf/supporting-multiple-functional-power-states-for-multiple-component-devices.md)

Windows provides a run-time power management framework (PoFx) which adds support for component-level power management. A component, or subdevice, is a functional hardware unit in a device that can be turned on or switched to a low-power state independently of the other components in the same device. For more information, see [Overview of the Power Management Framework](../kernel/overview-of-the-power-management-framework.md).

### ACX driver and power managed queues

WDF supports power-managed I/O queues. This type of queue is fully integrated with WDF power management. WDF invokes the queue’s callbacks at various steps in the power up/power down WDF sequence. For more information, see [Using Power-Managed I/O Queues](../wdf/using-power-managed-i-o-queues.md).

ACX Drivers can use this type of queue only if the driver is not using single/multi-component with multi-state (Fx) feature.

## ACX driver and D3Hot / D3Cold (D3) states

Audio drivers know when to go in D3Hot or D3Cold based on the information available in the [ACX_DX_EXIT_LATENCY enumeration](/windows-hardware/drivers/ddi/acxdevice/ne-acxdevice-acx_dx_exit_latency).

```cpp
typedef enum _ACX_DX_EXIT_LATENCY { 
  AcxDxExitLatencyInstant     = 0,
  AcxDxExitLatencyFast,
  AcxDxExitLatencyResponsive
} ACX_DX_EXIT_LATENCY;
```

**AcxDxExitLatencyFast** corresponds to D3Hot (DSP on) and **AcxDxExitLatencyResponsive** corresponds to D3Cold (DSP off).

Audio drivers can get the ACX_DX_EXIT_LATENCY value by calling the [AcxDeviceGetCurrentDxExitLatency function](/windows-hardware/drivers/ddi/acxdevice/nf-acxdevice-acxdevicegetcurrentdxexitlatency).

WDF knows about the D3Cold capabilities of the driver via the WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS’s ExcludeD3Cold field. The driver passes this struct as input to the WdfDeviceAssignS0IdleSettings. WDF Drivers can invoke the WdfDeviceAssignS0IdleSettings multiple times to turn on or off D3Cold depending on the system environment, i.e., in response to ACX. For more information, see [WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS structure](/windows-hardware/drivers/ddi/wdfdevice/ns-wdfdevice-_wdf_device_power_policy_idle_settings).

## See also

[ACX device enumeration](acx-device-enumeration.md)

[ACX reference documentation](acx-reference.md)

[ACX audio class extensions overview](acx-audio-class-extensions-overview.md)

[PnP and Power Management Callback Sequences](../wdf/pnp-and-power-management-callback-sequences.md)
