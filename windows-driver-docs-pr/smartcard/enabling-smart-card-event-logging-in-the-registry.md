---
title: Enabling Smart Card Event Logging in the Registry
description: Enabling Smart Card Event Logging in the Registry
ms.assetid: b07ff2d7-9025-424e-a57e-eb37ae4091f4
keywords:
- smart card drivers WDK , registry
- registry WDK smart card
- logs WDK smart card
- events WDK smart card
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Enabling Smart Card Event Logging in the Registry


## <span id="_ntovr_enabling_smart_card_event_logging_in_the_registry"></span><span id="_NTOVR_ENABLING_SMART_CARD_EVENT_LOGGING_IN_THE_REGISTRY"></span>


Smart card reader drivers should log errors in the system event log so that the system administrators can use the log to help diagnose why a driver fails.

To enable event logging, you must add several values to the registry under the following key:

**HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Services\\EventLog\\System\\** *SmartCardDriver*

The registry values that enable event logging are listed in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Registry value name</th>
<th align="left">Contents of the registry value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>EventMessageFile</strong></p></td>
<td align="left"><p><em>%SystemRoot%\System32\Drivers\SmartCardDriver.sys</em></p>
<div class="alert">
<strong>Important</strong>   The file name extension must be included in the <strong>EventMessageFile</strong> value name, but it must never appear in any other part of the registry path.
</div>
<div>
 
</div></td>
</tr>
<tr class="even">
<td align="left"><p><strong>TypesSupported</strong></p></td>
<td align="left"><p><strong>DWORD:0x00000007</strong></p></td>
</tr>
</tbody>
</table>

 

For more information about specifying these registry entries, see [**INF AddService Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546326).

 

 





