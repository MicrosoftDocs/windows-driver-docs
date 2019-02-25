---
title: Adding GDL Extensions to an Existing PPD File
description: Adding GDL Extensions to an Existing PPD File
ms.assetid: 4d425701-85af-43e8-9ff2-ddfcc755f90c
keywords:
- in-box autoconfiguration support WDK printer , GDL extensions
- GDL files WDK printer
- extensions WDK GDL files
- PPD files WDK autoconfiguration , GDL extensions
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Adding GDL Extensions to an Existing PPD File


If you intend to add support for autoconfiguration to an existing in-box PPD file, follow these steps:

1.  Create the GDL file. The GDL file should have the \***BidiQuery** and \***BidiResponse** elements that correspond to the \***Feature**/\***Option** constructs as specified in the PPD file. Note that you must do this only for features that require bidi information.

2.  Include the GDL file as part of driver-dependent file list.

This section includes:

[New Keyword for PPD Schema](new-keyword-for-ppd-schema.md)

[Autoconfig Flow in Windows Vista for PPD](autoconfig-flow-in-windows-vista-for-ppd.md)

[Adding Constructs to Your GDL File for PPD](adding-constructs-to-your-gdl-file-for-ppd.md)

 

 




