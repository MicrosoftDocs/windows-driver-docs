---
title: DevCon Remove
description: Removes the device from the device tree and deletes the device stack for the device.
ms.assetid: 02236d0d-4628-4b5b-9a15-331905f07358
keywords:
- DevCon Remove Driver Development Tools
topic_type:
- apiref
api_name:
- DevCon Remove
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DevCon Remove


Removes the device from the device tree and deletes the device stack for the device. As a result of these actions, child devices are removed from the device tree and the drivers that support the device are unloaded.

This operation does not delete the device driver or any files installed for the device. After removing the device from the device tree, the files remain and the device is still represented internally as a nonpresent device that can be reenumerated.

Valid only on the local computer.

```
    devcon [/r] remove {* | ID [ID ...] | =class [ID [ID ...]]} 
```

## <span id="ddk_devcon_remove_tools"></span><span id="DDK_DEVCON_REMOVE_TOOLS"></span>Parameters


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

The system might need to be rebooted to make this change effective. To have DevCon reboot the system, add the conditional reboot parameter (/r) to the command.

### <span id="sample_usage"></span><span id="SAMPLE_USAGE"></span>Sample Usage

```
devcon /r remove "PCI\VEN_8086&DEV_7110" 
devcon /r remove =printer
devcon /r remove =printer *deskj*
```

### <span id="examples"></span><span id="EXAMPLES"></span>Examples

[Example 35: Remove devices by device instance ID pattern](devcon-examples.md#ddk_example_35_remove_devices_by_device_instance_id_pattern_tools)

[Example 36: Remove a particular network device](devcon-examples.md#ddk_example_36_remove_a_particular_network_device_tools)









