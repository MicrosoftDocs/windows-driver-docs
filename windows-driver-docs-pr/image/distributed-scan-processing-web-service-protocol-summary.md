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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Distributed%20Scan%20Processing%20Web%20Service%20Protocol%20Summary%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


