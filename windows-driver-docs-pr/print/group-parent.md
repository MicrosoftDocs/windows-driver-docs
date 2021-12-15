---
title: Group Parent
description: Group Parent
keywords:
- group parents WDK print
- Common Property Sheet User Interface WDK print , group parents
- CPSUI WDK print , group parents
- property sheet pages WDK print , group parents
- grouping property sheet pages
ms.date: 04/20/2017
---

# Group Parent





Property sheet pages can be grouped together by assigning them to a single *group parent*. You can create a group parent by calling CPSUI's [**ComPropSheet**](/windows-hardware/drivers/ddi/compstui/nc-compstui-pfncompropsheet) function with a [**CPSFUNC\_INSERT\_PSUIPAGE**](/previous-versions/ff546414(v=vs.85)) function code, and specifying PSUIPAGEINSERT\_GROUP\_PARENT as the **Type** member for an [**INSERTPSUIPAGE\_INFO**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_insertpsuipage_info) structure.

When a new group parent is created, a handle is returned. The handle can then be used as the *hComPropSheet* parameter to [**ComPropSheet**](/windows-hardware/drivers/ddi/compstui/nc-compstui-pfncompropsheet), when adding or deleting property sheet pages.

Additionally, a group parent handle is received as the **hComPropSheet** member of the [**PROPSHEETUI\_INFO**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_propsheetui_info) structure that is received by an application's [**PFNPROPSHEETUI**](/windows-hardware/drivers/ddi/compstui/nc-compstui-pfnpropsheetui)-typed callback function. If you don't create new group parents, all property sheet pages should be assigned to this one.

You can create additional group parents under each group parent that is created. The property sheet itself is considered to be the top-level group parent. If you do not explicitly create additional group parents, all added property sheet pages are assigned to the top-level parent.

 

