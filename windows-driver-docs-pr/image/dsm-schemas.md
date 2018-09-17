---
title: DSM Schemas
author: windows-driver-content
description: DSM Schemas
ms.assetid: 54466df0-72e8-4ed0-adff-3d54cdf628bf
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
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

 

 




