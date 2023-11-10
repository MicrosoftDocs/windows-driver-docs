---
title: ACX device enumeration
description: This topic provides a summary of the ACX device enumeration, startup and shutdown, and device rebalance.
ms.date: 09/29/2023
ms.localizationpriority: medium
---

# ACX device enumeration

This topic discusses ACX  device enumeration, startup and shutdown, and device rebalance. For a general overview of ACX, see [ACX audio class extensions overview](acx-audio-class-extensions-overview.md). For information about ACX power management and PnP, see [ACX power management](acx-power-management.md).

>[!NOTE]
> The ACX headers and libraries are not included in the  WDK 10.0.22621.2428 (released October 24, 2023), but are available in previous versions, as well as the latest (25000 series builds) Insider Preview of the WDK. For more information about preview versions of the WDK, see [Installing preview versions of the Windows Driver Kit (WDK)](../installing-preview-versions-wdk.md).


## ACX device enumeration and startup for static audio devices

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

## ACX device enumeration and startup for dynamic audio devices

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

## ACX device rebalance

Rebalancing is done when system resource usage requires the operating system to rebalance resources between devices. For general information about rebalance, see [Implement PnP Rebalance for PortCls Audio Drivers](implement-pnp-rebalance-for-portcls-audio-drivers.md).

ACX supports device rebalance as follows:

- In the power down WDF/ACX sequence, the driver releases all streaming resources (EvtAcxStreamPowerDown, EvtAcxStreamReleaseHardware), circuit resources (EvtAcxCircuitPowerDown, EvtAcxCircuitReleaseHardware) and device resources (EvtDeviceReleaseHardware).

- All requests are pended, and handles are left open.

- In the power up WDF/ACX sequence, the driver makes sure the new resources are compatible with the current ones, and it makes any allowed adjustments to its settings. If the resources are not compatible with the current device/circuit initialization, the driver must delete the current circuits and create new ones. See below more information.

- In the power up sequence, WDF invokes its EvtDevicePrepareHardware and EvtDeviceD0 entry, and ACX invokes the corresponding EvtAcxCircuitPrepareHardware and EvtAcxCircuitPowerUp, and it moves all streams into its pre-existing states.

- As soon as the queues move to power up/run state, the I/O flow again.

ACX doesn't allow remove (fails query-remove) or rebalance (fails query-stop) to take place if there are streams in active (RUN) state.

Drivers may also opt to always destroy and recreate audio devices on rebalance. This is the same scenario above when the device detects that the new settings are not compatible with the old ones. The deletion of the circuit must be done in EvtDevicePrepareHardware/EvtDeviceReleaseHardware callbacks, and the new circuit is re-created in EvtDevicePrepareHardware. The driver deletes a circuit by un-registering the circuit (using [AcxDeviceRemoveCircuit](/windows-hardware/drivers/ddi//acxdevice/nf-acxdevice-acxdeviceremovecircuit)).

ACX doesn’t wait for the user mode file handles to be closed before re-creating new circuits. The lifetime of the files system handles is not tied to the lifetime of the hardware resources used by the device/circuits. It is the responsibility of clients to listen for interface arrival/removal and close and re-open file handles.

Old file handles are marked obsolete and ACX fails all the I/O requests associated with them.

## See also

[ACX audio class extensions overview](acx-audio-class-extensions-overview.md)

[ACX reference documentation](acx-reference.md)

[PnP and Power Management Callback Sequences](../wdf/pnp-and-power-management-callback-sequences.md)
