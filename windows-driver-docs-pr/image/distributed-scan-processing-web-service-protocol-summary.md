---
title: Distributed Scan Processing Web Service Protocol Summary
author: windows-driver-content
description: Distributed Scan Processing Web Service Protocol Summary
ms.assetid: c800383b-77d2-42cc-9fc5-c96ea0c0183f
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Distributed Scan Processing Web Service Protocol Summary


The Distributed Scan Processing Web Service protocol uses the elements of the Distributed Scan Processing Web Service schema for its request, response, and event messages. For more information about this schema, see [Distributed Scan Processing Web Service Schema](https://msdn.microsoft.com/library/windows/hardware/ff541133).

A client and a service host use the Distributed Scan Processing Web Service protocol to communicate over a network connection. The client sends service request messages to the host, and the host sends messages that contain responses to the requests. In addition, the host sends messages to the client that contains notifications of events that have occurred on the host.

The client is a DSM device (a standalone scanner or a scanner function in a copier or multifunction printer) that implements the client side of the Distributed Scan Processing Web Service protocol. The service host is a DSM scan server that runs post-scan processing jobs at the behest of the client. The client and host use the Distributed Scan Processing Web Service protocol to communicate over a network connection.

The Distributed Scan Processing Web Service protocol supports the following operations:

-   Cancel a post-scan job.

    Uses Distributed Scan Processing Web Service schema elements [CancelPostScanJobRequest](https://msdn.microsoft.com/library/windows/hardware/ff539442) and [CancelPostScanJobResponse](https://msdn.microsoft.com/library/windows/hardware/ff539450)

-   Create a post-scan job.

    Uses Distributed Scan Processing Web Service schema elements [CreatePostScanJobRequest](https://msdn.microsoft.com/library/windows/hardware/ff540230) and [CreatePostScanJobResponse](https://msdn.microsoft.com/library/windows/hardware/ff540247).

-   End a post-scan job.

    Uses Distributed Scan Processing Web Service schema elements [EndPostScanJobRequest](https://msdn.microsoft.com/library/windows/hardware/ff541328) and [EndPostScanJobResponse](https://msdn.microsoft.com/library/windows/hardware/ff541338).

-   Get a collection of scan processing elements.

    Uses Distributed Scan Processing Web Service schema elements [GetPostScanJobElementRequest](https://msdn.microsoft.com/library/windows/hardware/ff542596) and [GetPostScanJobElementResponse](https://msdn.microsoft.com/library/windows/hardware/ff542602).

-   Send an image to a post-scan job.

    Uses Distributed Scan Processing Web Service schema elements [SendImageRequest](https://msdn.microsoft.com/library/windows/hardware/ff548054) and [SendImageResponse](https://msdn.microsoft.com/library/windows/hardware/ff548110).

The Distributed Scan Processing Web Service schema defines the following event elements:

-   Notify a client that a post-scan job has completed.

    Uses Distributed Scan Processing Web Service schema element [PostScanJobEndStateEvent](https://msdn.microsoft.com/library/windows/hardware/ff546249)

-   Notify a client that the status of a post-scan job has changed.

    Uses Distributed Scan Processing Web Service schema element [PostScanJobStatusEvent](https://msdn.microsoft.com/library/windows/hardware/ff546316)

 

 




