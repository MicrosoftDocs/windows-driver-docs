---
title: Example 3 Setting a Flag by Using Its Hexadecimal Value
description: Example 3 Setting a Flag by Using Its Hexadecimal Value
ms.assetid: 64fa0b2e-9fe7-47d0-bf83-8ae7c06252b6
ms.author: domars
ms.date: 10/12/2018
ms.localizationpriority: medium
---

# Example 3: Setting a Flag by Using Its Hexadecimal Value


## <span id="ddk_example_3___setting_a_flag_by_using_its_hexadecimal_value_dtools"></span><span id="DDK_EXAMPLE_3___SETTING_A_FLAG_BY_USING_ITS_HEXADECIMAL_VALUE_DTOOLS"></span>


The following command sets the system-wide [Enable page heap](enable-page-heap.md) flag. **Enable Page Heap** adds a guard page and other tracking features to each heap allocation.

The command uses the **/r** parameter to indicate system-wide registry mode. To identify the flag, the command uses **2000000**, which represents 0x2000000, the hexadecimal value for **Enable page heap**.

Although the command sets a flag, it omits the plus (+) sign. When using hexadecimal values, the sign is optional and add (+) is the default.

```console
gflags /r 2000000 
```

In response, GFlags displays the system-wide flags set in the registry. The display indicates that the command is successful. The **Enable page heap** feature will be enabled for all processes when Windows restarts.

```console
Current Boot Registry Settings are: 02000000
    hpa - Enable page heap
```

 

 





