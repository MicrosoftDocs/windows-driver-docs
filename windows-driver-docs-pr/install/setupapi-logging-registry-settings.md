---
title: SetupAPI Logging Registry Settings
description: SetupAPI Logging Registry Settings
ms.assetid: 24694bce-5941-479f-9e2d-f9c7577a4f6a
keywords:
- SetupAPI logging WDK Windows Vista , registry settings
- registry WDK SetupAPI logging
- event levels WDK SetupAPI logging
- event categories WDK SetupAPI logging
- text logs WDK SetupAPI , registry entries
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SetupAPI Logging Registry Settings


[SetupAPI](setupapi.md) logging supports a global *event level* and a global *event category* that control whether information is written to a text log. The event level controls the level of detail that is written to a text log and the event category determines the type of operations that can make log entries. If a log entry has an event level numerically less than or equal to the global event level of a text log, and if the event category of the log entry is enabled for the text log, the log entry is written to the text log; otherwise, the log entry is not written to the text log.

For information about how to set the event level, see [Setting the Event Level for a Text Log](setting-the-event-level-for-a-text-log.md).

For information about how to set the event categories that are enabled for a log, see [Enabling Event Categories for a Text Log](enabling-event-categories-for-a-text-log.md).

By default, the SetupAPI text logs are located in the %*SystemRoot*%*\\Inf* directory. For information about how to change the directory where the text logs are located, see [Setting the Directory Path of the Text Logs](setting-the-directory-path-of-the-text-logs.md).

 

 





