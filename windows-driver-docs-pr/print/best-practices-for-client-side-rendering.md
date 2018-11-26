---
title: Best Practices for Client-Side Rendering
description: Best Practices for Client-Side Rendering
ms.assetid: d05086c1-4e0b-4767-bb1d-7b6d73b1b210
keywords:
- client-side rendering WDK print , best practices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Best Practices for Client-Side Rendering


You should keep the following items in mind when writing your printer drivers so that they work properly with client-side rendering:

-   Printer drivers should be installed as driver packages.

-   Printer drivers should use the SetPrinterData or SetPrinterDataEx function to store printer configuration information. For more information about these functions, see the Microsoft Windows SDK documentation.

-   Printer drivers that use a custom print processor must include the processor in the driver package and make sure that Point and Print loads it onto the client computer.

 

 




