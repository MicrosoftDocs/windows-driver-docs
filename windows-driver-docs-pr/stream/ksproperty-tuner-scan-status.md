---
title: KSPROPERTY\_TUNER\_SCAN\_STATUS
description: The KSPROPERTY\_TUNER\_SCAN\_STATUS property describes the status of a scanning operation. This property can be implemented optionally.
ms.assetid: ce7dd30b-84fc-46e2-847c-33c07e60e0f7
keywords: ["KSPROPERTY_TUNER_SCAN_STATUS Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_TUNER_SCAN_STATUS
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_TUNER\_SCAN\_STATUS


The KSPROPERTY\_TUNER\_SCAN\_STATUS property describes the status of a scanning operation. This property can be implemented optionally.

### Usage Summary Table

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Get</th>
<th>Set</th>
<th>Target</th>
<th>Property descriptor type</th>
<th>Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Yes</p></td>
<td><p>No</p></td>
<td><p>Pin</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565898" data-raw-source="[&lt;strong&gt;KSPROPERTY_TUNER_SCAN_STATUS_S&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565898)"><strong>KSPROPERTY_TUNER_SCAN_STATUS_S</strong></a></p></td>
<td><p>KSPROPERTY_TUNER_SCAN_STATUS_S</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a KSPROPERTY\_TUNER\_SCAN\_STATUS\_S structure that specifies the status of a scanning operation.

Remarks
-------

The *KsTvTune.ax* module can call the driver's KSPROPERTY\_TUNER\_SCAN\_STATUS property at any time. However, *KsTvTune.ax* typically calls KSPROPERTY\_TUNER\_SCAN\_STATUS after it calls the [**KSEVENT\_TUNER\_INITIATE\_SCAN**](ksevent-tuner-initiate-scan.md) event to set up a scan operation and to set up notification for when the scan completes. *KsTvTune.ax* then waits for the scan-completion notification to occur. As the worst case scenario, *KsTvTune.ax* waits for the amount of time that is specified in the **SettlingTime** member of the [**TUNER\_ANALOG\_CAPS\_S**](https://msdn.microsoft.com/library/windows/hardware/ff568547) structure. The driver should have returned a populated TUNER\_ANALOG\_CAPS\_S from a call to its [**KSPROPERTY\_TUNER\_NETWORKTYPE\_SCAN\_CAPS**](ksproperty-tuner-networktype-scan-caps.md) property with the ANALOG\_TV\_NETWORK\_TYPE value set in the **NetworkType** member of the [**KSPROPERTY\_TUNER\_NETWORKTYPE\_SCAN\_CAPS\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565885) structure. However, the tuner should typically determine the status of the signal quicker than the amount of time that is specified in **SettlingTime** and should then notify *KsTvTune.ax* that the scan completed by signaling the event.

The driver returns scan status only if the tuning device supports hardware-assisted scanning. The driver indicates such support by setting the **fSupportsHardwareAssistedScanning** member of the [**KSPROPERTY\_TUNER\_SCAN\_CAPS\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565892) structure to **TRUE** in a call to its [**KSPROPERTY\_TUNER\_SCAN\_CAPS**](ksproperty-tuner-scan-caps.md) property. The driver should signal an event and return one of the following lock types in the **LockStatus** member of the [**KSPROPERTY\_TUNER\_SCAN\_STATUS\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565898) structure:

-   **Tuner\_LockType\_None** if the tuning device could not find any signal at all.

-   **Tuner\_LockType\_Locked** if the tuning device locked onto the exact frequency.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available in Windows Vista and later versions of the operating system.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## See also


[**KSEVENT\_TUNER\_INITIATE\_SCAN**](ksevent-tuner-initiate-scan.md)

[**KSPROPERTY\_TUNER\_NETWORKTYPE\_SCAN\_CAPS**](ksproperty-tuner-networktype-scan-caps.md)

[**KSPROPERTY\_TUNER\_NETWORKTYPE\_SCAN\_CAPS\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565885)

[**KSPROPERTY\_TUNER\_SCAN\_CAPS**](ksproperty-tuner-scan-caps.md)

[**KSPROPERTY\_TUNER\_SCAN\_CAPS\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565892)

[**KSPROPERTY\_TUNER\_SCAN\_STATUS\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565898)

[**TUNER\_ANALOG\_CAPS\_S**](https://msdn.microsoft.com/library/windows/hardware/ff568547)

 

 






