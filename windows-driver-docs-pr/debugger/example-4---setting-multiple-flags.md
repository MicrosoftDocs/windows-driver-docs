---
title: Example 4 Setting Multiple Flags
description: Example 4 Setting Multiple Flags
ms.assetid: b8c7301b-4a34-4f03-8c5e-ba43a1fb3681
ms.author: domars
ms.date: 10/12/2018
ms.localizationpriority: medium
---

# Example 4: Setting Multiple Flags


## <span id="ddk_example_4___setting_multiple_flags_dtools"></span><span id="DDK_EXAMPLE_4___SETTING_MULTIPLE_FLAGS_DTOOLS"></span>


The following command sets these three flags for the current session:

-   [Enable heap free checking](enable-heap-free-checking.md) (hfc, 0x20)

-   [Enable heap parameter checking](enable-heap-parameter-checking.md) (hpc, 0x40)

-   [Enable heap validation on call](enable-heap-validation-on-call.md) (hvc, 0x80)

This command uses the **/k** parameter to specify kernel mode (session only). It sets the value for kernel mode to **E0** (0xE0), the sum of the hexadecimal values of the selected flags (0x20 + 0x40 + 0x80).

```console
gflags /k e0 
```

In response, GFlags displays the revised value of flags set for the session. The display indicates that the command is successful and that the three flags specified in the command are set.

```console
Current Running Kernel Settings are: 000000e0
    hfc - Enable heap free checking
    hpc - Enable heap parameter checking
    hvc - Enable heap validation on call
```

You can use several different GFlags commands to set flags. Each of the following commands has the same effect as the command used in this example and the methods can be used interchangeably:

```console
gflags /k +20 +40 +80 
gflags /k +E0 
gflags /k +hfc +hpc +hvc 
```

Kernel (run time) flags are effective immediately and remain effective until Windows shuts down.

 

 





