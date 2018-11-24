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

-   [**UPSInit**](https://msdn.microsoft.com/library/windows/hardware/ff536313)

-   [**UPSGetState**](https://msdn.microsoft.com/library/windows/hardware/ff536312)

-   [**UPSWaitForStateChange**](https://msdn.microsoft.com/library/windows/hardware/ff536316)

-   [**UPSCancelWait**](https://msdn.microsoft.com/library/windows/hardware/ff536311)

-   [**UPSTurnOff**](https://msdn.microsoft.com/library/windows/hardware/ff536315)

-   [**UPSStop**](https://msdn.microsoft.com/library/windows/hardware/ff536314)

Additionally, the minidriver must export a [**DLLMain**](https://msdn.microsoft.com/library/windows/desktop/ms682583) function, as described in Microsoft Windows SDK documentation.

Besides exporting these functions, the minidriver must provide initial values for [UPS registry entries](ups-registry-entries.md) and then modify the values as necessary to reflect UPS state changes.

Typically, a UPS minidriver communicates with a UPS unit through a COM port by calling the [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858), [**ReadFile**](https://msdn.microsoft.com/library/windows/desktop/aa365467), and [**WriteFile**](https://msdn.microsoft.com/library/windows/desktop/aa365747) functions (described in Windows SDK documentation). The minidriver is responsible for implementing whatever communication protocol the UPS unit supports.

 

 




