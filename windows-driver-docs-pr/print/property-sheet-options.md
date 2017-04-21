---
title: Property Sheet Options
author: windows-driver-content
description: Property Sheet Options
ms.assetid: 572330d6-1a1b-46fd-bfb4-be2b0990bca4
keywords:
- Common Property Sheet User Interface WDK print , property sheet options
- CPSUI WDK print , property sheet options
- property sheet pages WDK print , property sheet options
- property sheets WDK print
- selectable property sheet page items WDK print
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Property Sheet Options


## <a href="" id="ddk-property-sheet-options-gg"></a>


A property sheet option is a displayable, selectable item on a property sheet page. Typically, users can modify an option's value. CPSUI helps applications create options in a standard format, using a predefined set of [CPSUI-supported window controls](cpsui-supported-window-controls.md). Applications do not have to provide resources for these controls.

Each property sheet page typically contains several options. For each property sheet option, a CPSUI application must use the following CPSUI structures:

-   One [**OPTITEM**](https://msdn.microsoft.com/library/windows/hardware/ff559656) structure, which identifies the option's display name and other characteristics.

-   One [**OPTTYPE**](https://msdn.microsoft.com/library/windows/hardware/ff559670) structure, which identifies the option's display dialog type ([CPSUI option type](https://msdn.microsoft.com/library/windows/hardware/ff547142)).

-   One or more [**OPTPARAM**](https://msdn.microsoft.com/library/windows/hardware/ff559660) structures, which identify the option's user-selectable parameter values.

To use these CPSUI structures to describe property sheet options, the page containing the option must be defined using a [**COMPROPSHEETUI**](https://msdn.microsoft.com/library/windows/hardware/ff546211) structure.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Property%20Sheet%20Options%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


