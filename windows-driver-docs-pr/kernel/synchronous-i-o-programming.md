---
title: Synchronous I/O Programming
description: Synchronous I/O Programming
ms.assetid: ef021dd2-bd1d-4fb0-853f-014c62bda76b
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Synchronous I/O Programming


Synchronous programming simply waits for a call to return. This is fast and efficient from the programmer's point of view but in an environment like Windows where many programs are running at once, it can cause problems. Whenever possible, use [Asynchronous I/O Programming Techniques](asynchronous-i-o-programming.md).

**Note**  For driver developers using Microsoft Vista, this is not as serious a problem. For more information about synchronous programming in Vista, see [Restricting Waits in Vista](restricting-waits-in-vista.md).

 

 

 




