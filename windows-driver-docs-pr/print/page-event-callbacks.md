---
title: Page Event Callbacks
author: windows-driver-content
description: Page Event Callbacks
MS-HAID:
- 'cpsui\_539db0b2-f4a4-4a51-9813-58b097190591.xml'
- 'print.page\_event\_callbacks'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 891f62ec-d009-42c8-8143-73bfe737a946
keywords: ["callback functions WDK CPSUI", "Common Property Sheet User Interface WDK print , callbacks", "CPSUI WDK print , callbacks", "property sheet pages WDK print , callbacks", "page event callbacks WDK CPSUI", "event callbacks WDK CPSUI"]
---

# Page Event Callbacks


## <a href="" id="ddk-page-event-callbacks-gg"></a>


When a user interacts with a property sheet page, the operation system sends notification of such window events as a changed focus or a modified value. How a CPSUI application receives notification of a page's window events depends on how the application has defined the page:

-   If the page was defined using [CPSUI-supplied pages and templates](cpsui-supplied-pages-and-templates.md), it can supply a [CPSUI message handler](cpsui-message-handler.md).

-   If the application created a customized page that is not supplied by CPSUI, it must provide a dialog box procedure. For more information, see [Dialog Box Procedures and CPSUI](dialog-box-procedures-and-cpsui.md).

A CPSUI application supplies CPSUI with the address of a page event callback when it calls the [**ComPropSheet**](https://msdn.microsoft.com/library/windows/hardware/ff546207) function.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Page%20Event%20Callbacks%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


