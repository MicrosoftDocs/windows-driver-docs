---
title: DevCon Classes
description: Lists all device setup classes, including classes that devices on the system do not use. Valid on local and remote computers.
ms.assetid: 05b9339c-30d1-45df-8f43-20a07e520a42
keywords:
- DevCon Classes Driver Development Tools
topic_type:
- apiref
api_name:
- DevCon Classes
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DevCon Classes


Lists all [device setup classes](https://msdn.microsoft.com/library/windows/hardware/ff541509), including classes that devices on the system do not use. Valid on local and remote computers.

```
    devcon [/m:\\computer] classes 
```

## <span id="ddk_devcon_classes_tools"></span><span id="DDK_DEVCON_CLASSES_TOOLS"></span>Parameters


<span id="________m___computer______"></span><span id="________M___COMPUTER______"></span> **/m:\\\\computer**   
Runs the command on the specified remote computer. The backslashes are required.

**Note**   To run DevCon commands on a remote computer, the Group Policy setting must allow the Plug and Play service to run on the remote computer. On computers that run Windows Vista and Windows 7, the Group Policy disables remote access to the service by default. On computers that run WDK 8.1 and WDK 8, the remote access is unavailable.



### <span id="comments"></span><span id="COMMENTS"></span>Comments

The **/m** parameter must precede the operation name (**classes**). Otherwise, DevCon ignores the **/m** parameter and displays the classes on the local computer without returning a syntax error.

In the DevCon display, classes are listed in the order that they appear in the registry (alphanumeric order by GUID).

To find the devices in a setup class, use the [**DevCon ListClass**](devcon-listclass.md) operation. To find the setup class of a particular device, use the [**DevCon Stack**](devcon-stack.md) operation.

### <span id="sample_usage"></span><span id="SAMPLE_USAGE"></span>Sample Usage

```
devcon classes
devcon classes > setupclasses.txt
devcon /m:\\Server01 classes
```

### <span id="examples"></span><span id="EXAMPLES"></span>Examples

[Example 4: List classes on the local computer](devcon-examples.md#ddk_example_4_list_classes_on_the_local_computer_tools)

[Example 5: List classes on the remote computer](devcon-examples.md#ddk_example_5_list_classes_on_the_remote_computer_tools)









