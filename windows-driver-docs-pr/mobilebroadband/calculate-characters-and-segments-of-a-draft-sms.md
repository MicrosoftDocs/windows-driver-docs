---
title: Calculate characters and segments of a draft SMS
description: Calculate characters and segments of a draft SMS
ms.assetid: abbec0b0-dfa8-43e9-8b48-e99680d56b42
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Calculate%20characters%20and%20segments%20of%20a%20draft%20SMS%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





