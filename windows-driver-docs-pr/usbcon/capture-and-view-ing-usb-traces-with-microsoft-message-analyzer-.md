---
Description: 'You can use Microsoft Message Analyzer (MMA) to capture and view live USB traces, or view an existing trace.'
MS-HAID: 'buses.capture\_and\_view\_ing\_usb\_traces\_with\_microsoft\_message\_analyzer\_'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
Search.SourceType: Video
title: Capture and view USB traces with Microsoft Message Analyzer
---

# Capture and view USB traces with Microsoft Message Analyzer


**Summary**

-   Microsoft Message Analyzer installation and setup
-   Capture and view live USB traces

You can use Microsoft Message Analyzer (MMA) to capture and view live USB traces, or view an existing trace.

Instead of capturing traces by using the command line tool, logman, and then parsing them in Netmon 3.4, you can perform all those tasks from a single GUI.

## Install and launch Microsoft Message Analyzer


1.  [Download Microsoft Message Analyzer](http://www.microsoft.com/download/details.aspx?id=40308) and install the tool by following **Install Instructions** on the download page. After downloading, follow the install prompts and select **Update items**.

2.  After installation completes, the tool launches and the start page is shown.

## Set up a trace session and capture USB events


This video demonstrates how to set up Microsoft Message Analyzer for USB traces by adding specific columns. It also shows how to capture a live trace by starting and stopping a session.

**Note**  Under **Device**, choose between USB 2 or USB 3 tracing scenarios. Note that USB 3 tracing is only available on Windows 8 and later versions. Make your selection based on the host controller to which the device is connected, not the speed of the device. For example if you have a high speed device connected to an xHCI controller, choose the USB 3 trace scenario.

 

<iframe src="https://hubs-video.ssl.catalog.video.msn.com/embed/e5300401-351e-4dcc-bcc2-edd07079d7fa/IA?csid=ux-en-us&MsnPlayerLeadsWith=html&PlaybackMode=Inline&MsnPlayerDisplayShareBar=false&MsnPlayerDisplayInfoButton=false&iframe=true&QualityOverride=HD" width="720" height="405" allowFullScreen="true" frameBorder="0" scrolling="no"></iframe>

## Analyze a USB trace


Microsoft Message Analyzer parses the information dynamically as it is captured and displays them in a human-readable form. Most of that information is shown in the **Summary** column. That column displays detailed information about the event, such as, requests the USB driver stack sends to the device. By adding the required filters you can view the results of those requests.

This video demonstrates how you can determine the root cause of a device enumeration failure.

<iframe src="https://hubs-video.ssl.catalog.video.msn.com/embed/29cb1d44-a38a-4105-9513-256e69e9f6a0/IA?csid=ux-en-us&MsnPlayerLeadsWith=html&PlaybackMode=Inline&MsnPlayerDisplayShareBar=false&MsnPlayerDisplayInfoButton=false&iframe=true&QualityOverride=HD" width="720" height="405" allowFullScreen="true" frameBorder="0" scrolling="no"></iframe>

## Related topics


[Blog: Capturing USB ETW traces with Microsoft Message Analyzer (MMA)](http://blogs.msdn.com/b/usbcoreblog/archive/2013/11/09/capturing-usb-etw-traces-with-microsoft-message-analyzer-mma.aspx)

[USB Event Tracing for Windows](usb-event-tracing-for-windows.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Capture%20and%20view%20USB%20traces%20with%20Microsoft%20Message%20Analyzer%20%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




