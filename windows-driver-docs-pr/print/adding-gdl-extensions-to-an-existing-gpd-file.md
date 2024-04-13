---
title: Adding GDL Extensions to an Existing GPD File
description: Adding GDL Extensions to an Existing GPD File
keywords:
- in-box autoconfiguration support WDK printer , GDL extensions
- GDL files WDK printer
- extensions WDK GDL files
- GPD files WDK GDL extensions
- GPD files WDK GDL extensions , adding
ms.date: 04/20/2017
---

# Adding GDL Extensions to an Existing GPD File


If you intend to add support for autoconfiguration to an existing in-box GPD file, you should:

1.  Create the GDL file. The GDL file should have the **\*BidiQuery** and **\*BidiResponse** elements that correspond to the **\*Feature**/**\*Option** constructs, as specified in the PPD file. Note that you must add these elements only for features that require bidi information.

2.  Include the GDL file as part of the driver-dependent file list.

This section includes:

[New Keyword for GPD Schema](new-keyword-for-gpd-schema.md)

[Autoconfiguration Flow for GPD in Windows Vista](autoconfiguration-flow-for-gpd-in-windows-vista.md)

[Adding Constructs to Your GDL File for GPD](adding-constructs-to-your-gdl-file-for-gpd.md)

 

 




