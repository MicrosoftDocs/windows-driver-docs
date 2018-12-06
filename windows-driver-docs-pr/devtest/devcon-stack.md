---
title: DevCon Stack
description: Displays the expected driver stack for the specified devices, and the GUID and the name of the device setup class for each device.
ms.assetid: c06436d2-da66-4eb2-89ed-a1832967cdbb
keywords:
- DevCon Stack Driver Development Tools
topic_type:
- apiref
api_name:
- DevCon Stack
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DevCon Stack


Displays the expected driver stack for the specified devices, and the GUID and the name of the device setup class for each device. Valid on local and remote computers.

```
    devcon [/m:\\computer] stack {* | ID [ID ...] | =class [ID [ID...]]} 
```

## <span id="ddk_devcon_stack_tools"></span><span id="DDK_DEVCON_STACK_TOOLS"></span>Parameters


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
Specifies the device setup class of the devices. The equal sign (**=**) identifies the string as a class name. You can also specify hardware IDs, compatible IDs, device instance IDs, or ID patterns following the class name. Type a space between each ID or pattern. DevCon finds devices in the class that match the specified IDs.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The **/m** parameter must precede the operation name (**stack**). Otherwise, DevCon ignores the **/m** parameter and displays the stack of device drivers on the local computer without returning a syntax error.

The **DevCon Stack** operation displays the expected driver stack for a device. Although the actual driver stack typically matches the expected stack, variations are possible.

To investigate a device problem, compare the expected driver stack from the stack operation with the actual drivers that the device uses, as displayed by the [**DevCon DriverFiles**](devcon-driverfiles.md) operation.

### <span id="sample_usage"></span><span id="SAMPLE_USAGE"></span>Sample Usage

```
devcon /m:\\Server01 stack * > Server01Stack.txt
devcon stack ISAPNP\ReadDataPort
devcon /m:\\Server01 stack pci* 
devcon stack =multifunction
```

### <span id="examples"></span><span id="EXAMPLES"></span>Examples

[Example 14: Display the driver stack for storage devices](devcon-examples.md#ddk_example_14_display_the_driver_stack_for_storage_devices_tools)

[Example 15: Find the setup class of a device](devcon-examples.md#ddk_example_15_find_the_setup_class_of_a_device_tools)

[Example 16: Display the stack for related devices on a remote computer](devcon-examples.md#ddk_example_16_display_the_stack_for_related_devices_on_a_remote_compu)









