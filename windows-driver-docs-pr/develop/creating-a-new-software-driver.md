---
ms.assetid: AB35CE97-0C66-47B3-9C64-81BA01D65104
title: Creating a New Software Driver
description: In this topic we explain how to use Visual Studio to start writing a new software driver.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating a New Software Driver

In this topic we explain how to use Visual Studio to start writing a new software driver. Software drivers are different from device function drivers, filter drivers, and file system drivers, which we cover in other topics. For more information about software drivers and how they differ from other types of drivers, see [What is a Driver?](https://msdn.microsoft.com/Library/Windows/Hardware/Ff554678) and [Choosing a Driver Model](https://msdn.microsoft.com/Library/Windows/Hardware/Ff554652).

To begin, first determine which driver model is appropriate for your software driver. The three options are the Kernel Mode Driver Framework (KMDF), the legacy NT driver model, and the Windows Driver Model (WDM). For help determining which model is best for you, see [Choosing a Driver Model](https://msdn.microsoft.com/Library/Windows/Hardware/Ff554652).

## <span id="case_1__you_want_to_use_kmdf."></span><span id="CASE_1__YOU_WANT_TO_USE_KMDF."></span>Case 1: You want to use KMDF.


1.  In Visual Studio, on the **File** menu, choose **New | Project**.
2.  In the New Project dialog box, in the left pane, locate and select **WDF**.
3.  In the middle pane, select **Kernel Mode Driver (KMDF)**.
4.  Fill in the **Name** and **Location** boxes, and click **OK**. For more details, see [Writing a KMDF Driver Based on a Template](https://msdn.microsoft.com/Library/Windows/Hardware/Hh439654).
    **Note**  When you create a new KMDF driver, you must select a driver name that has 32 characters or less. This length limit is defined in wdfglobals.h.
5.  At this point, you have a driver project that implements the general code required by most KMDF drivers. Now you can supply the code that is specific to your software driver.

## <span id="case_2__you_want_to_use_the_legacy_nt_model."></span><span id="CASE_2__YOU_WANT_TO_USE_THE_LEGACY_NT_MODEL."></span>Case 2: You want to use the legacy NT model.


1.  In Visual Studio, on the **File** menu, choose **New | Project**.
2.  In Visual Studio, in the New Project dialog box, under **Windows Driver**, select **WDM | Empty WDM Driver.**

    **Note**  You are not going to write a WDM driver, but you need the **Empty WDM Driver** template.
3.  Fill in the **Name** and **Location** boxes, and click **OK**.
4.  At this point, you have an empty WDM driver project. In the Solution Explorer window, right-click your driver project, and choose **Add | New Item**.
5.  In the Add New Item dialog box, select **C++ File (.cpp)**, enter a name for your file, and click **OK**.

    **Note**  If you want to create a .c file instead of a .cpp file, enter a name that has the **.c** extension.
6.  Include ntddk.h.
7.  Implement the functions required by your software driver. As you implement and organize your functions, you might decide to add header files and additional .cpp or .c files.

## <span id="case_3__you_want_to_use_wdm."></span><span id="CASE_3__YOU_WANT_TO_USE_WDM."></span>Case 3: You want to use WDM.


It is extremely unlikely that you'll want to use WDM for a software driver. But if you do, follow these steps.

1.  In Visual Studio, on the **File** menu, choose **New | Project**.
2.  In Visual Studio, in the New Project dialog box, under **Windows Driver**, select **WDM.**
3.  Fill in the **Name** and **Location** boxes, and click **OK**.
4.  At this point, you have an empty WDM driver project. In the Solution Explorer window, right-click your driver project, and choose **Add | New Item**.
5.  In the Add New Item dialog box, select **C++ File (.cpp)**, enter a name for your file, and click **OK**.

    **Note**  If you want to create a .c file instead of a .cpp file, enter a name that has the **.c** extension.
6.  Include wdm.h.
7.  Implement the functions required by your software driver. As you implement and organize your functions, you might decide to add header files and additional .cpp or .c files.

 

 





