---
title: UPS Minidriver Functionality
description: UPS Minidriver Functionality
ms.assetid: a93dbada-bcf7-4963-ba57-c6db5922c66b
keywords: ["UPS minidrivers WDK , functionality"]
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[battery\battery]:%20UPS%20Minidriver%20Functionality%20%20RELEASE:%20%286/7/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


