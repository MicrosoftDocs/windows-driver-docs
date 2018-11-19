---
title: Troubleshooting UMDF 2.0 Driver Crashes
description: Starting in User-Mode Driver Framework (UMDF) version 2, you can use a subset of the debugger extension commands implemented in Wdfkd.dll to debug a UMDF driver.
ms.assetid: df1bfc10-379b-457f-a9c8-40fa10048f81
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Troubleshooting UMDF 2.0 Driver Crashes


Starting in User-Mode Driver Framework (UMDF) version 2, you can use a subset of the debugger extension commands implemented in Wdfkd.dll to debug a UMDF driver. This topic describes which commands you might start with to troubleshoot UMDF driver problems.

##  Determining Why a UMDF 2.0 Driver Crashed


If the driver host process is terminated, your driver might have a problem in a callback that results in the [host timeout](how-umdf-enforces-time-outs.md) threshold being exceeded. In this case, the reflector terminates the driver host process.

To investigate, first set up a kernel-mode debugging session as described in [How to Enable Debugging of a UMDF Driver](enabling-a-debugger.md).

- If **HostFailKdDebugBreak** is set, the reflector breaks into the kernel-mode debugger when the timeout threshold is exceeded. In the debugger output, you will see several suggestions on how to begin, including links you can click on. For example:

  ```cpp
  **** Problem detected in UMDF driver "WUDFOsrUsbFx2". !process 0xFFFFE0000495B080 0x1f, !devstack 0xFFFFE000032BFA10, Problem code 3 ****
  **** Dump UMDF driver image name and stack: !wdfkd.wdfumdevstack 0x000000BEBB49AE20
  **** Dump UM Irps for this stack: !wdfkd.wdfumirps 0x000000BEBB49AE20
  **** Dump UMDF trace log: !wmitrace.logdump WUDFTrace
  **** Helpful UMDF debugger extension commands: !wdfkd.wdfhelp
  **** Note that driver host process may get terminated if you go past this break, making it difficult to debug the problem!
  ```

- Use [**!analyze**](https://msdn.microsoft.com/library/windows/hardware/ff562112) to display information about the failure, and additional UMDF extension commands you can try.
- Use [**!process 0 0x1f wudfhost.exe**](https://msdn.microsoft.com/library/windows/hardware/ff564717) to list all Wudfhost.exe driver host processes, including thread stack information.

  You can also use [**!wdfkd.wdfldr**](https://msdn.microsoft.com/library/windows/hardware/ff565803) to display all drivers that are currently bound to WDF. When you click on the image name of a UMDF driver, the debugger displays the address of the hosting process. You can then click on the process address to display information specific to that process.

- If necessary, use [**.process /r /p *Process***](https://msdn.microsoft.com/library/windows/hardware/ff564723) to switch process context to that of the Wudfhost process that is hosting your driver. Use [**.cache forcedecodeuser**](https://msdn.microsoft.com/library/windows/hardware/ff562180) and **lmu** to verify that your driver is hosted in the current process.
- Examine thread call stacks ([**!thread *Address***](https://msdn.microsoft.com/library/windows/hardware/ff565440)) to determine if a driver callback timed out. Look at the tick count for the threads. In Windows 8.1, the reflector times out after one minute.
- Use [**!wdfkd.wdfdriverinfo MyDriver.dll 0x10**](https://msdn.microsoft.com/library/windows/hardware/ff565724) to display the device tree in verbose form. Then click on [**!wdfdevice**](https://msdn.microsoft.com/library/windows/hardware/ff565703). This command displays detailed power, power policy, and Plug and Play (PnP) state information.
- Use [**!wdfkd.wdfumirps**](https://msdn.microsoft.com/library/windows/hardware/dn265384) to look for pending IRPs.
- Use [**!wdfkd.wdfdevicequeues**](https://msdn.microsoft.com/library/windows/hardware/ff565715) to check the status of the driver's queues.
- In a kernel-mode debugging session, you can use [**!wmitrace.logdump WudfTrace**](https://msdn.microsoft.com/library/windows/hardware/ff566159) to display the trace log.

## Displaying the UMDF 2.0 IFR Log


In a kernel-mode debugging session, you can use the [**!wdfkd.wdflogdump**](https://msdn.microsoft.com/library/windows/hardware/ff565805) extension command to display the Windows Driver Frameworks (WDF) In-flight Recorder (IFR) log records, if available.

## Finding Memory Dump Files


See [Determining Why the Reflector Terminated the Host Process](determining-why-the-reflector-terminated-the-host-process.md) for information on finding user-mode dump files. See [Using WPP Software Tracing in UMDF Drivers](using-wpp-software-tracing-in-umdf-drivers.md) for information on how to set the **LogMinidumpType** registry value to specify the type of information stored in the minidump file.









