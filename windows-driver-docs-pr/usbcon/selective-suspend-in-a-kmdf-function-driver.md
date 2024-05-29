---
title: Selective Suspend in USB KMDF Function Drivers
description: This article describes how KMDF function drivers support USB selective suspend.
ms.date: 01/17/2024
---

# Selective suspend in USB KMDF function drivers

This article describes how KMDF function drivers support USB selective suspend.

If the USB driver requires features or resources that aren't available in user mode, you should supply a KMDF function driver. KMDF drivers implement selective suspend by setting relevant values in a KMDF initialization structure and then supplying the appropriate callback functions. KMDF handles the details of communicating with lower drivers to suspend and resume the device.

## Guidelines for selective suspend in KMDF drivers

KMDF drivers that support selective suspend must follow these guidelines:

- A KMDF function driver must be the PPO for its device stack. By default, KMDF function drivers are the PPO.
- A KMDF function driver that supports selective suspend can use queues that are power managed or queues that aren't power managed. By default, queue objects for PPOs are power managed.

### Power policy ownership and KMDF USB drivers

By default, the KMDF function driver for a USB device is the PPO for the device stack. KMDF manages selective suspend and resume on behalf of this driver.

### I/O queue configuration in KMDF drivers

A KMDF function driver that supports selective suspend can use queues that are power managed or queues that aren't power managed. Typically, a driver configures a queue that isn't power managed to receive incoming device I/O control requests and configures one or more power-managed queues to receive read, write, and other power-dependent requests. When a request arrives at a power-managed queue, KMDF ensures that the device is in D0 before it presents the request to the driver.

If you're writing a KMDF filter driver that is layered above the PPO in the device stack, you must not use power-managed queues. The reason is the same as for UMDF drivers. The framework doesn't present requests from power-managed queues while the device is suspended, so the use of such queues could stall the device stack.

## Selective suspend mechanism for KMDF function drivers

KMDF handles most of the work that is required to support USB selective suspend. It keeps track of I/O activity, manages the idle timer, and sends the device I/O control requests that cause the parent driver (Usbhub.sys or Usbccgp.sys) to suspend and resume the device.

If a KMDF function driver supports selective suspend, KMDF tracks the I/O activity on all power-managed queues that each device object owns. The framework starts an idle timer whenever the I/O count reaches zero. The default time-out value is 5 seconds.

If an I/O request arrives at a power-managed queue that belongs to the device object before the idle time-out period expires, the framework cancels the idle timer and doesn't suspend the device.

When the idle timer expires, KMDF issues the requests that are required to put the USB device in the suspended state. If a function driver uses a continuous reader on a USB endpoint, the reader's repeated polling doesn't count as activity toward the KMDF idle timer. However, in the **[EvtDeviceD0Exit](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_exit)** callback function, the USB driver must manually stop the continuous reader and any other I/O targets that are fed by queues that aren't power managed to ensure that the driver doesn't send I/O requests while the device isn't in the working state. To stop the targets, the driver calls **[WdfIoTargetStop](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetstop)** and specifies **WdfIoTargetWaitForSentIoToComplete** as the target action. In response, the framework stops the I/O target only after all I/O requests that are in the target's I/O queue have been completed and any associated I/O completion callbacks have run.

By default, KMDF transitions the device out of D0 and into the device power state that the driver specified in the idle settings. As part of the transition, KMDF calls the driver's power callback functions the same way it would for any other power-down sequence.

After the device has been suspended, the framework automatically resumes the device when any of the following events occur:

