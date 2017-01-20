---
title: Write a universal Hello World driver (KMDF)
description: This topic describes how to write a Universal Windows driver using Kernel-Mode Driver Framework (KMDF). You'll start with a Microsoft Visual Studio template and then deploy and install your driver on a separate computer.
ms.assetid: B4200732-67B5-4BD9-8852-81387912A9A4
keywords: ["KMDF Hello World"]
---

# Write a universal Hello World driver (KMDF)


This topic describes how to write a [Universal Windows driver](https://msdn.microsoft.com/windows-drivers/develop/getting_started_with_universal_drivers) using Kernel-Mode Driver Framework (KMDF). You'll start with a Microsoft Visual Studio template and then deploy and install your driver on a separate computer.

To get started, be sure you have [Microsoft Visual Studio 2015](https://go.microsoft.com/fwlink/p/?LinkId=698539) and the [Windows Driver Kit (WDK) 10](https://go.microsoft.com/fwlink/p/?LinkId=733614) installed.

[Debugging Tools for Windows](http://go.microsoft.com/fwlink/p?linkid=223405) is included when you install the WDK.

## <span id="Create_and_build_a_driver_package"></span><span id="create_and_build_a_driver_package"></span><span id="CREATE_AND_BUILD_A_DRIVER_PACKAGE"></span>Create and build a driver package


1.  Open Microsoft Visual Studio. On the **File** menu, choose **New &gt; Project**.
2.  In the **New Project** dialog box, select **WDF**.
3.  In the middle pane, select **Kernel Mode Driver, Empty (KMDF)**.
4.  In the **Name** field, enter "KmdfHelloWorld" for the project name.

    **Note**  \*When you create a new KMDF or UMDF driver, you must select a driver name that has 32 characters or less. This length limit is defined in wdfglobals.h.

     

5.  In the **Location** field, enter the directory where you want to create the new project.
6.  Check **Create directory for solution**. Click **OK**.

    ![screen shot of the new project dialog box](images/vs2015-new-project-kmdf-empty.png)

    Visual Studio creates one project and a solution. You can see them in the **Solution Explorer** window, shown here. (If the Solution Explorer window is not visible, choose **Solution Explorer** from the **View** menu.) The solution has a driver project named KmdfHelloWorld.

    ![screen shot of the solution explorer window, showing the package project (kmdfhelloworld packages) and the empty driver project (kmdfhelloworld)](images/vs2015-kmdf-hello-world-solution-explorer.png)

7.  In the **Solution Explorer** window, right-click **KmdfHelloWorld**, and choose **Properties**. Navigate to **Configuration Properties &gt; Driver Settings &gt; General**, and note that **Target Platform** defaults to **Universal.**

8.  In the **Solution Explorer** window, right-click **KmdfHelloWorld** and choose **Add &gt; New Item**.
9.  In the **Add New Item** dialog box, select **C++ File**. For **Name**, enter "Driver.c".

    **Note**  The file name extension is **.c**, not **.cpp**.

     

    Click **Add**. The Driver.c file is added under Source Files, as shown here.

    ![screen shot of the solution explorer window, showing the driver.c file added to the driver project](images/firstdriverkmdfsmall03.png)

10. Open Driver.c, and enter this code:

    ```
    #include <ntddk.h>
    #include <wdf.h>
    DRIVER_INITIALIZE DriverEntry;
    EVT_WDF_DRIVER_DEVICE_ADD KmdfHelloWorldEvtDeviceAdd;

    NTSTATUS DriverEntry(_In_ PDRIVER_OBJECT  DriverObject, _In_ PUNICODE_STRING RegistryPath)
    {
        NTSTATUS status;
        WDF_DRIVER_CONFIG config;
     
        KdPrintEx(( DPFLTR_IHVDRIVER_ID, DPFLTR_INFO_LEVEL, "KmdfHelloWorld: DriverEntry\n" ));
        WDF_DRIVER_CONFIG_INIT(&config, KmdfHelloWorldEvtDeviceAdd);
        status = WdfDriverCreate(DriverObject, RegistryPath, WDF_NO_OBJECT_ATTRIBUTES, &config, WDF_NO_HANDLE);
        return status;
    }

    NTSTATUS KmdfHelloWorldEvtDeviceAdd(_In_ WDFDRIVER Driver, _Inout_ PWDFDEVICE_INIT DeviceInit)
    {
        NTSTATUS status;
        WDFDEVICE hDevice;
        UNREFERENCED_PARAMETER(Driver);

        KdPrintEx(( DPFLTR_IHVDRIVER_ID, DPFLTR_INFO_LEVEL, "KmdfHelloWorld: KmdfHelloWorldEvtDeviceAdd\n" ));
        status = WdfDeviceCreate(&DeviceInit, WDF_NO_OBJECT_ATTRIBUTES, &hDevice);
        return status;
    }
    ```

11. Save Driver.c.
12. In the **Solution Explorer** window, right-click **Solution 'KmdfHelloWorld' (1 project)** and choose **Configuration Manager**. Choose a configuration and platform for both the driver project and the package project. For this exercise, we choose Debug and x64.

13. In the **Solution Explorer** window, right-click **KmdfHelloWorld** and choose **Properties**. In **Wpp Tracing &gt; All Options**, set **Run Wpp tracing** to **No**. Click **Apply** and then **OK**.
14. To build your driver and create a driver package, choose **Build Solution** from the **Build** menu. Visual Studio shows the build progress in the **Output** window. (If the **Output** window is not visible, choose **Output** from the **View** menu.)

    When you have verified that the solution built successfully, you can close Visual Studio.

15. To see the built driver, in File Explorer, go to your **KmdfHelloWorld** folder, and then to **C:\\KmdfHelloWorld\\x64\\Debug**. The folder includes:

    -   KmdfHelloWorld.sys -- the kernel-mode driver file
    -   KmdfHelloWorld.inf -- an information file that Windows uses when you install the driver
    -   KmdfHelloWorld.cat -- a catalog file that the installer uses to verify the test signature for the driver package

## <span id="Deploy_and_install_the_driver"></span><span id="deploy_and_install_the_driver"></span><span id="DEPLOY_AND_INSTALL_THE_DRIVER"></span>Deploy and install the driver


Typically when you test and debug a driver, the debugger and the driver run on separate computers. The computer that runs the debugger is called the *host computer*, and the computer that runs the driver is called the *target computer*. The target computer is also called the *test computer*.

So far you've used Visual Studio to build a driver on the host computer. Now you need to configure a target computer. Follow the instructions in [Provision a computer for driver deployment and testing (WDK 10)](provision-a-target-computer-wdk-8-1.md). Then you can deploy, install, load, and debug your driver:

1.  On the host computer, open your solution in Visual Studio. You can double-click the solution file, KmdfHelloWorld.sln, in your KmdfHelloWorld folder.
2.  In the **Solution Explorer** window, right-click the **KmdfHelloWorld** project, and choose **Properties**.
3.  In the **KmdfHelloWorld Property Pages** window, go to **Configuration Properties &gt; Driver Install &gt; Deployment**, as shown here.
4.  Check **Remove previous driver versions before deployment**.
5.  For **Target Device Name**, select the name of the computer that you configured for testing and debugging. In this exercise, we use a computer named MyTestComputer.
6.  Select **Hardware ID Driver Update**, and enter the hardware ID for your driver. For this exercise, the hardware ID is Root\\KmdfHelloWorld. Click **OK**.

    ![screen shot showing the kmdfhelloworld package property pages window with the deployment driver install selected ](images/vs2015-kmdf-hello-world-property-pages.png)

    **Note**  In this exercise, the hardware ID does not identify a real piece of hardware. It identifies an imaginary device that will be given a place in the [device tree](device-nodes-and-device-stacks.md) as a child of the root node. For real hardware, do not select **Hardware ID Driver Update**; instead, select **Install and Verify**.
    You'll see the hardware ID in your driver's information (INF) file. In the **Solution Explorer** window, go to **KmdfHelloWorld &gt; Driver Files**, and double-click KmdfHelloWorld.inf. The hardware ID is located under \[Standard.NT$ARCH$\].

    ```ManagedCPlusPlus
    [Standard.NT$ARCH$]
    %KmdfHelloWorld.DeviceDesc%=KmdfHelloWorld_Device, Root\KmdfHelloWorld
    ```

     

7.  On the **Debug** menu, choose **Start Debugging**, or press **F5** on the keyboard.
8.  Visual Studio first shows progress in the **Output** window. Then it opens the **Debugger Immediate** window and continues to show progress.

    Wait until your driver has been deployed, installed, and loaded on the target computer. This might take a minute or two.

9.  On the **Debug** menu, choose **Break All**. The debugger on the host computer will break into the target computer. In the **Debugger Immediate** window, you can see the kernel debugging command prompt: **kd&gt;**.

    ![screen shot of the command prompt in the debugger immediate window](images/firstdriverkmdfsmall09.png)

10. At this point, you can experiment with the debugger by entering commands at the **kd&gt;** prompt. For example, you could try these commands:

    -   [lm](http://go.microsoft.com/fwlink/p?linkid=399236)
    -   [.sympath](http://go.microsoft.com/fwlink/p?linkid=399238)
    -   [.reload](http://go.microsoft.com/fwlink/p?linkid=399239)
    -   [x KmdfHelloWorld!\*](http://go.microsoft.com/fwlink/p?linkid=399240)

11. To let the target computer run again, choose **Continue** from the **Debug** menu.
12. To stop the debugging session, choose **Stop Debugging** from the **Debug** menu.

## <span id="related_topics"></span>Related topics


[Developing, Testing, and Deploying Drivers](http://go.microsoft.com/fwlink/p?linkid=399234)

[Debugging Tools for Windows](http://go.microsoft.com/fwlink/p?linkid=223405)

[Write your first driver](writing-your-first-driver.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wdkgetstart\wdkgetstart]:%20Write%20a%20universal%20Hello%20World%20driver%20%28KMDF%29%20%20RELEASE:%20%281/20/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





