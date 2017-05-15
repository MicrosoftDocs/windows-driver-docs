---
title: Example 7 Clearing All Flags for an Image File
description: Example 7 Clearing All Flags for an Image File
ms.assetid: 832c79de-07ca-4212-b3b3-ace396986ebb
---

# Example 7: Clearing All Flags for an Image File


## <span id="ddk_example_7___clearing_all_flags_for_an_image_file_dtools"></span><span id="DDK_EXAMPLE_7___CLEARING_ALL_FLAGS_FOR_AN_IMAGE_FILE_DTOOLS"></span>


The following command clears all flags and image debugger options for an image file. The command adds high-values (0xFFFFFFFF) to the current flag value. GFlags responds by deleting the **GlobalFlag** registry entry for the image file, thereby deleting all of the values it stores.

This command does not affect flags set in the system-wide **GlobalFlag** registry entry or flags set for the session (kernel mode).

```
gflags /i notepad.exe ffffffff 
```

In response, GFlags displays a message indicating that there are no flags set for the image file:

```
No Registry Settings for notepad.exe executable 
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Example%207:%20%20Clearing%20All%20Flags%20for%20an%20Image%20File%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




