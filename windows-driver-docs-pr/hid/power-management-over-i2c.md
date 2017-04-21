---
title: Power management for HID over the I²C
author: windows-driver-content
description: This section describes power management for devices that support HID over the I²C.
ms.assetid: 00FE1248-683F-48FE-8422-E51E88224955
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Power%20management%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


