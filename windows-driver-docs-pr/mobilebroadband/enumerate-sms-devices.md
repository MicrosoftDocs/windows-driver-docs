---
title: Enumerate SMS Devices
description: Enumerate SMS devices
ms.date: 04/20/2017
---

# Enumerate SMS devices


The Mobile Broadband SMS platform provides the ability to get the first SMS-capable mobile broadband device, or to get a list of all SMS-capable mobile broadband devices. The following sample code shows instantiating an SMS object with the default SMS device and with a specific device.

**Note**  
In apps that use C# or C++ in Windows 8, Windows 8.1, or Windows 10, the first use of the [**SmsDevice**](/uwp/api/Windows.Devices.Sms.SmsDevice) object to call [**GetDefaultAsync**](/uwp/api/Windows.Devices.Sms.SmsDevice#Windows_Devices_Sms_SmsDevice_GetDefaultAsync) or [**FromIdAsync**](/uwp/api/Windows.Devices.Sms.SmsDevice#Windows_Devices_Sms_SmsDevice_FromIdAsync_System_String_) should be on the STA thread. Calls from an MTA thread can result in undefined behavior.

 

**JavaScript code example to use the default SMS device**

``` syntax
var smsDevice = new Windows.Devices.Sms.SmsDevice.getDefault();

try
{
  var smsDeviceOperation = Windows.Devices.Sms.SmsDevice.getDefaultAsync();
  smsDeviceOperation.done(smsDeviceReceived, errorCallback);
}
catch (err)
{
  // handle error
}
```

**JavaScript code example to enumerate all SMS devices**

``` syntax
Windows.Devices.Enumeration.DeviceInformation.findAllAsync(Windows.Devices.Sms.SmsDevice.getDeviceSelector()).then(function (smsdevices) 
{
  if (smsdevices.length > 0)
  {
    // for simplicity we choose the first device
    var smsDeviceId = smsdevices[0].Id;
    var smsDeviceOperation = Windows.Devices.Sms.SmsDevice.fromIdAsync(smsNotificationDetails.deviceId); 
    smsDeviceOperation.done(function (smsDeviceResult)
    {
      smsDevice = smsDeviceResult;
    }, errorCallback);
  }
}
```

## <span id="detecterr"></span><span id="DETECTERR"></span>Detect SMS device access errors


You can detect if enumerating the SMS device failed because the app does not have access to SMS. This can happen if the user explicitly denies access to the app or if the device metadata has not granted access to the app.

**JavaScript code example to detect SMS device access errors**

``` syntax
Windows.Devices.Enumeration.DeviceInformation.findAllAsync(Windows.Devices.Sms.SmsDevice.getDeviceSelector()).then(function (smsdevices)
{
  if (smsdevices.length > 0)
  {
    // for simplicity we choose the first device
    var smsDeviceId = smsdevices[0].Id.slice(startIndex,endIndex + 1);
    var smsDeviceOperation = Windows.Devices.Sms.SmsDevice.fromIdAsync(smsNotificationDetails.deviceId); 
    smsDeviceOperation.done(function (smsDeviceResult)
    {
      smsDevice = smsDeviceResult;
    }, errorCallback); 

    // detect if SMS access is denied due to user not granting app consent to use SMS or if metadata is missing or invalid.

  }

function errorCallback(error)
{
  WinJS.log(error.name + " : " + error.description, "sample", "error");

  // If the error was caused due to access being denied to this app
  // then the HResult is set to E_ACCESSDENIED (0x80007005)

  // var hResult = hex(error.number);

}

function hex(nmb)
{
  if (nmb >= 0)
  {
    return nmb.toString(16);
  }
  else
  {
    return (nmb + 0x100000000).toString(16);
  }
}
```

## <span id="related_topics"></span>Related topics


[Developing SMS apps](developing-sms-apps.md)

 

