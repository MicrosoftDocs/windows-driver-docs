---
title: Filtering the LogViewer Function List
description: Filtering the LogViewer Function List
ms.assetid: 258da8c3-ab94-40bd-bfa5-344571d34428
keywords: ["LogViewer, filtering the LogViewer function list"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Filtering the LogViewer Function List


## <span id="ddk_filtering_the_logviewer_function_list_dtoolq"></span><span id="DDK_FILTERING_THE_LOGVIEWER_FUNCTION_LIST_DTOOLQ"></span>


Logger usually captures some function calls that are not needed for your analysis. These can be filtered out by Logger when it creates the log file. However, this process is not reversible, so it is usually preferable to allow all functions to be logged, and then filter the display in LogViewer.

There are several ways to filter out function calls in LogViewer:

-   In the main viewing area, selected a function by clicking on it or using the cursor keys. (When a function is selected, LogViewer outlines it in red.) Then, press the DELETE key, or right-click and select **Hide**. This will hide all instances of that function call from view.

-   Select **View | APIs Display**. A dialog box will appear that has three areas. On the right is an alphabetical listing of all functions, and on the left are categorical groupings. You can enable or disable the display of any function by checking or clearing the box to the left of its name.

-   Select **View | Modules Display**. A dialog box will appear that allows you to select calling modules; only those functions that were called from these modules will be displayed.

-   Select **View | First Level Calls Only**. This will display only calls that have "d0" in the left column. It is often desirable to hide function calls that are made by other logged functions. (For example, it is usually not interesting to know that **ShellExecuteEx** makes thirty different registry calls during its course of execution.)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Filtering%20the%20LogViewer%20Function%20List%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




