---
title: DSM Schemas
author: windows-driver-content
description: DSM Schemas
MS-HAID:
- 'dsm\_des\_arch\_36bce8d1-718d-4994-a248-5672f688d040.xml'
- 'image.dsm\_schemas'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 54466df0-72e8-4ed0-adff-3d54cdf628bf
---

# DSM Schemas


To support DSM, a network-connected DSM device communicates with the following two networked components:

-   A control point--typically a desktop computer--on which an IT administrator runs the Windows scan-management console (SMC) to configure the scan job workflows for various groups of users.

-   A DSM scan server that performs scan processing of image data acquired by the scanner.

The DSM device uses the Distributed Scan Device Web Service (WS-DSD) protocol for its communications with the SMC on the control point. This communications protocol uses a subset of the schema elements in the WS-Scan Service schema for the request, response, and event messages exchanged between the DSM device and the control point. For more information about this schema, see [Web Services on Devices Scan Service Schema](https://msdn.microsoft.com/library/windows/hardware/ff547963).

The DSM device uses the Distributed Scan Processing Web Service (WS-DSP) protocol for its communications with the DSM scan server. This communications protocol uses Distributed Scan Processing Web Service schema elements for the request, response, and event messages exchanged between the DSM device and the DSM scan server.

In addition, the Distributed Scan Configuration Web Service (WS-DSC) schema defines a set of elements that are used for communication between the DSM scan server and the SMC. For more information about this schema, see the Windows SDK documentation.

A DSM device that supports DSM must implement the Distributed Scan Device Web Service and Distributed Scan Processing Web Service protocols. The following sections summarize these protocols:

[Distributed Scan Device Web Service Protocol Summary](distributed-scan-device-web-service-protocol-summary.md)

[Distributed Scan Processing Web Service Protocol Summary](distributed-scan-processing-web-service-protocol-summary.md)

The following sections describe the error messages that might be sent by a Distributed Scan Device Web Service host or a Distributed Scan Processing Web Service host that fails to perform an operation requested by a client:

[WS Scan Service Operation Error Reporting](https://msdn.microsoft.com/library/windows/hardware/ff553401)

[Distributed Scan Processing Web Service Operation Error Reporting](distributed-scan-processing-web-service-operation-error-reporting.md)

[Distributed Scan Processing Web Service Operation Error Reporting](distributed-scan-processing-web-service-operation-error-reporting.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20DSM%20Schemas%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


