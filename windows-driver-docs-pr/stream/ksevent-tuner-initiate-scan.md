---
title: KSEVENT_TUNER_INITIATE_SCAN
description: The KSEVENT_TUNER_INITIATE_SCAN event requests that the driver initiate a scan operation and notify a user-mode client when the driver's associated tuning device completes the scan operation.
keywords: ["KSEVENT_TUNER_INITIATE_SCAN Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSEVENT_TUNER_INITIATE_SCAN
api_type:
- NA
ms.date: 10/11/2021
ms.localizationpriority: medium
---

# KSEVENT_TUNER_INITIATE_SCAN

The **KSEVENT_TUNER_INITIATE_SCAN** event requests that the driver initiate a scan operation and notify a user-mode client when the driver's associated tuning device completes the scan operation.

## Usage Summary Table

| Get | Set | Target | Event descriptor type | Event value type |
|--|--|--|--|--|
| No | Yes | Pin | [**KSEVENT_TUNER_INITIATE_SCAN_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksevent_tuner_initiate_scan_s) | [**KSEVENTDATA**](/windows-hardware/drivers/ddi/ks/ns-ks-kseventdata) |

## Remarks

Every scan request should be non-blocking. That is, the driver should not wait for the scan operation to complete before it returns control. In fact, the driver should use a separate thread to perform the scan operation.

While the KSEVENT_TUNER_INITIATE_SCAN event is independent of [**KSPROPERTY_TUNER_FREQUENCY**](ksproperty-tuner-frequency.md), KSEVENT_TUNER_INITIATE_SCAN corresponds to the **KS_TUNER_TUNING_EXACT** tuning flag in the **TuningFlags** member of the [**KSPROPERTY_TUNER_FREQUENCY_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_tuner_frequency_s) structure. This means that the scan always attempts to determine the exact frequency of the next channel. Also, the tuning strategy that the tuning device follows is controlled by the driver (KS_TUNER_STRATEGY_DRIVER_TUNES from the **Strategy** member of the [**KSPROPERTY_TUNER_MODE_CAPS_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_tuner_mode_caps_s) structure). These fixed flags and strategy are always followed even if a different flag and strategy are used to control **KSPROPERTY_TUNER_FREQUENCY**.

In other words, KSTUNER_TUNING_FLAGS and KSTUNER_STRATEGY values do not affect the behavior of KSEVENT_TUNER_INITIATE_SCAN.

***Completion and Status***

The scan status property [**KSPROPERTY_TUNER_SCAN_STATUS**](ksproperty-tuner-scan-status.md) provides information about the current frequency and the status of the signal lock. The application queries the lock status from the KSPROPERTY_TUNER_SCAN_STATUS property. The application also queries [**KSPROPERTY_TUNER_STANDARD_MODE**](ksproperty-tuner-standard-mode.md) property for information about automatic-signal-standard detection. If no signal was found in the requested range, the KSPROPERTY_TUNER_SCAN_STATUS property returns the **Tuner_LockType_None** value in the **LockStatus** member of the [**KSPROPERTY_TUNER_SCAN_STATUS_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_tuner_scan_status_s) structure. If the tuning device can automatically detect the tuner standard from the signal and a signal in an alternate standard was found, the tuning device itself can process any requests to the [**KSPROPERTY_TUNER_STANDARD**](ksproperty-tuner-standard.md) property. The tuning device is possibly unable to proceed beyond a phased-lock-loop (PLL) lock, and it might specify that the standard is not known. Or, the tuning device might automatically adjust to a different signal standard. Also, the tuning device might even obtain a full lock on that signal standard and determine the alternate standard. Such situations might arise when there are multiple signal standards in the frequency spectrum.

***Boundary Conditions***

If the driver finds that the center frequency of a channel is outside the range that an application provides, the driver must ignore that signal and move to the next signal; the driver must not return the best possible approximation within the range provided. The driver must move to the next signal to avoid duplicate counting of channels when an application attempts to compile a channel list.

For the same reason, the application must shift the range of query by half the expected channel bandwidth (about 6/2 = 3MHz for analog and digital TV) to ensure that channels are not double counted particularly when the hardware encounters a signal that the hardware cannot decode. In this situation, the driver has difficulty avoiding double counting certain channels.

***Multi-Standard Spectra***

The scan operation must complete whenever a new channel or signal is found. The driver then returns scan status through the [**KSPROPERTY_TUNER_SCAN_STATUS**](ksproperty-tuner-scan-status.md) property. The scan must complete whenever a new channel is found even if the driver determines that the newly found channel does not match the previously applied standard. The application must process the new channel information and must resubmit a scan request to find another channel with the same signal standard.

## See also

[**KSEVENT_TUNER_INITIATE_SCAN_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksevent_tuner_initiate_scan_s)

[**KSEVENTDATA**](/windows-hardware/drivers/ddi/ks/ns-ks-kseventdata)

[**KSPROPERTY_TUNER_SCAN_STATUS**](ksproperty-tuner-scan-status.md)

[**KSPROPERTY_TUNER_SCAN_CAPS**](ksproperty-tuner-scan-caps.md)

[**KSPROPERTY_TUNER_STANDARD**](ksproperty-tuner-standard.md)

[**KSPROPERTY_TUNER_STANDARD_MODE**](ksproperty-tuner-standard-mode.md)
