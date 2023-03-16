---
title: UPS Minidriver Functionality
description: UPS Minidriver Functionality
keywords:
- UPS minidrivers WDK , functionality
ms.date: 04/20/2017
---

# UPS Minidriver Functionality

A UPS minidriver must export the following set of functions, which are called by the system-supplied UPS service:

- [**UPSInit**](/windows-hardware/drivers/ddi/upssvc/nf-upssvc-upsinit)

- [**UPSGetState**](/windows-hardware/drivers/ddi/upssvc/nf-upssvc-upsgetstate)

- [**UPSWaitForStateChange**](/windows-hardware/drivers/ddi/upssvc/nf-upssvc-upswaitforstatechange)

- [**UPSCancelWait**](/windows-hardware/drivers/ddi/upssvc/nf-upssvc-upscancelwait)

- [**UPSTurnOff**](/windows-hardware/drivers/ddi/upssvc/nf-upssvc-upsturnoff)

- [**UPSStop**](/windows-hardware/drivers/ddi/upssvc/nf-upssvc-upsstop)

Additionally, the minidriver must export a [**DLLMain**](/windows/desktop/Dlls/dllmain) function, as described in Microsoft Windows SDK documentation.

Besides exporting these functions, the minidriver must provide initial values for [UPS registry entries](ups-registry-entries.md) and then modify the values as necessary to reflect UPS state changes.

Typically, a UPS minidriver communicates with a UPS unit through a COM port by calling the [**CreateFile**](/windows/win32/api/fileapi/nf-fileapi-createfilea), [**ReadFile**](/windows/win32/api/fileapi/nf-fileapi-readfile), and [**WriteFile**](/windows/win32/api/fileapi/nf-fileapi-writefile) functions (described in Windows SDK documentation). The minidriver is responsible for implementing whatever communication protocol the UPS unit supports.
