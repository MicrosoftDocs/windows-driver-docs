---
Description: You can use Microsoft Message Analyzer (MMA) to capture and view live USB traces, or view an existing trace.
Search.SourceType: Video
title: Capture and view USB traces with Microsoft Message Analyzer
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Capture and view USB traces with Microsoft Message Analyzer


**Summary**

-   Microsoft Message Analyzer installation and setup
-   Capture and view live USB traces

You can use Microsoft Message Analyzer (MMA) to capture and view live USB traces, or view an existing trace.

Instead of capturing traces by using the command line tool, logman, and then parsing them in Netmon 3.4, you can perform all those tasks from a single GUI.

## Install and launch Microsoft Message Analyzer


1.  [Download Microsoft Message Analyzer](https://www.microsoft.com/download/details.aspx?id=44226) and install the tool by following **Install Instructions** on the download page. After downloading, follow the install prompts and select **Update items**.

2.  After installation completes, the tool launches and the start page is shown.

## Set up a trace session and capture USB events


This video demonstrates how to set up Microsoft Message Analyzer for USB traces by adding specific columns. It also shows how to capture a live trace by starting and stopping a session.

**Note**  Under **Device**, choose between USB 2 or USB 3 tracing scenarios. Note that USB 3 tracing is only available on Windows 8 and later versions. Make your selection based on the host controller to which the device is connected, not the speed of the device. For example if you have a high speed device connected to an xHCI controller, choose the USB 3 trace scenario.

>[!VIDEO https://www.microsoft.com/videoplayer/embed/e5300401-351e-4dcc-bcc2-edd07079d7fa]

## Analyze a USB trace


Microsoft Message Analyzer parses the information dynamically as it is captured and displays them in a human-readable form. Most of that information is shown in the **Summary** column. That column displays detailed information about the event, such as, requests the USB driver stack sends to the device. By adding the required filters you can view the results of those requests.

This video demonstrates how you can determine the root cause of a device enumeration failure.

>[!VIDEO https://www.microsoft.com/videoplayer/embed/29cb1d44-a38a-4105-9513-256e69e9f6a0]

## Related topics
[Blog: Capturing USB ETW traces with Microsoft Message Analyzer (MMA)](http://blogs.msdn.com/b/usbcoreblog/archive/2013/11/09/capturing-usb-etw-traces-with-microsoft-message-analyzer-mma.aspx)  
[USB Event Tracing for Windows](usb-event-tracing-for-windows.md)  



