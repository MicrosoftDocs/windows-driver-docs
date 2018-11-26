---
title: CPSUI-Supported Window Controls
description: CPSUI-Supported Window Controls
ms.assetid: 557aa4e6-e48e-44fe-b833-93728426b056
keywords:
- Common Property Sheet User Interface WDK print , window controls
- CPSUI WDK print , window controls
- property sheet pages WDK print , window controls
- window controls WDK CPSUI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# CPSUI-Supported Window Controls





CPSUI supports a set of window controls that provide a consistent interface to the user. Use of these window controls is particularly important when creating property sheet pages for printer devices and documents, because users expect a consistent interface for all printers.

CPSUI-supported window controls include:

-   Boxes containing two or three radio buttons

-   Scroll and track bars

-   Edit, list, and combo boxes

-   An up/down arrow box

-   A check box

This set of window controls must always be used when specifying [property sheet options](property-sheet-options.md). The window controls are specified by using [CPSUI option types](https://msdn.microsoft.com/library/windows/hardware/ff547142). While usually not necessary, appearance of these controls can be customized. For more information, see [Customizing CPSUI-Supported Window Controls](customizing-cpsui-supported-window-controls.md).

CPSUI also defines two special controls, called an extended check box and an extended push button. These controls, which provide capabilities beyond those of standard check boxes and push buttons, can be specified using the [**EXTCHKBOX**](https://msdn.microsoft.com/library/windows/hardware/ff548781) and [**EXTPUSH**](https://msdn.microsoft.com/library/windows/hardware/ff548795) structures, respectively.

 

 




