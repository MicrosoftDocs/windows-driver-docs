---
title: DevCon Enable
description: Enables devices on the computer. Valid only on the local computer.To enable a device means that the device driver is loaded into memory and the device is ready for use.
ms.assetid: 2fb2cb9b-ba37-4946-b78b-0cd2aaaadcb4
keywords:
- DevCon Enable Driver Development Tools
topic_type:
- apiref
api_name:
- DevCon Enable
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DevCon Enable


Enables devices on the computer. Valid only on the local computer.

To *enable* a device means that the device driver is loaded into memory and the device is ready for use.

```
    devcon [/r] enable {* | ID [ID ...] | =class [ID [ID ...]]} 
```

## <span id="ddk_devcon_enable_tools"></span><span id="DDK_DEVCON_ENABLE_TOOLS"></span>Parameters


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



<span id="________class______"></span><span id="________CLASS______"></span> *=class*   
Specifies the device setup class of the devices. The equal sign (**=**) identifies the string as a class name.

You can also specify hardware IDs, compatible IDs, device instance IDs, or ID patterns following the class name. Type a space between each ID or pattern. DevCon finds devices in the class that match the specified IDs.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

DevCon enables the device even if it is already enabled. Before and after enabling a device, use the [**DevCon Status**](devcon-status.md) operation to verify the device status.

The system might need to be rebooted to make this change effective. To have DevCon reboot the system, add the conditional reboot parameter (/r) to the command.

### <span id="sample_usage"></span><span id="SAMPLE_USAGE"></span>Sample Usage

```
devcon enable * (not recommended)
devcon /r enable *DVD-ROM* 
devcon /r enable =printer
```

### <span id="examples"></span><span id="EXAMPLES"></span>Examples

[Example 28: Enable a particular device](devcon-examples.md#ddk_example_28_enable_a_particular_device_tools)

[Example 29: Enable devices by class](devcon-examples.md#ddk_example_29_enable_devices_by_class_tools)









