---
title: CPSUI-Supported Window Controls
author: windows-driver-content
description: CPSUI-Supported Window Controls
ms.assetid: 557aa4e6-e48e-44fe-b833-93728426b056
keywords:
- Common Property Sheet User Interface WDK print , window controls
- CPSUI WDK print , window controls
- property sheet pages WDK print , window controls
- window controls WDK CPSUI
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# CPSUI-Supported Window Controls


## <a href="" id="ddk-cpsui-supported-window-controls-gg"></a>


CPSUI supports a set of window controls that provide a consistent interface to the user. Use of these window controls is particularly important when creating property sheet pages for printer devices and documents, because users expect a consistent interface for all printers.

CPSUI-supported window controls include:

-   Boxes containing two or three radio buttons

-   Scroll and track bars

-   Edit, list, and combo boxes

-   An up/down arrow box

-   A check box

This set of window controls must always be used when specifying [property sheet options](property-sheet-options.md). The window controls are specified by using [CPSUI option types](https://msdn.microsoft.com/library/windows/hardware/ff547142). While usually not necessary, appearance of these controls can be customized. For more information, see [Customizing CPSUI-Supported Window Controls](customizing-cpsui-supported-window-controls.md).

CPSUI also defines two special controls, called an extended check box and an extended push button. These controls, which provide capabilities beyond those of standard check boxes and push buttons, can be specified using the [**EXTCHKBOX**](https://msdn.microsoft.com/library/windows/hardware/ff548781) and [**EXTPUSH**](https://msdn.microsoft.com/library/windows/hardware/ff548795) structures, respectively.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20CPSUI-Supported%20Window%20Controls%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


