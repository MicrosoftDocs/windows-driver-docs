---
title: Retrieving the Status and Problem Code for a Device Instance
description: Retrieving the Status and Problem Code for a Device Instance
ms.date: 04/05/2022
---

# Retrieving the Status and Problem Code for a Device Instance

In Windows Vista and later versions of Windows, the [unified device property model](unified-device-property-model--windows-vista-and-later-.md) includes a [device status property](devpkey-device-devnodestatus.md) and a [problem code property](devpkey-device-problemcode.md). The unified device property model uses [property keys](property-keys.md) to represent these properties.

Windows Server 2003, Windows XP, and Windows 2000 do not support the property keys of the unified property model, nor do they support corresponding registry entry values that represent these properties. However, the corresponding information can be retrieved by calling the [**CM_Get_DevNode_Status**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_status) function. To maintain compatibility with earlier versions of Windows, Windows Vista and later versions also support **CM_Get_DevNode_Status**. However, you should use the property keys of the unified device property model to access the device properties.

Additionally, in Windows 8 and later versions of Windows, there is also a [problem status property](devpkey-device-problemstatus.md).  This property contains a [NTSTATUS](../kernel/using-ntstatus-values.md) value that may contain additional information relating to a problem code set on the device.  If the problem status value is STATUS_SUCCESS, then no additional information relating to the problem code was available when the problem code was set on the device.

For information about how to use property keys to access device driver properties in Windows Vista and later versions, see [Accessing Device Instance Properties (Windows Vista and Later)](accessing-device-instance-properties--windows-vista-and-later-.md).

To access the status and problem code for a device instance on Windows Server 2003, Windows XP, and Windows 2000, call **CM_Get_DevNode_Status** and supply the following parameters:

-   Set *pulStatus* to a pointer to a ULONG-typed value that receives the status bit flags that are set for a device instance. The status value can be any combination of the bit flags with prefix "DN_" that are defined in *Cfg.h*.

-   Set *pulProblemNumber* to a pointer to a ULONG-typed value that receives the problem number that is set for a device instance. The problem number is one of the constants with the prefix "CM_PROB_" that are defined in *Cfg.h*. **CM_Get_DevNode_Status** sets the problem number only if DN_HAS_PROBLEM is set in *pulStatus*.

-   Set *dnDevInst* to a device instance handle to the device for which to retrieve the status and problem code.

-   Set *ulFlags* to zero.

If the call to **CM_Get_DevNode_Status** succeeds, **CM_Get_DevNode_Status** retrieves the requested status and problem code for the device instance and returns CR_SUCCESS. If the function call fails, **CM_Get_DevNode_Status** returns one of the error codes with prefix "CR_" that are defined in *Cfgmgr32.h*.

## Using Device Manager to find problem code and problem status for a device

When there is a problem with a device, Device Manager will overlay the icon for the device in the tree view with a yellow triangle with an exclamation mark in it.  By right clicking on the device and choosing Properties, a dialog will appear with more information about the device. The problem code appears on the **General** tab, in the **Device status** field.

The [**Problem status**](devpkey-device-problemstatus.md) property appears in the **Property** dropdown on the **Details** tab for the device in Device Manager.

## Using the debugger to find problem code and problem status for a device

To view all devices that have a problem code in the kernel debugger, use the [**!devnode 0 21**](../debuggercmds/-devnode.md) extension. This also shows you the ProblemStatus on the device. For example:

```
0: kd> !devnode 0 21
Dumping IopRootDeviceNode (= 0x85d37e30)
DevNode 0x8ad6ab78 for PDO 0x81635c30
  InstancePath is "ROOT\DIINSTALLDRIVER\0003"
  ServiceName is "isolated"
  State = DeviceNodeRemoved (0x312)
  Previous State = DeviceNodeInitialized (0x302)
  Problem = CM_PROB_FAILED_ADD
  Problem Status = 0xc00000bb
```

You can also view problem code and problem status by issuing [**!devnode**](../debuggercmds/-devnode.md) on a DEVICE_NODE address:

```
0: kd> !devnode 0x8ad6ab78 
DevNode 0x8ad6ab78 for PDO 0x81635c30
  Parent 0x85d37e30   Sibling 0x8adee670   Child 0000000000   
  ...
  Problem = CM_PROB_FAILED_ADD
  Problem Status = 0xc00000bb
```

## See Also
 
* [**DEVPKEY_Device_DevNodeStatus**](devpkey-device-devnodestatus.md)
* [**DEVPKEY_Device_ProblemCode**](devpkey-device-problemcode.md)
* [**DEVPKEY_Device_ProblemStatus**](devpkey-device-problemstatus.md)
