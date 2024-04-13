---
title: Building a PSHED Plug-In
description: Building a PSHED Plug-In
ms.date: 03/03/2023
---

# Building a PSHED Plug-In


A PSHED plug-in is built by using the WDK like any other Windows Driver Model (WDM) device driver except that in addition to linking to the kernel and the hardware abstraction layer (HAL), a PSHED plug-in must also explicitly link to *Pshed.lib*.

**Note**  Starting with Windows 7, various Windows Hardware Error Architecture (WHEA) data types have been renamed from earlier versions of the WDK. For more information about these changes, see [Renamed WHEA Data Types](renamed-whea-data-types.md). If you plan to build an existing PSHED plug-in with Windows 7 or later version of the WDK, you can still use the former WHEA data type names. To do this, add the following information to the *sources* file that is used to build the plug-in:
`C_DEFINES = $(C_DEFINES) /DWHEA_DOWNLEVEL_TYPE_NAMES`

 

 

 




