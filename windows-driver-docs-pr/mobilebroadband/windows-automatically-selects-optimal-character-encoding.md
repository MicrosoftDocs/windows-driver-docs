---
title: Windows automatically selects optimal character encoding
description: Windows automatically selects optimal character encoding
ms.assetid: 3fde6e89-c9ea-43d2-a999-506686b223f4
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Windows automatically selects optimal character encoding


Windows 8, Windows 8.1, and Windows 10 choose the optimal character encoding to use when it sends a SMS message, based on the most efficient encoding that is supported by the message contents. SMS is encoded in a 7-bit character set, unless it contains at least one invalid character, in which case the whole message is encoded in Unicode.

**JavaScript code example for sending SMS messages using text-mode interface**

``` syntax
try
{
    if (smsDevice != null)
    {
      // defines a text message
      var smsMessage = new Windows.Devices.Sms.SmsTextMessage();
      smsMessage.to = id("phoneNumber").value;
      smsMessage.body = id("messageText").value + "\n\nSent via Windows 8 SMS API";
      var sendSmsMessageOperation = smsDevice.sendMessageAsync(smsMessage);
      console.log("Sending message...");
      sendSmsMessageOperation.then(function (reply)
      {
        console.log("Text message sent.");
      });
    }
    else
    {
      console.log("No SMS device found");
    }
} catch (err) {
    console.log("SMS exception: " + err);
}
```

Optionally, you can override the optimal encoding functionality and specify which character set to use.

Windows 8, Windows 8.1, and Windows 10 support common character sets for mobile broadband network adapters that are compatible with GSM (3GPP) and CDMA (3GPP2) networks.

The following table lists the character encodings supported by the text-mode API:

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Network type</th>
<th>Character sets</th>
<th>Character limit for single SMS segment</th>
<th>Character limit for multi-part SMS segments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>GSM</p></td>
<td><p>GSM 7-bit default alphabet and GSM 7-bit default alphabet extension table</p></td>
<td><p>160</p></td>
<td><p>142</p></td>
</tr>
<tr class="even">
<td><p>CDMA</p></td>
<td><p>7-bit ASCII</p></td>
<td><p>160 (can vary by network)</p></td>
<td><p></p></td>
</tr>
<tr class="odd">
<td><p>CDMA</p></td>
<td><p>Unicode</p></td>
<td><p>70 (can vary by network)</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

 

GSM character sets are defined [3GPP TS 23.038: "Alphabets and language-specific information"](http://www.3gpp.org/ftp/Specs/html-info/23038.md). CDMA character sets are defined in [3GPP2 C.R1001-D](http://www.3gpp2.org/Public_html/specs/C.R1001-D_v1.0_110403.pdf).

## <span id="related_topics"></span>Related topics


[Send SMS by using the text-mode interface](send-sms-by-using-the-text-mode-interface.md)

 

 






