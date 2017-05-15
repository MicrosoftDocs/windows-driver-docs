---
title: Debugging a Time Out
description: Debugging a Time Out
ms.assetid: 795774da-10fb-4431-908d-94c3baa01132
keywords: ["time outs"]
---

# Debugging a Time Out


## <span id="ddk_debugging_time_outs_dbg"></span><span id="DDK_DEBUGGING_TIME_OUTS_DBG"></span>


There are two main time outs that occur on Windows systems:

[Resource Time Outs](resource-time-outs.md) (kernel mode)

[Critical Section Time Outs](critical-section-time-outs.md) (user mode)

In many cases, these problems are simply a matter of a thread taking too long to release a resource or exit a section of code.

On a retail system, the time-out value is set high enough that you would not see the break (a true deadlock would simply hang). The time-out values are set in the registry under **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control\\SessionManager**. The integer values specify the number of seconds in each time out.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20a%20Time%20Out%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




