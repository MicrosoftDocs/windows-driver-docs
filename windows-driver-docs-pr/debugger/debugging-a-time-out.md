---
title: Debugging a Time Out
description: Debugging a Time Out
ms.assetid: 795774da-10fb-4431-908d-94c3baa01132
keywords: ["time outs"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Debugging a Time Out


## <span id="ddk_debugging_time_outs_dbg"></span><span id="DDK_DEBUGGING_TIME_OUTS_DBG"></span>


There are two main time outs that occur on Windows systems:

[Resource Time Outs](resource-time-outs.md) (kernel mode)

[Critical Section Time Outs](critical-section-time-outs.md) (user mode)

In many cases, these problems are simply a matter of a thread taking too long to release a resource or exit a section of code.

On a retail system, the time-out value is set high enough that you would not see the break (a true deadlock would simply hang). The time-out values are set in the registry under **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control\\SessionManager**. The integer values specify the number of seconds in each time out.

 

 





