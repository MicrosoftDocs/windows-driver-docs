---
title: Enabling Smart Card Event Logging in the Registry
description: Enabling Smart Card Event Logging in the Registry
ms.assetid: b07ff2d7-9025-424e-a57e-eb37ae4091f4
keywords:
- smart card drivers WDK , registry
- registry WDK smart card
- logs WDK smart card
- events WDK smart card
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[smartcrd\smartcrd]:%20Enabling%20Smart%20Card%20Event%20Logging%20in%20the%20Registry%20%20RELEASE:%20%287/20/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




