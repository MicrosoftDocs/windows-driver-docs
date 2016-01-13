Creating a New Software Driver
========================================================================================

In this topic we explain how to use Visual Studio to start writing a new software driver. Software drivers are different from device function drivers, filter drivers, and file system drivers, which we cover in other topics. For more information about software drivers and how they differ from other types of drivers, see [What is a Driver?](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff554678) and [Choosing a Driver Model](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff554652).

To begin, first determine which driver model is appropriate for your software driver. The three options are the Kernel Mode Driver Framework (KMDF), the legacy NT driver model, and the Windows Driver Model (WDM). For help determining which model is best for you, see [Choosing a Driver Model](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff554652).

<span id="Case_1__You_want_to_use_KMDF."></span><span id="case_1__you_want_to_use_kmdf."></span><span id="CASE_1__YOU_WANT_TO_USE_KMDF."></span>Case 1: You want to use KMDF.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1.  In Visual Studio, on the **File** menu, choose **New | Project**.
2.  In the New Project dialog box, in the left pane, locate and select **WDF**.
3.  In the middle pane, select **Kernel Mode Driver (KMDF)**.
4.  Fill in the **Name** and **Location** boxes, and click **OK**. For more details, see [Writing a KMDF Driver Based on a Template](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh439654).
    **Note**  When you create a new KMDF driver, you must select a driver name that has 32 characters or less. This length limit is defined in wdfglobals.h.
5.  At this point, you have a driver project that implements the general code required by most KMDF drivers. Now you can supply the code that is specific to your software driver.

<span id="Case_2__You_want_to_use_the_legacy_NT_model."></span><span id="case_2__you_want_to_use_the_legacy_nt_model."></span><span id="CASE_2__YOU_WANT_TO_USE_THE_LEGACY_NT_MODEL."></span>Case 2: You want to use the legacy NT model.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1.  In Visual Studio, on the **File** menu, choose **New | Project**.
2.  In Visual Studio, in the New Project dialog box, under **Windows Driver**, select **WDM | Empty WDM Driver.**

    **Note**  You are not going to write a WDM driver, but you need the **Empty WDM Driver** template.
3.  Fill in the **Name** and **Location** boxes, and click **OK**.
4.  At this point, you have an empty WDM driver project. In the Solution Explorer window, right-click your driver project, and choose **Add | New Item**.
5.  In the Add New Item dialog box, select **C++ File (.cpp)**, enter a name for your file, and click **OK**.

    **Note**  If you want to create a .c file instead of a .cpp file, enter a name that has the **.c** extension.
6.  Include ntddk.h.
7.  Implement the functions required by your software driver. As you implement and organize your functions, you might decide to add header files and additional .cpp or .c files.

<span id="Case_3__You_want_to_use_WDM."></span><span id="case_3__you_want_to_use_wdm."></span><span id="CASE_3__YOU_WANT_TO_USE_WDM."></span>Case 3: You want to use WDM.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

It is extremely unlikely that you'll want to use WDM for a software driver. But if you do, follow these steps.

1.  In Visual Studio, on the **File** menu, choose **New | Project**.
2.  In Visual Studio, in the New Project dialog box, under **Windows Driver**, select **WDM.**
3.  Fill in the **Name** and **Location** boxes, and click **OK**.
4.  At this point, you have an empty WDM driver project. In the Solution Explorer window, right-click your driver project, and choose **Add | New Item**.
5.  In the Add New Item dialog box, select **C++ File (.cpp)**, enter a name for your file, and click **OK**.

    **Note**  If you want to create a .c file instead of a .cpp file, enter a name that has the **.c** extension.
6.  Include wdm.h.
7.  Implement the functions required by your software driver. As you implement and organize your functions, you might decide to add header files and additional .cpp or .c files.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[VsDriver\vsdriver]:%20Creating%20a%20New%20Software%20Driver%20%20RELEASE:%20%289/30/2015%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default. "Send comments about this topic to Microsoft")


