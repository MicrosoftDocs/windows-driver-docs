---
title: Filtering the LogViewer Function List
description: Filtering the LogViewer Function List
ms.assetid: 258da8c3-ab94-40bd-bfa5-344571d34428
keywords: ["LogViewer, filtering the LogViewer function list"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Filtering the LogViewer Function List


## <span id="ddk_filtering_the_logviewer_function_list_dtoolq"></span><span id="DDK_FILTERING_THE_LOGVIEWER_FUNCTION_LIST_DTOOLQ"></span>


Logger usually captures some function calls that are not needed for your analysis. These can be filtered out by Logger when it creates the log file. However, this process is not reversible, so it is usually preferable to allow all functions to be logged, and then filter the display in LogViewer.

There are several ways to filter out function calls in LogViewer:

-   In the main viewing area, selected a function by clicking on it or using the cursor keys. (When a function is selected, LogViewer outlines it in red.) Then, press the DELETE key, or right-click and select **Hide**. This will hide all instances of that function call from view.

-   Select **View | APIs Display**. A dialog box will appear that has three areas. On the right is an alphabetical listing of all functions, and on the left are categorical groupings. You can enable or disable the display of any function by checking or clearing the box to the left of its name.

-   Select **View | Modules Display**. A dialog box will appear that allows you to select calling modules; only those functions that were called from these modules will be displayed.

-   Select **View | First Level Calls Only**. This will display only calls that have "d0" in the left column. It is often desirable to hide function calls that are made by other logged functions. (For example, it is usually not interesting to know that **ShellExecuteEx** makes thirty different registry calls during its course of execution.)

 

 





