---
title: KSEVENTSETID\_AudioControlChange
description: KSEVENTSETID\_AudioControlChange
ms.assetid: 5189c284-d53a-4fc4-981c-7d6b3851dab1
keywords: ["KSEVENTSETID_AudioControlChange"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSEVENTSETID\_AudioControlChange


## <span id="ddk_kseventsetid_audiocontrolchange_ks"></span><span id="DDK_KSEVENTSETID_AUDIOCONTROLCHANGE_KS"></span>


The `KSEVENTSETID_AudioControlChange` event set is used to notify clients when a miniport driver detects a [hardware event](https://msdn.microsoft.com/library/windows/hardware/ff536405), which is a change in a hardware volume-control knob, mute switch, or other type of manual control.

The event items in this set are specified as KSEVENT\_AUDIO\_CONTROL\_CHANGE enumeration values.

The only event in this set is [**KSEVENT\_CONTROL\_CHANGE**](ksevent-control-change.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSEVENTSETID_AudioControlChange%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




