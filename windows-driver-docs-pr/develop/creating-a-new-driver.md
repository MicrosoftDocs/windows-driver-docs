---
title: Creating a New Device Function Driver
description: In this topic we explain how to use Visual Studio to start writing a new device function driver.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating a New Device Function Driver

In this topic we explain how to use Visual Studio to start writing a new device function driver. Device function drivers are different from filter drivers, software drivers, and file system drivers, which we cover in other topics. To learn about device function drivers and how they differ from other types of drivers, see [What is a Driver?](../gettingstarted/what-is-a-driver-.md), [Choosing a Driver Model](../gettingstarted/choosing-a-driver-model.md), and [Device Nodes and Device Stacks](../gettingstarted/device-nodes-and-device-stacks.md).

To begin, first determine where your device fits in the list of technologies described in [Device and Driver Technologies](../index.yml). To learn about which driver models are available for your device, see the documentation for that particular technology. The recommended driver model varies from one technology to the next. For some technologies, the documentation recommends using the User Mode Driver Framework (UMDF) or the Kernel Mode Driver Framework (KMDF). For other technologies, the documentation explains how to create a minidriver that is part of a driver pair. Minidrivers go by a variety of names, including miniport and miniclass.

Next, determine which of the following cases describes your driver model recommendation and follow the steps:

### <span id="Case_1__The_documentation_for_your_technology_recommends_UMDF."></span><span id="case_1__the_documentation_for_your_technology_recommends_umdf."></span><span id="CASE_1__THE_DOCUMENTATION_FOR_YOUR_TECHNOLOGY_RECOMMENDS_UMDF."></span>Case 1: The documentation for your technology recommends UMDF.

1.  In Visual Studio, on the **File** menu, choose **New | Project**.
2.  In the New Project dialog box, in the left pane, locate and select **Visual C++ | Windows Driver | WDF**.
3.  In the middle pane, select **User Mode Driver (UMDF)**.
4.  Fill in the **Name** and **Location** boxes, and select **OK**. For more details, see [Writing a UMDF Driver Based on a Template](../gettingstarted/writing-a-umdf-driver-based-on-a-template.md).
    **Note**  When you create a new UMDF driver, you must select a driver name that has 32 characters or less. This length limit is defined in wdfglobals.h.
5.  At this point, you have a driver project that implements the general code required by most UMDF drivers. Now you can supply the code that is specific to your device. Refer to the documentation for your technology to learn about the interfaces that you need to implement.

### <span id="Case_2__The_documentation_for_your_technology_recommends_KMDF."></span><span id="case_2__the_documentation_for_your_technology_recommends_kmdf."></span><span id="CASE_2__THE_DOCUMENTATION_FOR_YOUR_TECHNOLOGY_RECOMMENDS_KMDF."></span>Case 2: The documentation for your technology recommends KMDF.

1.  In Visual Studio, on the **File** menu, choose **New | Project**.
2.  In the New Project dialog box, in the left pane, locate and select **WDF**.
3.  In the middle pane, select **Kernel Mode Driver (KMDF)**.
4.  Fill in the **Name** and **Location** boxes, and select **OK**. For more details, see [Writing a KMDF Driver Based on a Template](../gettingstarted/writing-a-kmdf-driver-based-on-a-template.md).
    **Note**  When you create a new KMDF driver, you must select a driver name that has 32 characters or less. This length limit is defined in wdfglobals.h.
5.  At this point, you have a driver project that implements the general code required by most KMDF drivers. Now you can supply the code that is specific to your device. Refer to the documentation for your technology to learn about the methods that you need to implement.

### <span id="Case_3__The_documentation_for_your_technology_describes_a_minidriver_model."></span><span id="case_3__the_documentation_for_your_technology_describes_a_minidriver_model."></span><span id="CASE_3__THE_DOCUMENTATION_FOR_YOUR_TECHNOLOGY_DESCRIBES_A_MINIDRIVER_MODEL."></span>Case 3: The documentation for your technology describes a minidriver model.

If your device technology has a miniport, miniclass, or some other kind of minidriver model, check to see if Visual Studio has a specific template for the model.

1.  In Visual Studio, on the **File** menu, choose **New | Project**.
2.  In the New Project dialog box, in the left pane, locate and select **Templates | Visual C++ | Windows Driver**.
3.  Browse the list of installed templates to find a template for the type of minidriver you need to write.
4.  If there is no template for your type of minidriver under **Windows Driver**, select **Online** and browse the templates that are available online.
5.  If you find a template for your type of minidriver, select the template, fill in the **Name** and **Location** boxes, and select **OK**.
6.  At this point, you have a driver project that implements the general code required by your minidriver. Now you can supply the code that is specific to your device. Refer to the documentation for your technology to learn about the functions that you need to implement.

If your device technology has a minidriver model, and you are not able to find a specific template for your type of minidriver, the Windows Driver Model (WDM) template is most likely going to be your starting point. Refer to your technology-specific documentation for guidance. In rare cases, you can use KMDF to write a minidriver, but usually the starting point is WDM.

1.  In Visual Studio, on the **File** menu, choose **New | Project**.
2.  In Visual Studio, in the New Project dialog box, under **Windows Driver**, select **WDM.**
3.  Fill in the **Name** and **Location** boxes, and select **OK**.
4.  At this point, you have an empty WDM driver project. In the Solution Explorer window, select and hold (or right-click) your driver project, and choose **Add | New Item**.
5.  In the Add New Item dialog box, select **C++ File (.cpp)**, enter a name for your file, and select **OK**.

    **Note**  If you want to create a .c file instead of a .cpp file, enter a name that has the **.c** extension.
6.  Refer to the documentation for your technology to learn about the functions that you need to implement. As you implement and organize your functions, you might decide to add additional .cpp or .c files.

 

