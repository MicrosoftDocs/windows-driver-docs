---
title: DevCon Reboot
description: Stops and then starts the operating system. Valid only on the local computer.
ms.assetid: 4e27c35c-8b98-4edc-98d7-8ba0f96d7a78
keywords: ["DevCon Reboot Driver Development Tools"]
topic_type:
- apiref
api_name:
- DevCon Reboot
api_type:
- NA
---

# DevCon Reboot


Stops and then starts the operating system. Valid only on the local computer.

``` syntax
    devcon reboot 

   
```

## <span id="ddk_devcon_reboot_tools"></span><span id="DDK_DEVCON_REBOOT_TOOLS"></span>


### <span id="comments"></span><span id="COMMENTS"></span>Comments

Unlike the **/r** parameter, which reboots the system only if required to make a change effective, the **DevCon Reboot** operation reboots the system without determining whether a reboot is required.

DevCon uses the standard **ExitWindowsEx** function to reboot. If the user has open files on the computer or a program will not close, the system does not reboot until the user has responded to system prompts to close the files or end the process. For more information about **ExitWindowsEx**, see the Microsoft Windows SDK.

### <span id="sample_usage"></span><span id="SAMPLE_USAGE"></span>Sample Usage

```
devcon reboot
```

### <span id="example"></span><span id="EXAMPLE"></span>Example

[Example 39: Reboot the local computer](devcon-examples.md#ddk_example_39_reboot_the_local_computer_tools)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20DevCon%20Reboot%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




