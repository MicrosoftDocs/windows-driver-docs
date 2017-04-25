---
title: Example 2 Setting a Flag by Using a Flag Abbreviation
description: Example 2 Setting a Flag by Using a Flag Abbreviation
ms.assetid: 3c011ca5-8901-4bf2-b95d-364d644cb476
---

# Example 2: Setting a Flag by Using a Flag Abbreviation


## <span id="ddk_example_2___setting_a_flag_by_using_a_flag_abbreviation_dtools"></span><span id="DDK_EXAMPLE_2___SETTING_A_FLAG_BY_USING_A_FLAG_ABBREVIATION_DTOOLS"></span>


The following command sets the [Show loader snaps](show-loader-snaps.md) flag for the notepad.exe image file. **Show Loader Snaps** takes snapshots of the load process, capturing in detail the loading and unloading of executable images and their supporting library modules.

The command uses the **/i** parameter to indicate image file mode and specifies the name of the image file notepad.exe. To identify the flag, the command uses **sls**, the abbreviation for **Show Loader Snaps**, and it precedes the abbreviation with a plus sign (+) to indicate that the flag is set. Without the plus sign, the command has no effect.

```
gflags /i notepad.exe +sls 
```

In response, GFlags displays the flags set for notepad.exe. The display indicates that the command is successful. The **Show Loader Snaps** feature is enabled for all new sessions of the Notepad program.

```
Current Registry Settings for notepad.exe executable are: 00000002
    sls - Show Loader Snaps
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Example%202:%20%20Setting%20a%20Flag%20by%20Using%20a%20Flag%20Abbreviation%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




