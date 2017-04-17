---
title: RAW Data Type
author: windows-driver-content
description: RAW Data Type
ms.assetid: f53264c1-97aa-42f0-8bab-76bf984f2c79
keywords: ["print processors WDK , data types", "data types WDK print processor", "RAW data type WDK print processor"]
---

# RAW Data Type


## <a href="" id="ddk-raw-data-type-gg"></a>


RAW data can be sent to a print monitor without further processing. The print processor just sends this data back to the spooler (by calling **WritePrinter**, described in the Microsoft Windows SDK documentation), sometimes inserting form feeds. An example of a RAW data file is one consisting of [*printer control language (PCL)*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-printer-control-language--pcl-) commands. Print jobs are sent from client to server in RAW format if either the client or the server does not support NT-based-operating system EMF, or if a server administrator has disabled EMF support. In such cases, image rendering is performed on the client before the job is sent to the server.

Postscript commands can be considered RAW data if the target printer supports Postscript. On the other hand, the Sfmpsprt.dll print processor takes Postscript input and interprets it for non-Postscript printers, so in that case the Postscript is not RAW data.

For more information about the RAW data type, see the *Windows 2000 Professional Resource Kit* or the *Windows 2000 Server Resource Kit*. (These resources may not be available in some languages and countries.)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20RAW%20Data%20Type%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


