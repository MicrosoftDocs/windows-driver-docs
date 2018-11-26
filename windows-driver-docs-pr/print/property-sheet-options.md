---
title: Property Sheet Options
description: Property Sheet Options
ms.assetid: 572330d6-1a1b-46fd-bfb4-be2b0990bca4
keywords:
- Common Property Sheet User Interface WDK print , property sheet options
- CPSUI WDK print , property sheet options
- property sheet pages WDK print , property sheet options
- property sheets WDK print
- selectable property sheet page items WDK print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Property Sheet Options





A property sheet option is a displayable, selectable item on a property sheet page. Typically, users can modify an option's value. CPSUI helps applications create options in a standard format, using a predefined set of [CPSUI-supported window controls](cpsui-supported-window-controls.md). Applications do not have to provide resources for these controls.

Each property sheet page typically contains several options. For each property sheet option, a CPSUI application must use the following CPSUI structures:

-   One [**OPTITEM**](https://msdn.microsoft.com/library/windows/hardware/ff559656) structure, which identifies the option's display name and other characteristics.

-   One [**OPTTYPE**](https://msdn.microsoft.com/library/windows/hardware/ff559670) structure, which identifies the option's display dialog type ([CPSUI option type](https://msdn.microsoft.com/library/windows/hardware/ff547142)).

-   One or more [**OPTPARAM**](https://msdn.microsoft.com/library/windows/hardware/ff559660) structures, which identify the option's user-selectable parameter values.

To use these CPSUI structures to describe property sheet options, the page containing the option must be defined using a [**COMPROPSHEETUI**](https://msdn.microsoft.com/library/windows/hardware/ff546211) structure.

 

 




