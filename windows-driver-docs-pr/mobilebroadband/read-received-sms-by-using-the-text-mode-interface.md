---
title: Read received SMS by using the text-mode interface
description: Read received SMS by using the text-mode interface
ms.assetid: 5e095fc0-59bf-4ec4-96a3-efe6f4ae054f
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 






