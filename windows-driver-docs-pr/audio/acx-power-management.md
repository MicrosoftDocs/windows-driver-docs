---
title: ACX device enumeration and power management
description: This topic provides a summary of the ACX power management
ms.date: 01/23/2023
ms.localizationpriority: medium
---

# ACX device enumeration and power management

>[!IMPORTANT]
> Some information relates to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

This topic discusses ACX  device enumeration, startup and shutdown, and power management. For a general overview of ACX, see [ACX Audio Class Extensions Overview](acx-audio-class-extensions-overview.md).

ACX leverages the WDF KMDF PnP power behavior. For more  information about KMDF power management sequences, see [PnP and Power Management Callback Sequences](../wdf/pnp-and-power-management-callback-sequences.md).

## ACX Device enumeration and startup for static audio devices

To learn about how ACX startup works, the following scenario will be described.

- An audio device is represented by a single circuit.
- An audio/circuit lifetime is tied to the PnP device lifetime.
- A single device can create multiple circuits for different audio devices.
- KMDF kernel-mode environment.

The sequence of start up is:

- WDM DriverEntry. Driver-scoped.
    - Init tracing.
    - Optionally register for unload.
    - Create WDFDRIVER.
    - Call ACX to do any post driver init.
    - Optionally do any post driver init.
    - For more information, see [DriverEntry for WDF Drivers routine](../wdf/driverentry-for-kmdf-drivers.md).

- WDF DeviceAdd. Device-scoped.
    - Call ACX to init the device init context.
    - Create device.
    - Call ACX to do any post device init.
    - Optionally do any post device init.
    - For more information, see [EVT_WDF_DRIVER_DEVICE_ADD callback function](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add).

- WDF PrepareHardware. Device-scoped.
    - Create and init hardware resources (for interrupts and threads, register them with ACX).
    - Create one or more circuits (one time creation).
        - Create an AcxCircuitInit Context.
        - Add callbacks.
        - Create an AcxCircuit.
        - Optionally do any post circuit init.
        - Register the circuit with AcxDeviceAddCircuit.
    - For more information, see [EVT_WDF_DEVICE_PREPARE_HARDWARE callback function](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware).

- WDF Device D0 Entry callback. Device-scoped.
   - For more information, see [EVT_WDF_DEVICE_D0_ENTRY callback function](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_entry).

- ACX invokes the [EvtAcxCircuitPowerUp callback](/windows-hardware/drivers/ddi/acxcircuit/nc-acxcircuit-evt_acx_circuit_power_up) on all the circuits. Circuit-scoped.
- ACX Moves the streams (if any) to their previous state before the device was powered down. Stream Instance-scoped.
- WDF Queues are restarted.
- WDF DeviceSelfManagedIoInit. Device-scoped.
   - For more information, see [EVT_WDF_DEVICE_SELF_MANAGED_IO_INIT callback function](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_init).
- WDF DeviceSelfManagedIoRestart. Device-scoped.
    - Init after each power up from Dx.
    - For more information, see [EVT_WDF_DEVICE_SELF_MANAGED_IO_RESTART callback function](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_restart).

- ACX StreamAdd (instance) on ACX Circuit (ACX callback on ACX circuits) – invoked at any time after the WDF self-managed I/O Init or Restart has been invoked and device is in D0.  Circuit-scoped.
    - Input: AcxStreamInit context, ACXCIRCUIT.
    - Add callbacks.
    - Create an AcxStream (instance).
    - Optionally do any post stream Instance init.
    - On return, ACX activates this stream instance, and since in this scenario is the only one on the audio path, it allows stream messages to go through.

## ACX Device enumeration and startup for dynamic audio devices

In this scenario the following are assumed.

- Dynamic audio support (create/delete audio devices at run-time).
- Device lifetime is not tied to the circuit lifetime.
- A single device can create multiple circuits for different audio devices.
- Piggybacks on the simple static pattern described above by only adding elements specific to dynamic pattern.
- Makes use of child raw PDOs.
- KMDF kernel-mode environment.

The sequence of start up for this scenario is:

- WDM DriverEntry. Driver-scoped.
    - Init tracing.
    - Optionally register for unload.
    - Create WDFDRIVER.
    - Call ACX to do any post driver init.
    - Optionally do any post driver init.
     
- WDF DeviceAdd. Device-scoped.
    - Call ACX to init the device init context.
    - Create device.
    - Call ACX to do any post device init.
    - Optionally do any post device init.

- WDF PrepareHardware. Device-scoped.
    - Create and init hardware resources (for interrupts and threads, register them with ACX).

- WDF Device D0 Entry callback. Device-scoped.
    
- WDF Queues are restarted.

- WDF DeviceSelfManagedIoInit. Device-scoped.

- WDF DeviceSelfManagedIoRestart. Device-scoped.
    - Init after each power up from Dx.

### Circuit dynamic creation (at any time)

- Driver allocates a [WDFDEVICE_INIT structure](../wdf/wdfdevice_init.md) by calling [WdfPdoInitAllocate](/windows-hardware/drivers/ddi/wdfpdo/nf-wdfpdo-wdfpdoinitallocate).
  The driver is responsible for invoking the [WdfDeviceInitFree](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitfree) if it encounters any failures before successfully creating a device.
- Driver specifies any PnP/power callbacks it wants to receive.
- Driver creates a device.
- Driver instantiates the new device/circuit by calling [AcxDeviceAddCircuitDevice](/windows-hardware/drivers/ddi/acxdevice/nf-acxdevice-acxdeviceaddcircuitdevice).
- WDF/PnP takes over and the simple enum/startup pattern described in the previous section takes place.

### Circuit dynamic removal

