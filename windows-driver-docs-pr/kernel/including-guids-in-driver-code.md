---
title: Including GUIDs in Driver Code
description: Including GUIDs in Driver Code
ms.assetid: 9235f9e6-9c40-4c4b-a98b-99e6b46a11ce
keywords: ["globally unique identifiers WDK kernel", "GUIDs WDK kernel", "identifiers WDK GUIDs"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Including GUIDs in Driver Code





To use GUIDs in a kernel-mode driver, you must do two things:

1.  Include the Initguid.h header file that redefines the **DEFINE\_GUID** macro.

    The Initguid.h header file redefines the **DEFINE\_GUID** macro to instantiate GUIDs (versus just declaring an EXTERN reference). Include this header file in the driver source file where the GUIDs should be instantiated. (User-mode applications include Objbase.h before including header files containing GUID definitions.)

2.  Include the header file(s) that define the GUIDs.

    After the statement to include Initguid.h, you include the header files containing the GUID definitions. A driver might include more than one header file that contains GUID definitions, including system-supplied header files and third-party header files.

The following code excerpt shows the sequence of statements for including GUIDs:

```cpp
:
// include system headers here such as wdm.h

#include <initguid.h>

// include system and driver-specific header files here that contain
// GUID definitions

...
```

Put the above statements in one module of the driver; typically the main module. When the above statements are present, the driver refers to a GUID using its symbolic name.








