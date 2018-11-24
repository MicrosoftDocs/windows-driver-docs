---
title: DevCon HwIDs
description: Displays the hardware IDs, compatible IDs, and device instance IDs of the specified devices. Valid on local and remote computers.
ms.assetid: b76de01e-fedf-41c2-ba2e-837b442ab93f
keywords:
- DevCon HwIDs Driver Development Tools
topic_type:
- apiref
api_name:
- DevCon HwIDs
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DevCon HwIDs


Displays the hardware IDs, compatible IDs, and device instance IDs of the specified devices. Valid on local and remote computers.

```
    devcon [/m:\\computer] hwids {* | ID [ID ...] | =class [ID [ID ...]]} 
```

## <span id="ddk_devcon_hwids_tools"></span><span id="DDK_DEVCON_HWIDS_TOOLS"></span>Parameters


<span id="________m___computer______"></span><span id="________M___COMPUTER______"></span> **/m:\\\\**<em>computer</em>   
Runs the command on the specified remote computer. The backslashes are required.

**Note**   To run DevCon commands on a remote computer, the Group Policy setting must allow the Plug and Play service to run on the remote computer. On computers that run Windows Vista and Windows 7, the Group Policy disables remote access to the service by default. On computers that run WDK 8.1 and WDK 8, the remote access is unavailable.



<span id="______________"></span> **\\***   
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
<td align="left"><p><strong>&#39;</strong></p>
<p>(single quote)</p></td>
<td align="left"><p>Matches the string literally (exactly as it appears). Precede a string with a single quote to indicate that an asterisk is part of the ID name and is not a wildcard character, for example, <strong>&#39;*PNP0600</strong>, where *PNP0600 (including the asterisk) is the hardware ID.</p></td>
</tr>
</tbody>
</table>



<span id="________class______"></span><span id="________CLASS______"></span> **=**<em>class</em>   
Specifies one or more devices by using a setup class.

Type all or part of the name of the setup class of the devices. The equal sign (**=**) identifies the string as a class name.

You can also specify hardware IDs, compatible IDs, device instance IDs, or ID patterns following the class name. Type a space between each ID or pattern. DevCon finds devices in the class that match the specified IDs.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The **/m** parameter must precede the operation name (**hwids**). Otherwise, DevCon ignores the **/m** parameter and displays the hardware IDs of devices on the local computer without returning a syntax error.

To create a hardware ID for a root-enumerated device, use the [**DevCon SetHwID**](devcon-sethwid.md) command.

### <span id="sample_usage"></span><span id="SAMPLE_USAGE"></span>Sample Usage

```
devcon hwids *
devcon /m:\\server01 hwids acpi* 
devcon hwids acpi* *port*
devcon hwids =usb
```

### <span id="examples"></span><span id="EXAMPLES"></span>Examples

[Example 1: Find all hardware IDs](devcon-examples.md#ddk_example_1_find_all_hardware_ids_tools)

[Example 2: Find hardware IDs by using a pattern](devcon-examples.md#ddk_example_2_find_hardware_ids_by_using_a_pattern_tools)

[Example 3: Find hardware IDs by using a class](devcon-examples.md#ddk_example_3_find_hardware_ids_by_using_a_class_tools)









