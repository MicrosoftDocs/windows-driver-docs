---
title: Write a Universal Windows driver (KMDF) based on a template
description: This topic describes how to write a Universal Windows driver using Kernel-Mode Driver Framework (KMDF). You'll start with a Microsoft Visual Studio template and then deploy and install your driver on a separate computer.
keywords:
- Write a KMDF driver
ms.date: 06/02/2021
ms.localizationpriority: medium
---

# Write a Universal Windows driver (KMDF) based on a template

This topic describes how to write a [Universal Windows driver](/windows-hardware/drivers) using Kernel-Mode Driver Framework (KMDF). You'll start with a Microsoft Visual Studio template and then deploy and install your driver on a separate computer.

To get started, be sure you have the latest versions of [Microsoft Visual Studio]https://visualstudio.microsoft.com/vs/) and the [Windows Driver Kit (WDK)](../download-the-wdk.md) installed.

[Debugging Tools for Windows](../debugger/index.md) is included when you install the WDK.

## Create and build a driver

1. Open Microsoft Visual Studio. On the **File** menu, choose **New &gt; Project**.
1. In the **Create a new project** dialog box, select **C++** in the left dropdown, choose **Windows** in the middle dropdown, and choose **Driver** in the right dropdown.
1. Select **Kernel Mode Driver (KMDF)** from the list of project types. Select **Next**.

    :::image type="content" source="images/vs2019-kmdf2-template.png" alt-text="Screen shot of the new project dialog box, showing kernel mode driver selected.":::

1. In the **Configure your new project** dialog box, enter "KmdfDriver" in the **Project name** field.

     > [!NOTE]
    > When you create a new KMDF or UMDF driver, you must select a driver name that has 32 characters or less. This length limit is defined in wdfglobals.h.  

1. In the **Location** field, enter the directory where you want to create the new project.
1. Check **Place solution and project in the same directory** and select **Create**.

    :::image type="content" source="images/vs2019-kmdf2-configure.png" alt-text="Screen shot of the project configuration dialog box.":::

    Visual Studio creates one project and a solution. You can see them in the **Solution Explorer** window. (If the **Solution Explorer** window is not visible, choose **Solution Explorer** from the **View** menu.) The solution has a driver project named KmdfDriver. To see the driver source code, open any of the files under **Source Files**. Driver.c and Device.c are good places to start.

    :::image type="content" source="images/vs2019-kmdf2-solution-explorer.png" alt-text="Screen shot of solution explorer showing the files in the driver project.":::

1. In the **Solution Explorer** window, select and hold (or right-click) **Solution 'KmdfDriver' (1 of 1 project)**, and choose **Configuration Manager**. Choose a configuration and platform for the driver project. For example, choose **Debug** and **x64**.
1. In the **Solution Explorer** window, select and hold (or right-click) **KmdfDriver**, and choose **Properties**. Navigate to **Configuration Properties &gt; Driver Settings &gt; General**, and note that **Target Platform** defaults to **Universal.**
1. To build your driver, choose **Build Solution** from the **Build** menu. Microsoft Visual Studio displays build progress in the **Output** window. (If the **Output** window is not visible, choose **Output** from the **View** menu.)

    Verify that the build output includes:

    ``` syntax
    >    Driver is 'Universal'.
    ```

    When you've verified that the solution built successfully, you can close Visual Studio.

1. To see the built driver, in File Explorer, go to your **UmdfDriver** folder, and then to **x64\\Debug\\UmdfDriver**. The directory includes the following files:

    * KmdfDriver.sys -- the kernel-mode driver file
    * KmdfDriver.inf -- an information file that Windows uses when you install the driver

1. In the **Solution Explorer** window, select and hold (or right-click) **Solution 'KmdfDriver' (1 project)**, and choose **Configuration Manager**. Choose a configuration and platform for both the driver project and the package project. In this exercise, we choose Debug and x64.

1. To build your driver and create a driver package, choose **Build Solution** from the **Build** menu. Visual Studio shows the build progress in the **Output** window. (If the **Output** window is not visible, choose **Output** from the **View** menu.)

    When you've verified that the solution built successfully, you can close Visual Studio.

