---
title: Using Multiple GPD Files in a Minidriver
description: Using Multiple GPD Files in a Minidriver
ms.assetid: 2ec08b46-a286-4af8-a5d4-e0306f731b3f
keywords:
- GPD files WDK Unidrv , multiple
- multiple GPD files WDK Unidrv
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Multiple GPD Files in a Minidriver





Unidrv minidrivers can consist of more than one GPD file. This allows you to place characteristics that are common to more than one printer in one or more GPD files, and then to include these common GPD files in a particular printer's individual GPD file.

To include additional GPD files, you use \*Include directives, which are described in [Preprocessor Directives](preprocessor-directives.md). You can use multiple \*Include directives, as shown in the following example:

```cpp
*Include: "common1.gpd"
*Include: "common2.gpd"
*Include: "common3.gpd"
```

The \*Include directive's filename parameter cannot be a macro reference, and it cannot include a path specification.

Each included file must end with a complete GPD file entry, and the file must contain equal numbers of left and right braces. Included files can also contain \*Include directives.

The GPD parser treats the top-level GPD file and all included files as if they were one long file. Therefore, macros defined in one file can be referenced in subsequently included files. If a GPD file entry is duplicated, the most recently parsed entry replaces previous ones. Entries not duplicated are added to Unidrv's database.

 

 




