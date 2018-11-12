---
title: Example 5 Clearing a Flag
description: Example 5 Clearing a Flag
ms.assetid: 63c8bae9-ae6e-4d82-9389-ec36554635ab
ms.author: domars
ms.date: 10/12/2018
ms.localizationpriority: medium
---

# Example 5: Clearing a Flag


## <span id="ddk_example_5___clearing_a_flag_dtools"></span><span id="DDK_EXAMPLE_5___CLEARING_A_FLAG_DTOOLS"></span>


The following command clears the system-wide [Enable page heap](enable-page-heap.md) flag set in the registry. The command uses the **/r** parameter to indicate the system-wide registry mode and **hpa**, the abbreviation for the **Enable page heap** flag. The minus sign (-) indicates that the flag is to be cleared.

```console
gflags /r -hpa 
```

In response, GFlags displays the current value of the system-wide registry entry. The display indicates that the command is successful and that there are no longer any flags set.

```console
Current Boot Registry Settings are: 00000000 
```

Note that the following command, which uses the hexadecimal value of the **Enable Page Heap** flag, has the same effect as the command used in this example. These commands can be used interchangeably:

```console
gflags /r -02000000 
```

 

 





