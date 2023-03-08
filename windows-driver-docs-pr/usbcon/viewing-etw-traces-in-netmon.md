---
title: Overview of USB ETW traces in Netmon
description: You can view USB ETW event traces using Microsoft Network Monitor, also referred to as Netmon.
ms.date: 03/08/2023
---

# Overview of USB ETW traces in Netmon

You can view USB ETW event traces using Microsoft Network Monitor, also referred to as Netmon. Netmon does not parse the trace automatically. It requires USB ETW parsers. USB ETW parsers are text files, written in Network Monitor Parser Language (NPL), that describe the structure of USB ETW event traces. The parsers also define USB-specific columns and filters. These parsers make Netmon the best tool for analyzing USB ETW traces.

## In this section

| Topic | Description |
|---|---|
| [How to install Netmon and USB ETW Parsers](how-to-install-netmon-and-the-netmon-usb-parser.md) | This topic provides installation information about Netmon and the USB ETW parsers. |
| [How to view a USB ETW trace in Netmon](how-to-examining-a-trace-file-by-using-netmon.md) | This topic describes how to example a event trace file by using Netmon. |
| [Debugging USB device issues by using ETW events](best-practices--debugging-usb-device-problems.md) | This topic provides tips for debugging USB device problems by using ETW events. |
| [Case Study: Troubleshooting an unknown USB device by using ETW and Netmon](case-study--troubleshooting-an-unknown-usb-device-by-using-etw-and-netmon.md) | This topic provides an example of how to use USB ETW and Netmon to troubleshoot a USB device that Windows does not recognize. |

## Related topics

- [USB Event Tracing for Windows](usb-event-tracing-for-windows.md)  
