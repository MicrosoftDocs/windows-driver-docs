---
title: Storing and Transferring Audio Data
description: Storing and Transferring Audio Data
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storing and Transferring Audio Data





Some WIA drivers for Microsoft Windows Me and Windows XP used the following three WIA properties to store audio data:

[**WIA\_IPC\_AUDIO\_AVAILABLE**](./wia-ipc-audio-available.md)

[**WIA\_IPC\_AUDIO\_DATA**](./wia-ipc-audio-data.md)

[**WIA\_IPC\_AUDIO\_DATA\_FORMAT**](./wia-ipc-audio-data-format.md)

These properties are obsolete and should no longer be used.

Audio for a picture item should be represented as an attachment. This provides easy access to all audio formats that the WIA minidriver supports. Audio content is transferred in the same way that other items in the WIA item tree are transferred.

 

