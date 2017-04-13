---
title: Customizing CPSUI-Supported Window Controls
author: windows-driver-content
description: Customizing CPSUI-Supported Window Controls
ms.assetid: b9ced902-6368-4b3b-a974-81e7d38c0ced
keywords: ["Common Property Sheet User Interface WDK print , window controls", "CPSUI WDK print , window controls", "property sheet pages WDK print , window controls", "window controls WDK CPSUI", "customizing CPSUI-supported window controls WDK print"]
---

# Customizing CPSUI-Supported Window Controls


## <a href="" id="ddk-customizing-cpsui-supported-window-controls-gg"></a>


If you are using [CPSUI-supported window controls](cpsui-supported-window-controls.md) in conjunction with [CPSUI-supplied pages and templates](cpsui-supplied-pages-and-templates.md), CPSUI provides window control resources that describe the controls in a manner that allows them to fit together. Therefore, you do not need to provide resources for the controls.

On the other hand, if you are creating a property sheet page that does not use a CPSUI-supplied page or template, you must customize the CPSUI-supported window controls that you use. To do this, you need to provide window control resources for the [CPSUI option types](https://msdn.microsoft.com/library/windows/hardware/ff547142). You must specify identifiers for these resources using the **BegCtrlID** member of each option's [**OPTTYPE**](https://msdn.microsoft.com/library/windows/hardware/ff559670) structure.

If you are customizing CPSUI-supported window controls, remember that CPSUI does not display an option if the OPTIF\_HIDE flag set in the [**OPTITEM**](https://msdn.microsoft.com/library/windows/hardware/ff559656) structure. CPSUI moves the remaining controls to fill the space normally taken up by the hidden option. Therefore, if you are creating a page containing several simultaneously-displayed options, the following rules should be obeyed:

-   Each option should occupy the entire horizontal space of the property sheet page.

-   Option dialogs should not overlay each other.

-   For options represented by radio buttons that are arranged from left to right, buttons and icons should be aligned on the x axis. If the buttons are arranged from top to bottom, buttons and icons should be aligned on the y axis.

-   If several items share one group box, the group box must belong to the first [**OPTITEM**](https://msdn.microsoft.com/library/windows/hardware/ff559656), which is the topmost item in the group box. The group box must be large enough to contain all items associated with it.

Also, note that if radio buttons and icons are arranged top to bottom and some of these controls are hidden, CPSUI does not remove resulting white space in the y direction.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Customizing%20CPSUI-Supported%20Window%20Controls%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