1. To see the built driver, in File Explorer, go to your **KmdfDriver** folder, and then to **x64\\Debug\\KmdfDriver**. The folder includes:

## Deploy the driver

Typically when you test and debug a driver, the debugger and driver run on separate computers. The computer that runs the debugger is called the *host computer*, and the computer that runs the driver is called the *target computer*. The target computer is also called the *test computer*. For more information about debugging drivers, see [Debugging Tools for Windows](../debugger/index.md).

So far you've used Visual Studio to build a driver on the host computer. Now you need to configure a target computer.

1. Follow the instructions in [Provision a computer for driver deployment and testing (WDK 10)](provision-a-target-computer-wdk-8-1.md).

    > [!TIP]
    > When you follow the steps to provision the target computer automatically using a network cable, take note of the port and key. You'll use them later in the debugging step. In this example, we'll use **50000** as the port and **1.2.3.4** as the key.
    >
    > In real driver debugging scenarios, we recommend using a KDNET-generated key. For more information about how to use KDNET to generate a random key, see the [Debug Drivers - Step by Step Lab (Sysvad Kernel Mode)](../debugger/debug-universal-drivers--kernel-mode-.md) topic.

1. On the host computer, open your solution in Visual Studio. You can double-click the solution file, KmdfDriver.sln, in your KmdfDriver folder.
1. In the **Solution Explorer** window, select and hold (or right-click) the **KmdfDriver** project, and choose **Properties**.
1. In the **KmdfDriver Package Property Pages** window, in the left pane, go to **Configuration Properties &gt; Driver Install &gt; Deployment**.
1. Check **Remove previous driver versions before deployment**.
1. For **Remote Computer Name**, select the name of the computer that you configured for testing and debugging. In this exercise, we use a computer named MyTestComputer.
1. Select **Hardware ID Driver Update**, and enter the hardware ID for your driver. In this exercise, the hardware ID is Root\\KmdfDriver. Select **OK**.

    :::image type="content" source="images/vs2019-kmdfdriver-property-pages.png" alt-text="screen shot of the kmdfdriver package property pages window, showing deployment driver install selected":::

    > [!NOTE]
    > In this exercise, the hardware ID does not identify a real piece of hardware. It identifies an imaginary device that will be given a place in the [device tree](./device-nodes-and-device-stacks.md) as a child of the root node. For real hardware, do not select **Hardware ID Driver Update**; instead, select **Install and Verify**. You'll see the hardware ID in your driver's information (INF) file. In the **Solution Explorer** window, go to **KmdfDriver &gt; Driver Files** and double-click KmdfDriver.inf. The hardware ID is located under \[Standard.NT$ARCH$\].

    ```C++
    [Standard.NT$ARCH$]
    %KmdfDriver.DeviceDesc%=KmdfDriver_Device, Root\KmdfDriver
    ```

1. On the **Build** menu, choose **Deploy Solution**. Visual Studio automatically copies the files required to install and run the driver to the target computer. This may take a minute or two.

    When you deploy a driver, the driver files are copied to the %Systemdrive%\drivertest\drivers folder on the test computer. If something goes wrong during deployment, you can check to see if the files are copied to the test computer. Verify that the .inf, .cat, test cert, and .sys files, and any other necessary files, are present in the %systemdrive%\drivertest\drivers folder.

    For more information about deploying drivers, see [Deploying a Driver to a Test Computer](../develop/deploying-a-driver-to-a-test-computer.md).

## Install the driver

With your KMDF driver deployed to the target computer, now you'll install the driver. When you previously provisioned the target computer with Visual Studio using the *automatic* option, Visual Studio set up the target computer to run test signed drivers as part of the provisioning process. Now you just need to install the driver using the DevCon tool.

1. On the host computer, navigate to the Tools folder in your WDK installation and locate the DevCon tool. For example, look in the following folder:

    *C:\\Program Files (x86)\\Windows Kits\\10\\Tools\\x64\\devcon.exe*

    Copy the DevCon tool to your remote computer.

