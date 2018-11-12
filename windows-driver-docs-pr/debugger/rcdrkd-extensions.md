---
title: RCDRKD Extensions
description: This section describes the RCDRKD debugger extension commands. These commands display WPP trace messages created by drivers.
ms.assetid: 11CEBCED-2C11-4450-A5FB-BC5B48B1E1A3
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# RCDRKD Extensions


This section describes the RCDRKD debugger extension commands. These commands display WPP trace messages created by drivers. Starting with Windows 8, you no longer need a separate trace message format (TMF) file to parse WPP messages. The TMF information is stored in the regular symbol file (PDB file).

Starting in Windows 10, kernel-mode and user-mode drivers can use [Inflight Trace Recorder (IFR) for logging traces](https://msdn.microsoft.com/library/windows/hardware/dn914610). Your kernel-mode driver can use the RCDRKD commands to read messages from the circular buffers, format the messages, and display the messages in the debugger.

**Note**  You cannot use the RCDRKD commands to view UMDF driver logs, UMDF framework logs, and KMDF framework logs. To view those logs, use [Windows Driver Framework Extensions (Wdfkd.dll)](kernel-mode-driver-framework-extensions--wdfkd-dll-.md) commands.

 

The RCDRKD debugger extension commands are implemented in Rcdrkd.dll. To load the RCDRKD commands, enter **.load rcdrkd.dll** in the debugger.

The following two commands are the primary commands for displaying trace messages.

-   [**!rcdrkd.rcdrlogdump**](-rcdrkd-rcdrlogdump.md)
-   [**!rcdrkd.rcdrcrashdump**](-rcdrkd-rcdrcrashdump.md)

The following auxiliary commands provide services related to displaying and saving trace messages.

-   [**!rcdrkd.rcdrloglist**](-rcdrkd-rcdrloglist.md)
-   [**!rcdrkd.rcdrlogsave**](-rcdrkd-rcdrlogsave.md)
-   [**!rcdrkd.rcdrsearchpath**](-rcdrkd-rcdrsearchpath.md)
-   [**!rcdrkd.rcdrsettraceprefix**](-rcdrkd-rcdrsettraceprefix.md)
-   [**!rcdrkd.rcdrtmffile**](-rcdrkd-rcdrtmffile.md)
-   [**!rcdrkd.rcdrtraceprtdebug**](-rcdrkd-rcdrtraceprtdebug.md)

The [**!rcdrkd.rcdrhelp**](-rcdrkd-rcdrhelp.md) displays help for the RCDRKD commands in the debugger.

## <span id="related_topics"></span>Related topics


[WPP Software Tracing](https://go.microsoft.com/fwlink/p?LinkID=251984)

[Using the Framework's Event Logger](https://go.microsoft.com/fwlink/p?LinkID=251985)

[USB 3.0 Extensions](usb-3-extensions.md)

 

 






