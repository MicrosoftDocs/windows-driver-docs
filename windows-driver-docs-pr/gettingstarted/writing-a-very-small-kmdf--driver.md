---
title: Write a Hello World Windows Driver (KMDF)
description: This topic describes how to write a Windows driver using Kernel-Mode Driver Framework (KMDF). You'll start with a Microsoft Visual Studio template and then deploy and install your driver on a separate computer.
keywords:
- KMDF Hello World
ms.date: 04/20/2018
ms.localizationpriority: medium
---

# Write a Hello World Windows Driver (KMDF)


This topic describes how to write a very small [Universal Windows driver](/windows-hardware/drivers) using Kernel-Mode Driver Framework (KMDF) and then deploy and install your driver on a separate computer. 

To get started, be sure you have [Microsoft Visual Studio](https://go.microsoft.com/fwlink/p/?LinkId=698539), the [Windows SDK](https://developer.microsoft.com/windows/downloads/windows-10-sdk), and the [Windows Driver Kit (WDK)](../download-the-wdk.md) installed.

[Debugging Tools for Windows](../debugger/index.md) is included when you install the WDK.

## Create and build a driver


1.  Open Microsoft Visual Studio. On the **File** menu, choose **New &gt; Project**.
2.  In the New Project dialog box, in the left pane, go to **Visual C++ &gt; Windows Drivers &gt; WDF**.
3.  In the middle pane, select **Kernel Mode Driver, Empty (KMDF)**.
4.  In the **Name** field, enter "KmdfHelloWorld" for the project name.

    > [!NOTE]
    > When you create a new KMDF or UMDF driver, you must select a driver name that has 32 characters or less. This length limit is defined in wdfglobals.h.
     

5.  In the **Location** field, enter the directory where you want to create the new project.
6.  Check **Create directory for solution**. Select **OK**.

    ![screen shot of the new project dialog box](images/vs2015-new-project-kmdf-empty.png)

    Visual Studio creates one project and a solution. You can see them in the **Solution Explorer** window, shown here. (If the Solution Explorer window is not visible, choose **Solution Explorer** from the **View** menu.) The solution has a driver project named KmdfHelloWorld.

    ![screen shot of the solution explorer window, showing the solution and the empty driver project (kmdfhelloworld)](images/vs2015-kmdf-hello-world-solution-explorer.png)

7.  In the **Solution Explorer** window, select and hold (or right-click) the **KmdfHelloWorld** project and choose **Properties**. Navigate to **Configuration Properties &gt; Driver Settings &gt; General**, and note that **Target Platform** defaults to **Universal.**  Select **Apply**, and then select **OK**..

8.  In the **Solution Explorer** window, again select and hold (or right-click) the **KmdfHelloWorld** project, choose **Add**, and then select **New Item**.
9.  In the **Add New Item** dialog box, select **C++ File**. For **Name**, enter "Driver.c".

    > [!NOTE]
    > The file name extension is **.c**, not **.cpp**.

     Select **Add**. The Driver.c file is added under Source Files, as shown here.

    ![screen shot of the solution explorer window, showing the driver.c file added to the driver project](images/firstdriverkmdfsmall03.png)

## Write your first driver code

Now that you've created your empty Hello World project and added the Driver.c source file, you'll write the most basic code necessary for the driver to run by implementing two basic event callback functions. 

1. In Driver.c, start by including these headers:

    ```C++
    #include <ntddk.h>
    #include <wdf.h>
    ```

    > [!TIP]
    > If you can't add `Ntddk.h`, open **Configuration -> C/C++ -> General -> Additional Include Directories** and add `C:\Program Files (x86)\Windows Kits\10\Include\<build#>\km`, replacing `<build#>` with the appropriate directory in your WDK installation.
    > 

    [Ntddk.h](/windows-hardware/drivers/ddi/ntddk) contains core Windows kernel definitions for all drivers, while [Wdf.h](/windows-hardware/drivers/ddi/_wdf) contains definitions for drivers based on the Windows Driver Framework (WDF). 

2. Next, provide declarations for the two callbacks you'll use:

    ```C++
    DRIVER_INITIALIZE DriverEntry;
    EVT_WDF_DRIVER_DEVICE_ADD KmdfHelloWorldEvtDeviceAdd;
    ```

3. Use the following code to write your *DriverEntry*:

    ```C++
    NTSTATUS 
    DriverEntry(
        _In_ PDRIVER_OBJECT     DriverObject, 
        _In_ PUNICODE_STRING    RegistryPath
    )
    {
        // NTSTATUS variable to record success or failure
        NTSTATUS status = STATUS_SUCCESS;
        
        // Allocate the driver configuration object
        WDF_DRIVER_CONFIG config;
        
        // Print "Hello World" for DriverEntry
        KdPrintEx(( DPFLTR_IHVDRIVER_ID, DPFLTR_INFO_LEVEL, "KmdfHelloWorld: DriverEntry\n" ));

        // Initialize the driver configuration object to register the
        // entry point for the EvtDeviceAdd callback, KmdfHelloWorldEvtDeviceAdd
        WDF_DRIVER_CONFIG_INIT(&config, 
                               KmdfHelloWorldEvtDeviceAdd
                               );

        // Finally, create the driver object
        status = WdfDriverCreate(DriverObject, 
                                 RegistryPath, 
                                 WDF_NO_OBJECT_ATTRIBUTES, 
                                 &config, 
                                 WDF_NO_HANDLE
                                 );
        return status;
    }
    ```

    [*DriverEntry*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) is the entry point for all drivers, like `Main()` is for many user mode applications. The job of *DriverEntry* is to initialize driver-wide structures and resources. In this example, you printed "Hello World" for *DriverEntry*, configured the driver object to register your *EvtDeviceAdd* callback's entry point, then created the driver object and returned. 

    The driver object acts as the parent object for all other framework objects you might create in your driver, which include device objects, I/O queues, timers, spinlocks, and more. For more information about framework objects, see [Introduction to Framework Objects](../wdf/introduction-to-framework-objects.md).

    > [!TIP]
    > For *DriverEntry*, we strongly recommend keeping the name as "DriverEntry" to help with code analysis and debugging.

4. Next, use the following code to write your *KmdfHelloWorldEvtDeviceAdd*:

    ```C++
    NTSTATUS 
    KmdfHelloWorldEvtDeviceAdd(
        _In_    WDFDRIVER       Driver, 
        _Inout_ PWDFDEVICE_INIT DeviceInit
    )
    {
        // We're not using the driver object,
        // so we need to mark it as unreferenced
        UNREFERENCED_PARAMETER(Driver);

        NTSTATUS status;

        // Allocate the device object
        WDFDEVICE hDevice;    

        // Print "Hello World"
        KdPrintEx(( DPFLTR_IHVDRIVER_ID, DPFLTR_INFO_LEVEL, "KmdfHelloWorld: KmdfHelloWorldEvtDeviceAdd\n" ));
        
        // Create the device object
        status = WdfDeviceCreate(&DeviceInit, 
                                 WDF_NO_OBJECT_ATTRIBUTES,
                                 &hDevice
                                 );
        return status;
    }
    ```

    [*EvtDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) is invoked by the system when it detects that your device has arrived. Its job is to initialize structures and resources for that device. In this example, you simply printed out a "Hello World" message for *EvtDeviceAdd*, created the device object, and returned. In other drivers you write, you might create I/O queues for your hardware, set up a *device context* storage space for device-specific information, or perform other tasks needed to prepare your device.

    > [!TIP]
    > For the device add callback, notice how you named it with your driver's name as a prefix (*KmdfHelloWorld*EvtDeviceAdd). Generally, we recommend naming your driver's functions in this way to differentiate them from other drivers' functions. *DriverEntry* is the only one you should name exactly that.

5. Your complete Driver.c now looks like this:

    ```C++
    #include <ntddk.h>
    #include <wdf.h>
    DRIVER_INITIALIZE DriverEntry;
    EVT_WDF_DRIVER_DEVICE_ADD KmdfHelloWorldEvtDeviceAdd;

    NTSTATUS 
    DriverEntry(
        _In_ PDRIVER_OBJECT     DriverObject, 
        _In_ PUNICODE_STRING    RegistryPath
    )
    {
        // NTSTATUS variable to record success or failure
        NTSTATUS status = STATUS_SUCCESS;
        
        // Allocate the driver configuration object
        WDF_DRIVER_CONFIG config;
        
        // Print "Hello World" for DriverEntry
        KdPrintEx(( DPFLTR_IHVDRIVER_ID, DPFLTR_INFO_LEVEL, "KmdfHelloWorld: DriverEntry\n" ));

        // Initialize the driver configuration object to register the
        // entry point for the EvtDeviceAdd callback, KmdfHelloWorldEvtDeviceAdd
        WDF_DRIVER_CONFIG_INIT(&config, 
                               KmdfHelloWorldEvtDeviceAdd
                               );

        // Finally, create the driver object
        status = WdfDriverCreate(DriverObject, 
                                 RegistryPath, 
                                 WDF_NO_OBJECT_ATTRIBUTES, 
                                 &config, 
                                 WDF_NO_HANDLE
                                 );
        return status;
    }

    NTSTATUS 
    KmdfHelloWorldEvtDeviceAdd(
        _In_    WDFDRIVER       Driver, 
        _Inout_ PWDFDEVICE_INIT DeviceInit
    )
    {
        // We're not using the driver object,
        // so we need to mark it as unreferenced
        UNREFERENCED_PARAMETER(Driver);

        NTSTATUS status;

        // Allocate the device object
        WDFDEVICE hDevice;    

        // Print "Hello World"
        KdPrintEx(( DPFLTR_IHVDRIVER_ID, DPFLTR_INFO_LEVEL, "KmdfHelloWorld: KmdfHelloWorldEvtDeviceAdd\n" ));
        
        // Create the device object
        status = WdfDeviceCreate(&DeviceInit, 
                                 WDF_NO_OBJECT_ATTRIBUTES,
                                 &hDevice
                                 );
        return status;
    }
    ```

6. Save Driver.c.

This example illustrates a fundamental concept of drivers: they are a "collection of callbacks" that, once initialized, sit and wait for the system to call them when it needs something. This could be a new device arrival event, an I/O request from a user mode application, a system power shutdown event, a request from another driver, or a surprise removal event when a user unplugs the device unexpectedly. Fortunately, to say "Hello World," you only needed to worry about driver and device creation.

Next, you'll build your driver.

## Build the driver

1. In the **Solution Explorer** window, select and hold (or right-click) **Solution 'KmdfHelloWorld' (1 project)** and choose **Configuration Manager**. Choose a configuration and platform for the driver project. For this exercise, we choose **Debug** and **x64**.

2. In the **Solution Explorer** window, select and hold (or right-click) **KmdfHelloWorld** and choose **Properties**. In **Wpp Tracing &gt; All Options**, set **Run Wpp tracing** to **No**. Select **Apply** and then **OK**.
3. To build your driver, choose **Build Solution** from the **Build** menu. Visual Studio shows the build progress in the **Output** window. (If the **Output** window is not visible, choose **Output** from the **View** menu.) When you have verified that the solution built successfully, you can close Visual Studio.
4. To see the built driver, in File Explorer, go to your **KmdfHelloWorld** folder, and then to **C:\\KmdfHelloWorld\\x64\\Debug\KmdfHelloWorld**. The folder includes:

    -   KmdfHelloWorld.sys -- the kernel-mode driver file
    -   KmdfHelloWorld.inf -- an information file that Windows uses when you install the driver
    -   KmdfHelloWorld.cat -- a catalog file that the installer uses to verify the driver's test signature


> [!TIP]
> If you see `DriverVer set to a date in the future` when building your driver, change your driver project settings so that Inf2Cat sets `/uselocaltime`. To do so, use **Configuration Properties->Inf2Cat->General->Use Local Time**. Now both [Stampinf](../devtest/stampinf-command-options.md) and Inf2Cat use local time.

## <span id="Deploy_the_driver"></span><span id="deploy_the_driver"></span><span id="DEPLOY_THE_DRIVER"></span>Deploy the driver

Typically when you test and debug a driver, the debugger and the driver run on separate computers. The computer that runs the debugger is called the *host computer*, and the computer that runs the driver is called the *target computer*. The target computer is also called the *test computer*.

So far you've used Visual Studio to build a driver on the host computer. Now you need to configure a target computer. 

1. Follow the instructions in [Provision a computer for driver deployment and testing (WDK 10)](provision-a-target-computer-wdk-8-1.md).

    > [!TIP]
    > When you follow the steps to provision the target computer automatically using a network cable, take note of the port and key. You'll use them later in the debugging step. In this example, we'll use **50000** as the port and **1.2.3.4** as the key.
    >
    > In real driver debugging scenarios, we recommend using a KDNET-generated key. For more information about how to use KDNET to generate a random key, see the [Debug Drivers - Step by Step Lab (Sysvad Kernel Mode)](../debugger/debug-universal-drivers--kernel-mode-.md) topic.

2.  On the host computer, open your solution in Visual Studio. You can double-click the solution file, KmdfHelloWorld.sln, in your KmdfHelloWorld folder.
3.  In the **Solution Explorer** window, select and hold (or right-click) the **KmdfHelloWorld** project, and choose **Properties**.
4.  In the **KmdfHelloWorld Property Pages** window, go to **Configuration Properties &gt; Driver Install &gt; Deployment**, as shown here.
5.  Check **Remove previous driver versions before deployment**.
6.  For **Target Device Name**, select the name of the computer that you configured for testing and debugging. In this exercise, we use a computer named MyTestComputer.
7.  Select **Hardware ID Driver Update**, and enter the hardware ID for your driver. For this exercise, the hardware ID is Root\\KmdfHelloWorld. Select **OK**.

    ![screen shot showing the kmdfhelloworld property pages window with the deployment driver install selected ](images/vs2015-kmdf-hello-world-property-pages.png)

    >[!NOTE]
    > In this exercise, the hardware ID does not identify a real piece of hardware. It identifies an imaginary device that will be given a place in the [device tree](device-nodes-and-device-stacks.md) as a child of the root node. For real hardware, do not select **Hardware ID Driver Update**; instead, select **Install and Verify**. You'll see the hardware ID in your driver's information (INF) file. In the **Solution Explorer** window, go to **KmdfHelloWorld &gt; Driver Files**, and double-click KmdfHelloWorld.inf. The hardware ID is located under \[Standard.NT$ARCH$\].

    ```C++
    [Standard.NT$ARCH$]
    %KmdfHelloWorld.DeviceDesc%=KmdfHelloWorld_Device, Root\KmdfHelloWorld
    ```

8. On the **Build** menu, choose **Deploy Solution**. Visual Studio automatically copies the files required to install and run the driver to the target computer. This may take a minute or two.

    When you deploy a driver, the driver files are copied to the %Systemdrive%\drivertest\drivers folder on the test computer. If something goes wrong during deployment, you can check to see if the files are copied to the test computer. Verify that the .inf, .cat, test cert, and .sys files, and any other necessary files, are present in the %systemdrive%\drivertest\drivers folder.

    For more information about deploying drivers, see [Deploying a Driver to a Test Computer](../develop/deploying-a-driver-to-a-test-computer.md).

## Install the driver

With your Hello World driver deployed to the target computer, now you'll install the driver. When you previously provisioned the target computer with Visual Studio using the *automatic* option, Visual Studio set up the target computer to run test signed drivers as part of the provisioning process. Now you just need to install the driver using the DevCon tool.

1. On the host computer, navigate to the Tools folder in your WDK installation and locate the DevCon tool. For example, look in the following folder:

    *C:\\Program Files (x86)\\Windows Kits\\10\\Tools\\x64\\devcon.exe*

    Copy the DevCon tool to your remote computer.

2. On the target computer, install the driver by navigating to the folder containing the driver files, then running the DevCon tool. 
    1. Here's the general syntax for the devcon tool that you will use to install the driver:

        *devcon install \<INF file\> \<hardware ID\>*

        The INF file required for installing this driver is KmdfHelloWorld.inf. The INF file contains the hardware ID for installing the driver binary, *KmdfHelloWorld.sys*. Recall that the hardware ID, located in the INF file, is **Root\\KmdfHelloWorld**.
    2. Open a Command Prompt window as Administrator. Navigate to your folder containing the built driver .sys file and enter this command:

        **devcon install kmdfhelloworld.inf root\\kmdfhelloworld**

        If you get an error message about *devcon* not being recognized, try adding the path to the *devcon* tool. For example, if you copied it to a folder on the target computer called *C:\\Tools*, then try using the following command:

        **c:\\tools\\devcon install kmdfhelloworld.inf root\kmdfhelloworld**

        A dialog box will appear indicating that the test driver is an unsigned driver. Select **Install this driver anyway** to proceed.

        ![screenshot of driver installation warning](../debugger/images/debuglab-image-install-security-warning.png)

## Debug the driver

Now that you have installed your KmdfHelloWorld driver on the target computer, you'll attach a debugger remotely from the host computer.

1. On the host computer, open a Command Prompt window as Administrator. Change to the WinDbg.exe directory. We will use the x64version of WinDbg.exe from the Windows Driver Kit (WDK) that was installed as part of the Windows kit installation. Here is the default path to WinDbg.exe:

    *C:\\Program Files (x86)\\Windows Kits\\10\\Debuggers\\x64*

2. Launch WinDbg to connect to a kernel debug session on the target computer by using the following command. The value for the port and key should be the same as what you used to provision the target computer. We'll use **50000** for the port and **1.2.3.4** for the key, the values we used during the deploy step. The *k* flag indicates that this is a kernel debug session.

    **WinDbg -k net:port=50000,key=1.2.3.4**

3.  On the **Debug** menu, choose **Break**. The debugger on the host computer will break into the target computer. In the **Debugger Command** window, you can see the kernel debugging command prompt: **kd\>**.

4. At this point, you can experiment with the debugger by entering commands at the **kd&gt;** prompt. For example, you could try these commands:

    -   [lm](./device-nodes-and-device-stacks.md)
    -   [.sympath](../debugger/-sympath--set-symbol-path-.md)
    -   [.reload](../debugger/-reload--reload-module-.md)
    -   [x KmdfHelloWorld!\*](../debugger/x--examine-symbols-.md)

5. To let the target computer run again, choose **Go** from the **Debug** menu or press "g," then press "enter."
6. To stop the debugging session, choose **Detach Debuggee** from the **Debug** menu.

    > [!IMPORTANT]
    > Make sure you use the "go" command to let the target computer run again before exiting the debugger, or the target computer will remain unresponsive to your mouse and keyboard input because it is still talking to the debugger.

For a detailed step-by-step walkthrough of the driver debugging process, see [Debug Universal Drivers - Step by Step Lab (Echo Kernel-Mode)](../debugger/debug-universal-drivers---step-by-step-lab--echo-kernel-mode-.md).

For more information about remote debugging, see [Remote Debugging Using WinDbg](../debugger/remote-debugging-using-windbg.md).

## <span id="related_topics"></span>Related topics

[Developing, Testing, and Deploying Drivers](https://go.microsoft.com/fwlink/p?linkid=399234)

[Debugging Tools for Windows](../debugger/index.md)

[Debug Universal Drivers - Step by Step Lab (Echo Kernel-Mode)](../debugger/debug-universal-drivers---step-by-step-lab--echo-kernel-mode-.md)

[Write your first driver](writing-your-first-driver.md)