1. On the target computer, install the driver by navigating to the folder containing the driver files, then running the DevCon tool.
    1. Here's the general syntax for the devcon tool that you will use to install the driver:

        *devcon install \<INF file\> \<hardware ID\>*

        The INF file required for installing this driver is KmdfDriver.inf. The INF file contains the hardware ID for installing the driver binary, *KmdfDriver.sys*. Recall that the hardware ID, located in the INF file, is **Root\\KmdfDriver**.
    1. Open a Command Prompt window as Administrator. Navigate to your driver package folder, then enter this command:

        **devcon install kmdfdriver.inf root\\kmdfdriver**

        If you get an error message about *devcon* not being recognized, try adding the path to the *devcon* tool. For example, if you copied it to a folder on the target computer called *C:\\Tools*, then try using the following command:

        **c:\\tools\\devcon install kmdfdriver.inf root\kmdfdriver**

        A dialog box will appear indicating that the test driver is an unsigned driver. Select **Install this driver anyway** to proceed.

        :::image type="content" source="../debugger/images/debuglab-image-install-security-warning.png" alt-text="screenshot of driver installation warning.":::

## Debug the driver

Now that you have installed your KMDF driver on the target computer, you'll attach a debugger remotely from the host computer.

1. On the host computer, open a Command Prompt window as Administrator. Change to the WinDbg.exe directory. We will use the x64version of WinDbg.exe from the Windows Driver Kit (WDK) that was installed as part of the Windows kit installation. Here is the default path to WinDbg.exe:

    *C:\\Program Files (x86)\\Windows Kits\\10\\Debuggers\\x64*

1. Launch WinDbg to connect to a kernel debug session on the target computer by using the following command. The value for the port and key should be the same as what you used to provision the target computer. We'll use **50000** for the port and **1.2.3.4** for the key, the values we used during the deploy step. The *k* flag indicates that this is a kernel debug session.

    **WinDbg -k net:port=50000,key=1.2.3.4**

1. On the **Debug** menu, choose **Break**. The debugger on the host computer will break into the target computer. In the **Debugger Command** window, you can see the kernel debugging command prompt: **kd\>**.

1. At this point, you can experiment with the debugger by entering commands at the **kd&gt;** prompt. For example, you could try these commands:

    * [lm](./device-nodes-and-device-stacks.md)
    * [.sympath](../debugger/-sympath--set-symbol-path-.md)
    * [.reload](../debugger/-reload--reload-module-.md)
    * [x KmdfHelloWorld!\*](../debugger/x--examine-symbols-.md)

1. To let the target computer run again, choose **Go** from the **Debug** menu or press "g," then press "enter."
1. To stop the debugging session, choose **Detach Debuggee** from the **Debug** menu.

    > [!IMPORTANT]
    > Make sure you use the "go" command to let the target computer run again before exiting the debugger, or the target computer will remain unresponsive to your mouse and keyboard input because it is still talking to the debugger.

For a detailed step-by-step walkthrough of the driver debugging process, see [Debug Universal Drivers - Step by Step Lab (Echo Kernel-Mode)](../debugger/debug-universal-drivers---step-by-step-lab--echo-kernel-mode-.md).

For more information about remote debugging, see [Remote Debugging Using WinDbg](../debugger/remote-debugging-using-windbg.md).

## Using the Driver Module Framework (DMF)

The [Driver Module Framework (DMF)](https://github.com/Microsoft/DMF) is an extension to WDF that enables extra functionality for a WDF driver developer. It helps developers write any type of WDF driver better and faster.

DMF as a framework allows creation of WDF objects called DMF Modules. The code for these DMF Modules can be shared between different drivers. In addition, DMF bundles a library of DMF Modules that we have developed for our drivers and feel would provide value to other driver developers.

DMF does not replace WDF. DMF is a second framework that is used with WDF. The developer leveraging DMF still uses WDF and all its primitives to write device drivers.

For more info, see [Driver Module Framework (DMF)](https://github.com/Microsoft/DMF).

## Related topics

[Developing, Testing, and Deploying Drivers](../develop/index.md)

[Debugging Tools for Windows](../debugger/index.md)

[Debug Universal Drivers - Step by Step Lab (Echo Kernel-Mode)](../debugger/debug-universal-drivers---step-by-step-lab--echo-kernel-mode-.md)

[Write your first driver](writing-your-first-driver.md)
