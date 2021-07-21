---
title: Enable WSPrint 2.0 on a device
description: Use these settings to enable WSPrint 2.0 on a device
ms.date: 05/18/2020
ms.localizationpriority: medium
---

# Enable WSPrint 2.0 on a device

This topic describes the settings required to enable WSPrint 2.0 on a device.

## Broadcast a Mdns printer service

This must be done using the service type of PrintService.\_printer.\_tcp.local on port 80.

## Implement a HTTP endpoint

The endpoint needs to be able to respond to WSPrint 2.0 operations. You do not need to perform SOAP validation and processing. You can instead use string detection and replacement.

Once the WSPrint endpoint is functioning, you need to customize the XML returned from the GetPrinterElements call with a custom device id:

```xml
<wprt:DeviceId>MFG:MS3D; CMD:XPS; MDL:Compat; CLS:Printer; DES:Compat; CID:MS3DWSD</wprt:DeviceId>
```

This matches with the Compatible ID in the published INF:

```xml
WSDPRINT\MS3DCompatE2D2
```

## WSPrint interactions

The following diagram shows WSPrint 2.0 interactions:

![wsprint interactions.](images/wsprint-interactions.png)

The following steps are a more detailed description of WSPrint 2.0 interactions:

1. Probe – Network Discovery bootstrap

1. Resolve – Network Discovery bootstrap

1. Get – Printer MetaData Query

1. GetPrinterElements – Printer MetaData Query

1. Subscribe – Event model registration

1. Unsubscribe – Event unregistration

1. SetEventRate – Event rate

1. Renew – Renew

1. PrepareToPrint – Print initialization

1. CreatePrintJob – Print submission

1. CreatePrintJob2 – Print submission

1. GetPrintDeviceResources – Allows retrieval of localized resources in ResX (Multi Part Outgoing Response)

1. GetPrintDeviceCapabilities  - Allows retrieval of Print Device Capabilities (Multi Part Outgoing Response)

1. GetBidiSchemaExtensions - Allows retrieval of Bidi Schema extensions (Multi Part Outgoing Response)

1. CancelJob – Job cancellation

1. GetActiveJobs – Job progress

1. GetJobHistory – Job history

1. AddDocument – Add document to current print

1. GetJobElements – Get job statuses

1. SendDocument – Actual print data (Multi Part Incoming Request)

For more information on WSPrint 2.0, see the following resources:

[Implementing Web Services on Devices for Printing](/windows-hardware/design/whitepapers/implementing-web-services-on-devices-for-printing)

[WSPrint 2.0 specification](/windows-hardware/design/whitepapers/implementing-web-services-on-devices-for-printing#file-downloads)