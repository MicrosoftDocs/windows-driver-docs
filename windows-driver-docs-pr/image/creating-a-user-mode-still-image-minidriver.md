---
title: Creating a User-Mode Still Image Minidriver
description: Creating a User-Mode Still Image Minidriver
ms.assetid: 94fdbeba-5b4a-4b66-b381-ec362b6d38c9
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating a User-Mode Still Image Minidriver





All user-mode still image minidrivers must implement the interface methods defined by [IStiUSD COM Interface](istiusd-com-interface.md). This implementation is relatively easy, using the following procedure.

**To implement the methods defined by the IStiUSD COM interface:**

1.  Obtain a GUID for the interface, and include it in a header file and a setup information (INF) file.

2.  Create a implementation file such as ( .cpp).

3.  Create a customized class definition, using **IStiUSD** as an inherited class.

4.  Implement all of the methods that have been defined for the [IStiUSD COM Interface](istiusd-com-interface.md). If a method is not needed, it must return STIERR\_UNSUPPORTED.

This section provides information about the following topics:

[Still Image Device Events](still-image-device-events.md)

[Transfer Modes](transfer-modes.md)

[Security Issues for Still Image Drivers](security-issues-for-still-image-drivers.md)

 

 




