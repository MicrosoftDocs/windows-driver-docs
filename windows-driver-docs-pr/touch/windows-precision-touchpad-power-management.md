---
title: Power Management
description: This topic describes power management for a Windows Precision Touchpad implementation.
ms.assetid: 7B7181F2-08EF-4231-8DAB-5297F0962173
---

#  Power Management


This topic describes power management for a Windows Precision Touchpad implementation.

## <span id="Power_consumption"></span><span id="power_consumption"></span><span id="POWER_CONSUMPTION"></span>Power consumption


Power consumption requirements for the Active and Idle modes of a Windows Precision Touchpad (irrespective of bus connectivity) are governed by the following formula:

**0.9 x (IDLE Power Consumption in mA) + 0.1 x (Active Power Consumption in mA) &lt;= 25**

Power consumption for the Sleep mode of a Windows Precision Touchpad (irrespective of bus connectivity) is required to be &lt;= 1mW.

## <span id="I2C_devices"></span><span id="i2c_devices"></span><span id="I2C_DEVICES"></span>I²C devices


I²C connected Windows Precision Touchpads shall implement support for four distinct power states: Active, Idle, Sleep (Armed for Wake) and Off, as shown in *Figure 1 I2C Device Power States*.

![i2c device power states](images/implementationfig2i2cdevicepowerstates.jpg)

**Figure 1 I2C Device Power States**

### <span id="Active_state"></span><span id="active_state"></span><span id="ACTIVE_STATE"></span>Active state

The Active state is defined as the device operating mode when one or more contacts are present, the button is down, or there has been activity within 120 seconds. When power is applied to a device, after device booting is completed, it shall be ready in the Active power state.

A device shall adhere to the contact down latency and contact move latency requirements for this mode.

### <span id="Idle_state"></span><span id="idle_state"></span><span id="IDLE_STATE"></span>Idle state

The Idle state is defined as the device operating mode when no contacts or button activity has occurred within 120 seconds.

A device can elect to reduce scan rate in this mode to meet the power consumption requirements while still adhering to the contact down latency requirement for this mode.

After the device has detected either contact or button activity, it shall transition back to the Active state.

### <span id="Sleep__armed_for_wake__state"></span><span id="sleep__armed_for_wake__state"></span><span id="SLEEP__ARMED_FOR_WAKE__STATE"></span>Sleep (armed for wake) state

The Sleep state is defined as the device operating mode when the device has been issued a HID I2C SET\_POWER SLEEP command by the host.

In the Sleep state, a device shall consume no greater than 1mW. A device can elect to reduce scan rate significantly in this mode to meet the power consumption requirement while still being capable of asserting an interrupt for either contact or button activity to wake the system. A Windows Precision Touchpad shall ensure that interrupts are not asserted for spurious contacts that would result in an unintended system wake. There are no contact down latency requirements for this mode; however it is recommended that greater than one second of continuous contact should result in an interrupt being asserted.

The device shall transition to the Active state upon receipt of a host issued HID I2C SET\_POWER ON command.

### <span id="Off_state"></span><span id="off_state"></span><span id="OFF_STATE"></span>Off state

The Off state is defined as the device operating mode when the device has had its power completely removed. When power is applied to a device, after device booting is completed (which shall take no longer than 100ms), it shall be ready in the Active power state.

In the Off state, a device shall consume no power.

## <span id="USB_devices"></span><span id="usb_devices"></span><span id="USB_DEVICES"></span>USB devices


USB-connected Windows Precision Touchpads shall implement support for four distinct power states; Active, Idle, Sleep (Armed for Wake) and Off, as shown in *Figure 2 USB Device Power States*.

![usb power states](images/implementationfig3usbpowerstates.png)

**Figure 2 USB Device Power States**

### <span id="Active_state"></span><span id="active_state"></span><span id="ACTIVE_STATE"></span>Active state

The Active state is defined as the device operating mode when the host has not suspended the device. When power is applied to a device, after device booting is completed, it shall be ready in the Active power state.

A device shall adhere to the contact down latency and contact move latency requirements for this mode.

### <span id="Idle_state"></span><span id="idle_state"></span><span id="IDLE_STATE"></span>Idle state

The Idle State is defined as the device operating mode when no contacts or button activity has occurred within a host defined period and has therefore been suspended. This is referred to as USB selective suspend.

All USB connected Windows Precision Touchpads shall support selective suspend and report this capability by using a Microsoft OS descriptor. For additional details see [Microsoft OS Descriptors](http://go.microsoft.com/fwlink/p/?LinkID=318026).

A device can elect to reduce scan rate in this mode to meet the power consumption requirements while still adhering to the contact down latency requirement for this mode.

After the device has detected either contact or button activity, it shall signal a remote wake. From that event, the device shall buffer at least 100ms worth of contact reports to ensure that the little to no input is lost while the USB host controller is resuming.

### <span id="Sleep__armed_for_wake__state"></span><span id="sleep__armed_for_wake__state"></span><span id="SLEEP__ARMED_FOR_WAKE__STATE"></span>Sleep (armed for wake) state

The Sleep state is defined as the device operating mode when the host has transitioned to S3 or connected standby. This is indicated to the device by the latency mode feature report, with a value of one indicating maximum latency is permitted. The device shall exit this high latency mode both on activity and on host resume.

In the Sleep state, a device shall consume no greater than 1mW. A device can elect to reduce scan rate significantly in this mode to meet the power consumption requirement while still being capable of signaling a remote wake for either contact or button activity to wake the system. A Windows Precision Touchpad shall ensure that remote wake is not signaled for spurious contacts that would result in an unintended system wake. There are no contact down latency requirements for this mode. It is recommended that a continuous contact of more than 1 second should result in signaling a remote wake. A contact occurrence that causes entry into the sleep state should not be reported to wake the system.

### <span id="Off_state"></span><span id="off_state"></span><span id="OFF_STATE"></span>Off state

The Off state is defined as the device operating mode when the device has had its power completely removed. When power is applied to a device, after device booting is completed (which shall take no longer than 250ms), it shall be ready in the Active power state.

In the Off state, a device shall consume no power.

 

 




