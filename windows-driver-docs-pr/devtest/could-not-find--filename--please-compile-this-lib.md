---
title: Could not find filename please compile this lib
description: Could not find filename please compile this lib
ms.assetid: e572ed6d-a3f3-402a-aa99-66c503de8457
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Could not find &lt;filename&gt; please compile this lib


This warning appears when SDV detects that a driver requires a library, but it cannot find one or more of the files that it creates when processing a library with the **staticdv /lib** command. This situation can occur when the library has not been processed or because files have been deleted.

Because library processing is recommended, but not required, SDV continues with the verification after displaying this message.

To process or reprocess a library that the driver requires, use the **staticdv /lib** command. Do not delete any files in the driver's sources directory or the library's sources directory. You do not need to delete any files before reprocessing a library that has already been processed.

For more information about processing libraries, see [Library Processing in SDV](library-processing-in-static-driver-verifier.md)

 

 





