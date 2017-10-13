---
title: Device Maintenance
author: windows-driver-content
description: A device maintenance feature has been introduced in Windows 8.1 and later versions of Windows.
ms.assetid: 310E92A9-F751-4346-9B2D-0578A136AD20
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Device Maintenance


A device maintenance feature has been introduced in Windows 8.1 and later versions of Windows.

This feature uses bidirectional communication (Bidi) to allow you to send device maintenance commands from within a UWP device app or a printer extension to the print subsystem. For example, you could send commands to your print device to clean the ink nozzles.

The port monitor works in conjunction with the vendor-provided Bidi extension files to translate these Bidi requests into device and protocol-specific commands, and then transmit them to the print device. A device maintenance task is performed by sending Bidi “Set” queries to the print device, and the Bidi response from the device indicates whether the operation succeeded or failed.

The new asynchronous interface that helps to implement this feature takes in XML data in the form of a string parameter, and a callback object.

Because the interface is asynchronous, the caller does not have to wait for a response. When the Bidi operation is completed, the callback object is invoked.

## The new interfaces


The following interfaces have been introduced in Windows (code-named “Blue”) to implement the device maintenance feature.

[**IPrinterBidiSetRequestCallback**](https://msdn.microsoft.com/library/windows/hardware/dn265385)

[**IPrinterExtensionAsyncOperation**](https://msdn.microsoft.com/library/windows/hardware/dn265387)

[**IPrinterQueue2**](https://msdn.microsoft.com/library/windows/hardware/dn265389)

## Initiating a device maintenance Session


To initiate a device maintenance session, you must first create your command string as XML data. Then you must create an instance of the callback object that will be invoked after the asynchronous Bidi operation is completed.

After the operation is completed, the callback object is invoked on the IPrinterBidiSetRequestCallback::Completed method, and that provides the HRESULT value of the operation. You can then parse this HRESULT value and perform any other needed tasks.

The following C# snippet outlines how to issue a device maintenance task from a UWP device app.

```CSharp
//
// Declare a global constant that will be used
// to determine whether method calls were successful
//
const int S_OK = 0;
 
class BidiSendAsyncDemo
{
    //
    // Create a queue object and also
    // create the command string
    //
    void PerformDeviceMaintenance(
        IPrinterQueue2 queue,
        string bidiRequestInXml
        )
    {
        BidiSetResultCallback callBack = new BidiSetResultCallback();

        IPrinterExtensionAsyncOperation asyncOperation =
          queue.SendBidiSetRequestAsync(bidiRequestInXml, callBack);
    }
}

/// <summary>
/// This class represents the callback object
/// </summary>
public class BidiSetResultCallback :
    IPrinterBidiSetRequestCallback
{
    void Completed(
        string bidiResponse,
        int hr
        )
    {
        if (S_OK == hr)
        {
            // parse and interpret &#39;bidiResponse&#39;
        }
    }
} 
```

Device maintenance is supported in UWP device apps after the app is invoked via any of the three entry points.

## Related topics
[**IPrinterBidiSetRequestCallback**](https://msdn.microsoft.com/library/windows/hardware/dn265385)  
[**IPrinterExtensionAsyncOperation**](https://msdn.microsoft.com/library/windows/hardware/dn265387)  
[**IPrinterQueue2**](https://msdn.microsoft.com/library/windows/hardware/dn265389)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Device%20Maintenance%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


