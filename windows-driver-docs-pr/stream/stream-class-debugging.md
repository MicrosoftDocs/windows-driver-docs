---
title: Stream Class Debugging
author: windows-driver-content
description: Stream Class Debugging
ms.assetid: 544b922b-58e4-4cbb-a76c-d8e13ae17e55
keywords: ["Stream.sys class driver WDK Windows 2000 Kernel , debugging", "streaming minidrivers WDK Windows 2000 Kernel , debugging", "minidrivers WDK Windows 2000 Kernel Streaming , debugging", "debugging stream class minidrivers WDK Windows 2000 Kernel"]
---

# Stream Class Debugging


## <a href="" id="ddk-stream-class-debugging-ksg"></a>


Use the checked (debug) version of *stream.sys* to print out informative messages about the status of the minidriver and ASSERT when errors in the minidriver are encountered.

The following, additional tips can be used when debugging stream class minidrivers:

-   When debugging with the wdeb386 debugger (or with Softice) on Windows Me systems, debugging information is available by breaking into the debugger, typing .NTKERN, and then selecting option D. This displays the debug log, which shows entries in chronological order. When debugging with Windows 2000, the debug information is printed to the debug terminal in real time.

-   To adjust the output level of the debugger, load *stream.sys* symbols (*stream.sym* for Windows Me and *stream.sys* for Windows 2000) and modify the *StreamDebug* variable with "e StreamDebug *xx*". The default is 00, which prints only severe errors. Set it to FF to print all messages.

-   Minidrivers can print their own messages, using *stream.sys* facilities previously described, by calling [**StreamClassDebugPrint**](https://msdn.microsoft.com/library/windows/hardware/ff568235). Note that the output level as previously described must be set to be greater than or equal to the output level chosen in the call.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Stream%20Class%20Debugging%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


