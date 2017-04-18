---
title: Saving a Group Log
description: Saving a Group Log
ms.assetid: 3e572e3e-68c9-4161-97bd-f93505ead496
keywords: ["grouping trace sessions", "trace sessions WDK , groups", "saving trace group logs", "log files WDK TraceView , group logs", "log files WDK TraceView"]
---

# Saving a Group Log


Membership in a trace session group does not affect the content of the event trace log (.etl) files or the TraceView listing (.out) files for the trace sessions in the group. They continue to record data about only one trace session.

To create a record of the messages for the group as they appear in the [Trace Message List](trace-message-lists.md), copy the messages from the group Trace Message List and paste them into a document that you can save, such as a text or spreadsheet file.

Because the arrival of trace messages in the [Trace Session List](trace-session-list.md) is affected by the message rate, the buffer size, and the flush timer for each trace session, trace messages from different sessions that arrive together might actually have occurred at quite different times. For a more accurate view of the combined trace messages, sort them by the timestamp (in the **System Time** column) of each message.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Saving%20a%20Group%20Log%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




