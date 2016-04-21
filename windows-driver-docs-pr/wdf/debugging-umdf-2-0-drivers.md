---
title: Troubleshooting UMDF 2.0 Driver Crashes
author: windows-driver-content
description: Starting in User-Mode Driver Framework (UMDF) version 2, you can use a subset of the debugger extension commands implemented in Wdfkd.dll to debug a UMDF driver.
ms.assetid: df1bfc10-379b-457f-a9c8-40fa10048f81
---

# Troubleshooting UMDF 2.0 Driver Crashes


Starting in User-Mode Driver Framework (UMDF) version 2, you can use a subset of the debugger extension commands implemented in Wdfkd.dll to debug a UMDF driver. This topic describes which commands you might start with to troubleshoot UMDF driver problems.

##  Determining Why a UMDF 2.0 Driver Crashed


If the driver host process is terminated, your driver might have a problem in a callback that results in the [host timeout](how-umdf-enforces-time-outs.md) threshold being exceeded. In this case, the reflector terminates the driver host process.

To investigate, first set up a kernel-mode debugging session as described in [How to Enable Debugging of a UMDF Driver](enabling-a-debugger.md).

-   If **HostFailKdDebugBreak** is set, the reflector breaks into the kernel-mode debugger when the timeout threshold is exceeded. In the debugger output, you will see several suggestions on how to begin, including links you can click on. For example:

    ```
    **** Problem detected in UMDF driver "WUDFOsrUsbFx2". !process 0xFFFFE0000495B080 0x1f, !devstack 0xFFFFE000032BFA10, Problem code 3 ****
    **** Dump UMDF driver image name and stack: !wdfkd.wdfumdevstack 0x000000BEBB49AE20
    **** Dump UM Irps for this stack: !wdfkd.wdfumirps 0x000000BEBB49AE20
    **** Dump UMDF trace log: !wmitrace.logdump WUDFTrace
    **** Helpful UMDF debugger extension commands: !wdfkd.wdfhelp
    **** Note that driver host process may get terminated if you go past this break, making it difficult to debug the problem!
    
    ```

-   Use [**!analyze**](https://msdn.microsoft.com/library/windows/hardware/ff562112) to display information about the failure, and additional UMDF extension commands you can try.
-   Use [**!process 0 0x1f wudfhost.exe**](https://msdn.microsoft.com/library/windows/hardware/ff564717) to list all Wudfhost.exe driver host processes, including thread stack information.

    You can also use [**!wdfkd.wdfldr**](https://msdn.microsoft.com/library/windows/hardware/ff565803) to display all drivers that are currently bound to WDF. When you click on the image name of a UMDF driver, the debugger displays the address of the hosting process. You can then click on the process address to display information specific to that process.

-   If necessary, use [**.process /r /p *Process***](https://msdn.microsoft.com/library/windows/hardware/ff564723) to switch process context to that of the Wudfhost process that is hosting your driver. Use [**.cache forcedecodeuser**](https://msdn.microsoft.com/library/windows/hardware/ff562180) and **lmu** to verify that your driver is hosted in the current process.
-   Examine thread call stacks ([**!thread *Address***](https://msdn.microsoft.com/library/windows/hardware/ff565440)) to determine if a driver callback timed out. Look at the tick count for the threads. In Windows 8.1, the reflector times out after one minute.
-   Use [**!wdfkd.wdfdriverinfo MyDriver.dll 0x10**](https://msdn.microsoft.com/library/windows/hardware/ff565724) to display the device tree in verbose form. Then click on [**!wdfdevice**](https://msdn.microsoft.com/library/windows/hardware/ff565703). This command displays detailed power, power policy, and Plug and Play (PnP) state information.
-   Use [**!wdfkd.wdfumirps**](https://msdn.microsoft.com/library/windows/hardware/dn265384) to look for pending IRPs.
-   Use [**!wdfkd.wdfdevicequeues**](https://msdn.microsoft.com/library/windows/hardware/ff565715) to check the status of the driver's queues.
-   In a kernel-mode debugging session, you can use [**!wmitrace.logdump WudfTrace**](https://msdn.microsoft.com/library/windows/hardware/ff566159) to display the trace log.

## <a href="" id="displaying-the--umdf-2-0-ifr-log"></a>Displaying the UMDF 2.0 IFR Log


In a kernel-mode debugging session, you can use the [**!wdfkd.wdflogdump**](https://msdn.microsoft.com/library/windows/hardware/ff565805) extension command to display the Windows Driver Frameworks (WDF) In-flight Recorder (IFR) log records, if available.

## Finding Memory Dump Files


See [Determining Why the Reflector Terminated the Host Process](determining-why-the-reflector-terminated-the-host-process.md) for information on finding user-mode dump files. See [Using WPP Software Tracing in UMDF Drivers](using-wpp-software-tracing-in-umdf-drivers.md) for information on how to set the **LogMinidumpType** registry value to specify the type of information stored in the minidump file.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Troubleshooting%20UMDF%202.0%20Driver%20Crashes%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




