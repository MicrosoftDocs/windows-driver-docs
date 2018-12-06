---
title: Providing DEVMODE Structure Additions
description: Providing DEVMODE Structure Additions
ms.assetid: 7ce698f5-14c7-484d-be3d-b41c690b9576
keywords:
- user interface plug-ins WDK print , DEVMODEW structure additions
- UI plug-ins WDK print , DEVMODEW structure additions
- DEVMODEW
- private DEVMODE WDK print
- public DEVMODE WDK print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Providing DEVMODE Structure Additions





Your UI plug-in can add its own private members to the [**DEVMODEW**](https://msdn.microsoft.com/library/windows/hardware/ff552837) structure, as illustrated in the following figure.

![diagram illustrating public and private devmode sections](images/dvmdstru.png)

A UI plug-in can use these private DEVMODE members to store values associated with customized printer options. The plug-in makes these options available to the user by [modifying a driver-supplied property sheet page](modifying-a-driver-supplied-property-sheet-page.md) or by [adding new property sheet pages](adding-new-property-sheet-pages.md).

If your UI plug-in adds private DEVMODE members, the [**OEM\_DMEXTRAHEADER**](https://msdn.microsoft.com/library/windows/hardware/ff559588) structure must prefix the added members.

You are not required to add members to the DEVMODE structure, but if you do, your UI plug-in must implement the [**IPrintOemUI::DevMode**](https://msdn.microsoft.com/library/windows/hardware/ff554167) method. This method's purpose, depending on input arguments, is to return the size of, initialize, convert, or validate the additional DEVMODE members.

 

 




