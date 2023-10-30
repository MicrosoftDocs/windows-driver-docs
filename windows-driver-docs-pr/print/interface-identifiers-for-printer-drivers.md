---
title: Interface Identifiers for Printer Drivers
description: Interface Identifiers for Printer Drivers
keywords:
- COM interfaces WDK print , interface identifiers
- interface identifiers WDK print
- plug-ins WDK print , interface identifiers
- identifiers WDK printer
- GUIDs WDK printer
ms.date: 01/27/2023
---

# Interface Identifiers for Printer Drivers

[!include[Print Support Apps](../includes/print-support-apps.md)]

A set of GUIDs is defined in prcomoem.h. Each of these GUIDs is an interface identifier for one of the COM interfaces used for communication between the printer drivers (Unidrv and Pscript5) and plug-ins.

For Windows 2000 and Windows XP, the following GUIDs are defined:

**IID_IPrintOemUI**
**IID_IPrintOemUI2** (Pscript5 UI plug-ins on Windows XP and later versions of the Windows operating system)
**IID_IPrintOemDriverUI**
**IID_IPrintCoreUI2** (Pscript5 UI plug-ins on Windows XP and later versions of the Windows operating system)
**IID_IPrintOemUni**
**IID_IPrintOemUni2** (Unidrv render plug-ins on Windows XP and later versions of the Windows operating system)
**IID_IPrintOemUni3** (Unidrv render plug-ins on Windows Vista and later versions of the Windows operating system)
**IID_IPrintOemDriverUni**
**IID_IPrintOemPS**
**IID_IPrintOemPS2** (Pscript5 render plug-ins on Windows XP and later versions of the Windows operating system)
**IID_IPrintOemDriverPS**
**IID_IPrintCorePS2** (Pscript5 render plug-ins on Windows XP and later versions of the Windows operating system)
Each GUID identifies one version of one interface. If a new version of an interface is defined, a new GUID is added to the list.

User interface plug-ins and rendering plug-ins must identify the interface versions they support. The printer driver (Unidrv or Pscript5) calls a plug-in's **IUnknown::QueryInterface** method (described in the Windows SDK documentation), specifying an interface identifier as input. If the plug-in supports the specified version, the method must return a pointer to the interface along with a return status of S_OK. Otherwise, it must return E_NOINTERFACE. The driver starts with the interface identifier for the most recent version and continues to call **QueryInterface** with earlier version identifiers until the method returns S_OK or the driver exhausts the list of version identifiers.

Likewise, Unidrv and Pscript5 provide **IUnknown::QueryInterface** methods for the [IPrintOemDriverUI](iprintoemdriverui-com-interface.md), [IPrintCoreUI2](iprintcoreui2-com-interface.md), [IPrintOemDriverUni](iprintoemdriveruni-com-interface.md), [IPrintOemDriverPS](iprintoemdriverps-com-interface.md), or [IPrintCorePS2](iprintcoreps2-com-interface.md) COM interfaces. Plug-ins should call the appropriate interface's **QueryInterface** method to determine the driver's supported interface version and to receive an interface pointer.
