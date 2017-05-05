---
title: Windows automatically selects optimal character encoding
description: Windows automatically selects optimal character encoding
ms.assetid: 3fde6e89-c9ea-43d2-a999-506686b223f4
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Windows%20automatically%20selects%20optimal%20character%20encoding%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





