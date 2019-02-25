---
title: KSPROPSETID\_TSRateChange
description: KSPROPSETID\_TSRateChange
ms.assetid: bd2855e5-dd90-4ae3-a96e-e2163e94c7d6
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPSETID\_TSRateChange


## <span id="ddk_kspropsetid_tsratechange_ks"></span><span id="DDK_KSPROPSETID_TSRATECHANGE_KS"></span>


The KSPROPSETID\_TSRateChange property set defines properties to control time stamp rate changes. This property set can be used to implement fast-forward and rewind capabilities.

The KS\_AM\_PROPERTY\_TS\_RATE\_CHANGE enumeration in *Ksmedia.h* specifies the properties of this set.

Minidrivers can use KSPROPSETID\_TSRateChange for any MPEG2 stream, not just DVDs.

The following properties are defined:

[**KS\_AM\_RATE\_SimpleRateChange**](ks-am-rate-simpleratechange.md)

[**KS\_AM\_RATE\_ExactRateChange**](ks-am-rate-exactratechange.md)

[**KS\_AM\_RATE\_MaxFullDataRate**](ks-am-rate-maxfulldatarate.md)

[**KS\_AM\_RATE\_Step**](ks-am-rate-step.md)

 

 





