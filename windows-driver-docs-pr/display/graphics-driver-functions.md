---
title: Graphics Driver Functions
description: Graphics Driver Functions
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Graphics Driver Functions


## <span id="ddk_graphics_driver_functions_gg"></span><span id="DDK_GRAPHICS_DRIVER_FUNCTIONS_GG"></span>


The topics that follow describe the driver entry point functions, categorizing them as required, required under certain circumstances, and optional.

[Required Graphics Driver Functions](required-graphics-driver-functions.md)

[Conditionally Required Graphics Driver Functions](conditionally-required-graphics-driver-functions.md)

[Optional Graphics Driver Functions](optional-graphics-driver-functions.md)

When a device driver returns an error, it should typically call the GDI [**EngSetLastError**](/windows/win32/api/winddi/nf-winddi-engsetlasterror) function to report an extended error code. The application program can then retrieve the error code.

 

