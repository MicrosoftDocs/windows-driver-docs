---
title: Specifying Priority Boosts When Completing I/O Requests
description: Specifying Priority Boosts When Completing I/O Requests
ms.assetid: 9a501ca1-58c9-4458-b202-9581f8ce5e5f
keywords:
- request processing WDK KMDF , priority boosts
- priority boosts WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Specifying Priority Boosts When Completing I/O Requests


When a driver completes an I/O request, it can call [**WdfRequestCompleteWithPriorityBoost**](https://msdn.microsoft.com/library/windows/hardware/ff549949) to specify a value that the system uses to boost the run-time priority of the thread that requested the I/O operation.

If the driver calls [**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945) or [**WdfRequestCompleteWithInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549948) instead of [**WdfRequestCompleteWithPriorityBoost**](https://msdn.microsoft.com/library/windows/hardware/ff549949), the framework uses a default priority boost value that is based on the device type. The following table lists the default priority boost values that the framework uses. The device type and priority boost constants are defined in *Wdm.h*.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Device Type</th>
<th align="left">Default Priority Boost</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>FILE_DEVICE_UNDEFINED</p></td>
<td align="left"><p>IO_NO_INCREMENT</p></td>
</tr>
<tr class="even">
<td align="left"><p>FILE_DEVICE_BEEP</p></td>
<td align="left"><p>IO_NO_INCREMENT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FILE_DEVICE_CD_ROM</p></td>
<td align="left"><p>IO_CD_ROM_INCREMENT</p></td>
</tr>
<tr class="even">
<td align="left"><p>FILE_DEVICE_CD_ROM_FILE_SYSTEM</p></td>
<td align="left"><p>IO_CD_ROM_INCREMENT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FILE_DEVICE_CONTROLLER</p></td>
<td align="left"><p>IO_NO_INCREMENT</p></td>
</tr>
<tr class="even">
<td align="left"><p>FILE_DEVICE_DATALINK</p></td>
<td align="left"><p>IO_NO_INCREMENT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FILE_DEVICE_DFS</p></td>
<td align="left"><p>IO_NO_INCREMENT</p></td>
</tr>
<tr class="even">
<td align="left"><p>FILE_DEVICE_DISK</p></td>
<td align="left"><p>IO_DISK_INCREMENT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FILE_DEVICE_DISK_FILE_SYSTEM</p></td>
<td align="left"><p>IO_DISK_INCREMENT</p></td>
</tr>
<tr class="even">
<td align="left"><p>FILE_DEVICE_FILE_SYSTEM</p></td>
<td align="left"><p>IO_NO_INCREMENT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FILE_DEVICE_INPORT_PORT</p></td>
<td align="left"><p>IO_NO_INCREMENT</p></td>
</tr>
<tr class="even">
<td align="left"><p>FILE_DEVICE_KEYBOARD</p></td>
<td align="left"><p>IO_KEYBOARD_INCREMENT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FILE_DEVICE_MAILSLOT</p></td>
<td align="left"><p>IO_MAILSLOT_INCREMENT</p></td>
</tr>
<tr class="even">
<td align="left"><p>FILE_DEVICE_MIDI_IN</p></td>
<td align="left"><p>IO_SOUND_INCREMENT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FILE_DEVICE_MIDI_OUT</p></td>
<td align="left"><p>IO_SOUND_INCREMENT</p></td>
</tr>
<tr class="even">
<td align="left"><p>FILE_DEVICE_MOUSE</p></td>
<td align="left"><p>IO_MOUSE_INCREMENT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FILE_DEVICE_MULTI_UNC_PROVIDER</p></td>
<td align="left"><p>IO_NO_INCREMENT</p></td>
</tr>
<tr class="even">
<td align="left"><p>FILE_DEVICE_NAMED_PIPE</p></td>
<td align="left"><p>IO_NAMED_PIPE_INCREMENT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FILE_DEVICE_NETWORK</p></td>
<td align="left"><p>IO_NETWORK_INCREMENT</p></td>
</tr>
<tr class="even">
<td align="left"><p>FILE_DEVICE_NETWORK_BROWSER</p></td>
<td align="left"><p>IO_NETWORK_INCREMENT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FILE_DEVICE_NETWORK_FILE_SYSTEM</p></td>
<td align="left"><p>IO_NETWORK_INCREMENT</p></td>
</tr>
<tr class="even">
<td align="left"><p>FILE_DEVICE_NULL</p></td>
<td align="left"><p>IO_NO_INCREMENT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FILE_DEVICE_PARALLEL_PORT</p></td>
<td align="left"><p>IO_PARALLEL_INCREMENT</p></td>
</tr>
<tr class="even">
<td align="left"><p>FILE_DEVICE_PHYSICAL_NETCARD</p></td>
<td align="left"><p>IO_NETWORK_INCREMENT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FILE_DEVICE_PRINTER</p></td>
<td align="left"><p>IO_NO_INCREMENT</p></td>
</tr>
<tr class="even">
<td align="left"><p>FILE_DEVICE_SCANNER</p></td>
<td align="left"><p>IO_NO_INCREMENT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FILE_DEVICE_SERIAL_MOUSE_PORT</p></td>
<td align="left"><p>IO_SERIAL_INCREMENT</p></td>
</tr>
<tr class="even">
<td align="left"><p>FILE_DEVICE_SERIAL_PORT</p></td>
<td align="left"><p>IO_SERIAL_INCREMENT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FILE_DEVICE_SCREEN</p></td>
<td align="left"><p>IO_VIDEO_INCREMENT</p></td>
</tr>
<tr class="even">
<td align="left"><p>FILE_DEVICE_SOUND</p></td>
<td align="left"><p>IO_SOUND_INCREMENT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FILE_DEVICE_STREAMS</p></td>
<td align="left"><p>IO_SOUND_INCREMENT</p></td>
</tr>
<tr class="even">
<td align="left"><p>FILE_DEVICE_TAPE</p></td>
<td align="left"><p>IO_NO_INCREMENT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FILE_DEVICE_TAPE_FILE_SYSTEM</p></td>
<td align="left"><p>IO_NO_INCREMENT</p></td>
</tr>
<tr class="even">
<td align="left"><p>FILE_DEVICE_TRANSPORT</p></td>
<td align="left"><p>IO_NO_INCREMENT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FILE_DEVICE_UNKNOWN</p></td>
<td align="left"><p>IO_NO_INCREMENT</p></td>
</tr>
<tr class="even">
<td align="left"><p>FILE_DEVICE_VIDEO</p></td>
<td align="left"><p>IO_VIDEO_INCREMENT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FILE_DEVICE_VIRTUAL_DISK</p></td>
<td align="left"><p>IO_DISK_INCREMENT</p></td>
</tr>
<tr class="even">
<td align="left"><p>FILE_DEVICE_WAVE_IN</p></td>
<td align="left"><p>IO_SOUND_INCREMENT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FILE_DEVICE_WAVE_OUT</p></td>
<td align="left"><p>IO_SOUND_INCREMENT</p></td>
</tr>
<tr class="even">
<td align="left"><p>FILE_DEVICE_8042_PORT</p></td>
<td align="left"><p>IO_KEYBOARD_INCREMENT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FILE_DEVICE_NETWORK_REDIRECTOR</p></td>
<td align="left"><p>IO_NETWORK_INCREMENT</p></td>
</tr>
<tr class="even">
<td align="left"><p>FILE_DEVICE_BATTERY</p></td>
<td align="left"><p>IO_NO_INCREMENT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FILE_DEVICE_BUS_EXTENDER</p></td>
<td align="left"><p>IO_NO_INCREMENT</p></td>
</tr>
<tr class="even">
<td align="left"><p>FILE_DEVICE_MODEM</p></td>
<td align="left"><p>IO_SERIAL_INCREMENT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FILE_DEVICE_VDM</p></td>
<td align="left"><p>IO_NO_INCREMENT</p></td>
</tr>
<tr class="even">
<td align="left"><p>FILE_DEVICE_MASS_STORAGE</p></td>
<td align="left"><p>IO_DISK_INCREMENT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FILE_DEVICE_SMB</p></td>
<td align="left"><p>IO_NETWORK_INCREMENT</p></td>
</tr>
<tr class="even">
<td align="left"><p>FILE_DEVICE_KS</p></td>
<td align="left"><p>IO_SOUND_INCREMENT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FILE_DEVICE_CHANGER</p></td>
<td align="left"><p>IO_NO_INCREMENT</p></td>
</tr>
<tr class="even">
<td align="left"><p>FILE_DEVICE_SMARTCARD</p></td>
<td align="left"><p>IO_NO_INCREMENT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FILE_DEVICE_ACPI</p></td>
<td align="left"><p>IO_NO_INCREMENT</p></td>
</tr>
<tr class="even">
<td align="left"><p>FILE_DEVICE_DVD</p></td>
<td align="left"><p>IO_NO_INCREMENT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FILE_DEVICE_FULLSCREEN_VIDEO</p></td>
<td align="left"><p>IO_VIDEO_INCREMENT</p></td>
</tr>
<tr class="even">
<td align="left"><p>FILE_DEVICE_DFS_FILE_SYSTEM</p></td>
<td align="left"><p>IO_NO_INCREMENT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FILE_DEVICE_DFS_VOLUME</p></td>
<td align="left"><p>IO_NO_INCREMENT</p></td>
</tr>
<tr class="even">
<td align="left"><p>FILE_DEVICE_SERENUM</p></td>
<td align="left"><p>IO_SERIAL_INCREMENT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FILE_DEVICE_TERMSRV</p></td>
<td align="left"><p>IO_NO_INCREMENT</p></td>
</tr>
<tr class="even">
<td align="left"><p>FILE_DEVICE_KSEC</p></td>
<td align="left"><p>IO_NO_INCREMENT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FILE_DEVICE_FIPS</p></td>
<td align="left"><p>IO_NO_INCREMENT</p></td>
</tr>
<tr class="even">
<td align="left"><p>FILE_DEVICE_INFINIBAND</p></td>
<td align="left"><p>IO_NO_INCREMENT</p></td>
</tr>
</tbody>
</table>

 

 

 





