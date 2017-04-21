---
title: Windows automatically segments long messages
description: Windows automatically segments long messages
ms.assetid: 0c1d7347-4e53-4f17-bdb5-908479f903de
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Windows automatically segments long messages


The Mobile Broadband SMS platform automatically segments long messages that are sent on GSM networks into separate segments that fit in the supported maximum character limit based on message contents. Segmentation information (that is, part 1 of 2) is encoded in SMS User Data Header (UDH), to enable the receiving SMS client to combine segments into a single message. All segments of a multi-part SMS are encoded by using the same character set.

Mobile network operators charge users per message segment. SMS platform automatically creates a maximum of 10 segments and truncates text above the limit.

## <span id="related_topics"></span>Related topics


[Send SMS by using the text-mode interface](send-sms-by-using-the-text-mode-interface.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Windows%20automatically%20segments%20long%20messages%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





