---
title: DevCon DriverNodes
description: Lists all driver packages that are compatible with the device, along with their version and ranking. Valid only on the local computer.
ms.assetid: 891aa022-44f5-4920-ab57-a0573deb94de
keywords:
- DevCon DriverNodes Driver Development Tools
topic_type:
- apiref
api_name:
- DevCon DriverNodes
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DevCon DriverNodes


Lists all [driver packages](https://msdn.microsoft.com/library/windows/hardware/ff539954) that are compatible with the device, along with their version and ranking. Valid only on the local computer.

```
    devcon drivernodes {* | ID [ID ...] | =class [ID [ID ...]]} 
```

## <span id="ddk_devcon_drivernodes_tools"></span><span id="DDK_DEVCON_DRIVERNODES_TOOLS"></span>Parameters


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
<td align="left"><p>Matches any character or no character. Use the wildcard character (<strong></em></strong>) to create an ID pattern, for example, <strong><em>disk</em></strong>.</p></td>
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

The **DevCon DriverNodes** operation runs only on the local computer.

The **DevCon DriverNodes** operation is particularly useful for troubleshooting setup problems. For example, you can use it to determine whether a Windows INF file or a customized third-party INF file was used for a device.

### <span id="sample_usage"></span><span id="SAMPLE_USAGE"></span>Sample Usage

```
devcon drivernodes *
devcon drivernodes *miniport*
devcon drivernodes =usb pci* usb*
```

### <span id="examples"></span><span id="EXAMPLES"></span>Examples

[Example 10: List driver packages by hardware ID pattern](devcon-examples.md#ddk_example_10_list_driver_packages_by_hardware_id_pattern_tools)

[Example 11: List driver packages by device instance ID pattern](devcon-examples.md#ddk_example_11_list_driver_packages_by_device_instance_id_pattern_tool)









