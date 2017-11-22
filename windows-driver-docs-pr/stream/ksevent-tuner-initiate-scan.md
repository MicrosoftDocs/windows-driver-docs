---
title: KSEVENT\_TUNER\_INITIATE\_SCAN
description: The KSEVENT\_TUNER\_INITIATE\_SCAN event requests that the driver initiate a scan operation and notify a user-mode client when the driver's associated tuning device completes the scan operation.
MS-HAID:
- 'vidcapevent\_d30dfc52-bf34-41be-8b3d-9ddafdd8a46e.xml'
- 'stream.ksevent\_tuner\_initiate\_scan'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 63f6917e-30d2-4734-92fa-49a4291efafd
keywords: ["KSEVENT_TUNER_INITIATE_SCAN Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSEVENT_TUNER_INITIATE_SCAN
api_type:
- NA
---

# KSEVENT\_TUNER\_INITIATE\_SCAN


The KSEVENT\_TUNER\_INITIATE\_SCAN event requests that the driver initiate a scan operation and notify a user-mode client when the driver's associated tuning device completes the scan operation.

### <span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

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
<th>Event descriptor type</th>
<th>Event value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>Pin</p></td>
<td><p>[<strong>KSEVENT_TUNER_INITIATE_SCAN_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561901)</p></td>
<td><p>[<strong>KSEVENTDATA</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561750)</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Every scan request should be non-blocking. That is, the driver should not wait for the scan operation to complete before it returns control. In fact, the driver should use a separate thread to perform the scan operation.

While the KSEVENT\_TUNER\_INITIATE\_SCAN event is independent of [**KSPROPERTY\_TUNER\_FREQUENCY**](ksproperty-tuner-frequency.md), KSEVENT\_TUNER\_INITIATE\_SCAN corresponds to the **KS\_TUNER\_TUNING\_EXACT** tuning flag in the **TuningFlags** member of the [**KSPROPERTY\_TUNER\_FREQUENCY\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565839) structure. This means that the scan always attempts to determine the exact frequency of the next channel. Also, the tuning strategy that the tuning device follows is controlled by the driver (KS\_TUNER\_STRATEGY\_DRIVER\_TUNES from the **Strategy** member of the [**KSPROPERTY\_TUNER\_MODE\_CAPS\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565872) structure). These fixed flags and strategy are always followed even if a different flag and strategy are used to control **KSPROPERTY\_TUNER\_FREQUENCY**.

In other words, KSTUNER\_TUNING\_FLAGS and KSTUNER\_STRATEGY values do not affect the behavior of KSEVENT\_TUNER\_INITIATE\_SCAN.

****Completion and Status****

The scan status property [**KSPROPERTY\_TUNER\_SCAN\_STATUS**](ksproperty-tuner-scan-status.md) provides information about the current frequency and the status of the signal lock. The application queries the lock status from the KSPROPERTY\_TUNER\_SCAN\_STATUS property. The application also queries [**KSPROPERTY\_TUNER\_STANDARD\_MODE**](ksproperty-tuner-standard-mode.md) property for information about automatic-signal-standard detection. If no signal was found in the requested range, the KSPROPERTY\_TUNER\_SCAN\_STATUS property returns the **Tuner\_LockType\_None** value in the **LockStatus** member of the [**KSPROPERTY\_TUNER\_SCAN\_STATUS\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565898) structure. If the tuning device can automatically detect the tuner standard from the signal and a signal in an alternate standard was found, the tuning device itself can process any requests to the [**KSPROPERTY\_TUNER\_STANDARD**](ksproperty-tuner-standard.md) property. The tuning device is possibly unable to proceed beyond a phased-lock-loop (PLL) lock, and it might specify that the standard is not known. Or, the tuning device might automatically adjust to a different signal standard. Also, the tuning device might even obtain a full lock on that signal standard and determine the alternate standard. Such situations might arise when there are multiple signal standards in the frequency spectrum.

****Boundary Conditions****

If the driver finds that the center frequency of a channel is outside the range that an application provides, the driver must ignore that signal and move to the next signal; the driver must not return the best possible approximation within the range provided. The driver must move to the next signal to avoid duplicate counting of channels when an application attempts to compile a channel list.

For the same reason, the application must shift the range of query by half the expected channel bandwidth (about 6/2 = 3MHz for analog and digital TV) to ensure that channels are not double counted particularly when the hardware encounters a signal that the hardware cannot decode. In this situation, the driver has difficulty avoiding double counting certain channels.

****Multi-Standard Spectra****

The scan operation must complete whenever a new channel or signal is found. The driver then returns scan status through the [**KSPROPERTY\_TUNER\_SCAN\_STATUS**](ksproperty-tuner-scan-status.md) property. The scan must complete whenever a new channel is found even if the driver determines that the newly found channel does not match the previously applied standard. The application must process the new channel information and must resubmit a scan request to find another channel with the same signal standard.

## <span id="see_also"></span>See also


[**KSEVENT\_TUNER\_INITIATE\_SCAN\_S**](https://msdn.microsoft.com/library/windows/hardware/ff561901)

[**KSEVENTDATA**](https://msdn.microsoft.com/library/windows/hardware/ff561750)

[**KSPROPERTY\_TUNER\_SCAN\_STATUS**](ksproperty-tuner-scan-status.md)

[**KSPROPERTY\_TUNER\_SCAN\_CAPS**](ksproperty-tuner-scan-caps.md)

[**KSPROPERTY\_TUNER\_STANDARD**](ksproperty-tuner-standard.md)

[**KSPROPERTY\_TUNER\_STANDARD\_MODE**](ksproperty-tuner-standard-mode.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSEVENT_TUNER_INITIATE_SCAN%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





