---
title: Troubleshooting UMDF 2.0 Driver Crashes
description: Starting in User-Mode Driver Framework (UMDF) version 2, you can use a subset of the debugger extension commands implemented in Wdfkd.dll to debug a UMDF driver.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Troubleshooting UMDF 2.0 Driver Crashes


Starting in User-Mode Driver Framework (UMDF) version 2, you can use a subset of the debugger extension commands implemented in Wdfkd.dll to debug a UMDF driver. This topic describes which commands you might start with to troubleshoot UMDF driver problems.

##  Determining Why a UMDF 2.0 Driver Crashed


If the driver host process is terminated, your driver might have a problem in a callback that results in the [host timeout](how-umdf-enforces-time-outs.md) threshold being exceeded. In this case, the reflector terminates the driver host process.

To investigate, first set up a kernel-mode debugging session as described in [How to Enable Debugging of a UMDF Driver](enabling-a-debugger.md). We strongly recommend doing all development and testing of your UMDF driver with a kernel debugger attached to the test system and enabling [Application Verifier (AppVerif.exe)](../debugger/debugger-download-tools.md) on WUDFHost.exe. Use the following command, attach a kernel debugger and then reboot.

```cpp
AppVerif –enable Heaps Exceptions Handles Locks Memory TLS Leak –for WudfHost.exe
```

- If **HostFailKdDebugBreak** is set (this should be enabled by default starting Windows 8), the reflector breaks into the kernel-mode debugger when the timeout threshold is exceeded. In the debugger output, you will see several suggestions on how to begin, including links you can click on. For example:

  ```cpp
  **** Problem detected in UMDF driver "WUDFOsrUsbFx2". !process 0xFFFFE0000495B080 0x1f, !devstack 0xFFFFE000032BFA10, Problem code 3 ****
  **** Dump UMDF driver image name and stack: !wdfkd.wdfumdevstack 0x000000BEBB49AE20
  **** Dump UM Irps for this stack: !wdfkd.wdfumirps 0x000000BEBB49AE20
  **** Dump UMDF trace log: !wmitrace.logdump WUDFTrace
  **** Helpful UMDF debugger extension commands: !wdfkd.wdfhelp
  **** Note that driver host process may get terminated if you go past this break, making it difficult to debug the problem!
  ```

- Use [**!analyze**](../debugger/-analyze.md) to display information about the failure, and additional UMDF extension commands you can try.
- Use [**!process 0 0x1f wudfhost.exe**](../debugger/-process.md) to list all Wudfhost.exe driver host processes, including thread stack information.

  You can also use !wdfkd.wdfumtriage and [**!wdfkd.wdfldr**](../debugger/-wdfkd-wdfldr.md) to display all drivers that are currently bound to WDF. When you click on the image name of a UMDF driver, the debugger displays the address of the hosting process. You can then click on the process address to display information specific to that process.

- If necessary, use [**.process /r /p *Process***](../debugger/-process--set-process-context-.md) to switch process context to that of the Wudfhost process that is hosting your driver. Use [**.cache forcedecodeuser**](../debugger/-cache--set-cache-size-.md) and **lmu** to verify that your driver is hosted in the current process.
- Examine thread call stacks ([**!thread *Address***](../debugger/-thread.md)) to determine if a driver callback timed out. Look at the tick count for the threads. In Windows 8.1, the reflector times out after one minute.
- Use [**!wdfkd.wdfdriverinfo MyDriver.dll 0x10**](../debugger/-wdfkd-wdfdriverinfo.md) to display the device tree in verbose form. Then click on [**!wdfdevice**](../debugger/-wdfkd-wdfdevice.md). This command displays detailed power, power policy, and Plug and Play (PnP) state information.
- Use [**!wdfkd.wdfumirps**](../debugger/-wdfkd-wdfumirps.md) to look for pending IRPs.
- Use [**!wdfkd.wdfdevicequeues**](../debugger/-wdfkd-wdfdevicequeues.md) to check the status of the driver's queues.
- In a kernel-mode debugging session, you can use [**!wmitrace.logdump WudfTrace**](../debugger/-wmitrace-logdump.md) to display the trace log.

## Displaying the UMDF 2.0 IFR Log


In a kernel-mode debugging session, you can use the [**!wdfkd.wdflogdump**](../debugger/-wdfkd-wdflogdump.md) extension command to display the Windows Driver Frameworks (WDF) In-flight Recorder (IFR) log records, if available.

## Finding Memory Dump Files


See [Determining Why the Reflector Terminated the Host Process](determining-why-the-reflector-terminated-the-host-process.md) for information on finding user-mode dump files. See [Using WPP Software Tracing in UMDF Drivers](using-wpp-software-tracing-in-umdf-drivers.md) for information on how to set the **LogMinidumpType** registry value to specify the type of information stored in the minidump file.
