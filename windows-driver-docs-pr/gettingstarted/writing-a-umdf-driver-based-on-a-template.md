---
title: Write a Universal Windows Driver (UMDF 2) Based on a Template
description: This topic describes how to write a Universal Windows driver using User-Mode Driver Framework (UMDF) 2. You'll start with a Microsoft Visual Studio template and then deploy and install your driver on a separate computer.
keywords:
- Write a UMDF driver
ms.date: 06/02/2021
---

# Write a Universal Windows driver (UMDF 2) based on a template

This topic describes how to write a [Universal Windows driver](/windows-hardware/drivers) using User-Mode Driver Framework (UMDF) 2. You'll start with a Microsoft Visual Studio template and then deploy and install your driver on a separate computer.

To get started, be sure you have the most recent version of Microsoft Visual Studio and the Windows Driver Kit (WDK). For download links, see [Download the Windows Driver Kit (WDK)](../download-the-wdk.md).

[Debugging Tools for Windows](../debugger/index.md) is included when you install the WDK.

## Create and build a driver

>[!NOTE]
>When you create a new KMDF or UMDF driver, you must select a driver name that has 32 characters or less. This length limit is defined in wdfglobals.h.

1. Open Visual Studio. On the **File** menu, choose **New &gt; Project**.
1. In the **Create a new project** dialog box, select **C++** in the left dropdown, choose **Windows** in the middle dropdown, and choose **Driver** in the right dropdown.
1. Select **User Mode Driver (UMDF V2)** from the list of project types. Select **Next**.

    :::image type="content" source="images/vs2019-umdf2-template.png" alt-text="Screen shot of the new project dialog box, showing user mode driver selected.":::

1. In the **Configure your new project** dialog box, enter "UmdfDriver" in the **Project name** field.

     > [!NOTE]
    > When you create a new KMDF or UMDF driver, you must select a driver name that has 32 characters or less. This length limit is defined in wdfglobals.h.  

1. In the **Location** field, enter the directory where you want to create the new project.
1. Check **Place solution and project in the same directory** and select **Create**.

    :::image type="content" source="images/vs2019-umdf2-configure.png" alt-text="Screen shot of the project configuration dialog box.":::

    Visual Studio creates one project and a solution. You can see them in the **Solution Explorer** window. (If the **Solution Explorer** window is not visible, choose **Solution Explorer** from the **View** menu.) The solution has a driver project named UmdfDriver. To see the driver source code, open any of the files under **Source Files**. Driver.c and Device.c are good places to start.

    :::image type="content" source="images/vs2019-umdf2-solution-explorer.png" alt-text="Screen shot of solution explorer showing the files in the driver project.":::

1. In the **Solution Explorer** window, select and hold (or right-click) **Solution 'UmdfDriver' (1 of 1 project)**, and choose **Configuration Manager**. Choose a configuration and platform for the driver project. For example, choose **Debug** and **x64**.
1. In the **Solution Explorer** window, select and hold (or right-click) **UmdfDriver**, and choose **Properties**. Navigate to **Configuration Properties &gt; Driver Settings &gt; General**, and note that **Target Platform** defaults to **Universal.**
1. To build your driver, choose **Build Solution** from the **Build** menu. Microsoft Visual Studio displays build progress in the **Output** window. (If the **Output** window is not visible, choose **Output** from the **View** menu.)

    Verify that the build output includes:

    ``` syntax
    >    Driver is 'Universal'.
    ```

    When you've verified that the solution built successfully, you can close Visual Studio.

1. To see the built driver, in File Explorer, go to your **UmdfDriver** folder, and then to **x64\\Debug\\UmdfDriver**. The directory includes the following files:

    * UmdfDriver.dll -- the user-mode driver file
    * UmdfDriver.inf -- an information file that Windows uses when you install the driver

## Deploy and install the Universal Windows driver

Typically when you test and debug a driver, the debugger and driver run on separate computers. The computer that runs the debugger is called the *host computer*, and the computer that runs the driver is called the *target computer*. The target computer is also called the *test computer*.

So far, you've used Visual Studio to build a driver on the host computer. Now you need to configure a target computer. Follow the instructions in [Provision a computer for driver deployment and testing (WDK 10)](provision-a-target-computer-wdk-8-1.md). Then you'll be ready to deploy, install, load, and debug your driver:

1. On the host computer, open your solution in Visual Studio. You can double-click the solution file, UmdfDriver.sln, in your UmdfDriver folder.
2. In the **Solution Explorer** window, select and hold (or right-click) **UmdfDriver**, and choose **Properties**.
3. In the **UmdfDriver Property Pages** window, go to **Configuration Properties &gt; Driver Install &gt; Deployment**, as shown here.
4. Check **Remove previous driver versions before deployment**.
5. For **Target Device Name**, select the name of the computer that you configured for testing and debugging.
6. Select **Hardware ID Driver Update**, and enter the hardware ID for your driver. In this exercise, the hardware ID is Root\\UmdfDriver. Select **OK**.

    :::image type="content" source="images/vs2019-umdf2-deploy.png" alt-text="screen shot of the umdfdriver property pages, showing deployment driver install selected":::

    **Note**  In this exercise, the hardware ID does not identify a real piece of hardware. It identifies an imaginary device that will be given a place in the [device tree](./device-nodes-and-device-stacks.md) as a child of the root node. For real hardware, do not select **Hardware ID Driver Update**; instead, select **Install and Verify**.
    You can see the hardware ID in your driver's information (INF) file. In the **Solution Explorer** window, go to **UmdfDriver &gt; Driver Files**, and double-click UmdfDriver.inf. The hardware ID is under \[Standard.NT$ARCH$\].

    ```ManagedCPlusPlus
    [Standard.NT$ARCH$]
    %DeviceName%=MyDevice_Install,Root\UmdfDriver
    ```

7. On the **Debug** menu, choose **Start Debugging**, or press **F5** on the keyboard.
8. Wait until your driver has been deployed, installed, and loaded on the target computer. This might take several minutes.

## Using the Driver Module Framework (DMF)

The [Driver Module Framework (DMF)](https://github.com/Microsoft/DMF) is an extension to WDF that enables extra functionality for a WDF driver developer. It helps developers write any type of WDF driver better and faster.

DMF as a framework allows creation of WDF objects called DMF Modules. The code for these DMF Modules can be shared between different drivers. In addition, DMF bundles a library of DMF Modules that we have developed for our drivers and feel would provide value to other driver developers.

DMF does not replace WDF. DMF is a second framework that is used with WDF. The developer leveraging DMF still uses WDF and all its primitives to write device drivers.

For more info, see [Driver Module Framework (DMF)](https://github.com/Microsoft/DMF).

## Related topics

[Developing, Testing, and Deploying Drivers](../develop/index.md)

[Debugging Tools for Windows](../debugger/index.md)

[Write your first driver](writing-your-first-driver.md)
