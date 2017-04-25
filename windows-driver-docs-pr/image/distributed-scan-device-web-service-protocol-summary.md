---
title: DISTRIBUTED SCAN DEVICE WEB SERVICE PROTOCOL SUMMARY
author: windows-driver-content
description: DISTRIBUTED SCAN DEVICE WEB SERVICE PROTOCOL SUMMARY
ms.assetid: de9925b1-be55-4d22-8255-0f0b8744ee75
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DISTRIBUTED SCAN DEVICE WEB SERVICE PROTOCOL SUMMARY


The Distributed Scan Device Web Service (WS-DSD) protocol uses a subset of the elements of the WS-Scan Service schema for its request, response, and event messages. For more information about this schema, see [Web Services on Devices Scan Service Schema](https://msdn.microsoft.com/library/windows/hardware/ff547963).

A client and a service host use the WS-DSD protocol to communicate over a network connection. The client sends the host messages that contain service requests, and the host sends messages that contain responses to the requests. In addition, the host sends messages to the client that contain notifications of events that have occurred on the host.

The client is a control point (typically, a desktop computer) that runs a DSM administration application like the scan-management console (SMC). The service host is a DSM device (typically, a standalone scanner or a scanner function in a copier or multifunction printer) that implements the host side of the Distributed Scan Device Web Service protocol.

The Distributed Scan Device Web Service protocol supports the following operations:

-   Get a summary of all currently active scan jobs in the DSM device.

    Uses WS-DSD schema elements [**GetActiveJobsRequest**](https://msdn.microsoft.com/library/windows/hardware/ff541599) and [**GetActiveJobsResponse**](https://msdn.microsoft.com/library/windows/hardware/ff541611), and WS-Scan Service schema element **ListOfSummarysType**.

-   Get a set of elements that contain parameter values for a scan job.

    Uses WS-DSD schema elements [**GetJobElementsRequest**](https://msdn.microsoft.com/library/windows/hardware/ff541653) and [**GetJobElementsResponse**](https://msdn.microsoft.com/library/windows/hardware/ff541711), and WS-Scan Service schema elements **RequestedJobElementsType** and **JobElementsType** ..

-   Get the history of a recently completed scan jobs.

    Uses WS-DSD schema elements [**GetJobHistoryRequest**](https://msdn.microsoft.com/library/windows/hardware/ff542572) and [**GetJobHistoryResponse**](https://msdn.microsoft.com/library/windows/hardware/ff542582)**,** and WS-Scan Service schema element **ListOfSummarysType**.

-   Get a set of elements that contain configuration settings for a DSM device.

    Uses WS-DSD schema elements [**GetScannerElementsRequest**](https://msdn.microsoft.com/library/windows/hardware/ff542654) and [**GetScannerElementsResponse**](https://msdn.microsoft.com/library/windows/hardware/ff542671), and WS-Scan Service schema elements **RequestedScannerElementsType** and **ScannerElementsType**.

-   Validate a scan ticket.

    Uses WS Scan Service schema elements [**ValidateScanTicketRequest**](https://msdn.microsoft.com/library/windows/hardware/ff549049) and [**ValidateScanTicketResponse**](https://msdn.microsoft.com/library/windows/hardware/ff549074)**,** and WS-Scan Service schema elements **ScanTicketType** and **ValidationInfoType**.

The Distributed Scan Device Web Service schema defines the following event elements:

-   Notify a client that a scan job has completed.

    Uses WS-DSD schema element [**JobEndStateEvent**](https://msdn.microsoft.com/library/windows/hardware/ff545105)**,** and WS-Scan Service schema element **JobStatusType**.

-   Notify a client that the status of a scan job has changed.

    Uses WS-DSD schema element [**JobStatusEvent**](https://msdn.microsoft.com/library/windows/hardware/ff545167)**,** and WS-Scan Service schema element **JobStatusType**.

-   Notify a client that one or more of the scanner elements [**ScannerDescription**](https://msdn.microsoft.com/library/windows/hardware/ff547372), [**ScannerConfiguration**](https://msdn.microsoft.com/library/windows/hardware/ff547366), and [**DefaultScanTicket**](https://msdn.microsoft.com/library/windows/hardware/ff540494), used by a DSM device, have changed.

    Uses WS-DSD schema element [**ScannerElementsChangeEvent**](https://msdn.microsoft.com/library/windows/hardware/ff547385)**,** and WS-Scan Service schema element **ElementChangesType**.

-   Notify a client that a previously reported scanner status condition has been cleared at the scanner.

    Uses WS-DSD schema element [**ScannerStatusConditionClearedEvent**](https://msdn.microsoft.com/library/windows/hardware/ff547462)**,** and WS-Scan Service schema element **DeviceConditionClearedType**.

-   Provide the client with detailed information about a single status change (described by a [**DeviceCondition**](https://msdn.microsoft.com/library/windows/hardware/ff540552) element) in the DSM device.

    Uses WS-DSD schema element [**ScannerStatusConditionEvent**](https://msdn.microsoft.com/library/windows/hardware/ff547491).

-   Inform the client that the status of the DSM device has changed.

    Uses WS-DSD schema element [**ScannerStatusSummaryEvent**](https://msdn.microsoft.com/library/windows/hardware/ff547525), and WS-Scan Service schema element **StatusSummaryType**.

    .

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20DISTRIBUTED%20SCAN%20DEVICE%20WEB%20SERVICE%20PROTOCOL%20SUMMARY%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


