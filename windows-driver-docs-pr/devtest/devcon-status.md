---
title: DevCon Status
description: Displays the status (running, stopped, or disabled) of the driver for devices on the computer. 
keywords:
- DevCon Status Driver Development Tools
topic_type:
- apiref
api_name:
- DevCon Status
api_type:
- NA
ms.date: 02/11/2022
---

# DevCon Status

[!NOTE] [PnPUtil](pnputil.md) ships with every release of Windows and makes use of the most reliable and secure APIs available. It's use is recommended instead of DevCon. See the [Recommended Replacement](#recommended-replacement) below and [Replacing DevCon](devcon-migration.md) for more information.

Displays the status (running, stopped, or disabled) of the driver for devices on the computer. 

```
    devcon status {* | ID [ID ...] | =class [ID [ID ...]]}
```

## <span id="ddk_devcon_status_tools"></span><span id="DDK_DEVCON_STATUS_TOOLS"></span>Parameters

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

<span id="________class______"></span><span id="________CLASS______"></span>  
**=**_class_
Specifies the device setup class of the devices. The equal sign (**=**) identifies the string as a class name.

You can also specify hardware IDs, compatible IDs, device instance IDs, or ID patterns following the class name. Type a space between each ID or pattern. DevCon finds devices in the class that match the specified IDs.

## Recommended Replacement

```
pnputil /enum-devices
```

For more recommended replacements, see [Replacing DevCon](devcon-migration.md).

## <span id="comments"></span><span id="COMMENTS"></span>Comments

If DevCon cannot determine the status of the device, such as when the device is no longer attached to the computer, DevCon omits the line describing the status from the status display.

The following example shows a successful status command. The text describing the device status appears in bold type.

```
STORAGE\VOLUME\1&30A96598&0&SIGNATURE80OFFSET7E0000LENGTH270987600
    Name: Generic volume
    Driver is running.
1 matching device(s) found.
```

In contrast, the following example shows how DevCon displays the status of a device that it cannot find. The status description is missing from the display.

```
STORAGE\VOLUME\1&30A96598&0&SIGNATURE80OFFSET7E0000LENGTH270987600
    Name: Generic volume
1 matching device(s) found.
```

## <span id="sample_usage"></span><span id="SAMPLE_USAGE"></span>Sample Usage

```
devcon status *
devcon status pci*
devcon status "PCI\VEN_115D&DEV_0003&SUBSYS_0181115D"
devcon status =printer
```

## <span id="examples"></span><span id="EXAMPLES"></span>Examples

[Example 17: Display the status of all devices on the local computer](devcon-examples.md#example-17-display-the-status-of-all-devices)

[Example 18: Display the status of a device by device instance ID](devcon-examples.md#example-18-display-the-status-of-a-device-by-device-instance-id)

[Example 19: Display the status of related devices](devcon-examples.md#example-19-display-the-status-of-related-devices)
