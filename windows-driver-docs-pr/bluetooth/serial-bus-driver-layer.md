---
title: Serial Bus Driver Layer
description: The serial bus driver is loaded based on a PDO created by ACPI, and can query and access the system resources, such as GPIO and I2C controllers to perform signaling control.
ms.date: 01/10/2024
---

# Serial bus driver layer

The serial bus driver is loaded based on a PDO created by ACPI, and can query and access the system resources, such as GPIO and I2C controllers to perform signaling control.

## Sample mechanism for power control

Bluetooth over USB has a built-in mechanism for in-band signaling to support sleep and wake. However, in a SoC platform, the mechanism to support power control can be more flexible (and customizable) using various controllers.

Here's a sample implementation to walk through idle and wake signaling:

- A GPIO interrupt HOST_WAKE line - to signal by the Bluetooth controller when it needs to wake the host to service a request from a remote device (for example, remote connection)
- A GPIO signal line BT_ENABLE line - set by a bus driver and is asserted when the radio is active (core stack in D0) or is deasserted when Bluetooth core stack has detected idleness (entering into D2).

These two GPIO lines in the form of system resources are reported to the serial bus driver during driver loading as a regular interrupt and a new GPIO signal. Its interconnection properties are defined in the ACPI table by the system integrator and the Bluetooth chipset vendor (IHV). A serial bus driver can query and cache these dependent controller's connection IDs in order to open and access their resources.

## Start up to enable idle

The serial bus driver is required to perform the following tasks for supporting idle in the S0 system power state:

1. Report PnP and power management capabilities; as an integrated device, its Removable flag for the child PDO should be set to WdfFalse.
1. Report that it can support idle to its function driver (Bluetooth core driver).
1. Handle arm and disarm for wake, and wake signal.
1. Receive device power state notification and synchronize I/O completion with current device power state.

### Power management capabilities

The child PDO created by the bus driver sets power capabilities to enable idle state support. The child PDO is managed by the Power Manager, including settings to indicate:

- Its capability to support D2 device state.
- Its capability to enter idle and wake from D2.
- Its mapping of system state to device states and be in sync with the Bluetooth core driver.

```cpp
WDF_DEVICE_POWER_CAPABILITIES_INIT(&PowerCaps);
…
PowerCaps.DeviceD1 = WdfFalse;
PowerCaps.DeviceD2 = WdfTrue;
…
PowerCaps.DeviceWake = PowerDeviceD2;

PowerCaps.DeviceState[PowerSystemWorking]   = PowerDeviceD0;
PowerCaps.DeviceState[PowerSystemSleeping1] = PowerDeviceD2;
PowerCaps.DeviceState[PowerSystemSleeping2] = PowerDeviceD2;
PowerCaps.DeviceState[PowerSystemSleeping3] = PowerDeviceD2;
PowerCaps.DeviceState[PowerSystemHibernate] = PowerDeviceD2;
PowerCaps.DeviceState[PowerSystemShutdown]  = PowerDeviceD3;
..
WdfDeviceSetPowerCapabilities(ChildDevice, &PowerCaps);
```

The child PDO creates a WDF queue to receive IOCTL (I/O Control) request from the Bluetooth core driver. Such requests do come to query for the interface version and static capabilities prior to the device being started; therefore, this queue must not be power managed.

```cpp
QueueConfig.PowerManaged = WdfFalse;

QueueConfig.EvtIoDeviceControl = PdoIoQuDeviceControl;

Status = WdfIoQueueCreate(ChildDevice, 
                          &QueueConfig, 
                          WDF_NO_OBJECT_ATTRIBUTES,
                          &Queue);
```

### Bluetooth transport specific query for idle capability

In addition to reporting power management capabilities (as highlighted in the prior section), the child PDO also responds to the Bluetooth core driver's query for its capabilities to enter the idle state. In order to support idle in S0, this flag is set:

```cpp
FdoExtension->BthXCaps.IsDeviceIdleCapable = TRUE;
```

### Arm and disarm for wake

A requirement for idle support is the ability to receive a wake request from a remote Bluetooth device. The setup for such a wake request involves being armed for wake. The PDO for the Bluetooth function can register to receive callbacks to accomplish arm/disarm actions:

```cpp
WDF_PDO_EVENT_CALLBACKS_INIT(&Callbacks);

// Receive this callback to arming the device for wake
Callbacks.EvtDeviceEnableWakeAtBus  = PdoDevEnableWakeAtBus;

// Receive this callback to disarming the device for wake
Callbacks.EvtDeviceDisableWakeAtBus = PdoDevDisableWakeAtBus;

WdfPdoInitSetEventCallbacks(DeviceInit, &Callbacks);
```

With the above mechanisms supported, the Bluetooth core driver can then enable idle and wake support.

### Device power state notification

Child PDO registers to receive a callback to enter and exit D0 in order to be notified of the device power state transition. The current device power state is used to synchronize IO completion – that is, normal IO completion should only be completed in D0.

```cpp
    //
    // Register to receive device power state change notification
    //
    WDF_PNPPOWER_EVENT_CALLBACKS_INIT(&PnpPowerCallbacks);  

    PnpPowerCallbacks.EvtDeviceD0Entry = PdoDevD0Entry;
    PnpPowerCallbacks.EvtDeviceD0Exit  = PdoDevD0Exit; 

    
    WdfDeviceInitSetPnpPowerEventCallbacks(DeviceInit, 
                                           &PnpPowerCallbacks);
```

