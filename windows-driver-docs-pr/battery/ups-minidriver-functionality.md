---
title: UPS Minidriver Functionality
description: UPS Minidriver Functionality
ms.assetid: a93dbada-bcf7-4963-ba57-c6db5922c66b
keywords:
- UPS minidrivers WDK , functionality
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# UPS Minidriver Functionality


## <span id="ddk_ups_minidriver_functionality_kg"></span><span id="DDK_UPS_MINIDRIVER_FUNCTIONALITY_KG"></span>


A UPS minidriver must export the following set of functions, which are called by the system-supplied UPS service:

-   [**UPSInit**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/upssvc/nf-upssvc-upsinit)

-   [**UPSGetState**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/upssvc/nf-upssvc-upsgetstate)

-   [**UPSWaitForStateChange**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/upssvc/nf-upssvc-upswaitforstatechange)

-   [**UPSCancelWait**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/upssvc/nf-upssvc-upscancelwait)

-   [**UPSTurnOff**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/upssvc/nf-upssvc-upsturnoff)

-   [**UPSStop**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/upssvc/nf-upssvc-upsstop)

Additionally, the minidriver must export a [**DLLMain**](https://docs.microsoft.com/windows/desktop/Dlls/dllmain) function, as described in Microsoft Windows SDK documentation.

Besides exporting these functions, the minidriver must provide initial values for [UPS registry entries](ups-registry-entries.md) and then modify the values as necessary to reflect UPS state changes.

Typically, a UPS minidriver communicates with a UPS unit through a COM port by calling the [**CreateFile**](https://docs.microsoft.com/windows/desktop/api/fileapi/nf-fileapi-createfilea), [**ReadFile**](https://docs.microsoft.com/windows/desktop/api/fileapi/nf-fileapi-readfile), and [**WriteFile**](https://docs.microsoft.com/windows/desktop/api/fileapi/nf-fileapi-writefile) functions (described in Windows SDK documentation). The minidriver is responsible for implementing whatever communication protocol the UPS unit supports.

 

 




