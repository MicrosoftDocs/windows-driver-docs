---
title: Windows automatically segments long messages
description: Windows automatically segments long messages
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Windows automatically segments long messages


The Mobile Broadband SMS platform automatically segments long messages that are sent on GSM networks into separate segments that fit in the supported maximum character limit based on message contents. Segmentation information (that is, part 1 of 2) is encoded in SMS User Data Header (UDH), to enable the receiving SMS client to combine segments into a single message. All segments of a multi-part SMS are encoded by using the same character set.

Mobile network operators charge users per message segment. SMS platform automatically creates a maximum of 10 segments and truncates text above the limit.

## <span id="related_topics"></span>Related topics


[Send SMS by using the text-mode interface](calculate-characters-and-segments-of-a-draft-sms.md)

 

 






