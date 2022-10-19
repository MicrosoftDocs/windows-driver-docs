---
title: DevCon Resources
description: Lists the resources allocated to the specified devices. Resources are assignable and addressable bus paths, such as DMA channels, I/O ports, IRQ, and memory addresses. 
keywords:
- DevCon Resources Driver Development Tools
topic_type:
- apiref
api_name:
- DevCon Resources
api_type:
- NA
ms.date: 02/11/2022
---

# DevCon Resources

Lists the resources allocated to the specified devices. Resources are assignable and addressable bus paths, such as DMA channels, I/O ports, IRQ, and memory addresses. 

```
    devcon resources {* | ID [ID ...] | =class [ID [ID...]]}
```

## Recommended Replacement

```
pnputil /enum-devices /resources
```

For more recommended replacements, see [Replacing DevCon](devcon-migration.md).


## <span id="ddk_devcon_resources_tools"></span><span id="DDK_DEVCON_RESOURCES_TOOLS"></span>Parameters

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
<td align="left"><p>Matches the string literally (exactly as it appears). Precede a string with a single quote to indicate that an asterisk is part of the ID name and is not a wildcard character, for example, <strong>'*PNP0600'</strong>, where *PNP0600 (including the asterisk) is the hardware ID.</p></td>
</tr>
</tbody>
</table>  

<span id="________class______"></span><span id="________CLASS______"></span> **=**<em>class</em>
Specifies the device setup class of the devices. The equal sign (**=**) identifies the string as a class name.

You can also specify hardware IDs, compatible IDs, device instance IDs, or ID patterns following the class name. Type a space between each ID or pattern. DevCon finds devices in the class that match the specified IDs.

### <span id="comments"></span><span id="COMMENTS"></span>Comments


### <span id="sample_usage"></span><span id="SAMPLE_USAGE"></span>Sample Usage

```
devcon resources *
devcon resources =media
devcon resources acpi* *port*
devcon resources =class port* (by class and hardware ID)
devcon resources =class @port*(by class and device instance ID)
```

### <span id="examples"></span><span id="EXAMPLES"></span>Examples

[Example 12: List resources of a class of devices](devcon-examples.md#example-12-list-resources-of-a-class-of-devices)

[Example 13: List resources of device by ID](devcon-examples.md#example-13-list-resources-of-device-by-id)
