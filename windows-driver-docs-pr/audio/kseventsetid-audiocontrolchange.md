---
title: KSEVENTSETID\_AudioControlChange
description: KSEVENTSETID\_AudioControlChange
ms.assetid: 5189c284-d53a-4fc4-981c-7d6b3851dab1
keywords: ["KSEVENTSETID_AudioControlChange"]
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSEVENTSETID\_AudioControlChange


## <span id="ddk_kseventsetid_audiocontrolchange_ks"></span><span id="DDK_KSEVENTSETID_AUDIOCONTROLCHANGE_KS"></span>


The `KSEVENTSETID_AudioControlChange` event set is used to notify clients when a miniport driver detects a [hardware event](https://msdn.microsoft.com/library/windows/hardware/ff536405), which is a change in a hardware volume-control knob, mute switch, or other type of manual control.

The event items in this set are specified as KSEVENT\_AUDIO\_CONTROL\_CHANGE enumeration values.

The only event in this set is [**KSEVENT\_CONTROL\_CHANGE**](ksevent-control-change.md).

 

 





