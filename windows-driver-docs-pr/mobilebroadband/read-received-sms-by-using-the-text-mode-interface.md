---
title: Read received SMS by using the text-mode interface
description: Read received SMS by using the text-mode interface
ms.assetid: 5e095fc0-59bf-4ec4-96a3-efe6f4ae054f
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Read received SMS by using the text-mode interface


You can choose between using the text-mode read interface, which is suitable for simple plain text SMS messages, or the PDU-mode mode read interface, which is suitable for advanced control of decoding SMS messages.

Received messages are stored in encoded format on mobile broadband devices. The Mobile Broadband SMS platform supports decoding received messages to plain text. The character sets that are supported for decoding received messages are the same as the character sets supported for encoding messages sent.

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

 

**JavaScript code example for reading received SMS messages using the text-mode interface**

``` syntax
try
{
  if (smsDevice!= null)
  {
    var messageStore = smsDevice.messageStore;
    var messageID = id('whichMessage').value;

    var getSmsMessageOperation = messageStore.getMessageAsync(messageID);

    getSmsMessageOperation.operation.completed = function ()
    {
      result = getSmsMessageOperation.operation.getResults();
      var readableMessage = new Windows.Devices.Sms.SmsTextMessage.fromBinaryMessage(result);
      id('fromWho').innerHTML = readableMessage.from;
      id('fromMessageBody').innerHTML = readableMessage.body;
      console.log("Successfully retrieved message " + messageID + " from message store.");
    }
    getSmsMessageOperation.operation.start();
  }
  else 
  {
    console.log("No SMS Device Found");
  }
}
catch (err) 
{
  console.log("SMS did not set up: " + err);
}
```

**Note**  
SMS client apps can use the decoded segmentation information that is provided by Windows to concatenate multiple segments of a long message and reconstruct the full message. For more info about segmented SMS messages, see [Windows automatically segments long messages](windows-automatically-segments-long-messages.md).

 

## <span id="related_topics"></span>Related topics


[Developing SMS apps](developing-sms-apps.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Read%20received%20SMS%20by%20using%20the%20text-mode%20interface%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





