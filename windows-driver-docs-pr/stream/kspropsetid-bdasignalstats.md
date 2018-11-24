---
title: KSPROPSETID\_BdaSignalStats
description: KSPROPSETID\_BdaSignalStats
ms.assetid: ea368344-e56d-47d1-bc1f-241ba8aa0bc4
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPSETID\_BdaSignalStats


## <span id="ddk_kspropsetid_bdasignalstats_ks"></span><span id="DDK_KSPROPSETID_BDASIGNALSTATS_KS"></span>


KSPROPSETID\_BdaSignalStats is the BDA signal statistics property set. It is used to retrieve signal statistics from a control node or a pin.

The following properties are available:

<span id="KSPROPERTY_BDA_SIGNAL_STRENGTH"></span><span id="ksproperty_bda_signal_strength"></span>[**KSPROPERTY\_BDA\_SIGNAL\_STRENGTH**](ksproperty-bda-signal-strength.md)
Required.
Indicates the carrier strength of the signal in mDb (1/1000 of a decibel (DB)).
<span id="KSPROPERTY_BDA_SIGNAL_QUALITY"></span><span id="ksproperty_bda_signal_quality"></span>[**KSPROPERTY\_BDA\_SIGNAL\_QUALITY**](ksproperty-bda-signal-quality.md)
Required.
Indicates the amount of data successfully extracted from the signal as a percent.
<span id="KSPROPERTY_BDA_SIGNAL_PRESENT"></span><span id="ksproperty_bda_signal_present"></span>[**KSPROPERTY\_BDA\_SIGNAL\_PRESENT**](ksproperty-bda-signal-present.md)
Required.
Indicates whether a signal carrier is present.
<span id="KSPROPERTY_BDA_SIGNAL_LOCKED"></span><span id="ksproperty_bda_signal_locked"></span>[**KSPROPERTY\_BDA\_SIGNAL\_LOCKED**](ksproperty-bda-signal-locked.md)
Required.
Indicates whether a signal can be locked.
<span id="KSPROPERTY_BDA_SAMPLE_TIME"></span><span id="ksproperty_bda_sample_time"></span>[**KSPROPERTY\_BDA\_SAMPLE\_TIME**](ksproperty-bda-sample-time.md)
Optional.
Indicates the sample time over which signal level and quality are averaged.
<span id="KSPROPERTY_BDA_SIGNAL_LOCK_CAPS"></span><span id="ksproperty_bda_signal_lock_caps"></span>[**KSPROPERTY\_BDA\_SIGNAL\_LOCK\_CAPS**](ksproperty-bda-signal-lock-caps.md)
Required.
Indicates the lock types that the driver can support for a signal.
<span id="KSPROPERTY_BDA_SIGNAL_LOCK_TYPE"></span><span id="ksproperty_bda_signal_lock_type"></span>[**KSPROPERTY\_BDA\_SIGNAL\_LOCK\_TYPE**](ksproperty-bda-signal-lock-type.md)
Required.
Indicates the current lock type for a signal.
### Comments

When specifying the particular property of the KSPROPSETID\_BdaSignalStats property set to get a signal statistic from a pin, set the **NodeId** member of the KSP\_NODE structure to −1.

 

 





