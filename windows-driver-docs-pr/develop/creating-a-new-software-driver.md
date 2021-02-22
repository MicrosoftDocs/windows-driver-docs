---
title: Creating a New Software Driver
description: In this topic we explain how to use Visual Studio to start writing a new software driver.
ms.date: 04/20/2017
ms.localizationpriority: medium
ms.custom: 19H1
---

# Creating a New Software Driver

In this topic we explain how to use Visual Studio to start writing a new software driver. Software drivers are different from device function drivers, filter drivers, and file system drivers, which we cover in other topics. For more information about software drivers and how they differ from other types of drivers, see [What is a Driver?](../gettingstarted/what-is-a-driver-.md) and [Choosing a Driver Model](../gettingstarted/choosing-a-driver-model.md).

To begin, first determine which driver model is appropriate for your software driver. The three options are the Kernel Mode Driver Framework (KMDF), the legacy NT driver model, and the Windows Driver Model (WDM). For help determining which model is best for you, see [Choosing a Driver Model](../gettingstarted/choosing-a-driver-model.md).

## Case 1: You want to use KMDF

1. In Visual Studio, on the **File** menu, choose **New | Project**.
2. In the New Project dialog box, in the left pane, locate and select **WDF**.
3. In the middle pane, select **Kernel Mode Driver (KMDF)**.
4. Fill in the **Name** and **Location** boxes, and select **OK**. For more details, see [Writing a KMDF Driver Based on a Template](../gettingstarted/writing-a-kmdf-driver-based-on-a-template.md).
    > [!NOTE]
    > When you create a new KMDF driver, you must select a driver name that has 32 characters or less. This length limit is defined in wdfglobals.h.
5. At this point, you have a driver project that implements the general code required by most KMDF drivers. Now you can supply the code that is specific to your software driver.

## Case 2: You want to use the legacy NT model

1. In Visual Studio, on the **File** menu, choose **New | Project**.
2. In Visual Studio, in the New Project dialog box, under **Windows Driver**, select **WDM | Empty WDM Driver.**

    > [!NOTE]
    > You are not going to write a WDM driver, but you need the **Empty WDM Driver** template.
3. Fill in the **Name** and **Location** boxes, and select **OK**.
4. At this point, you have an empty WDM driver project. In the Solution Explorer window, select and hold (or right-click) your driver project, and choose **Add | New Item**.
5. In the Add New Item dialog box, select **C++ File (.cpp)**, enter a name for your file, and select **OK**.

    > [!NOTE]
    > If you want to create a .c file instead of a .cpp file, enter a name that has the **.c** extension.
6. Include ntddk.h.
7. Implement the functions required by your software driver. As you implement and organize your functions, you might decide to add header files and additional .cpp or .c files.

## Case 3: You want to use WDM

It is extremely unlikely that you'll want to use WDM for a software driver. But if you do, follow these steps.

1. In Visual Studio, on the **File** menu, choose **New | Project**.
2. In Visual Studio, in the New Project dialog box, under **Windows Driver**, select **WDM.**
3. Fill in the **Name** and **Location** boxes, and select **OK**.
4. At this point, you have an empty WDM driver project. In the Solution Explorer window, select and hold (or right-click) your driver project, and choose **Add | New Item**.
5. In the Add New Item dialog box, select **C++ File (.cpp)**, enter a name for your file, and select **OK**.

    > [!NOTE]
    > If you want to create a .c file instead of a .cpp file, enter a name that has the **.c** extension.
6. Include wdm.h.
7. Implement the functions required by your software driver. As you implement and organize your functions, you might decide to add header files and additional .cpp or .c files.
