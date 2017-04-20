---
title: Bass Management
description: Bass Management
ms.assetid: b3fb6fcf-cf86-4627-912e-253b5864ab9e
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Bass Management


There are two bass management modes: forward bass management and reverse bass management.

-   Forward bass management filters out the low frequency content of the audio data stream. The forward bass management algorithm redirects the filtered output to the subwoofer or to the front-left and front-right loudspeaker channels, depending on the channels that can handle deep bass frequencies. This decision is based on the setting of the LRBig flag.

    To set the LRBig flag, the user uses the Sound applet in Control Panel to access the Bass Management Settings dialog box. The user selects a check box to indicate, for example, that the front-right and front-left speakers are full range and this action sets the LRBig flag. To clear this flag, click the check box to clear it.

-   Reverse bass management distributes the signal from the subwoofer channel to the other output channels. The signal is directed either to all channels or to the front-left and front-right channels, depending on the setting of the LRBig flag. This process uses a substantial gain reduction when mixing the subwoofer signal into the other channels.

    The bass management mode that is used depends on the availability of a subwoofer and the bass-handling capability of the main speakers. In Windows Vista, the user provides this information via the Sound applet in Control Panel.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Bass%20Management%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


