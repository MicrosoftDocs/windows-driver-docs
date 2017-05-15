---
title: Example 3 Setting a Flag by Using Its Hexadecimal Value
description: Example 3 Setting a Flag by Using Its Hexadecimal Value
ms.assetid: 64fa0b2e-9fe7-47d0-bf83-8ae7c06252b6
---

# Example 3: Setting a Flag by Using Its Hexadecimal Value


## <span id="ddk_example_3___setting_a_flag_by_using_its_hexadecimal_value_dtools"></span><span id="DDK_EXAMPLE_3___SETTING_A_FLAG_BY_USING_ITS_HEXADECIMAL_VALUE_DTOOLS"></span>


The following command sets the system-wide [Enable page heap](enable-page-heap.md) flag. **Enable Page Heap** adds a guard page and other tracking features to each heap allocation.

The command uses the **/r** parameter to indicate system-wide registry mode. To identify the flag, the command uses **2000000**, which represents 0x2000000, the hexadecimal value for **Enable page heap**.

Although the command sets a flag, it omits the plus (+) sign. When using hexadecimal values, the sign is optional and add (+) is the default.

```
gflags /r 2000000 
```

In response, GFlags displays the system-wide flags set in the registry. The display indicates that the command is successful. The **Enable page heap** feature will be enabled for all processes when Windows restarts.

```
Current Boot Registry Settings are: 02000000
    hpa - Enable page heap
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Example%203:%20%20Setting%20a%20Flag%20by%20Using%20Its%20Hexadecimal%20Value%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




