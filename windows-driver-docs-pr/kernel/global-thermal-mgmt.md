---
title: Global thermal management 
description: Learn about the GUID_THERMAL_COOLING_INTERFACE driver interface and how it's used in global thermal management.
keywords: ["global thermal managment", "thermal"]
ms.date: 06/16/2017
---

# Global thermal management 

The GUID_THERMAL_COOLING_INTERFACE driver interface enables device drivers to participate in global thermal management across a variety of devices in the hardware platform. Drivers for devices that have thermal management capabilities implement the callback routines in this interface. The operating system calls these routines to dynamically manage thermal levels in the platform in response to changes in user activity and environmental conditions.

By preventing overheating, Windows thermal management keeps devices operating reliably and prevents user-accessible surfaces from becoming uncomfortably hot. Windows intelligently balances the thermal-level requirements of the devices in the platform to extend the time that the platform can operate on a battery charge, and to maintain the appearance of a computer that is always on and always connected.

For more information, see [Device-Level Thermal Management](device-level-thermal-management.md).

