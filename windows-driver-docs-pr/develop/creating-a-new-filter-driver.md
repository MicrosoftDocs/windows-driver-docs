---
title: Creating a New Filter Driver
description: In this topic we explain how to use Visual Studio to start writing a new filter driver. Filter drivers are different from device function drivers, software drivers, and file system drivers, which we cover in other topics.
keywords: filter driver
ms.date: 04/20/2017
---

# Creating a New Filter Driver

In this topic we explain how to use Visual Studio to start writing a new filter driver. Filter drivers are different from device function drivers, software drivers, and file system drivers, which we cover in other topics. To learn about filter drivers and how they differ from other types of drivers, see the following topics.

-   [What is a Driver?](../gettingstarted/what-is-a-driver-.md)
-   [Choosing a Driver Model](../gettingstarted/choosing-a-driver-model.md)
-   [Device Nodes and Device Stacks](../gettingstarted/device-nodes-and-device-stacks.md)
-   [Filter Drivers](../kernel/filter-drivers.md)
-   [Types of WDM Drivers](../kernel/types-of-wdm-drivers.md)

To begin, first determine which driver model is appropriate for your filter driver. For help determining which model is best for you, see [Choosing a Driver Model](../gettingstarted/choosing-a-driver-model.md). If you are writing a filter driver for a hardware device, determine where your device fits in the list of technologies described in [Device and Driver Technologies](../index.yml). See the documentation for that particular technology to see whether there is any guidance for choosing a filter driver model. The recommended filter driver model varies from one technology to the next. For some technologies, the documentation recommends using the User Mode Driver Framework (UMDF), the Kernel Mode Driver Framework (KMDF), or the Windows Driver Model (WDM). For other technologies, the documentation gives explicit details on how to write a filter driver. Some technologies have mini filter models. For some technologies, there might not be any recommendation for a filter driver model.

Next, determine which of the following cases describes your driver model recommendation and follow the steps:

## <span id="case_1__the_documentation_for_your_technology_recommends_umdf."></span><span id="CASE_1__THE_DOCUMENTATION_FOR_YOUR_TECHNOLOGY_RECOMMENDS_UMDF."></span>Case 1: The documentation for your technology recommends UMDF.


1.  In Visual Studio, on the **File** menu, choose **New | Project**.
2.  In the New Project dialog box, in the left pane, locate and select **Visual C++ | Windows Driver | WDF**.
3.  In the middle pane, select **User Mode Driver (UMDF)**.
4.  Fill in the **Name** and **Location** boxes, and select **OK**. For more information, see [Writing a UMDF Driver Based on a Template](../gettingstarted/writing-a-umdf-driver-based-on-a-template.md).
    **Note**  When you create a new UMDF driver, you must select a driver name that has 32 characters or less. This length limit is defined in wdfglobals.h.
5.  At this point, you have a driver project that implements the general code required by most UMDF drivers. Now you can supply the code that is specific to your filter.

## <span id="case_2__the_documentation_for_your_technology_recommends_kmdf."></span><span id="CASE_2__THE_DOCUMENTATION_FOR_YOUR_TECHNOLOGY_RECOMMENDS_KMDF."></span>Case 2: The documentation for your technology recommends KMDF.


1.  In Visual Studio, on the **File** menu, choose **New | Project**.
2.  In the New Project dialog box, in the left pane, locate and select **WDF**.
3.  In the middle pane, select **Kernel Mode Driver (KMDF)**.
4.  Fill in the **Name** and **Location** boxes, and select **OK**. For more information, see [Writing a KMDF Driver Based on a Template](../gettingstarted/writing-a-kmdf-driver-based-on-a-template.md).
    **Note**  When you create a new KMDF driver, you must select a driver name that has 32 characters or less. This length limit is defined in wdfglobals.h.
5.  At this point, you have a driver project that implements the general code required by most KMDF drivers. Now you can supply the code that is specific to your filter.

## <span id="case_3__the_documentation_for_your_technology_describes_a_specific_filter_or_mini_filter_model."></span><span id="CASE_3__THE_DOCUMENTATION_FOR_YOUR_TECHNOLOGY_DESCRIBES_A_SPECIFIC_FILTER_OR_MINI_FILTER_MODEL."></span>Case 3: The documentation for your technology describes a specific filter or mini filter model.


If your device technology has a specific filter or minifilter model, check to see if Visual Studio has a template for the model.

1.  In Visual Studio, on the **File** menu, choose **New | Project**.
2.  In the New Project dialog box, in the left pane, locate and select **Templates | Visual C++ | Windows Driver**.
3.  Browse the list of installed templates to see whether there is a template for the type of filter you need to write. For example, you might choose the **Filter Driver: NDIS** template under **Networking**.
4.  If there is no template for your type of filter driver under **Windows Driver**, select **Online** and browse the templates that are available online.
5.  If you find a template for your type of filter driver, select the template, fill in the **Name** and **Location** boxes, and select **OK**.
6.  At this point, you have a driver project that implements the general code required by your filter driver. Now you can supply the code that is specific to your filter. Refer to the documentation for your technology to learn about the functions that you need to implement.

If your device technology has a specific filter model or a minifilter model, and you can't find a template for your type of filter driver, refer to your technology-specific documentation for guidance to determine whether to use UMDF, KMDF, or WDM.

## <span id="case_4__the_documentation_for_your_technology_recommends_wdm."></span><span id="CASE_4__THE_DOCUMENTATION_FOR_YOUR_TECHNOLOGY_RECOMMENDS_WDM."></span>Case 4: The documentation for your technology recommends WDM.


1.  In Visual Studio, on the **File** menu, choose **New | Project**.
2.  In Visual Studio, in the New Project dialog box, under **Windows Driver**, select **WDM.**
3.  Fill in the **Name** and **Location** boxes, and select **OK**.
4.  At this point, you have an empty WDM driver project. In the Solution Explorer window, select and hold (or right-click) your driver project, and choose **Add | New Item**.
5.  In the Add New Item dialog box, select **C++ File (.cpp)**, enter a name for your file, and select **OK**.

    **Note**  If you want to create a .c file instead of a .cpp file, enter a name that has the **.c** extension.
6.  Implement the functions required by your filter. As you implement and organize your functions, you might decide to add additional .cpp or .c files.

## <span id="case_5__the_documentation_for_your_technology_does_not_have_a_recommendation_for_a_filter_driver_model."></span><span id="CASE_5__THE_DOCUMENTATION_FOR_YOUR_TECHNOLOGY_DOES_NOT_HAVE_A_RECOMMENDATION_FOR_A_FILTER_DRIVER_MODEL."></span>Case 5: The documentation for your technology does not have a recommendation for a filter driver model.


1.  Determine whether UMDF, KMDF, or WDM is the best model for your filter driver. For help, see [Choosing a Driver Model](../gettingstarted/choosing-a-driver-model.md).
2.  In Visual Studio, on the **File** menu, choose **New | Project**.
3.  In Visual Studio, in the New Project dialog box, under **Windows Driver**, select one of the following templates:

    -   **WDF | User Mode Driver (UMDF)**
    -   **WDF | Kernel Mode Driver (KMDF)**
    -   **WDM | Empty Kernel Driver**

    **Note**  When you create a new KMDF or UMDF driver, you must select a driver name that has 32 characters or less. This length limit is defined in wdfglobals.h.
4.  Implement the functions required by your filter. Create new .c or .cpp files as needed.

If you are not sure which template to use, consider reading or posting to the [Windows Hardware WDK and Driver Development](https://go.microsoft.com/fwlink/p?LinkID=252169) forum.

 

