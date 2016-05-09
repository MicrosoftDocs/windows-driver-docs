---
title: Storport Event Log Extensions
description: Storport Event Log Extensions
ms.assetid: 03b0bdef-cefa-4ad8-b9bf-a5f6b5f64cc6
---

# Storport Event Log Extensions


Like many other types of drivers, Storport miniport drivers must create entries in the system event log to keep administrators informed of the condition of attached storage devices. Often these event log entries are created in response to device-related failures. Although the Windows kernel itself provides a flexible interface for creating event log entries, the Storport miniport model does not allow miniport drivers to access that interface directly. Rather, Storport provides a wrapper around the kernel's system event log facility, and miniport drivers use the wrapper to create event log entries.

In versions of Storport prior to Windows 7, Storport's system event log interface gave miniport drivers access to a small fraction of the capabilities of the kernel's system event log facility, which severely impacts the usefulness of miniport event log entries. For Windows 7, the new Storport event log interface gives miniport drivers full access to the capabilities of the Windows kernel event facility. This access enables miniport drivers to create event log entries that are truly useful in troubleshooting storage issues.

[**StorPortLogSystemEvent**](https://msdn.microsoft.com/library/windows/hardware/ff567428) is implemented as a Storport extended function and is available to miniport drivers using the existing extended function interface. Use of the extended function interface avoids a direct dynamic link reference to the new function; by avoiding that direct reference, miniport drivers that use the new function load properly on operating systems that do not support the function, with the function returning STOR\_STATUS\_NOT\_IMPLEMENTED when not supported. In this way, vendors can create a single miniport driver that runs on multiple OS releases, taking advantage of the new event logging function where it is supported.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Storport%20Event%20Log%20Extensions%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