## Arm for wake

Prior to entering idle, the serial bus driver receives the callback **[EvtDeviceEnableWakeAtBus](/windows-hardware/drivers/ddi/wdfpdo/nc-wdfpdo-evt_wdf_device_enable_wake_at_bus)** to arm for wake.

The mechanism to arm for wake is vendor specific for SoC platforms and is thus outside the scope of this section. However, Windows expects that the bus driver will be prepared to receive a wake signal, and there will be a callback function (for example, ISR) to process such a signal.

## Enter idle

The Bluetooth core driver enables a time-based idle detection mechanism. Upon satisfying idle requirements, the core driver starts to initiate the stack to enter the idle state. It invokes **[PoRequestPowerIrp](/windows-hardware/drivers/ddi/wdm/nf-wdm-porequestpowerirp)** to set the power to go into D2 along with a completion function. After the bus driver has completed the IRP, this completion function is invoked. It is at this time, the transition to D2 gets completed.

While transitioning into idle state, the Bluetooth core driver cancels all pending read requests and restarts them when resuming to active. An empty power managed queue is required in order for the serial bus driver itself to enter idle.

In addition to idle timeout, the Bluetooth core driver takes into consideration many different situations before entering into the idle state, such as:

- Wait for the completion of an HCI Command that it has issued. Note: the Bluetooth core driver won't enter idle until its completion.
- All connected devices are in sniff mode.

In this idle state, the multifunction controller can throttle down its power by the Bluetooth function, but it must continue to supply power to maintain its volatile settings and configuration. It can then rely on its wake mechanism to wake the stack back to active (D0) state after which I/O communication can resume.

## Wake from sleep

While the Bluetooth function has been paired with one or more devices and is in the sleep state, its radio is periodically scanning for requests from its paired devices. When a paired device initiates a request and gets received by the Bluetooth radio, the process to resume to active state begins. Once the device stack has resumed to active (D0), the drivers can begin servicing this remote request.

This remote request is processed by the wake-signal processing function in the bus driver as discussed in the last section. This wake-signal processing function should ensure that the PDO's device state is indeed in D2 state and then invoke **[WdfDeviceIndicateWakeStatus](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceindicatewakestatus)** (PDO, success status) to notify KMDF to complete the W/W (Wait Wake) IRP. It is at this time when the completion function of this W/W IRP can be invoked and get processed by its initiator - the Bluetooth core driver and the power policy owner.

The completion of the W/W IRP triggers the Bluetooth core driver to initiate a transition to D0. It requests a **[PoRequestPowerIrp](/windows-hardware/drivers/ddi/wdm/nf-wdm-porequestpowerirp)** with a completion function to set the device power state to D0.

Prior to resuming to the active D0 state, the serial bus driver may receive a notification **[EvtDeviceDisableWakeAtBus](/windows-hardware/drivers/ddi/wdfpdo/nc-wdfpdo-evt_wdf_device_disable_wake_at_bus)** to disable wake – this completes the process to reverse what **[EvtDeviceEnableWakeAtBus](/windows-hardware/drivers/ddi/wdfpdo/nc-wdfpdo-evt_wdf_device_enable_wake_at_bus)** did earlier.

After Bluetooth driver stack resumes to D0, the serial bus driver can then complete the remote device request.

Some events need to be synchronized in the serial bus driver, such as:

- While entering D2, there should already be a pending W/W Irp. This is when arming for wake to receive the wake signal should take place instead of when receiving a W/W Irp. The wake signal is only actionable while in D2 state.
- If data is arriving (to form a packet) while entering D2 and there's no pending read request in the queue, the bus driver can cache the incoming data and enter D2. It can then complete the W/W Irp (with success) to wake the system back to D0 to resend and complete the read request.
- Bthport cancels all pending read requests and waits for their completion before entering D2. At the same time, the serial bus driver may have received a complete HCI packet and has dequeued a read request to return this HCI packet. The serial bus driver should complete this request, and will then be initiated to enter D2.

An action initiated by a Bluetooth application on the host side can also wake the stack from idle. In this case, only the device power state transition is required, and this action is initiated by the Bluetooth core driver.

In order to reduce power-up time, the callback functions (for example, the EnterD0 and wake) in the serial bus driver shouldn't be marked pageable.

## A flowchart to express the idle/wake, arm/disarm, and device power state transitions

The following is a simplified flowchart to illustrate a typical sequence and logic for idle and wake support. This logic spans many drivers and threads, and there are exceptions as well as corner cases that aren't expressed (for example, an application on the host side can also wake the stack from idle state).

:::image type="content" source="images/bthdevicepwrstatetransitionsflowchart.png" alt-text="Flowchart illustrating Bluetooth device power state transitions for idle and wake support.":::

## Bus driver's own power management

The serial bus driver is a function driver (FD) and the power policy owner (PPO) of its layer. Thus, it needs to handle its own power management. After all of its children have entered lower device power states, it can then enter into a lower power state itself. When it's ready to enter this lower power state, it can cancel any pending I/O requests to the UART controller driver – this allows the UART driver to also enter a lower power state. However, the UART driver should persist and restore its device settings (including the baud rate) when its power state is later resumed to active.
