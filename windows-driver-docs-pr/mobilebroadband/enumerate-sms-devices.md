---
title: Enumerate SMS devices
description: Enumerate SMS devices
ms.assetid: d0d57a4f-df83-4f3b-b7b4-417ad4e11350
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Enumerate SMS devices


The Mobile Broadband SMS platform provides the ability to get the first SMS-capable mobile broadband device, or to get a list of all SMS-capable mobile broadband devices. The following sample code shows instantiating an SMS object with the default SMS device and with a specific device.

**Note**  
In apps that use C# or C++ in Windows 8, Windows 8.1, or Windows 10, the first use of the [**SmsDevice**](https://msdn.microsoft.com/library/windows/apps/br206511) object to call [**GetDefaultAsync**](https://msdn.microsoft.com/library/windows/apps/br211915) or [**FromIdAsync**](https://msdn.microsoft.com/library/windows/apps/br211914) should be on the STA thread. Calls from an MTA thread can result in undefined behavior.

 

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Enumerate%20SMS%20devices%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





