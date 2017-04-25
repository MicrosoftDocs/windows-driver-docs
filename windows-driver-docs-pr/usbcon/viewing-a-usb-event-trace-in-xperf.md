---
Description: This topic describes how to view a USB event trace in Xperf.
title: Viewing a USB Event Trace in Xperf
author: windows-driver-content
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Viewing a USB Event Trace in Xperf


This topic describes how to view a USB event trace in Xperf.

To analyze performance and timing issues, you can use Xperf to view a USB event trace. For example, if you have an event trace log file that is named usb.etl and you have downloaded the Xperf tool, issue the following command to analyze the trace:

```
xperf usb.etl

```

Xperf displays a view of the events in graphical form. The initial view is a timeline view, in which each diamond represents one or more events in this image. The diamonds are color coded according to the event provider.

![windows performance analyzer - xperf](images/xperf.png)

The timeline view graphically presents clusters of event activity. In the graphical view, it is easy to see the periodic nature of event activity at 1-second intervals as USB transfer requests that occurred for the USB mass storage device after the device summary events in this example trace.

You can move the mouse pointer across sections of the timeline and zoom in. This image shows zooming in on the device summary events that occur at the very beginning of the trace.

![windows performance analyzer - xperf](images/xperf1.png)

You can display an event summary table, in a spreadsheet form, for the entire trace or for just a selected interval as shown in this image.

![windows performance analyzer - xperf](images/xperf2.png)

To display a summary table, right-click in the **Generic Events** screen and select **Summary Table**.

The event summary table is a very powerful view because you can drag the columns to reorder them and the view pivots the events based on the new column order. To enable you to focus on items of interest, you can expand or collapse items with identical sort order.

Sometimes Netmon presents USB event data in a more readable form than Xperf, but Netmon lacks the Xperf timeline and table views. To analyze the trace’s events at a particular period of time, you can switch between Xperf and Netmon.

## Related topics
[USB Event Tracing for Windows](usb-event-tracing-for-windows.md)  
[Using Xperf with USB ETW](using-xperf-with-usb-etw.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Viewing%20a%20USB%20Event%20Trace%20in%20Xperf%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


