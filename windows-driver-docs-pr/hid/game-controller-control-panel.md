---
title: Game Controller Control Panel
author: windows-driver-content
description: Game Controller Control Panel
MS-HAID:
- 'di\_ed719f0f-7ceb-4b44-9959-e8de9b5e37a0.xml'
- 'hid.game\_controller\_control\_panel'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: fb68102a-24d6-4dda-8f27-69366a2129bc
keywords: ["property sheets WDK DirectInput , control panel structure", "game controllers WDK DirectInput , control panel structure", "control panels WDK DirectInput , architecture"]
---

# Game Controller Control Panel


## <a href="" id="ddk-game-controller-control-panel-di"></a>


The basic architecture of the DirectInput control panel consists of the DirectInput game controller control panel, the abstraction-layer library that supports the **IDIGameCntrlPropSheet** COM interface, and a COM object for each game controller property sheet.

**Note**   The word "object" describes an entity created by CreateInstance to support the methods of a COM interface, even when these methods are not being called through an object-oriented programming language such as C++. The word "sheet" describes the dialog into which the pages insert. The word "page" describes the content dialogs of the "property sheet" dialog.

 

In the interest of portability between Microsoft Windows 95/98/Me and Windows NT 4.0 and later, the DirectInput control panel works directly with DirectInput, which in turn works directly with device drivers. As a by-product of this, the DirectInput control panel has access to input devices even when the application is in the background.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Game%20Controller%20Control%20Panel%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