- Driver invokes [AcxDeviceRemoveCircuitDevice](/windows-hardware/drivers/ddi/acxdevice/nf-acxdevice-acxdeviceremovecircuitdevice) to remove the audio device from the device list. This triggers the power down sequence on the ACX circuit device/circuit entity. The circuit device/circuit is deleted asynchronously.

- Circuit Providers (AcxFactoryCircuit):
    - ACX invokes a driver callback to let the driver know when to create dynamic circuits.

## ACX device power-down and removal

This section describes power down sequences.

- WDF [DeviceSelfManagedIoSuspend](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_suspend) callback. Device-Scoped. This can be invoked for the following reasons:
    - Device is entering a low power state.
    - The device is being removed, or it was surprise-removed.
    - PnP manager is about to redistribute the system’s hardware resources among system’s attached devices.
Stop any I/O in progress when receiving this callback.
- Power managed queues are stopped (no pending I/O in process).
- If streams are present, ACX SetState callbacks to transition all circuit’s streams to Pause. Stream Instance-scoped.
- ACX Set power state callback [EvtAcxCircuitPowerDown](/windows-hardware/drivers/ddi/acxcircuit/nc-acxcircuit-evt_acx_circuit_power_down) for each circuit (Dx). Circuit-scoped.
- WDF Device D0 Exit callback.

*Stop here if transitioning to low power state.*

- If streams are present, ACX SetState callbacks to transition all circuit’s streams to Stop. Stream Instance-scoped.
- ACX PnP callback [EvtAcxCircuitReleaseHardware](/windows-hardware/drivers/ddi/acxcircuit/nc-acxcircuit-evt_acx_circuit_release_hardware) for each circuit. Circuit-scoped.
- WDF Device Release Hardware callback.

*Stop here if rebalancing resources.*

- Purge queues.
- Self Managed I/O Cleanup.
- ACX unregisters and deletes circuits.
- ACX Stream instances cleanup context.
- ACX Circuit cleanup context.
- WDF Other release/remove callbacks.

Device is removed.
- WDM Driver’s Unload callback.
- WDF Driver’s cleanup callback.

Driver is removed.

## ACX device surprise removal

The WDF framework can call the [EvtDeviceSurpriseRemoval](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_surprise_removal) at any time, i.e., this callback is not serialized with the power down sequence. The WDF driver should not take any action on receiving this callback except for taking note that the device was surprise removed.

The power down surprise removal callback sequence is identical to the power down Dx and remove cases, WDF doesn’t invoke the following callbacks on the surprise removal path:

- EvtDeviceArmWakeFrom*
- EvtIoStop (purge power-managed queues's)
- EvtDeviceSelfManagedIoFlush (flush I/O buffers)

For more information, see [PnP and Power Management Callback Sequences](../wdf/pnp-and-power-management-callback-sequences.md).

## ACX device rebalance

Rebalancing is done when system resource usage requires the operating system to rebalance resources between devices. For general information about rebalance, see [Implement PnP Rebalance for PortCls Audio Drivers](implement-pnp-rebalance-for-portcls-audio-drivers.md).

ACX supports device rebalance as follows:

- In the power down WDF/ACX sequence, the driver releases all streaming resources (EvtAcxStreamPowerDown, EvtAcxStreamReleaseHardware), circuit resources (EvtAcxCircuitPowerDown, EvtAcxCircuitReleaseHardware) and device resources (EvtDeviceReleaseHardware).

- All requests are pended, and handles are left open.

- In the power up WDF/ACX sequence, the driver makes sure the new resources are compatible with the current ones, and it makes any allowed adjustments to its settings.
If the resources are not compatible with the current device/circuit initialization, the driver must delete the current circuits and create new ones. See below more information.

- In the power up sequence, WDF invokes its EvtDevicePrepareHardware and EvtDeviceD0 entry, and ACX invokes the corresponding EvtAcxCircuitPrepareHardware and EvtAcxCircuitPowerUp, and it moves all streams into its pre-existing states.

- As soon as the queues move to power up/run state, the I/O flow again.

ACX doesn't allow remove (fails query-remove) or rebalance (fails query-stop) to take place if there are streams in active (RUN) state.

Drivers may also opt to always destroy and recreate audio devices on rebalance. This is the same scenario above when the device detects that the new settings are not compatible with the old ones. The deletion of the circuit must be done in EvtDevicePrepareHardware/EvtDeviceReleaseHardware callbacks, and the new circuit is re-created in EvtDevicePrepareHardware. The driver deletes a circuit by un-registering the circuit (using [AcxDeviceRemoveCircuit](/windows-hardware/drivers/ddi//acxdevice/nf-acxdevice-acxdeviceremovecircuit)).

ACX doesn’t wait for the user mode file handles to be closed before re-creating new circuits. The lifetime of the files system handles is not tied to the lifetime of the hardware resources used by the device/circuits. It is the responsibility of clients to listen for interface arrival/removal and close and re-open file handles.

Old file handles are marked obsolete and ACX fails all the I/O requests associated with them.

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

WDF knows about the D3Cold capabilities of the driver via the WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS’s ExcludeD3Cold field. The driver passes this struct as input to the WdfDeviceAssignS0IdleSettings. WDF Drivers can invoke the WdfDeviceAssignS0IdleSettings multiple times to turn on or off D3Cold depending on the system environment, i.e., in response to ACX. For more information, see [WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS structure](/windows-hardware/drivers/ddi/wdfdevice/ns-wdfdevice-_wdf_device_power_policy_idle_settings)

## See also

[ACX Audio Class Extensions overview](acx-audio-class-extensions-overview.md)

[PnP and Power Management Callback Sequences](../wdf/pnp-and-power-management-callback-sequences.md)