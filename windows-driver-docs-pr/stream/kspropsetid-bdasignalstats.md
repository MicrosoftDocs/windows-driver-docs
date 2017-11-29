---
title: KSPROPSETID\_BdaSignalStats
description: KSPROPSETID\_BdaSignalStats
ms.assetid: ea368344-e56d-47d1-bc1f-241ba8aa0bc4
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
### <span id="comments"></span><span id="COMMENTS"></span>Comments

When specifying the particular property of the KSPROPSETID\_BdaSignalStats property set to get a signal statistic from a pin, set the **NodeId** member of the KSP\_NODE structure to −1.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPSETID_BdaSignalStats%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




