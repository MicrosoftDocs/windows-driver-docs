---
title: Registering a WDM Smart Card Reader Driver
description: Registering a WDM Smart Card Reader Driver
ms.assetid: 0f82c18b-3bbc-4bc6-825a-58e957f4e3aa
keywords:
- smart card drivers WDK , registry
- registry WDK smart card
- WDM device registering WDK smart card
- registering smart card drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registering a WDM Smart Card Reader Driver


## <span id="_ntovr_registering_a_wdm_smart_card_reader_driver"></span><span id="_NTOVR_REGISTERING_A_WDM_SMART_CARD_READER_DRIVER"></span>


To make a smart card reader driver visible to Device Manager, you must put the indicated registry values under the following key:

**HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Services\\**<em>SmartCardDriver</em>

The required values are listed in the following table.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Registry value name</th>
<th align="left">Contents of the registry value</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Start</strong></p></td>
<td align="left"><p><strong>DWORD:0x0000002</strong></p></td>
<td align="left"><p>A value of 2 makes the driver start automatically. During development, use a <strong>Start</strong> value of 3 to make the driver start manually.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Type</strong></p></td>
<td align="left"><p><strong>DWORD:0x0000001</strong></p></td>
<td align="left"><p>A value of 1 identifies the driver as a kernel-mode driver.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Group</strong></p></td>
<td align="left"><p><strong>SmartCardReader</strong></p></td>
<td align="left"><p>Every driver has to be a member of the <strong>SmartCardReader</strong> setup class, because the smart card resource manager waits for this class to start.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>ErrorControl</strong></p></td>
<td align="left"><p><strong>DWORD:0x0000001</strong></p></td>
<td align="left"><p>A value of 1 shows an error message if the driver fails to load, but lets the system continue to start up.</p></td>
</tr>
</tbody>
</table>

 

 

 





