---
title: What is a Network Redirector
description: What is a Network Redirector
ms.assetid: 5c966d92-7796-4cba-a90e-8c83240655ce
keywords: ["network redirectors WDK , about network redirectors", "redirector drivers WDK , about network redirectors"]
---

# What is a Network Redirector?


## <span id="ddk_what_is_a_network_redirector_if"></span><span id="DDK_WHAT_IS_A_NETWORK_REDIRECTOR_IF"></span>


A network redirector consists of software components installed on a client computer that is used for accessing files and other resources (printers and plotters, for example) on a remote system. The network redirector sends (or redirects) requests for file operations from local client applications to a remote server where the requests are processed. The network redirector receives responses from the remote server that are then returned to the local application. The network redirector software creates the appearance on the client system that remote files and resources are the same as local files and resources and allows them to be used and manipulated in the same ways.

The network redirector tries to make access to remote resources as transparent as possible for the local client application. If there are network problems, the request may be retried several times before the network redirector gives up and returns an error to the client application.

This section includes the following topic:

[Basic Architecture of a Network Redirector](basic-architecture-of-a-network-redirector.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20What%20is%20a%20Network%20Redirector?%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




