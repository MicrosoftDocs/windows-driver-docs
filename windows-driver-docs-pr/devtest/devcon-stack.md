---
title: DevCon Stack
description: Displays the expected driver stack for the specified devices, and the GUID and the name of the device setup class for each device.
keywords:
- DevCon Stack Driver Development Tools
topic_type:
- apiref
api_name:
- DevCon Stack
api_type:
- NA
ms.date: 02/11/2022
---

# DevCon Stack

Displays the expected driver stack for the specified devices, and the GUID and the name of the device setup class for each device. 

```
    devcon stack {* | ID [ID ...] | =class [ID [ID...]]}
```

## <span id="ddk_devcon_stack_tools"></span><span id="DDK_DEVCON_STACK_TOOLS"></span>Parameters

<span id="______________"></span> **\***
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
<td align="left"><p><strong>'</strong></p>
<p>(single quote)</p></td>
<td align="left"><p>Matches the string literally (exactly as it appears). Precede a string with a single quote to indicate that an asterisk is part of the ID name and is not a wildcard character, for example, <strong>'*PNP0600</strong>, where *PNP0600 (including the asterisk) is the hardware ID.</p></td>
</tr>
</tbody>
</table>  

<span id="________class______"></span><span id="________CLASS______"></span> **=**<em>class</em>
Specifies the device setup class of the devices. The equal sign (**=**) identifies the string as a class name. You can also specify hardware IDs, compatible IDs, device instance IDs, or ID patterns following the class name. Type a space between each ID or pattern. DevCon finds devices in the class that match the specified IDs.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The **DevCon Stack** operation displays the expected driver stack for a device. Although the actual driver stack typically matches the expected stack, variations are possible.

To investigate a device problem, compare the expected driver stack from the stack operation with the actual drivers that the device uses, as displayed by the [**DevCon DriverFiles**](devcon-driverfiles.md) operation.

### <span id="sample_usage"></span><span id="SAMPLE_USAGE"></span>Sample Usage

```
devcon stack pci*
devcon stack * > Stack.txt
devcon stack ISAPNP\ReadDataPort
devcon stack =multifunction
```

### <span id="examples"></span><span id="EXAMPLES"></span>Examples

[Example 14: Display the driver stack for storage devices](devcon-examples.md#example-14-display-the-driver-stack-for-storage-devices)

[Example 15: Find the setup class of a device](devcon-examples.md#example-15-find-the-setup-class-of-a-device)

[Example 16: Display the stack for related devices](devcon-examples.md#example-16-display-the-stack-for-related-devices)
