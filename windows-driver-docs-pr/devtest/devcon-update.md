---
title: DevCon Update
description: Forcibly replaces the current device drivers for a specified device with drivers listed in the specified INF file. Valid only on the local computer.
ms.assetid: c07d7abe-31d8-4a8d-87da-8db649710c15
keywords:
- DevCon Update Driver Development Tools
topic_type:
- apiref
api_name:
- DevCon Update
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DevCon Update


Forcibly replaces the current device drivers for a specified device with drivers listed in the specified INF file. Valid only on the local computer.

```
    devcon [/r] update INFfile HardwareID 
```

## <span id="ddk_devcon_update_tools"></span><span id="DDK_DEVCON_UPDATE_TOOLS"></span>Parameters


<span id="________r______"></span><span id="________R______"></span> **/r**   
Conditional reboot. Reboots the system after completing an operation only if a reboot is required to make a change effective.

<span id="_______INFfile______"></span><span id="_______inffile______"></span><span id="_______INFFILE______"></span> *INFfile*   
Specifies the full path and file name of the INF (information) file used in the update. If you omit the path, DevCon assumes that the file is in the current directory.

<span id="_______HardwareID______"></span><span id="_______hardwareid______"></span><span id="_______HARDWAREID______"></span> *HardwareID*   
Updates the drivers for devices with the specified hardware ID. The hardware ID specified in this command must exactly match the hardware ID of the device. Patterns are not valid. Do not type a single quote character (**'**) to indicate a literal value.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The **DevCon Update** operation forces an update to the most appropriate drivers in the specified INF file, even if those drivers are older or less appropriate than the current drivers or the drivers in a different INF file. For more information, see [How Setup Selects Drivers](https://msdn.microsoft.com/library/windows/hardware/ff546228).

You cannot use a **DevCon Update** command to update drivers for nonpresent devices.

Before updating the driver for any device, determine which devices will be affected by the update command. To do so, use the hardware ID in a display command, such as [**DevCon HwIDs**](devcon-hwids.md) or [**DevCon DriverFiles**](devcon-driverfiles.md). This is especially important in a **DevCon Update** operation because DevCon does not list the device drivers that it updates.

DevCon prompts the user if the INF file specifies an unsigned driver or if it cannot find a required file, such as a driver file on removable media. To suppress prompts that require a response, use the noninteractive update operation, [**DevCon UpdateNI**](devcon-updateni.md).

The system might need to be rebooted to make this change effective. To have DevCon reboot the system, add the conditional reboot parameter (/r) to the command.

### <span id="sample_usage"></span><span id="SAMPLE_USAGE"></span>Sample Usage

```
devcon update c:\windows\inf\newdvc.inf ISAPNP\CSC4324\0
devcon /r update c:\windows\inf\newdvc.inf *PNP030b
```

### <span id="example"></span><span id="EXAMPLE"></span>Example

[Example 32: Update the driver for communication ports](devcon-examples.md#ddk_example_32_update_the_driver_for_communication_ports_tools)

[Example 44: Forcibly update the HAL](devcon-examples.md#ddk_example_44_forcibly_update_the_hal_tools)









