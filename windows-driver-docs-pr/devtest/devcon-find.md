---
title: DevCon Find
description: Finds all devices that are currently attached to the computer. Displays the device instance ID and device description. Valid on local and remote computers.
ms.assetid: ecd72b34-4117-4360-95d2-e87702f025a1
keywords:
- DevCon Find Driver Development Tools
topic_type:
- apiref
api_name:
- DevCon Find
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DevCon Find


Finds all devices that are currently attached to the computer. Displays the device instance ID and device description. Valid on local and remote computers.

```
    devcon [/m:\\computer] find {* | ID [ID ...] | =class [ID [ID ...]]} 
```

## <span id="ddk_devcon_find_tools"></span><span id="DDK_DEVCON_FIND_TOOLS"></span>Parameters


<span id="________m___computer______"></span><span id="________M___COMPUTER______"></span> **/m:\\\\**<em>computer</em>   
Runs the command on the specified remote computer. The backslashes are required.

**Note**   To run DevCon commands on a remote computer, the Group Policy setting must allow the Plug and Play service to run on the remote computer. On computers that run Windows Vista and Windows 7, the Group Policy disables remote access to the service by default. On computers that run WDK 8.1 and WDK 8, the remote access is unavailable.



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

The **/m** parameter must precede the operation name (**find**). Otherwise, DevCon ignores the **/m** parameter and searches the local computer without returning a syntax error.

You can use the **DevCon Find** operation to find devices that are not currently attached to the computer by specifying the full device instance ID of the device instead of a hardware ID or ID pattern. Specifying the full device instance ID overrides the restriction on the **DevCon Find** operation that limits it to attached devices.

The **DevCon Find** operation with a single class argument is the same as the [**DevCon ListClass**](devcon-listclass.md) operation.

To find all devices, including those that are not currently attached to the computer, use the [**DevCon FindAll**](devcon-findall.md) operation.

### <span id="sample_usage"></span><span id="SAMPLE_USAGE"></span>Sample Usage

```
devcon find *
devcon find =media *pnp*
devcon /m:\\Server01 find *mou* 
devcon find @*hub*
```

### <span id="examples"></span><span id="EXAMPLES"></span>Examples

[Example 20: Find devices by hardware ID pattern](devcon-examples.md#ddk_example_20_find_devices_by_hardware_id_pattern_tools)

[Example 21: Find devices by device instance ID or class](devcon-examples.md#ddk_example_21_find_devices_by_device_instance_id_or_class_tools)









