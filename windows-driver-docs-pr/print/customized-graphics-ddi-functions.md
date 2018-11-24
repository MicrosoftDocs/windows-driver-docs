---
title: Customized Graphics DDI Functions
description: Customized Graphics DDI Functions
ms.assetid: 33d7d567-5371-4873-a4ef-cd2b06f65d73
keywords:
- rendering plug-ins WDK print , graphics DDI functions
- graphics DDI functions WDK print
- hooking graphics DDI functions WDK print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Customized Graphics DDI Functions





Printer minidriver developers can extend the capabilities of the core printer driver graphics DDIs by implementing plug-in methods. A rendering plug-in can hook out some graphics DDI functions to provide customized implementations of the core printer driver functions. Developers of new printer rendering plug-ins should implement COM-based methods for their plug-ins. See [COM Interfaces for Rendering Plug-Ins](com-interfaces-for-rendering-plug-ins.md) for a list of the defined COM interfaces.

Prior to the publication of the COM interfaces, IHVs could extend the capabilities of the graphics DDIs by implementing one or more OEM*Xxx* functions for their rendering plug-ins. Although the use of these functions is still supported for compatibility reasons, writers of new rendering plug-ins should use the methods in the COM interfaces.

The rest of this section contains the following topics:

[COM-Based Rendering Plug-Ins](com-based-rendering-plug-ins.md)

[Non-COM-Based Rendering Plug-Ins](non-com-based-rendering-plug-ins.md)

 

 




