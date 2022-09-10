---
title: DevCon Classes
description: Lists all device setup classes, including classes that devices on the system do not use. 
keywords:
- DevCon Classes Driver Development Tools
topic_type:
- apiref
api_name:
- DevCon Classes
api_type:
- NA
ms.date: 04/20/2017
---

# DevCon Classes


Lists all [device setup classes](../install/overview-of-device-setup-classes.md), including classes that devices on the system do not use. 

```
    devcon classes 
```

## <span id="ddk_devcon_classes_tools"></span><span id="DDK_DEVCON_CLASSES_TOOLS"></span>Parameters


### <span id="comments"></span><span id="COMMENTS"></span>Comments

In the DevCon display, classes are listed in the order that they appear in the registry (alphanumeric order by GUID).

To find the devices in a setup class, use the [**DevCon ListClass**](devcon-listclass.md) operation. To find the setup class of a particular device, use the [**DevCon Stack**](devcon-stack.md) operation.

### <span id="sample_usage"></span><span id="SAMPLE_USAGE"></span>Sample Usage

```
devcon classes
devcon classes > setupclasses.txt
```

### <span id="examples"></span><span id="EXAMPLES"></span>Examples

[Example 4: List classes on the local computer](devcon-examples.md#example-4-list-classes-on-the-local-computer)
