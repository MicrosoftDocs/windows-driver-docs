---
title: Game Controller Control Panel
description: Game Controller Control Panel
ms.assetid: fb68102a-24d6-4dda-8f27-69366a2129bc
keywords: ["property sheets WDK DirectInput , control panel structure", "game controllers WDK DirectInput , control panel structure", "control panels WDK DirectInput , architecture"]
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Game Controller Control Panel





The basic architecture of the DirectInput control panel consists of the DirectInput game controller control panel, the abstraction-layer library that supports the **IDIGameCntrlPropSheet** COM interface, and a COM object for each game controller property sheet.

**Note**   The word "object" describes an entity created by CreateInstance to support the methods of a COM interface, even when these methods are not being called through an object-oriented programming language such as C++. The word "sheet" describes the dialog into which the pages insert. The word "page" describes the content dialogs of the "property sheet" dialog.

 

In the interest of portability between Microsoft Windows 95/98/Me and Windows NT 4.0 and later, the DirectInput control panel works directly with DirectInput, which in turn works directly with device drivers. As a by-product of this, the DirectInput control panel has access to input devices even when the application is in the background.

 

 




