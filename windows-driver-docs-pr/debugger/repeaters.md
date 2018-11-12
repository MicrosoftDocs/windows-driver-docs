---
title: Repeaters
description: Repeaters
ms.assetid: 10f4f033-f6c1-4b4f-a35f-eadb4e15686d
keywords: ["remote debugging through a repeater", "repeater", "repeater, overview", "DbEngPrx", "DbEngPrx, overview"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Repeaters


## <span id="ddk_repeaters_dbg"></span><span id="DDK_REPEATERS_DBG"></span>


A *repeater* is a lightweight proxy server that runs on a computer and relays data between two other computers. The repeater does not process the data in any way. The two other computers barely notice the repeater; from their perspective it seems as if they are directly connected to each other.

The processes running on these two other computers are called the *server* and the *client*. There is not any fundamental difference between them from the repeater's point of view, except that in most cases the server is started first, then the repeater, and finally the client.

The Debugging Tools for Windows package includes a repeater called DbEngPrx (dbengprx.exe).

This section includes:

[**Activating a Repeater**](activating-a-repeater.md)

[Using a Repeater](using-a-repeater.md)

[Repeater Examples](repeater-examples.md)

 

 





