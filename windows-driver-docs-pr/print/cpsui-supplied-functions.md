---
title: CPSUI-Supplied Functions
description: CPSUI-Supplied Functions
ms.assetid: 49da252a-fb51-43f3-b2e8-27253470b4b5
keywords:
- Common Property Sheet User Interface WDK print , functions
- CPSUI WDK print , functions
- property sheet pages WDK print , functions
- functions WDK CPSUI
- CommonPropertySheetUI
- ComPropSheet
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# CPSUI-Supplied Functions





CPSUI provides the following two important functions for applications:

-   [**CommonPropertySheetUI**](https://msdn.microsoft.com/library/windows/hardware/ff546148)

    The [**CommonPropertySheetUI**](https://msdn.microsoft.com/library/windows/hardware/ff546148) function is CPSUI's entry point. The function causes property sheet pages to be created and displayed, and then allows them to be viewed and modified by a user.

    When an application calls [**CommonPropertySheetUI**](https://msdn.microsoft.com/library/windows/hardware/ff546148), it supplies the address of a [page creation callback](page-creation-callbacks.md) that describes the pages to be created. CPSUI calls this callback to obtain the page descriptions. Then it displays the pages, allows the application user to modify values contained in the page, and delivers modified values to the application using [page event callbacks](page-event-callbacks.md). The **CommonPropertySheetUI** function doesn't return until the user has dismissed the property sheet by clicking on **OK** or **Cancel**.

    Note that printer interface DLLs do not call this function; it is called by the print spooler.

-   [**ComPropSheet**](https://msdn.microsoft.com/library/windows/hardware/ff546207)

    The [**ComPropSheet**](https://msdn.microsoft.com/library/windows/hardware/ff546207) function is the means by which applications describe property sheet pages to CPSUI, so that CPSUI can create and display them. CPSUI applications call this function from within [page creation callbacks](page-creation-callbacks.md). Typically, a page description includes a pointer to a [page event callback](page-event-callbacks.md), which CPSUI will call when the application user modifies page values.

For a detailed description of when these functions are called, see [Using CPSUI with Printer Drivers](using-cpsui-with-printer-drivers.md).

Two additional CPSUI-supplied functions, [**SetCPSUIUserData**](https://msdn.microsoft.com/library/windows/hardware/ff562624) and [**GetCPSUIUserData**](https://msdn.microsoft.com/library/windows/hardware/ff549922), can be used by application-supplied dialog box procedures to store and retrieve an application-supplied value.

 

 




