---
title: Making Driver Code or Data Pageable
description: Making Driver Code or Data Pageable
ms.assetid: c4ffd222-8ea5-48df-9c79-7d68e5462b3e
keywords: ["memory management WDK kernel , pageable drivers", "pageable drivers WDK kernel , setting up"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Making Driver Code or Data Pageable





To make a driver routine pageable, you must make sure that it runs at IRQL &lt; DISPATCH\_LEVEL and that it does not acquire any spin locks.

This section contains the following topics:

[Detecting Code That Can Be Pageable](detecting-code-that-can-be-pageable.md)

[Isolating Pageable Code](isolating-pageable-code.md)

[Locking Pageable Code or Data](locking-pageable-code-or-data.md)

[Paging an Entire Driver](paging-an-entire-driver.md)

 

 




