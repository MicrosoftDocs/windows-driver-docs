---
title: Format Operations
description: Format Operations
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , texture format lists
- texture format lists WDK DirectX 8.0
- DPIXELFORMAT
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Format Operations


## <span id="ddk_format_operations_gg"></span><span id="DDK_FORMAT_OPERATIONS_GG"></span>


When reporting supported surface formats a DirectX 8.0 driver must also indicate which operations can be performed on surfaces of that format. The supported operations for a pixel format are reported through the **dwOperations** field of the [**DDPIXELFORMAT**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ddpixelformat) structure. The driver should set this field to the logical combination of all supported operations for surfaces of that format.

 

