---
title: Creating a new device function driver
description: In this article, we explain how to use Visual Studio to start writing a new device function driver.
ms.date: 04/05/2023
---

# Creating a new device function driver

In this article, we explain how to use Visual Studio to start writing a new device function driver. Device function drivers are different from filter drivers, software drivers, and file system drivers, which we cover in other articles. To learn about device function drivers and how they differ from other types of drivers, see [What is a Driver?](../gettingstarted/what-is-a-driver-.md), [Choosing a Driver Model](../gettingstarted/choosing-a-driver-model.md), and [Device Nodes and Device Stacks](../gettingstarted/device-nodes-and-device-stacks.md).

To begin, determine where your device fits in the list of technologies described in [Device and Driver Technologies](../index.yml). To learn about which driver models are available for your device, see the documentation for that particular technology. The recommended driver model varies from one technology to the next. For some technologies, the documentation recommends using the User Mode Driver Framework (UMDF) or the Kernel Mode Driver Framework (KMDF). For other technologies, the documentation explains how to create a minidriver that is part of a driver pair. Minidrivers go by various names, including miniport and miniclass.

Determine which of the following cases describes your driver model recommendation and follow the steps:

## Case 1: The documentation for your technology recommends UMDF

1. Start Visual Studio.
1. Choose **Create a new project** in the startup dialog, or select **New | Project** from the Visual Studio **File** menu.
1. In the right pane of the **Create a new project** dialog box, locate and select **User Mode Driver (UMDF V2)**.
1. Select **Next**.
1. Fill in the **Project name**, **Location**, and **Solution name** boxes, and select **Create**. For more information, see [Writing a UMDF Driver Based on a Template](../gettingstarted/writing-a-umdf-driver-based-on-a-template.md).
    > [!NOTE]
    > When you create a new UMDF driver, you must select a driver name that has 32 characters or less. This length limit is defined in wdfglobals.h.
1. At this point, you have a driver project that implements the general code required by most UMDF drivers. Now you can supply the code that is specific to your device. Refer to the documentation for your technology to learn about the interfaces that you need to implement.

## Case 2: The documentation for your technology recommends KMDF

1. Start Visual Studio.
1. Choose **Create a new project** in the startup dialog, or select **New | Project** from the Visual Studio **File** menu.
1. In the right pane of the **Create a new project** dialog box, locate and select **Kernel Mode Driver (KMDF)**.
1. Select **Next**.
1. Fill in the **Project name**, **Location**, and **Solution name** boxes, and select **Create**. For more information, see [Writing a KMDF Driver Based on a Template](../gettingstarted/writing-a-kmdf-driver-based-on-a-template.md).
    > [!NOTE]
    > When you create a new KMDF driver, you must select a driver name that has 32 characters or less. This length limit is defined in wdfglobals.h.
1. At this point, you have a driver project that implements the general code required by most KMDF drivers. Now you can supply the code that is specific to your device. Refer to the documentation for your technology to learn about the methods that you need to implement.

## Case 3: The documentation for your technology describes a minidriver model

If your device technology has a miniport, miniclass, or some other minidriver model, check to see if Visual Studio has a specific template for the model.

1. Start Visual Studio.
1. Choose **Create a new project** in the startup dialog, or select **New | Project** from the Visual Studio **File** menu.
1. In the right pane of the **Create a new project** dialog box, browse the list of installed templates to find a template for the type of driver you need to write.
1. If you find a template for your type of driver, select it.
1. Select **Next**.
1. Fill in the **Project name**, **Location**, and **Solution name** boxes, and select **Create**.
1. If you're presented with a driver wizard, step through the wizard to create your driver project.
1. At this point, you have a driver project that implements the general code required by your driver. Now you can supply the code that is specific to your device. Refer to the documentation for your technology to learn about the functions that you need to implement.

If your device technology has a minidriver model, and you aren't able to find a specific template for your type of minidriver, the Windows Driver Model (WDM) template is most likely going to be your starting point. Refer to your technology-specific documentation for guidance. In rare cases, you can use KMDF to write a minidriver, but usually the starting point is WDM.

1. Start Visual Studio.
1. Choose **Create a new project** in the startup dialog, or select **New | Project** from the Visual Studio **File** menu.
1. In the right pane of the **Create a new project** dialog box, locate and select **Empty WDM Driver**.
1. Select **Next**.
1. Fill in the **Project name**, **Location**, and **Solution name** boxes, and select **Create**.
1. At this point, you have an empty WDM driver project. In the Solution Explorer window, right-click your driver project, and choose **Add | New Item**.
1. In the **Add New Item** dialog box, enter a name for your .cpp file, and select **Add**.
    > [!NOTE]
    > If you want to create a .c file instead of a .cpp file, enter a name that has the **.c** extension.
1. Refer to the documentation for your technology to learn about the functions that you need to implement. As you implement and organize your functions, you might decide to add more .cpp or .c files.
