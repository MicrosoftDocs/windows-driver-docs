---
title: Image Processing
description: Image Processing
ms.assetid: 84e10fcc-3998-434c-922a-65b42dccbdaf
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Image Processing





Some minidrivers, in particular scanner minidrivers, require an image processing layer. This layer is mandatory only if the data acquired from the still image device requires some manipulation before being passed on to the application.

If the raw data acquired from the device needs no further processing, then the image processing layer can be omitted.

Microsoft recommends the use of GDI+ in the WIA minidriver if any image manipulation is required.

### Using GDI+ in a WIA Driver

GDI+ is a library that provides two-dimensional image manipulation routines. The library provides mechanisms for modifying image attributes, as well as for rotation and resizing.

To use GDI+ in the WIA minidriver, make sure that GDI+ is properly initialized. GDI+ can be initialized when the WIA minidriver is created and loaded. Also, make sure that the WIA driver includes *Gdiplus.h* and links to the *Gdiplus.lib* library.

For more information about GDI+, see the Microsoft Windows SDK documentation.

 

 




