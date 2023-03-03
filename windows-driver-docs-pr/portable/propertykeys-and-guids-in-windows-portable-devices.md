---
description: PROPERTYKEYs and GUIDs in Windows Portable Devices
title: PROPERTYKEYs and GUIDs in Windows Portable Devices
ms.date: 03/03/2023
---

# PROPERTYKEYs and GUIDs in Windows Portable Devices


A property or command is identified by a **PROPERTYKEY** structure. A **PROPERTYKEY** structure is made up of two parts: a GUID (the *fmtid* member) and a DWORD (the *pid* member). The GUID part is used to indicate the category the property or command belongs to (that is, related properties belong to the same category and related commands belong to the same category; therefore they will have the same *fmtid*). The DWORD part indicates the property or command ID, and is used to distinguish the individual properties or commands within a property or command category (that is, the *pid* values for properties or commands in the same category will be different).

The reference section of this document describes all the PROPERTYKEY values defined by WPD. These values correspond to commands, properties, and resources. If you create a custom PROPERTYKEY value, you should define a new GUID category; do not reuse the WPD GUID values or you risk conflicting with existing and future WPD-specified PROPERTYKEYs.

## <span id="related_topics"></span>Related topics


[**WPD\_CONTENT\_TYPE\_FUNCTIONAL\_OBJECT**](/previous-versions/windows/hardware/drivers/ff597845(v=vs.85))

[**Requirements for Objects**](requirements-for-objects.md)

[**Object Format GUIDs**](/previous-versions/windows/hardware/drivers/ff597651(v=vs.85))

[**Requirements for Resources**](/previous-versions/windows/hardware/drivers/ff597663(v=vs.85))

[**Commands**](/previous-versions/windows/hardware/drivers/ff597554(v=vs.85))

[**Properties and Attributes**](/previous-versions/windows/hardware/drivers/ff597900(v=vs.85))

[**WPD Drivers Overview**](wpd-drivers-overview.md)

 

