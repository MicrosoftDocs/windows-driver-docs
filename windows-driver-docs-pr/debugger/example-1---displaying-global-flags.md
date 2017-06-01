---
title: Example 1 Displaying Global Flags
description: Example 1 Displaying Global Flags
ms.assetid: c1a1eafd-d70a-43f9-af90-33ddc33758fe
---

# Example 1: Displaying Global Flags


## <span id="ddk_example_1___displaying_global_flags_dtools"></span><span id="DDK_EXAMPLE_1___DISPLAYING_GLOBAL_FLAGS_DTOOLS"></span>


The commands demonstrated in this example display the system-wide flags set in the registry, the system flags set for the session (kernel mode), and the flags set for an image file.

The following GFlags command displays the current value of the system-wide flags set in the registry. It uses the **/r** parameter to specify the system-wide registry entry.

```
gflags /r 
```

In response, GFlags displays a single hexadecimal value representing the sum of all flags set and a list of the flags set.

```
Current Boot Registry Settings are: 40001400
    ptg - Enable pool tagging
    ust - Create user mode stack trace database
    bhd - Enable bad handles detection
```

In this example, the results show that there are three tags set, with a combined value of 0x40001400.

-   [Enable pool tagging](enable-pool-tagging.md) (ptg) = 0x400

-   [Create user mode stack trace database](create-user-mode-stack-trace-database.md) (ust) = 0x1000

-   [Enable bad handles detection](enable-bad-handles-detection.md) (bhd) = 0x40000000

The following command displays the flags set for the current session. It uses the **/k** parameter to indicate kernel mode.

```
gflags /k 
```

The following command displays flags set in the registry for the image file notepad.exe. It uses the **/i** parameter to indicate image file mode and specifies the image file.

```
gflags /i notepad.exe 
```

Remember that the flag value displayed might not be the current, effective flag value. Changes to the system-wide flags are not effective until you restart Windows. Changes to image file flag settings are not effective until you restart the program.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Example%201:%20%20Displaying%20Global%20Flags%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




