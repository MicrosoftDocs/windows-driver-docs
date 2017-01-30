---
title: Send SMS by using custom character sets
description: Send SMS by using custom character sets
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: c1f19c16-66f5-4bcd-ba28-950eaa6472d2
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Send%20SMS%20by%20using%20custom%20character%20sets%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





