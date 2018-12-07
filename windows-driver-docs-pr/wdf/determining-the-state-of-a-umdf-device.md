---
title: Determining the State of a UMDF Device
description: This topic describes how you can use debugger extensions in conjunction with a User-Mode Driver Framework (UMDF) version 1 or 2 driver to determine what state your UMDF device is in.
ms.assetid: ed1a4429-4f36-44b9-9564-587aa381342f
keywords:
- UMDF WDK , UMDF device state
- UMDF WDK , device state
- user-mode debuggers WDK UMDF , determining the UMDF device state
- kernel-mode debuggers WDK UMDF , determining the UMDF device state
- debugging scenarios WDK UMDF , UMDF device state
- UMDF WDK , debugging scenarios, UMDF device state
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Determining the State of a UMDF Device


This topic describes how you can use debugger extensions in conjunction with a User-Mode Driver Framework (UMDF) version 1 or 2 driver to determine what state your UMDF device is in.

For UMDF version 1, you'll use extension commands implemented in wudfext.dll. Starting in UMDF version 2, you'll use extension commands implemented in wdfkd.dll.

To determine device state, use the following steps:

1.  Break into a driver host process by using one of the following debugger types:
    -   User-mode debugger:
        1.  Locate the appropriate driver host process for the device (that is, WUDFHost.exe). If there are multiple instances of the host process, you can use the operating system-supplied Tasklist.exe application to determine which process is hosting your driver.

            Use this command from an elevated Command Prompt.

            **tasklist -m &lt;yourdriver.dll&gt;**

        2.  Start the debugger with elevated privilege and attach to the appropriate process.
        3.  Reload symbols by using the **.reload** debugger command.
        4.  You can view all the threads by using the **~\*k** debugger command.

    -   Kernel-mode debugger:
        1.  Locate the appropriate driver host process for the device (that is, WUDFHost.exe). Use the **!process** kernel-mode debugger extension as shown in the following example to obtain a list of all WUDFHost.exe instances:

            **!process 0 0 WUDFHost.exe**

            The process address and Process Environment Block (PEB) address from the **!process 0 0** output are used in the next steps.

        2.  Attach to the host process in one of the following ways:
            -   Use the **.process** debugger command for a non-invasive attach as shown in the following example:

                **.process /p /r &lt;process-addr&gt;**

                You should use non-invasive attach when you cannot let the execution continue. For example, you should use non-invasive attach when you receive a break in your application and you want to see what the driver did to cause that break or when the reflector prepares to terminate your host process.

            -   Use the **.process** debugger command in an invasive attach as shown in the following example:

                **.process /i &lt;process-addr&gt;**

                The debugger will request that you continue by using the **g** debugger command; shortly after you execute the **g** debugger command, the debugger will break into the active process. Reload user symbols by using the **.reload** debugger command as shown in the followingexample:

                **.reload /user**

        3.  If there are multiple instances of host process, you can use the **!peb** general debugger extension as shown in the following example to obtain the list of modules that are loaded in the process:

            **!peb &lt;PEB-Address&gt;**

            You need to attach to the process for this command to work. You can attach non-invasively as shown in the previous step.

            Locate the process in which your driver DLL is loaded.

        4.  Use the **!process** kernel-mode debugger extension as shown in the following example to obtain information about the process. The information includes the threads that run in the process and the addresses of those threads:

            **!process &lt;process-addr&gt;**

        5.  Use the **!thread** kernel-mode debugger extension as shown in the following example to obtain information about each thread:

            **!thread &lt;thread-addr&gt;**

2.  In the debugger, use the **.chain** command to see if the wudfext.dll (UMDF 1) or wdfkd.dll (UMDF 2) debugger extension library is loaded.
3.  If the library you need is not present, use the [**.load**](https://msdn.microsoft.com/library/windows/hardware/ff563964) command to load the extension DLL into the debugger. Then enter **.reload** to reload symbol information.
4.  Use [**!wudfext.umdevstacks**](https://msdn.microsoft.com/library/windows/hardware/ff566191) (UMDF 1) or [**!wdfkd.wdfumdevstacks**](https://msdn.microsoft.com/library/windows/hardware/dn265380) (UMDF 2) to see all device stacks loaded in the host process.

    Then use [**!wudfext.umdevstack**](https://msdn.microsoft.com/library/windows/hardware/ff566189) (UMDF 1) or [**!wdfkd.wdfumdevstack**](https://msdn.microsoft.com/library/windows/hardware/dn265379) (UMDF 2) to get detailed information about the device stack.

5.  Use [**!wudfext.wudfdevice**](https://msdn.microsoft.com/library/windows/hardware/ff566199) (UMDF 1) or [**!wdfkd.wdfdevice**](https://msdn.microsoft.com/library/windows/hardware/ff565703) (UMDF 2) to obtain information about the Plug and Play (PnP) and power-management state of the device.

6.  Use [**!wudfext.wudfdriverinfo**](https://msdn.microsoft.com/library/windows/hardware/ff566207) (UMDF 1) or [**!wdfkd.wdfdriverinfo**](https://msdn.microsoft.com/library/windows/hardware/ff565724) (UMDF 2) to display additional information about the driver, including its device tree.

 

 





