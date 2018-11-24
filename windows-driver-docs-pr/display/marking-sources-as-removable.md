---
title: Marking Sources as Removable
description: Marking Sources as Removable
ms.assetid: 7fe48a4b-25d2-4e2c-9c26-a425928947ce
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Marking Sources as Removable


To prevent a display application from making a video present source the primary view, you should mark the source as removable. To indicate which sources are removable, you can specify a DWORD Plug and Play (PnP) value in the registry named **RemovableSources**.

**Note**   You cannot mark source 0 in the DWORD bit-field value as removable.

 

The n<sup>th</sup> bit in the bit-field value specifies whether source n-1 is removable. For example, to mark source 1 as removable, you can add the following line to a display miniport driver's INF file:

```inf
HKR,, RemovableSources, %REG_DWORD%, 2
...
```

For more information about installing display drivers, see [Installation Requirements for Display Miniport and User-Mode Display Drivers](installing-display-miniport-and-user-mode-display-drivers.md).

 

 





