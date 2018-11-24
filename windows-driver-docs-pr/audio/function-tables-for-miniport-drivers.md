---
title: Function Tables for Miniport Drivers
description: Function Tables for Miniport Drivers
ms.assetid: 86b8bfa7-0c57-480b-b6f6-7c0214f53773
keywords:
- function tables WDK audio
- audio miniport drivers WDK , function tables
- miniport drivers WDK audio , function tables
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Function Tables for Miniport Drivers


## <span id="function_tables_for_miniport_drivers"></span><span id="FUNCTION_TABLES_FOR_MINIPORT_DRIVERS"></span>


A generic miniport driver's upper-edge interfaces (see [WDM Audio Terminology](wdm-audio-terminology.md)) consist of function tables. Some non-audio miniport drivers supply the function table to the port driver during registration, at which time the miniport driver informs the port driver of the size of the context structure that the miniport driver will require. The port driver copies the function table to some private location, allocates the context structure, and calls an initialization function in the function table, passing a pointer to the context structure.

Similarly, audio miniport drivers use function tables, but they are statically allocated and do not need to be copied by the port driver. The port driver also retrieves its context ("object") memory from a specified pool and installs a pointer to the function table into the context. Because the function table pointer is always the first field in the context, the port driver needs only a context pointer and can access the function table through the context.

This approach was taken because COM supplies a solid, efficient, widely-understood model for creating abstracted objects. The audio miniport driver model leverages industry experience with COM and the body of COM literature. Objects can be implemented and used in C or C++. Assembly language can also be used, but should only be used where portability is not required.

 

 




