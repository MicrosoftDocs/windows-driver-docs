---
title: Storing and Transferring Audio Data
description: Storing and Transferring Audio Data
ms.assetid: c8d0af2f-1c3d-49d5-96ca-de1703f85448
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storing and Transferring Audio Data





Some WIA drivers for Microsoft Windows Me and Windows XP used the following three WIA properties to store audio data:

[**WIA\_IPC\_AUDIO\_AVAILABLE**](https://msdn.microsoft.com/library/windows/hardware/ff552530)

[**WIA\_IPC\_AUDIO\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552534)

[**WIA\_IPC\_AUDIO\_DATA\_FORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff552538)

These properties are obsolete and should no longer be used.

Audio for a picture item should be represented as an attachment. This provides easy access to all audio formats that the WIA minidriver supports. Audio content is transferred in the same way that other items in the WIA item tree are transferred.

 

 




