---
title: Security
author: windows-driver-content
description: Security
ms.assetid: 2d2cd7be-fc19-4714-af07-38a032f1ab02
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Security


The DSM device must provide the following security features:

-   A certificate manager to manage X.509 certificates, maintain an up-to-date trusted root certificate store for connections to DSM scan servers, validate the certificates received from DSM scan servers, and verify that the certificate for a DSM scan server is a trusted root certificate.

-   The ability to create an HTTPS connection to a DSM scan server specified in a scan process.

-   The ability to access a user's X.509 certificate and to use this certificate to create an HTTPS connection to a DSM scan server.

For more information about X.509 certificates, see the [X.509 Certificate Profile](http://go.microsoft.com/fwlink/p/?linkid=70416).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Security%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


