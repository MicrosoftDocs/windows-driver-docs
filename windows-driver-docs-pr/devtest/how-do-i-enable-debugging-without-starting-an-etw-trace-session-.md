---
title: How do I enable debugging without starting an ETW trace session
description: How do I enable debugging without starting an ETW trace session
ms.assetid: d0487973-c66a-4ede-bc94-2e7e2060ab54
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20How%20do%20I%20enable%20debugging%20without%20starting%20an%20ETW%20trace%20session?%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




