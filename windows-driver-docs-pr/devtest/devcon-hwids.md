---
title: DevCon HwIDs
description: Displays the hardware IDs, compatible IDs, and device instance IDs of the specified devices. 
keywords:
- DevCon HwIDs Driver Development Tools
topic_type:
- apiref
api_name:
- DevCon HwIDs
api_type:
- NA
ms.date: 02/11/2022
---

# DevCon HwIDs

Displays the hardware IDs, compatible IDs, and device instance IDs of the specified devices. 

```
    devcon hwids {* | ID [ID ...] | =class [ID [ID ...]]}
```

## Recommended Replacement

```
pnputil /enum-devices /deviceids
```

For more recommended replacements, see [Replacing DevCon](devcon-migration.md).

## <span id="ddk_devcon_hwids_tools"></span><span id="DDK_DEVCON_HWIDS_TOOLS"></span>Parameters

<span id="______________"></span> **\***
Represents all devices on the computer.

<span id="_______ID______"></span><span id="_______id______"></span> *ID*
Specifies one or more devices by using an identifier.

Type all or part of a hardware ID, compatible ID, or device instance ID of a device. When specifying multiple IDs, type a space between each ID. IDs that include an ampersand character (**&**) must be enclosed in quotation marks.

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
<td align="left"><p>Matches any character or no character. Use the wildcard character (<strong></em></strong>) to create an ID pattern, for example, <strong><em>disk</em></strong>.</p></td>
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
Specifies one or more devices by using a setup class.

Type all or part of the name of the setup class of the devices. The equal sign (**=**) identifies the string as a class name.

You can also specify hardware IDs, compatible IDs, device instance IDs, or ID patterns following the class name. Type a space between each ID or pattern. DevCon finds devices in the class that match the specified IDs.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

To create a hardware ID for a root-enumerated device, use the [**DevCon SetHwID**](devcon-sethwid.md) command.

### <span id="sample_usage"></span><span id="SAMPLE_USAGE"></span>Sample Usage

```
devcon hwids *
devcon hwids acpi* *port*
devcon hwids =usb
```

### <span id="examples"></span><span id="EXAMPLES"></span>Examples

[Example 1: Find all hardware IDs](devcon-examples.md#example-1-find-all-hardware-ids)

[Example 2: Find hardware IDs by using a pattern](devcon-examples.md#example-2-find-hardware-ids-by-using-a-pattern)

[Example 3: Find hardware IDs by using a class](devcon-examples.md#example-3-find-hardware-ids-by-using-a-class)
