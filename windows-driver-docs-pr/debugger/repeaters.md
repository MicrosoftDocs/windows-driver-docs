---
title: Repeaters
description: Repeaters
ms.assetid: 10f4f033-f6c1-4b4f-a35f-eadb4e15686d
keywords: ["remote debugging through a repeater", "repeater", "repeater, overview", "DbEngPrx", "DbEngPrx, overview"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Repeaters%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




