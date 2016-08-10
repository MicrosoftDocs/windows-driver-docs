---
title: Smart Card Driver Debugging
description: Smart Card Driver Debugging
ms.assetid: 701528f6-d8ba-4a73-ad68-cb35497a3474
keywords: ["smart card drivers WDK , debugging", "debugging drivers WDK smart card", "DebugLevel", "vendor-supplied drivers WDK smart card , debugging"]
---

# Smart Card Driver Debugging


## <span id="_ntovr_smart_card_driver_debugging"></span><span id="_NTOVR_SMART_CARD_DRIVER_DEBUGGING"></span>


The smart card driver libraries support several debugging features. Each debugging feature is represented by one of the following constants, which are defined in the *Smclib.h* header file:

```
DEBUG_IOCTL
DEBUG_ATR
DEBUG_PROTOCOL
DEBUG_DRIVER
DEBUG_TRACE
DEBUG_ERROR
DEBUG_BREAK
DEBUG_ALL
```

The combined set of enabled debugging features is represented by a value called the *debugging level*. You can calculate this value by taking the bitwise OR of the constants that correspond to the features you want to enable.

There are two ways to set the debugging level. First, you can use the smart card driver test program, *Scdrvtst*, that comes with the Windows Driver Kit (WDK). The second is to use the [**SmartcardSetDebugLevel**](https://msdn.microsoft.com/library/windows/hardware/ff548960) smart card driver library routine.

In both cases, you must pass the value for the debugging level you want to the program or routine that sets the debugging level. For instance, to set the debugging level from the driver by using a smart card library routine, make the following call:

```
SmartcardSetDebugLevel(DebugLevel);
```

**Important**   You must install the checked version of the operating system and the checked version of the driver to get debugging messages.

 

To write debugging messages from a reader driver, the driver must call the following routine:

```
SmartcardDebug(
 ULONG DebugLevel,
 PCHAR Message
);
```

This routine can also be used to write messages to a remote debugger in the following ways.

-   To write error messages, use the DEBUG\_ERROR constant for the *DebugLevel*.

-   To write standard driver messages, use the DEBUG\_DRIVER constant.

-   To write trace messages that indicate when the reader driver enters or exits a routine, use DEBUG\_TRACE as the *DebugLevel*.

While developing a driver, use the checked version of the smart card driver library and set the debugging level to the maximum by using **SmartcardSetDebugLevel**(DEBUG\_ALL) in your *DriverEntry* routine.

For information about setting up a remote debugging session, see [Windows Debugging](https://msdn.microsoft.com/library/windows/hardware/ff551063).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[smartcrd\smartcrd]:%20Smart%20Card%20Driver%20Debugging%20%20RELEASE:%20%287/20/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




