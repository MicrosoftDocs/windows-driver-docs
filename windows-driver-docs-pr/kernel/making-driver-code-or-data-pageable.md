---
title: Making Driver Code or Data Pageable
author: windows-driver-content
description: Making Driver Code or Data Pageable
ms.assetid: c4ffd222-8ea5-48df-9c79-7d68e5462b3e
keywords: ["memory management WDK kernel , pageable drivers", "pageable drivers WDK kernel , setting up"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Making Driver Code or Data Pageable


## <a href="" id="ddk-making-driver-code-or-data-pageable-kg"></a>


To make a driver routine pageable, you must make sure that it runs at IRQL &lt; DISPATCH\_LEVEL and that it does not acquire any spin locks.

This section contains the following topics:

[Detecting Code That Can Be Pageable](detecting-code-that-can-be-pageable.md)

[Isolating Pageable Code](isolating-pageable-code.md)

[Locking Pageable Code or Data](locking-pageable-code-or-data.md)

[Paging an Entire Driver](paging-an-entire-driver.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Making%20Driver%20Code%20or%20Data%20Pageable%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


