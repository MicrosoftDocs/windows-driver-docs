---
title: Registering a WDM Smart Card Reader Driver
description: Registering a WDM Smart Card Reader Driver
ms.assetid: 0f82c18b-3bbc-4bc6-825a-58e957f4e3aa
keywords:
- smart card drivers WDK , registry
- registry WDK smart card
- WDM device registering WDK smart card
- registering smart card drivers
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Registering a WDM Smart Card Reader Driver


## <span id="_ntovr_registering_a_wdm_smart_card_reader_driver"></span><span id="_NTOVR_REGISTERING_A_WDM_SMART_CARD_READER_DRIVER"></span>


To make a smart card reader driver visible to Device Manager, you must put the indicated registry values under the following key:

**HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Services\\***SmartCardDriver*

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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[smartcrd\smartcrd]:%20Registering%20a%20WDM%20Smart%20Card%20Reader%20Driver%20%20RELEASE:%20%287/20/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




