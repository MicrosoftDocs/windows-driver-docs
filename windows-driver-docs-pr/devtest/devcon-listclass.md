---
title: DevCon ListClass
description: Lists all devices in the specified device setup classes. 
keywords:
- DevCon ListClass Driver Development Tools
topic_type:
- apiref
api_name:
- DevCon ListClass
api_type:
- NA
ms.date: 02/11/2022
---

# DevCon ListClass


Lists all devices in the specified device setup classes. 

```
    devcon listclass class [class...] 
```

## Recommended Replacement

```
pnputil /enum-devices /class <name or GUID>
```

For more recommended replacements, see [Replacing DevCon](devcon-migration.md).

## <span id="ddk_devcon_listclass_tools"></span><span id="DDK_DEVCON_LISTCLASS_TOOLS"></span>Parameters

<span id="_______class______"></span><span id="_______CLASS______"></span> *class*   
Specifies a device setup class. No equal sign (=) is required.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

Each entry in a setup class display represents one device. The entry consists of the unique instance name and a description of the device in *instance* **:** *description* format.

To find the setup class of a particular device, use the [**DevCon Stack**](devcon-stack.md) operation.

### <span id="sample_usage"></span><span id="SAMPLE_USAGE"></span>Sample Usage

```
devcon listclass printers ports
devcon listclass SmartCardReader
```

### <span id="examples"></span><span id="EXAMPLES"></span>Examples

[Example 6: List the devices in a device setup class](devcon-examples.md#example-6-list-the-devices-in-a-device-setup-class)

[Example 7: List the devices in multiple classes](devcon-examples.md#example-7-list-the-devices-in-multiple-classes)









