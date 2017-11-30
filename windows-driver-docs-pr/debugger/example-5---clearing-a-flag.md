---
title: Example 5 Clearing a Flag
description: Example 5 Clearing a Flag
ms.assetid: 63c8bae9-ae6e-4d82-9389-ec36554635ab
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Example 5: Clearing a Flag


## <span id="ddk_example_5___clearing_a_flag_dtools"></span><span id="DDK_EXAMPLE_5___CLEARING_A_FLAG_DTOOLS"></span>


The following command clears the system-wide [Enable page heap](enable-page-heap.md) flag set in the registry. The command uses the **/r** parameter to indicate the system-wide registry mode and **hpa**, the abbreviation for the **Enable page heap** flag. The minus sign (-) indicates that the flag is to be cleared.

```
gflags /r -hpa 
```

In response, GFlags displays the current value of the system-wide registry entry. The display indicates that the command is successful and that there are no longer any flags set.

```
Current Boot Registry Settings are: 00000000 
```

Note that the following command, which uses the hexadecimal value of the **Enable Page Heap** flag, has the same effect as the command used in this example. These commands can be used interchangeably:

```
gflags /r -02000000 
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Example%205:%20%20Clearing%20a%20Flag%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




