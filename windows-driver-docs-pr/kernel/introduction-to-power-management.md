---
title: Introduction to Power Management
description: Introduction to Power Management
ms.assetid: d0cac254-d723-45f3-bef6-eb1d64b5d656
keywords: ["power management WDK kernel , about power management"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Introduction to Power Management





Microsoft Windows supports a power management architecture that provides a comprehensive approach to system and device power management. This power management architecture is designed to meet ever-increasing user requirements, which include:

-   Customers are demanding that their computers be automatically available at all times, even when turned off. For example, network administrators want to manage computers late at night, and home users want to use their computer to receive faxes. Users with computers hidden away under desks want to be able to turn them by pressing a button on the keyboard or monitor.

-   Customers want to decrease the amount of power and total energy that a PC uses, whether the power comes from an electrical wall outlet or a battery.

To meet these ever-increasing user requirements, Windows must be able to manage the power that is used by any device in the system, including add-in boards such as graphics cards, network adapters, modems, and sound cards. To effectively manage power, the PC software, hardware, and Windows must work together in a framework that enables every device to be power managed in a consistent manner.

A PC configuration that takes full advantage of the Windows power management architecture, provides the following advantages to users:

-   Energy savings and extended battery life.

    Reducing system power consumption results in lower energy costs and longer battery life.

-   Minimal startup and shutdown delays.

    If a working state is not required, the system power state can be changed from the working state to a sleep state and, subsequently, quickly changed back to a working state as required. This allows the system to be responsive to the user, yet energy can be conserved during the time period that a working state is not required.

-   Quiet operation.

    In many cases the full capabilities of a system might not be required. Powering down devices that are not being used can reduce noise. This capability is important in situations where near-silent operation is highly desirable, such as in Media Center PCs.

In systems that support power management, the computer and its peripheral devices are maintained at the lowest feasible power level to accomplish the tasks at hand. Drivers cooperate with the operating system to manage power for their devices. If all drivers support power management, the operating system can manage power consumption on a system-wide basis, thus conserving power, shutting down and resuming quickly, and waking up when required.

This integrated approach to power management—involving the operating system, system hardware, device drivers, and device hardware—results in the following:

-   More intelligent power management decisions. At each level, the best-informed component directs power usage.

-   Greater reliability. Better power management decisions reduce the chance of ill-timed shutdowns and loss of data.

-   Platform independence. The operating system manages power in a controlled, uniform way across different hardware platforms, allowing maximum conservation of power on various devices.

-   Better device integration. Device drivers that conform to industry-wide specifications ensure maximum conservation regardless of the hardware platform.

Combined, these advantages result in greater power conservation and more efficient usage than has previously been possible.

The industry-wide OnNow initiative defines the hardware and software requirements for power management. For more information, see [Industry Initiatives for Power Management](industry-initiatives-for-power-management.md).

 

 




