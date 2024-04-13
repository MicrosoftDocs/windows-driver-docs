---
title: Using EnumOptions
description: Using EnumOptions
keywords:
- EnumOptions
ms.date: 01/31/2023
---

# Using EnumOptions

[!include[Print Support Apps](../includes/print-support-apps.md)]

A caller can use **EnumOptions** to retrieve a keyword list of options for supported driver features and any PPD features. For PPD features, **EnumOptions** is always supported and it returns the options defined by PPD.

For driver features, **EnumOptions** is supported only for features that are currently supported and have a fixed set of options. For example: %AddEuro has two options: "True" and "False", and %PageOrder has two options "FrontToBack" and "BackToFront". **EnumOptions** is supported for %AddEuro (if the Language level is 2 and higher), as is %PageOrder (if spooler EMF spooling is enabled). But features such as %CustomPageSize, %PSMemory, and others have an unlimited number of possible options, which means that **EnumOptions** isn't supported for them.

For driver features that aren't currently supported, or for supported driver features that aren't enumerable via **EnumOptions**, **EnumOptions** returns E\_NOTIMPL.

Also, some options of a driver feature may not be supported under certain conditions. For example, if spooler EMF spooling is disabled on Windows 2000 and later operating system releases, then the "Booklet" option isn't supported for the %PagePerSheet feature. For another example, if the printer doesn't have a Type42 rasterizer, then "NativeTrueType" option isn't supported for %TTDownloadFormat. These unsupported options won't appear in the output keyword list of EnumOptions.

Pscript handles the following feature keywords in a special way:

- The \*CustomPageSize feature keyword is converted into an option of the \*PageSize feature keyword, with "CustomPageSize" being the option keyword. Call **GetOptionAttribute** to obtain its PPD parameters.

- The \*ManualFeed True entry is converted into an option of the \*InputSlot feature keyword, with "ManualFeed" being the option keyword name.

- For the \*InputSlot feature keyword, Pscript always adds a driver-generated option with option keyword name "\*UseFormTrayTable" as the first option (the "\*" prefix is used in the option keyword name to avoid possible name conflict with PPD-defined options), which is followed by options defined in the PPD. If the "\*UseFormTrayTable" option is selected, Pscript will use the form-to-tray assignment table to automatically select the paper tray that supports the selected paper size.
