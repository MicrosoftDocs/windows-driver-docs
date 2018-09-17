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
ms.localizationpriority: medium
---

# Security


The DSM device must provide the following security features:

-   A certificate manager to manage X.509 certificates, maintain an up-to-date trusted root certificate store for connections to DSM scan servers, validate the certificates received from DSM scan servers, and verify that the certificate for a DSM scan server is a trusted root certificate.

-   The ability to create an HTTPS connection to a DSM scan server specified in a scan process.

-   The ability to access a user's X.509 certificate and to use this certificate to create an HTTPS connection to a DSM scan server.

For more information about X.509 certificates, see the [X.509 Certificate Profile](http://go.microsoft.com/fwlink/p/?linkid=70416).

 

 




