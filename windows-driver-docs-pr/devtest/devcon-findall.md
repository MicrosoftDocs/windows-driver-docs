---
title: DevCon FindAll
description: Finds all devices on the computer, including devices that were once attached to the computer but have been detached or moved.
keywords:
- DevCon FindAll Driver Development Tools
topic_type:
- apiref
api_name:
- DevCon FindAll
api_type:
- NA
ms.date: 02/11/2022
---

# DevCon FindAll

Finds all devices on the computer, including devices that were once attached to the computer but have been detached or moved. (These are known as nonpresent devices or *phantom* devices.) The **DevCon FindAll** operation also finds devices that are enumerated differently as a result of a BIOS change. 

```
    devcon findall {* | ID [ID ...] | =class [ID [ID ...]]}
```

## <span id="ddk_devcon_findall_tools"></span><span id="DDK_DEVCON_FINDALL_TOOLS"></span>Parameters

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
Specifies the device setup class of the devices. The equal sign (**=**) identifies the string as a class name.

You can also specify hardware IDs, compatible IDs, device instance IDs, or ID patterns following the class name. Type a space between each ID or pattern. DevCon finds devices in the class that match the specified IDs.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

To find only devices that are currently attached to the computer, use the [**DevCon Find**](devcon-find.md) operation.

### <span id="sample_usage"></span><span id="SAMPLE_USAGE"></span>Sample Usage

```
devcon resources STORAGE\Volume
devcon resources =ports lpt*
devcon resources @pci*
```

### <span id="example"></span><span id="EXAMPLE"></span>Example

[Example 22: Find (and find all) devices in a setup class](devcon-examples.md#ddk_example_22_find_and_find_all_devices_in_a_setup_class_tools)
