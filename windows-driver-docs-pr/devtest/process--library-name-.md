---
title: Process library name
description: Process library name
ms.assetid: 4c075256-1e2a-498f-b738-890580392156
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Process &lt;library name&gt;


SDV reports this error when it detects that a driver depends on a library that it has not processed.

As a best practice, this error message should be regarded as indicating an error. Because the libraries might include code that changes the verification result, the verification is not reliable until it is run with all dependent libraries.

However, because some libraries cannot be processed, either because the source code is not available, or because the library is not written in C, SDV does not terminate the verification. It continues the verification without the library code. The user must determine if the verification is still valid without the libraries.

To process a library, in the library's sources directory, type **staticdv /lib**.

For more information about library processing, see [Library Processing in Static Driver Verifier](library-processing-in-static-driver-verifier.md).

 

 