- An I/O request arrives for any of the driver's power-managed queues.
- The user disables USB selective suspend by using Device Manager.
- The driver calls **[WdfDeviceStopIdle](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicestopidle)**, as described in [Preventing USB device suspension](#preventing-usb-device-suspension).

To resume the device, KMDF sends a power-up request down the device stack and then invokes the driver's callback functions in the same way that it would for any other power-up sequence.

For detailed information about the callbacks that are involved in the power-down and power-up sequences, see the [Plug and Play and Power Management in WDF Drivers](https://download.microsoft.com/download/5/d/6/5d6eaf2b-7ddf-476b-93dc-7cf0072878e6/WDF-pnpPower.docx) white paper.

## Supporting USB selective suspend in a KMDF function driver

To implement USB selective suspend in a KMDF function driver:

- Initialize power policy settings that are related to idle, including idle time-out.
- Optionally include logic to temporarily prevent suspension or resume operation when the driver determines that the device shouldn't be suspended because of an open handle or other reason that isn't related to the device's I/O queues.
- In a USB driver for a human interface device (HID), indicate in the INF that it supports selective suspend.

### Initializing Power Policy Settings in a KMDF Function Driver

To configure support for USB selective suspend, a KMDF driver uses the **[WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS](/windows-hardware/drivers/ddi/wdfdevice/ns-wdfdevice-_wdf_device_power_policy_idle_settings)** structure. The driver must first initialize the structure and can then set fields that provide details about the capabilities of the driver and its device. Typically, the driver fills in this structure in its *EvtDriverDeviceAdd* or *EvtDevicePrepareHardware* function.

### To initialize the WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS structure

After the driver creates the device object, the driver uses the **[WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS_INIT](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdf_device_power_policy_idle_settings_init)** function to initialize the structure. This function takes two arguments:

- A pointer to the **[WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS](/windows-hardware/drivers/ddi/wdfdevice/ns-wdfdevice-_wdf_device_power_policy_idle_settings)** structure to initialize.
- An enumeration value that indicates support for selective suspend. The driver should specify **IdleUsbSelectiveSuspend**.

If the driver specifies **IdleUsbSelectiveSuspend**, the function initializes the structure's members as follows:

- **IdleTimeout** is set to **IdleTimeoutDefaultValue** (currently 5000 milliseconds or 5 seconds).
- **UserControlOfIdleSettings** is set to **IdleAllowUserControl** .
- **Enabled** is set to **WdfUseDefaul**t, which indicates that selective suspend is enabled but a user can disable it if the **UserControlOfIdleSettings** member permits it.
- **DxState** is set to **PowerDeviceMaximum**, which uses the reported power capabilities for the device to determine the state to which to transition the idle device.

### To configure USB selective suspend

After the driver initializes the **[WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS](/windows-hardware/drivers/ddi/wdfdevice/ns-wdfdevice-_wdf_device_power_policy_idle_settings)** structure, the driver can set other fields in the structure, and then call **WdfDeviceAssignS0IdleSettings** to pass these settings to the framework. The following fields apply to USB function drivers:

- IdleTimeout—The interval, in milliseconds, that must elapse without receiving an I/O request before the framework considers the device idle. The driver can specify a ULONG value or can accept the default.
- UserControlOfIdleSettings—Whether the user can modify the device's idle settings. Possible values are IdleDoNotAllowUserControl and IdleAllowUserControl.
- DxState—The device power state to which the framework suspends the device. Possible values are PowerDeviceD1, PowerDeviceD2, and PowerDeviceD3.

    USB drivers shouldn't change the initial setting of this value. The **[WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS_INIT](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdf_device_power_policy_idle_settings_init)** function sets this value to PowerDeviceMaximum, which ensures that the framework chooses the correct value based on the device capabilities.

The following code snippet is from the Osrusbfx2 sample driver's Device.c file:

```cpp
WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS idleSettings;
NTSTATUS    status = STATUS_SUCCESS;
//
// Initialize the idle policy structure.
//
WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS_INIT(&idleSettings, 
     IdleUsbSelectiveSuspend);
idleSettings.IdleTimeout = 10000; // 10 sec

status = WdfDeviceAssignS0IdleSettings(Device, &idleSettings);
if ( !NT_SUCCESS(status)) {
     TraceEvents(TRACE_LEVEL_ERROR, DBG_PNP,
                 "WdfDeviceSetPowerPolicyS0IdlePolicy failed %x\n", 
                 status);
    return status;
}
```

In the example, the driver calls **[WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS_INIT](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdf_device_power_policy_idle_settings_init)**, specifying **IdleUsbSelectiveSuspend**. The driver sets **IdleTimeout** to 10,000 milliseconds (10 seconds) and accepts the framework defaults for **DxState** and **UserControlOfIdleSettings**. As a result, the framework transitions the device to the D3 state when it's idle and creates a Device Manager property page that allows users with administrator privilege to enable or disable device idle support. The driver then calls **[WdfDeviceAssignS0IdleSettings](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceassigns0idlesettings)** to enable idle support and register these settings with the framework.

A driver can call **[WdfDeviceAssignS0IdleSettings](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceassigns0idlesettings)** any time after it creates the device object. Although most drivers call this method initially from the *EvtDriverDeviceAdd* callback, this might not always be possible or even desirable. If a driver supports multiple devices or device versions, the driver might not know all device capabilities until it queries the hardware. Such drivers can postpone calling **WdfDeviceAssignS0IdleSettings** until the *EvtDevicePrepareHardware* callback.

At any time after its initial call to **[WdfDeviceAssignS0IdleSettings](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceassigns0idlesettings)**, the driver can change the idle time-out value and the device state in which the device idles. To change one or more settings, the driver simply initializes another **[WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS](/windows-hardware/drivers/ddi/wdfdevice/ns-wdfdevice-_wdf_device_power_policy_idle_settings)** structure as described earlier and calls **WdfDeviceAssignS0IdleSettings** again.

### Preventing USB device suspension

Sometimes, a USB device shouldn't be powered down even if no I/O requests are present within the time-out period—typically when a handle is open to the device or the device is charging. A USB driver can prevent the framework from suspending an idle device in such situations by calling **[WdfDeviceStopIdle](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicestopidle)** and calling **[WdfDeviceResumeIdle](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceresumeidle)** when it's again acceptable for the device to be suspended.

**[WdfDeviceStopIdle](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicestopidle)** stops the idle timer. If the **IdleTimeout** period hasn't expired and the device hasn't yet been suspended, the framework cancels the idle timer and doesn't suspend the device. If the device has already been suspended, the framework returns the device to the working state. **WdfDeviceStopIdle**does not prevent the framework from suspending the device when the system changes to an Sx sleep state. Its only effect is to prevent device suspension while the system is in the S0 working state. **[WdfDeviceResumeIdle](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceresumeidle)** restarts the idle timer. These two methods manage a reference count on the device, so if the driver calls **WdfDeviceStopIdle** several times, the framework doesn't suspend the device until the driver has called **WdfDeviceResumeIdle** the same number of times. A driver must not call **WdfDeviceResumeIdle**without first calling **WdfDeviceStopIdle**.

### Including a registry key (HID drivers only)

KMDF upper filter drivers for USB HID devices must indicate in the INF that they support selective suspend so that the Microsoft-supplied HIDClass.sys port driver can enable selective suspend for the HID stack. The INF should include an AddReg directive that adds the SelectiveSuspendEnabled key and set its value to 1, as the following string shows:

```cpp
HKR,,"SelectiveSuspendEnabled",0x00000001,0x1
```

For an example, see Hidusbfx2.inx in the WDK at %WinDDK%\\BuildNumber\\Src\\Hid\\ Hidusbfx2\\sys.

## Remote wake support for KMDF drivers

As with selective suspend, KMDF incorporates support for wakeup, so that a USB device can trigger a wake signal while the device is idle and the system is in the working state (S0) or in a sleep state (S1–S4). In KMDF terms, these two features are called "wake from S0" and "wake from Sx," respectively.

For USB devices, wakeup merely indicates that the device itself can initiate the transition from a lower-power state to the working state. Thus, in USB terms, wake from S0 and wake from Sx are the same, and are called "remote wake."

KMDF USB function drivers don't require any code to support wake from S0 because KMDF provides this capability as part of the selective suspend mechanism. However, to support remote wake when the system is in Sx, a function driver must:

- Check whether the device supports remote wake by calling **[WdfUsbTargetDeviceRetrieveInformation](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdeviceretrieveinformation)**.
- Enable remote wake by initializing wake settings and calling **[WdfDeviceAssignSxWakeSettings](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceassignsxwakesettings)**.

KMDF drivers typically configure wake support at the same time that they configure support for USB selective suspend in the *EvtDriverDeviceAdd* or *EvtDevicePrepareHardware* function.

### Checking device capabilities

Before a KMDF USB function driver initializes its power policy settings for idle and wake, it should verify that the device supports remote wake. To get information about device hardware features, the driver initializes a **[WDF_USB_DEVICE_INFORMATION](/windows-hardware/drivers/ddi/wdfusb/ns-wdfusb-_wdf_usb_device_information)** structure and calls **[WdfUsbTargetDeviceRetrieveInformation](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdeviceretrieveinformation)**, typically in its *EvtDriverDeviceAdd* or *EvtDevicePrepareHardware* callback.

In the call to **[WdfUsbTargetDeviceRetrieveInformation](/windows-hardware/drivers/ddi/wdfusb/nf-wdfusb-wdfusbtargetdeviceretrieveinformation)**, the driver passes a handle to the device object and a pointer to the initialized **[WDF_USB_DEVICE_INFORMATION](/windows-hardware/drivers/ddi/wdfusb/ns-wdfusb-_wdf_usb_device_information)** structure. Upon successful return from the function, the Traits field of the structure contains flags that indicate whether the device is self-powered, can operate at high speed, and supports remote wake.

The following example from the Osrusbfx2 KMDF sample shows how to call this method to determine whether a device supports remote wake. After these lines of code have run, the waitWakeEnable variable contains TRUE if the device supports remote wake and FALSE if it doesn't:

```cpp
    WDF_USB_DEVICE_INFORMATION          deviceInfo;
// Retrieve USBD version information, port driver capabilities and device
// capabilities such as speed, power, etc.
//

WDF_USB_DEVICE_INFORMATION_INIT(&deviceInfo);

status = WdfUsbTargetDeviceRetrieveInformation(
                            pDeviceContext->UsbDevice,
                            &deviceInfo);
waitWakeEnable = deviceInfo.Traits & WDF_USB_DEVICE_TRAIT_REMOTE_WAKE_CAPABLE;
```

### Enabling remote wakeup

In USB terminology, a USB device is enabled for remote wakeup when its DEVICE_REMOTE_WAKEUP feature is set. According to the USB specification, host software must set the remote wakeup feature on a device "only just prior" to putting the device to sleep. The KMDF function driver is required only to initialize the wake settings. KMDF and the Microsoft-supplied USB bus drivers issue the I/O requests and handle the hardware manipulation that is required to enable remote wakeup.

#### To initialize wake settings

1. Call **[WDF_DEVICE_POWER_POLICY_WAKE_SETTINGS_INIT](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdf_device_power_policy_wake_settings_init)** to initialize a **[WDF_DEVICE_POWER_POLICY_WAKE_SETTINGS](/windows-hardware/drivers/ddi/wdfdevice/ns-wdfdevice-_wdf_device_power_policy_wake_settings)** structure. This function sets the structure's **Enabled** member to **WdfUseDefault**, sets the **DxState** member to **PowerDeviceMaximum**, and sets the **UserControlOfWakeSettings** member to **WakeAllowUserControl**.
1. Call **[WdfDeviceAssignSxWakeSettings](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceassignsxwakesettings)** with the initialized structure. As a result, the device is enabled to wake from the D3 state, and the user can enable or disable the wake signal from the device property page in Device Manager.

The following code snippet from the Osrusbfx2 sample shows how to initialize wake settings to their default values:

```cpp
WDF_DEVICE_POWER_POLICY_WAKE_SETTINGS wakeSettings;

WDF_DEVICE_POWER_POLICY_WAKE_SETTINGS_INIT(&wakeSettings);
status = WdfDeviceAssignSxWakeSettings(Device, &wakeSettings);
if (!NT_SUCCESS(status)) {
    return status;
}
```

For USB devices that support selective suspend, the underlying bus driver prepares the device hardware to wake. So, USB function drivers rarely require an *EvtDeviceArmWakeFromS0* callback. The framework sends a selective suspend request to the USB bus driver when the idle time-out expires.

For the same reason, USB function drivers rarely require a *EvtDeviceWakeFromS0Triggered* or *EvtDeviceWakeFromSxTriggered* callback. Instead, the framework and the underlying bus driver handle all requirements for returning the device to the working state.

## Related topics

- [Selective suspend in USB drivers (WDF)](selective-suspend-in-usb-drivers-wdf.md)
- **[WdfDeviceAssignS0IdleSettings](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceassigns0idlesettings)**
- **[WdfDeviceAssignSxWakeSettings](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceassignsxwakesettings)**
- **[WdfDeviceStopIdle](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicestopidle)**
