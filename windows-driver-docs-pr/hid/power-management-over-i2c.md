---
title: Power management for HID over the I²C
description: This section describes power management for devices that support HID over the I²C.
ms.assetid: 00FE1248-683F-48FE-8422-E51E88224955
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Power management


This section describes power management for devices that support HID over the I²C transport.

## Power management and optimization


Windows 8 introduces a new power model labeled *Always On, Always Connected*. This model allows slates and PCs to be optimized for power and performance. At the same time,Windows 8is highly optimized for power consumption in situations when the PC is not in use. For example, it conserves power when the screen is turned off either intentionally or as a result of no user activity.

Because HID devices are a primary device class in Windows, they must adhere to this new power model.

### connected standby

Below is a short summary of how devices should behave during the connected standby power state.

|                                                                                                                                                                 |                                              |                                           |                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|-------------------------------------------|-----------------------------------------------------------|
| Input Source                                                                                                                                                    | Indicates User Presence in connected standby | Processed while in connected standby      | Device State when System transitions to connected standby |
| Digitizer                                                                                                                                                       | No                                           | Must not process                          | D3                                                        |
| Mouse                                                                                                                                                           | Yes                                          | Must process, will exit connected standby | D0                                                        |
| Keyboard                                                                                                                                                        | Yes                                          | Must process, will exit connected standby | D0                                                        |
| Rotation Lock                                                                                                                                                   | No                                           | Must not process                          | D3                                                        |
| Generic Desktop Controls - Volume Up - Volume Down - Channel Down - Channel Up - Fast Forward - Track Forward - Track Back - Play - Pause - Record - Track Stop | No                                           | Must process                              | D0                                                        |

 

For more information about connected standby please refer to the [Understanding Connected Standby](http://go.microsoft.com/fwlink/p/?linkid=241608) video.

### <a href="" id="supporting-connected-standby-in-hid-i2c-devices"></a>Supporting connected standby in HID I²C Devices

Devices on the I²C bus are enumerated by the Advanced Configuration and Power Interface (ACPI). As part of the HID-I²C Protocol Specification, power management for HIDI²C devices is supported by the SET\_POWER command. This command instructs the device to transition in and out of its lower power mode.

The inbox HIDI²C miniport driver passes along the D-IRP from HIDClass. This allows ACPI to, in turn, power-manage the device.

 

 




