---
title: What is a Network Redirector
description: What is a Network Redirector
ms.assetid: 5c966d92-7796-4cba-a90e-8c83240655ce
keywords:
- network redirectors WDK , about network redirectors
- redirector drivers WDK , about network redirectors
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# What is a Network Redirector?


## <span id="ddk_what_is_a_network_redirector_if"></span><span id="DDK_WHAT_IS_A_NETWORK_REDIRECTOR_IF"></span>


A network redirector consists of software components installed on a client computer that is used for accessing files and other resources (printers and plotters, for example) on a remote system. The network redirector sends (or redirects) requests for file operations from local client applications to a remote server where the requests are processed. The network redirector receives responses from the remote server that are then returned to the local application. The network redirector software creates the appearance on the client system that remote files and resources are the same as local files and resources and allows them to be used and manipulated in the same ways.

The network redirector tries to make access to remote resources as transparent as possible for the local client application. If there are network problems, the request may be retried several times before the network redirector gives up and returns an error to the client application.

This section includes the following topic:

[Basic Architecture of a Network Redirector](basic-architecture-of-a-network-redirector.md)

 

 




