---
title: Enable WSPrint 2.0 on a device
author: windows-driver-content
description: Use these settings to enable WSPrint 2.0 on a device
---

# Enable WSPrint 2.0 on a device


This topic describes the settings required to enable WSPrint 2.0 on a device.

## Broadcast a Mdns printer service


This must be done using the service type of PrintService.\_printer.\_tcp.local on port 80.

## Implement a HTTP endpoint 


The endpoint needs to be able to respond to WSPrint 2.0 operations. You do not need to perform SOAP validation and processing. You can instead use string detection and replacement.

Once the WSPrint endpoint is functioning, you need to customize the XML returned from the GetPrinterElements call with a custom device id:

```
<wprt:DeviceId>MFG:MS3D; CMD:XPS; MDL:Compat; CLS:Printer; DES:Compat; CID:MS3DWSD</wprt:DeviceId>
```
This matches with the Compatible ID in the published INF:

```
WSDPRINT\MS3DCompatE2D2
```

## WSPrint interactions


The following diagram shows WSPrint 2.0 interactions:

![wsprint interactions](images/wsprint-interactions.png)

The following steps are a more detailed description of WSPrint 2.0 interactions:

```
1.  Probe – Network Discovery bootstrap

2.  Resolve – Network Discovery bootstrap

3.  Get – Printer MetaData Query

4.  GetPrinterElements – Printer MetaData Query

5.  Subscribe – Event model registration

6.  Unsubscribe – Event unregistration

7.  SetEventRate – Event rate

8.  Renew – Renew 

9.  PrepareToPrint – Print initialization

10. CreatePrintJob – Print submission

11. CreatePrintJob2 – Print submission

12. GetPrintDeviceResources – Allows retrieval of localized resources in ResX (Multi Part Outgoing Response)

13. GetPrintDeviceCapabilities  - Allows retrieval of Print Device Capabilities (Multi Part Outgoing Response)

14. GetBidiSchemaExtensions - Allows retrieval of Bidi Schema extensions (Multi Part Outgoing Response)

15. CancelJob – Job Cancellation

16. GetActiveJobs – Job Progress 

17. GetJobHistory – Job History

18. AddDocument – Add document to current print

19. GetJobElements – Get job statuses

20. SendDocument – Actual print data (Multi Part Incoming Request)
```

For more information on WSPrint 2.0, see the following resources:

[Implementing Web Services on Devices for Printing](https://msdn.microsoft.com/en-us/library/windows/hardware/dn641604(v=vs.85).aspx)

[WSPrint 2.0 specification](http://go.microsoft.com/fwlink/p/?LinkId=534008) 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Slicer%20settings%20%20RELEASE:%20%289/2/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")

