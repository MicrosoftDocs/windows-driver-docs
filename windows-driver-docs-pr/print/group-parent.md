---
title: Group Parent
description: Group Parent
ms.assetid: b4c40c15-df16-4af0-81c8-9e70d26ba598
keywords:
- group parents WDK print
- Common Property Sheet User Interface WDK print , group parents
- CPSUI WDK print , group parents
- property sheet pages WDK print , group parents
- grouping property sheet pages
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Group Parent





Property sheet pages can be grouped together by assigning them to a single *group parent*. You can create a group parent by calling CPSUI's [**ComPropSheet**](https://msdn.microsoft.com/library/windows/hardware/ff546207) function with a [**CPSFUNC\_INSERT\_PSUIPAGE**](https://msdn.microsoft.com/library/windows/hardware/ff546414) function code, and specifying PSUIPAGEINSERT\_GROUP\_PARENT as the **Type** member for an [**INSERTPSUIPAGE\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff551634) structure.

When a new group parent is created, a handle is returned. The handle can then be used as the *hComPropSheet* parameter to [**ComPropSheet**](https://msdn.microsoft.com/library/windows/hardware/ff546207), when adding or deleting property sheet pages.

Additionally, a group parent handle is received as the **hComPropSheet** member of the [**PROPSHEETUI\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff561767) structure that is received by an application's [**PFNPROPSHEETUI**](https://msdn.microsoft.com/library/windows/hardware/ff559812)-typed callback function. If you don't create new group parents, all property sheet pages should be assigned to this one.

You can create additional group parents under each group parent that is created. The property sheet itself is considered to be the top-level group parent. If you do not explicitly create additional group parents, all added property sheet pages are assigned to the top-level parent.

 

 




