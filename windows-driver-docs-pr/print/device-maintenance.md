---
title: Device Maintenance
description: A device maintenance feature has been introduced in Windows 8.1 and later versions of Windows.
ms.assetid: 310E92A9-F751-4346-9B2D-0578A136AD20
ms.date: 04/20/2017
ms.localizationpriority: medium
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

```csharp
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
            // parse and interpret 'bidiResponse'
        }
    }
} 
```

Device maintenance is supported in UWP device apps after the app is invoked via any of the three entry points.

## Related topics
[**IPrinterBidiSetRequestCallback**](https://msdn.microsoft.com/library/windows/hardware/dn265385)  
[**IPrinterExtensionAsyncOperation**](https://msdn.microsoft.com/library/windows/hardware/dn265387)  
[**IPrinterQueue2**](https://msdn.microsoft.com/library/windows/hardware/dn265389)  



