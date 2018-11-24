---
title: How do I enable debugging without starting an ETW trace session
description: How do I enable debugging without starting an ETW trace session
ms.assetid: d0487973-c66a-4ede-bc94-2e7e2060ab54
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How do I enable debugging without starting an ETW trace session?


To debug problems without starting an ETW trace session, add a **WPP\_DEBUG** macro definition to your source code.

Here is an example for the WDK Tracedrv.sys sample driver:

```
#define WPP_DEBUG(b) DbgPrint b, DbgPrint("\n")
```

Most formats and arguments can be used with **WPP\_DEBUG**. However, you cannot use extended format specifications such as %!HEXDUMP!% with this macro.

See also [How do I send trace messages to a user-mode debugger?](how-do-i-send-trace-messages-to-a-user-mode-debugger-.md).

### <span id="when_using_the_kernel_debugger"></span><span id="WHEN_USING_THE_KERNEL_DEBUGGER"></span>When Using the Kernel Debugger

If you are using the kernel debugger, set the level and flag values for the WPP control structure.

1.  Locate the address of the WPP control structure as follows:
    ```
     kd>   x tracedrv!WPP_MAIN_CB    // tracedrv is the WPP instrumented driver
    9fbf3040 tracedrv!WPP_MAIN_CB = union WPP_PROJECT_CONTROL_BLOCK [1]
    kd>dt WPP_TRACE_CONTROL_BLOCK 9fbf3040  
    +0x000 Callback : 0x9fbf127c tracedrv!WppTraceCallback+0
    +0x004 ControlGuid : 0x9fbf206c _GUID {d58c126f-b309-11d1-969e-0000f875a5bc}
    +0x008 Next : (null) 
    +0x010 Logger : 0
    +0x018 RegistryPath : (null) 
    +0x01c FlagsLen : 0x1 &#39;&#39;
    +0x01d Level : 0x0 &#39;&#39;    <--- Set the Level
    +0x01e Reserved : 0
    +0x020 Flags : [1] 0x0  <--- Set the Flag
    ```

2.  Set the value for the level to **5** and for the flags to **0xf**, as follows:
    ```
    kd>eb 9fbf305d 5    // setting the level value to 5
    ```

    ```
    kd>ed 9fbf3060 0xf    // setting the flag value to 0xf
    ```

3.  (Windows Vista and later versions of Windows) Enable the filter mask to receive the messages as follows:
    ```
    kd>ed nt!Kd_DEFAULT_Mask 0xff
    ```

 

 





