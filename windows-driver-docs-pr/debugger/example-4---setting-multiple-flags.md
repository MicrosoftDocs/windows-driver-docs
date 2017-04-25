---
title: Example 4 Setting Multiple Flags
description: Example 4 Setting Multiple Flags
ms.assetid: b8c7301b-4a34-4f03-8c5e-ba43a1fb3681
---

# Example 4: Setting Multiple Flags


## <span id="ddk_example_4___setting_multiple_flags_dtools"></span><span id="DDK_EXAMPLE_4___SETTING_MULTIPLE_FLAGS_DTOOLS"></span>


The following command sets these three flags for the current session:

-   [Enable heap free checking](enable-heap-free-checking.md) (hfc, 0x20)

-   [Enable heap parameter checking](enable-heap-parameter-checking.md) (hpc, 0x40)

-   [Enable heap validation on call](enable-heap-validation-on-call.md) (hvc, 0x80)

This command uses the **/k** parameter to specify kernel mode (session only). It sets the value for kernel mode to **E0** (0xE0), the sum of the hexadecimal values of the selected flags (0x20 + 0x40 + 0x80).

```
gflags /k e0 
```

In response, GFlags displays the revised value of flags set for the session. The display indicates that the command is successful and that the three flags specified in the command are set.

```
Current Running Kernel Settings are: 000000e0
    hfc - Enable heap free checking
    hpc - Enable heap parameter checking
    hvc - Enable heap validation on call
```

You can use several different GFlags commands to set flags. Each of the following commands has the same effect as the command used in this example and the methods can be used interchangeably:

```
gflags /k +20 +40 +80 
gflags /k +E0 
gflags /k +hfc +hpc +hvc 
```

Kernel (run time) flags are effective immediately and remain effective until Windows shuts down.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Example%204:%20%20Setting%20Multiple%20Flags%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




