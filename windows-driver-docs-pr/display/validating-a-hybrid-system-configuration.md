---
title: Validating a hybrid system configuration
ms.assetid: 9DB53DAB-0A3D-48A4-84C0-8D60F56B64E8
description: A decription of the procedure to validate a hybrid system.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Validating a hybrid system configuration


This procedure is used starting in Windows 8.1 to validate the configuration of a [hybrid system](using-cross-adapter-resources-in-a-hybrid-system.md) of display adapters:

1.  When the system boots, one of the display adapters is marked as the current POST adapter. If this POST adapter supports Windows Display Driver Model (WDDM) 1.3 and has an integrated display panel, it's considered an *integrated hybrid* adapter.
2.  A discrete adapter in a hybrid system is considered a *hybrid discrete* adapter. It must:
    -   Set the [**DXGK\_DRIVERCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff561062).**HybridDiscrete** member.
    -   Support WDDM 1.3.
    -   Support cross-adapter resources.
    -   Have no display outputs.

3.  Only one WDDM hybrid discrete adapter is allowed on the system.
4.  When an integrated hybrid adapter is detected:
    -   Any new WDDM 1.3 display adapter (excluding an adapter that matches (2) or (3) or is a basic display or basic render driver) will not be loaded.
    -   Any loaded WDDM 1.3 display adapter (excluding an adapter that matches (2) or (3) or is a basic display or basic render driver) that is not a hybrid discrete adapter will be stopped.

5.  Drivers that support WDDM versions prior to 1.3 are allowed to load even when an integrated hybrid adapter is present.

 

 





