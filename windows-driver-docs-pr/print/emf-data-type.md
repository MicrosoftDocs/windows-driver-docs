---
title: EMF Data Type
description: EMF Data Type
ms.assetid: d5a05778-3637-4dba-b036-5f0fc236d52d
keywords: ["print processors WDK , data types", "data types WDK print processor", "EMF data type WDK print processor"]
---

# EMF Data Type


## <a href="" id="ddk-emf-data-type-gg"></a>


Enhanced Metafile (EMF) data consists of instructions to call GDI functions. The print processor must call the GDI functions to render printable images. The GDI functions make calls to the printer driver's [printer graphics DLL](printer-graphics-dll.md), which renders the image and sends it to the spooler as RAW data (by calling [**EngWritePrinter**](https://msdn.microsoft.com/library/windows/hardware/ff565467)).

NT-based operating system clients send EMF data to NT-based operating system print servers. EMF data is device independent and can be sent to a server more quickly than RAW data. A print job is also spooled as EMF data when the requesting application is local to the server, allowing a quick return to the application while the EMF data is subsequently rendered by a background spooler thread.

For more information about the EMF data type, see the *Windows 2000 Professional Resource Kit* or the *Windows 2000 Server Resource Kit*. For more information about enhanced metafiles, see the Windows SDK documentation. (These resources may not be available in some languages and countries.)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20EMF%20Data%20Type%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




