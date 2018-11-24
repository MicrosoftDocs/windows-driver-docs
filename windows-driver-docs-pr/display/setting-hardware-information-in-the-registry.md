---
title: Setting Hardware Information in the Registry
description: Setting Hardware Information in the Registry
ms.assetid: 82f5d399-58c3-4bed-a3f2-3501f21fa3e8
keywords:
- hardware WDK video miniport
- registry WDK video miniport
- VideoPortSetRegistryParameters
- VideoPortGetRegistryParameters
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting Hardware Information in the Registry


## <span id="ddk_setting_hardware_information_in_the_registry_gg"></span><span id="DDK_SETTING_HARDWARE_INFORMATION_IN_THE_REGISTRY_GG"></span>


[*HwVidFindAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff567332) can call the [**VideoPortGetRegistryParameters**](https://msdn.microsoft.com/library/windows/hardware/ff570316) and [**VideoPortSetRegistryParameters**](https://msdn.microsoft.com/library/windows/hardware/ff570365) functions to get and set configuration information in the registry. For example, *HwVidFindAdapter* might call **VideoPortSetRegistryParameters** to set up nonvolatile configuration information in the registry for the next boot. It might call **VideoPortGetRegistryParameters** to get adapter-specific, bus-relative configuration parameters written into the registry by an installation program.

It is recommended that miniport drivers set certain hardware information in the registry to display useful information to the user and for assistance in debugging. A miniport driver can set a chip type, DAC type, memory size (of the adapter), and a string to identify the adapter. This information is shown by the Display program in Control Panel.

The driver sets this information by calling **VideoPortSetRegistryParameters**. Typically, the driver makes the call in its *HwVidFindAdapter* routine.

The following table describes the information that the driver can register and provides details for the *ValueName* and *ValueData* parameters of **VideoPortSetRegistryParameters**:

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Information for Entry</th>
<th align="left"><em>ValueName</em></th>
<th align="left"><em>ValueData</em></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Chip type</p></td>
<td align="left"><p>HardwareInformation.ChipType</p></td>
<td align="left"><p>Null terminated string containing the chip name.</p></td>
</tr>
<tr class="even">
<td align="left"><p>DAC type</p></td>
<td align="left"><p>HardwareInformation.DacType</p></td>
<td align="left"><p>Null terminated string containing the DAC name or ID.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Memory size</p></td>
<td align="left"><p>HardwareInformation.MemorySize</p></td>
<td align="left"><p>ULONG containing, in MB, the amount of video memory on the adapter.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Adapter ID</p></td>
<td align="left"><p>HardwareInformation.AdapterString</p></td>
<td align="left"><p>Null-terminated string containing the name of the adapter.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>BIOS</p></td>
<td align="left"><p>HardwareInformation.BiosString</p></td>
<td align="left"><p>Null-terminated string containing information about the BIOS.</p></td>
</tr>
</tbody>
</table>

 

 

 





