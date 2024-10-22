---
title: Power Management for HID Over the I2C
description: This article describes power management for devices that support HID over the I2C.
ms.date: 10/22/2024
---

# HID power management over the I2C

This article describes power management for devices that support HID over the I2C transport.

## Power management and optimization

Windows 8 introduces a new power model labeled *Always On, Always Connected*. This model allows slates and PCs to be optimized for power and performance. At the same time, Windows 8 is highly optimized for power consumption in situations when the PC isn't in use. For example, it conserves power when the screen is turned off either intentionally or as a result of no user activity.

Because HID devices are a primary device class in Windows, they must adhere to this new power model.

### Connected standby

The following table shows a short summary of how devices should behave during the connected standby power state.

| Input Source | Indicates User Presence in connected standby | Processed while in connected standby | Device State when System transitions to connected standby |
|--|--|--|--|
| Digitizer | No | Must not process | D3 |
| Mouse | Yes | Must process, exits connected standby | D0 |
| Keyboard | Yes | Must process, exits connected standby | D0 |
| Rotation Lock | No | Must not process | D3 |
| Generic Desktop Controls - Volume Up - Volume Down - Channel Down - Channel Up - Fast Forward - Track Forward - Track Back - Play - Pause - Record - Track Stop | No | Must process | D0 |

For more information about connected standby, see the [Understanding Connected Standby](/events/build-build2011/hw-456t) video.

### Supporting connected standby in HID I2C Devices

The Advanced Configuration and Power Interface (ACPI) enumerates devices on the I2C bus. The SET_POWER command supports power management for HIDI2C devices as specified in the HID-I2C Protocol Specification. This command instructs the device to transition in and out of its lower power mode.

The inbox HIDI2C miniport driver passes along the D-IRP from HIDClass, allowing ACPI to power-manage the device.
