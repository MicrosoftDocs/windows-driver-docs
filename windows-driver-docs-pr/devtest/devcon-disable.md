---
title: DevCon Disable
description: Disables devices on the computer.
ms.assetid: 544b219c-30dd-41d1-ac47-9760c772b07e
keywords:
- DevCon Disable Driver Development Tools
topic_type:
- apiref
api_name:
- DevCon Disable
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DevCon Disable


Disables devices on the computer. Valid only on the local computer.

To *disable* a device means that the device remains physically connected to the computer, but its driver is unloaded from memory and its resources are freed so that the device cannot be used.

```
    devcon [/r] disable {* | ID [ID ...] | =class [ID [ID ...]]} 
```

## <span id="ddk_devcon_disable_tools"></span><span id="DDK_DEVCON_DISABLE_TOOLS"></span>Parameters


<span id="________r______"></span><span id="________R______"></span> **/r**   
Conditional reboot. Reboots the system after completing an operation only if a reboot is required to make a change effective.

<span id="______________"></span> **\\***   
Represents all devices on the computer.

<span id="_______ID______"></span><span id="_______id______"></span> *ID*   
Specifies all or part of a hardware ID, compatible ID, or device instance ID of a device. When specifying multiple IDs, type a space between each ID. IDs that include an ampersand character (**&**) must be enclosed in quotation marks.

The following special characters modify the ID parameter.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Character</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong><em></strong></p></td>
<td align="left"><p>Matches any character or no character. Use the wildcard character (</em>) to create an ID pattern, for example, <em>disk</em>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>@</strong></p></td>
<td align="left"><p>Indicates a device instance ID, for example, <strong><xref href="ROOT\FTDISK\0000" data-throw-if-not-resolved="False" data-raw-source="@ROOT\FTDISK\0000"></xref></strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>&#39;</strong></p>
<p>(single quote)</p></td>
<td align="left"><p>Matches the string literally (exactly as it appears). Precede a string with a single quote to indicate that an asterisk is part of the ID name and is not a wildcard character, for example, <strong>&#39;*PNP0600</strong>, where *PNP0600 (including the asterisk) is the hardware ID.</p></td>
</tr>
</tbody>
</table>



<span id="________class______"></span><span id="________CLASS______"></span> **=**<em>class</em>   
Specifies the device setup class of the devices. The equal sign (**=**) identifies the string as a class name.

You can also specify hardware IDs, compatible IDs, device instance IDs, or ID patterns following the class name. Type a space between each ID or pattern. DevCon finds devices in the class that match the specified IDs.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

DevCon disables the device even if the device is already disabled. Before and after disabling a device, use the [**DevCon Status**](devcon-status.md) operation to verify the device status.

Before using an ID pattern to disable a device, determine which devices will be affected. To do so, use the pattern in a display command, such as **devcon status USB\\*** or **devcon hwids USB\\***.

The system might need to be rebooted to make this change effective. To have DevCon reboot the system, add the conditional reboot parameter (/r) to the command.

### <span id="sample_usage"></span><span id="SAMPLE_USAGE"></span>Sample Usage

```
devcon disable * (not recommended)
devcon /r disable *DVD-ROM*
devcon /r disable =printer
```

### <span id="examples"></span><span id="EXAMPLES"></span>Examples

[Example 30: Disable devices by an ID pattern](devcon-examples.md#ddk_example_30_disable_devices_by_an_id_pattern_tools)

[Example 31: Disable devices by device instance ID](devcon-examples.md#ddk_example_31_disable_devices_by_device_instance_id_tools)









