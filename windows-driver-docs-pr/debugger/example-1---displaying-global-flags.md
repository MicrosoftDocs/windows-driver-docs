---
title: Example 1 Displaying Global Flags
description: Example 1 Displaying Global Flags
ms.assetid: c1a1eafd-d70a-43f9-af90-33ddc33758fe
ms.author: domars
ms.date: 10/12/2018
ms.localizationpriority: medium
---

# Example 1: Displaying Global Flags


## <span id="ddk_example_1___displaying_global_flags_dtools"></span><span id="DDK_EXAMPLE_1___DISPLAYING_GLOBAL_FLAGS_DTOOLS"></span>


The commands demonstrated in this example display the system-wide flags set in the registry, the system flags set for the session (kernel mode), and the flags set for an image file.

The following GFlags command displays the current value of the system-wide flags set in the registry. It uses the **/r** parameter to specify the system-wide registry entry.

```console
gflags /r 
```

In response, GFlags displays a single hexadecimal value representing the sum of all flags set and a list of the flags set.

```console
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

```console
gflags /k 
```

The following command displays flags set in the registry for the image file notepad.exe. It uses the **/i** parameter to indicate image file mode and specifies the image file.

```console
gflags /i notepad.exe 
```

Remember that the flag value displayed might not be the current, effective flag value. Changes to the system-wide flags are not effective until you restart Windows. Changes to image file flag settings are not effective until you restart the program.

 

 





