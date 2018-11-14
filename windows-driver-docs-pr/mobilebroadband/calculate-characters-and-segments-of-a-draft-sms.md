---
title: Calculate characters and segments of a draft SMS
description: Calculate characters and segments of a draft SMS
ms.assetid: abbec0b0-dfa8-43e9-8b48-e99680d56b42
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Calculate characters and segments of a draft SMS


The Mobile Broadband SMS platform provides a function to estimate the number of characters remaining and number of segments used (in a multi-part messages) during the composition of an SMS message.

**Note**  
The number of characters in each segment is not constant, and it varies based on the text string in the message body and the network type. On GSM networks, a single SMS message supports up to 160 7-bit characters or 70 16-bit characters. A message that spans multiple segments supports 142 7-bit characters in each segment due to additional header information.

 

Providing an accurate estimate on the number of segments that are used while composing an SMS message promotes user confidence, because users are typically charged per SMS message that is sent.

**JavaScript code example**

``` syntax
var smsMessage = new Windows.Devices.Sms.SmsTextMessage();
smsMessage.body = id('messageText').value;  // Set message body text to text of messageText HTML element
var messageLength = smsDevice.calculateLength(smsMessage);
id('remainingCharsCount').innerText = messageLength.charactersPerSegment - messageLength.characterCountLastSegment;
id('messageSegmentsCount').innerText = messageLength.segmentCount;
```

## <span id="related_topics"></span>Related topics


[Send SMS by using the text-mode interface](send-sms-by-using-the-text-mode-interface.md)

 

 






