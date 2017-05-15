---
title: When to Use This Technique
description: When to Use This Technique
ms.assetid: 40c9e2aa-35a3-4169-8305-bddc199a5c98
---

# When to Use This Technique


## <span id="ddk_opening_a_crash_dump_dbg"></span><span id="DDK_OPENING_A_CRASH_DUMP_DBG"></span>


There are several situations in which it is useful, or even necessary, to [control user-mode debugging from the kernel debugger](controlling-the-user-mode-debugger-from-the-kernel-debugger.md):

-   When you need to perform user-mode debugging, but also need control over the Windows kernel that the user-mode target is running on or need to use some kernel-mode debugging features to analyze the problem.

-   When your user-mode target is a Windows process such as CSRSS or WinLogon. For a detailed description of how to debug these targets, see [Debugging CSRSS](debugging-csrss.md) and [Debugging WinLogon](debugging-winlogon.md).

-   When your user-mode target is a service application. For a detailed description of how to debug these targets, see [Debugging a Service Application](debugging-a-service-application.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20When%20to%20Use%20This%20Technique%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




