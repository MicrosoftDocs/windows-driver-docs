---
title: Example 6 Clearing All Flags
description: Example 6 Clearing All Flags
ms.assetid: 07a6af3d-3ef7-429d-9afa-439b20915ab1
ms.author: domars
ms.date: 10/12/2018
ms.localizationpriority: medium
---

# Example 6: Clearing All Flags


## <span id="ddk_example_6___clearing_all_flags_dtools"></span><span id="DDK_EXAMPLE_6___CLEARING_ALL_FLAGS_DTOOLS"></span>


This example demonstrates two different ways to clear all flags set in the registry and for the session:

-   Subtract the current flag value.

-   Subtract high values.

**Note**   The methods demonstrated by this example clear flags only. They do not reset the maximum stack trace size or kernel special pool tag to the default values.

 

### <span id="Subtract_the_Current_Flag_Value"></span><span id="subtract_the_current_flag_value"></span><span id="SUBTRACT_THE_CURRENT_FLAG_VALUE"></span>Subtract the Current Flag Value

The following command clears all flags set in the system-wide flag entry in the registry by subtracting the current value of the entry. In this example, the current value is 0xE0. The command uses the **/r** parameter to indicate the system-wide registry mode and the E0 value with a minus sign (-) to subtract E0 from the flag value.

```console
gflags /r -E0 
```

In response, GFlags displays the revised value of system-wide flag registry entry. A value of zero indicates that the command is successful and that there are no longer any system-wide flags set in the registry.

```console
Current Boot Registry Settings are: 00000000 
```

Note that the following commands have the same effect as the command used in this example and can be used interchangeably:

```console
gflags /r -20 -40 -80 
gflags /r -hfc -hpc -hvc 
```

### <span id="Subtract_High_Values"></span><span id="subtract_high_values"></span><span id="SUBTRACT_HIGH_VALUES"></span>Subtract High Values

The following command clears all system-wide flags by subtracting high values (0xFFFFFFFF) from the system-wide flag setting.

```console
gflags /r -ffffffff 
```

In response, GFlags displays the revised value of the system-wide flag entry. A value of zero indicates that the command is successful and that there are no longer any system-wide flags set in the registry.

```console
Current Boot Registry Settings are: 00000000 
```

**Tip**   Type this command into Notepad, then save the file as clearflag.bat. Thereafter, to clear all flags, just type **ClearFlag**.

 

Finally, the following example demonstrates that the intuitive method of clearing all flags does not work.

The following command appears to set the value of the system-wide flag entry to 0. However, it actually adds zero to the system-wide flag value. In this example, the current value of the system-wide flag entry is 0xE0.

```console
gflags /r 0 
```

In response, GFlags displays the system-wide flag value after the command completes:

```console
Current Boot Registry Settings are: 000000e0
    hfc - Enable heap free checking
    hpc - Enable heap parameter checking
    hvc - Enable heap validation on call
```

The command has no effect because it adds the value 0 to system-wide flag entry.

 

 





