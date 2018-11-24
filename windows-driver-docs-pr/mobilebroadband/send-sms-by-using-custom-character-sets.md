---
title: Send SMS by using custom character sets
description: Send SMS by using custom character sets
ms.assetid: c1f19c16-66f5-4bcd-ba28-950eaa6472d2
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Send SMS by using custom character sets


If you need access to raw message protocol data units (PDU) to achieve scenarios that are not supported by the text-mode interface, Windows 8, Windows 8.1, and Windows 10 enable PDU-mode sending and reading received SMS messages.

You might need to use the PDU-mode SMS interface in the following cases:

-   To send or read received SMS by using a National Language Single Shift Table or National Language Locking Shift Table as defined in [3GPP TS 23.038](http://go.microsoft.com/fwlink/?LinkId=329080).

-   To send multi-part SMS using different character sets for each segment.

**JavaScript code example to send SMS messages by using the PDU-mode interface**

``` syntax
function smsDevicePDUSend()
{
  if (smsDevice !== null)
  {
    // Defines a binary message
    var smsMessage = new Windows.Devices.Sms.SmsBinaryMessage();
    var messsagePdu = “0011000B914152828377F90000AA0CC8F71D14969741F977FD07”;
    var messagePduByteArray = hexToByteArray(messsagePdu);
    smsMessage.setData(messagePduByteArray);

    if (smsDevice.cellularClass === Windows.Devices.Sms.CellularClass.gsm)
    {
      smsMessage.format = Windows.Devices.Sms.SmsDataFormat.gsmSubmit;
    }
    else
    {
      smsMessage.format = Windows.Devices.Sms.SmsDataFormat.cdmaSubmit;
    }
    var sendSmsMessageOperation = smsDevice.sendMessageAsync(smsMessage);

    sendSmsMessageOperation.done(function (reply) {
      WinJS.log("Sent message in PDU format", "sample", "status");
    }, errorCallback);
}

// Used to convert hex PDU to byte array for sending SMS using PDU //mode
function hexToByteArray(hexString)
{
  var result = [];
  var hexByte = "";
  var decByte = 0;
  for (var i = 0; i < hexString.length; i = i + 2) {
    hexByte = hexString.substring(i, i + 2);
    decByte = parseInt(hexByte, 16);
    result.push(decByte);
  }
  return result;
}
```

**JavaScript code example to read received SMS messages by using the PDU-mode interface**

``` syntax
function smsDeviceRead()
{
  try
  {
    if (smsDevice !== null)
    {
      var messageStore = smsDevice.messageStore;
      var messageID = “1” // select a Message Id to read 

      // Check for a valid ID number
      if (isNaN(messageID) || messageID < 1 || messageID > messageStore.maxMessages)
      {
        WinJS.log("Invalid ID number", "sample", "error");
        return;
     }

     var getSmsMessageOperation = messageStore.getMessageAsync(messageID);

     // Display message when get is completed
     getSmsMessageOperation.done(smsMessageReadSuccess, errorCallback);
     } 
  }
  catch (err) {
    // handle error
  }
}

function smsMessageReadSuccess(smsMessage)
{
  try
  {
    if (smsMessage instanceof SmsBinaryMessage) {
    var format  = smsMessage.format;
    var pduData = smsMessage.getData(); // byte array 
  }
  catch (err)
  {
    WinJS.log("SMS did not set up: " + err, "sample", "error");
  }
}
```

## <span id="related_topics"></span>Related topics


[Developing SMS apps](developing-sms-apps.md)

 

 






