---
title: DevCon Reboot
description: Stops and then starts the operating system. Valid only on the local computer.
ms.assetid: 4e27c35c-8b98-4edc-98d7-8ba0f96d7a78
keywords:
- DevCon Reboot Driver Development Tools
topic_type:
- apiref
api_name:
- DevCon Reboot
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DevCon Reboot


Stops and then starts the operating system. Valid only on the local computer.

```
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









