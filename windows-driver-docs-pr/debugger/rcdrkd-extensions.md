---
title: RCDRKD Extensions
description: This section describes the RCDRKD debugger extension commands. These commands display WPP trace messages created by drivers.
ms.assetid: 11CEBCED-2C11-4450-A5FB-BC5B48B1E1A3
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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


[WPP Software Tracing](http://go.microsoft.com/fwlink/p?LinkID=251984)

[Using the Framework's Event Logger](http://go.microsoft.com/fwlink/p?LinkID=251985)

[USB 3.0 Extensions](usb-3-extensions.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20RCDRKD%20Extensions%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





