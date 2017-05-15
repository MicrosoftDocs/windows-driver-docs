---
title: Important Breakpoints for Analyzing Reproducible Problems
description: Important Breakpoints for Analyzing Reproducible Problems
ms.assetid: 3f501bbe-990a-4f46-ba88-c1fc4b73537f
keywords: ["SCSI Miniport Debugging, breakpoints and reproducible problems"]
---

# Important Breakpoints for Analyzing Reproducible Problems


## <span id="ddk_device_manager_problem_codes_dbg"></span><span id="DDK_DEVICE_MANAGER_PROBLEM_CODES_DBG"></span>


When debugging a SCSI miniport driver, there are three routines in which it is useful to set a breakpoint:

-   **scsiport!scsiportnotification**

-   **scsiport!spstartiosynchronized**

-   **miniport!HwStartIo**

The routine **scsiport!scsiportnotification** is called right after a request is sent to the miniport. Thus, if you set a breakpoint in **scsiport!scsiportnotification** and then run a stack backtrace using [**kb 3**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md), you can determine whether the miniport is receiving and completing requests. If the first parameter is zero, the request has been completed. If the first parameter is nonzero, the third parameter is the address of the SCSI request block (SRB) that is not being completed, and you can use the [**!minipkd.srb**](-minipkd-srb.md) extension to further analyze the situation.

Placing a breakpoint in either **scsiport!spstartiosynchronized** or **miniport!HwStartIo** will cause a break just prior to sending a request to the miniport.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Important%20Breakpoints%20for%20Analyzing%20Reproducible%20Problems%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




