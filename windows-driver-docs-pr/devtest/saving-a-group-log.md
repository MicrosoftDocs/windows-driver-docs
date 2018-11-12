---
title: Saving a Group Log
description: Saving a Group Log
ms.assetid: 3e572e3e-68c9-4161-97bd-f93505ead496
keywords:
- grouping trace sessions
- trace sessions WDK , groups
- saving trace group logs
- log files WDK TraceView , group logs
- log files WDK TraceView
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Saving a Group Log


Membership in a trace session group does not affect the content of the event trace log (.etl) files or the TraceView listing (.out) files for the trace sessions in the group. They continue to record data about only one trace session.

To create a record of the messages for the group as they appear in the [Trace Message List](trace-message-lists.md), copy the messages from the group Trace Message List and paste them into a document that you can save, such as a text or spreadsheet file.

Because the arrival of trace messages in the [Trace Session List](trace-session-list.md) is affected by the message rate, the buffer size, and the flush timer for each trace session, trace messages from different sessions that arrive together might actually have occurred at quite different times. For a more accurate view of the combined trace messages, sort them by the timestamp (in the **System Time** column) of each message.

 

 





