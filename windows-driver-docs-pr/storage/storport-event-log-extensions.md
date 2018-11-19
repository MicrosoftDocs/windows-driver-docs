---
title: Storport Event Log Extensions
description: Storport Event Log Extensions
ms.assetid: 03b0bdef-cefa-4ad8-b9bf-a5f6b5f64cc6
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storport Event Log Extensions


Like many other types of drivers, Storport miniport drivers must create entries in the system event log to keep administrators informed of the condition of attached storage devices. Often these event log entries are created in response to device-related failures. Although the Windows kernel itself provides a flexible interface for creating event log entries, the Storport miniport model does not allow miniport drivers to access that interface directly. Rather, Storport provides a wrapper around the kernel's system event log facility, and miniport drivers use the wrapper to create event log entries.

In versions of Storport prior to Windows 7, Storport's system event log interface gave miniport drivers access to a small fraction of the capabilities of the kernel's system event log facility, which severely impacts the usefulness of miniport event log entries. For Windows 7, the new Storport event log interface gives miniport drivers full access to the capabilities of the Windows kernel event facility. This access enables miniport drivers to create event log entries that are truly useful in troubleshooting storage issues.

[**StorPortLogSystemEvent**](https://msdn.microsoft.com/library/windows/hardware/ff567428) is implemented as a Storport extended function and is available to miniport drivers using the existing extended function interface. Use of the extended function interface avoids a direct dynamic link reference to the new function; by avoiding that direct reference, miniport drivers that use the new function load properly on operating systems that do not support the function, with the function returning STOR\_STATUS\_NOT\_IMPLEMENTED when not supported. In this way, vendors can create a single miniport driver that runs on multiple OS releases, taking advantage of the new event logging function where it is supported.

 

 




