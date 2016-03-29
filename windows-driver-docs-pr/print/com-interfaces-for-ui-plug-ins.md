---
title: COM Interfaces for UI Plug-Ins
description: COM Interfaces for UI Plug-Ins
ms.assetid: 9cc6502b-a003-4d0b-857e-4653cf6fa0ea
keywords: ["user interface plug-ins WDK print , COM interfaces", "UI plug-ins WDK print , COM interfaces", "COM interfaces WDK print , user interface plug-ins"]
---

# COM Interfaces for UI Plug-Ins


## <a href="" id="ddk-com-interfaces-for-ui-plug-ins-gg"></a>


The following COM interfaces are defined for communication between Microsoft's printer drivers and UI plug-ins:

-   [IPrintOemCommon COM interface](iprintoemcommon-com-interface.md), which provides methods to specify and get device information.

-   [IPrintOemUI COM interface](iprintoemui-com-interface.md), which enables the [printer interface DLL](printer-interface-dll.md) for Unidrv or Pscript5 to call UI plug-ins.

-   [IPrintOemUI2 COM interface](iprintoemui2-com-interface.md), which extends the [IPrintOemUI COM interface](iprintoemui-com-interface.md).

-   [IPrintOemUIMXDC COM interface](iprintoemuimxdc-com-interface.md), which enables UI plug-ins to control the conversion from GDI calls to XPS output in filter pipeline drivers.

-   [IPrintOemDriverUI COM interface](iprintoemdriverui-com-interface.md), which supplies utility operations to UI plug-ins.

-   [IPrintCoreUI2 COM interface](iprintcoreui2-com-interface.md), which provides helper methods for minidriver UI plug-ins.

The following figure shows the inheritance tree for the COM interfaces that are used in UI plug-ins.

![diagram illustrating the inheritance tree for the com interfaces used in ui plug-ins](images/uiintf2.png)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20COM%20Interfaces%20for%20UI%20Plug-Ins%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




