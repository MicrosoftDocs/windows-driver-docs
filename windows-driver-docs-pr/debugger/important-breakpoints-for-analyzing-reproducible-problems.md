---
title: Important Breakpoints for Analyzing Reproducible Problems
description: Important Breakpoints for Analyzing Reproducible Problems
ms.assetid: 3f501bbe-990a-4f46-ba88-c1fc4b73537f
keywords: ["SCSI Miniport Debugging, breakpoints and reproducible problems"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Important Breakpoints for Analyzing Reproducible Problems


## <span id="ddk_device_manager_problem_codes_dbg"></span><span id="DDK_DEVICE_MANAGER_PROBLEM_CODES_DBG"></span>


When debugging a SCSI miniport driver, there are three routines in which it is useful to set a breakpoint:

-   **scsiport!scsiportnotification**

-   **scsiport!spstartiosynchronized**

-   **miniport!HwStartIo**

The routine **scsiport!scsiportnotification** is called right after a request is sent to the miniport. Thus, if you set a breakpoint in **scsiport!scsiportnotification** and then run a stack backtrace using [**kb 3**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md), you can determine whether the miniport is receiving and completing requests. If the first parameter is zero, the request has been completed. If the first parameter is nonzero, the third parameter is the address of the SCSI request block (SRB) that is not being completed, and you can use the [**!minipkd.srb**](-minipkd-srb.md) extension to further analyze the situation.

Placing a breakpoint in either **scsiport!spstartiosynchronized** or **miniport!HwStartIo** will cause a break just prior to sending a request to the miniport.

 

 





