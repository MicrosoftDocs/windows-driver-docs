---
title: Using EnumOptions
author: windows-driver-content
description: Using EnumOptions
ms.assetid: 6ce16d28-eff7-4701-a592-046f364cda44
keywords:
- EnumOptions
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using EnumOptions


## <a href="" id="ddk-using-enumoptions-gg"></a>


A caller can use **EnumOptions** to retrieve a keyword list of options for supported driver features and any PPD features. For PPD features, **EnumOptions** is always supported and it returns the options defined by PPD.

For driver features, **EnumOptions** is supported only for features that are currently supported and have a fixed set of options. For example: %AddEuro has two options: "True" and "False", and %PageOrder has two options "FrontToBack" and "BackToFront". **EnumOptions** is supported for %AddEuro (if the Language level is 2 and above), as is %PageOrder (if spooler EMF spooling is enabled). But features such as %CustomPageSize, %PSMemory, and others have an unlimited number of possible options, which means that **EnumOptions** is not supported for them.

For driver features that are not currently supported, or for supported driver features that are not enumerable via **EnumOptions**, **EnumOptions** returns E\_NOTIMPL.

Also, some options of a driver feature may not be supported under certain conditions. For example, if spooler EMF spooling is disabled on Windows 2000 and later operating system releases, then the "Booklet" option is not supported for the %PagePerSheet feature. For another example, if the printer does not have a Type42 rasterizer, then "NativeTrueType" option is not supported for %TTDownloadFormat. These unsupported options will not appear in the output keyword list of EnumOptions.

Pscript handles the following feature keywords in a special way:

-   The \*CustomPageSize feature keyword is converted into an option of the \*PageSize feature keyword, with "CustomPageSize" being the option keyword. Call **GetOptionAttribute** to obtain its PPD parameters.

-   The \*ManualFeed True entry is converted into an option of the \*InputSlot feature keyword, with "ManualFeed" being the option keyword name.

-   For the \*InputSlot feature keyword, Pscript always adds a driver-generated option with option keyword name "\*UseFormTrayTable" as the first option (the "\*" prefix is used in the option keyword name to avoid possible name conflict with PPD-defined options), which is followed by options defined in the PPD. If the "\*UseFormTrayTable" option is selected, Pscript will use the form-to-tray assignment table to automatically select the paper tray that supports the selected paper size.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Using%20EnumOptions%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


