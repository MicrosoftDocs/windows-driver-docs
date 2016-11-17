---
title: Downloading Queue-Specific Files
author: windows-driver-content
description: Downloading Queue-Specific Files
MS-HAID:
- 'prtinst\_7c16afd8-3364-4262-bc16-125817806499.xml'
- 'print.downloading\_queue\_specific\_files'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: b6aad46a-2934-461a-ad11-6ad699687fc1
keywords: ["downloading queue-specific printer files", "Point and Print WDK , queue-specific files", "queue-specific files WDK printer", "print queues WDK , Point and Print", "queues WDK printer , Point and Print"]
---

# Downloading Queue-Specific Files


## <a href="" id="ddk-downloading-queue-specific-files-gg"></a>


If a user decides to create a printer connection from his or her client system to a print server, and if an installation application has created the registry entries described in [Supporting Point and Print During Printer Installations](supporting-point-and-print-during-printer-installations.md), the following events occur:

1.  The user application calls **AddPrinterConnection**, which is described in the Microsoft Windows SDK documentation.

2.  The client's remote print provider (Win32spl.dll) creates a connection to the server.

3.  The server's spooler sends driver files to the client.

4.  The client's Win32spl.dll calls EnumPrinterKey and EnumPrinterDataEx on the server to copy the printer's registry entries.

5.  As the server's spooler enumerates registry values during processing of EnumPrinterDataEx, it performs the following operations each time it encounters a subkey of the printer's **CopyFiles** key, such as **CopyFiles\\ICM**:
    -   Loads the [Point and Print DLL](point-and-print-dlls.md), if specified, and calls its [**GenerateCopyFilePaths**](https://msdn.microsoft.com/library/windows/hardware/ff549896) function, which can modify source and/or destination paths.
    -   Creates **SourceDir** and **TargetDir** keys, based on source and destination paths returned by **GenerateCopyFilePaths**, and returns them to the client spooler as EnumPrinterDataEx data. (These keys do not really exist on the server.)

6.  The client's Win32spl.dll caches printer keys received in response to EnumPrinterData and EnumPrinterDataEx calls.

7.  For each subkey of the printer's **CopyFiles** key, such as **CopyFiles\\ICM**, the client's Win32spl.dll performs the following operations:
    -   Loads the local Point and Print DLL, if one is provided, and calls its **GenerateCopyFilePaths** function, which can modify source and/or destination paths. (Inputs are the **SourceDir** and **TargetDir** keys received from the server.)
    -   Downloads all files associated with the **Files** key from the server.
    -   Logs an event, indicating Point and Print files were downloaded.
    -   Calls the Point and Print DLL's [**SpoolerCopyFileEvent**](https://msdn.microsoft.com/library/windows/hardware/ff562681) function, if a DLL is provided, specifying a COPYFILE\_EVENT\_FILES\_CHANGED event.

8.  The client spooler calls the driver's [**DrvPrinterEvent**](https://msdn.microsoft.com/library/windows/hardware/ff548564) function, specifying a PRINTER\_EVENT\_CACHE\_REFRESH event.

9.  The client spooler calls the driver's [**DrvPrinterEvent**](https://msdn.microsoft.com/library/windows/hardware/ff548564) function again, specifying a PRINTER\_EVENT\_ADD\_CONNECTION event.

10. If a Point and Print DLL is provided, the client spooler calls its [**SpoolerCopyFileEvent**](https://msdn.microsoft.com/library/windows/hardware/ff562681) function, specifying a COPYFILE\_EVENT\_ADD\_PRINTER\_CONNECTION event.

### Connection Example

As an example, assume that an installation application has defined the server registry entries described in the installation example. Additionally, assume that the server is named NTPRINT and the client is named MyClient.

To connect to the print queue named HpColor on NTPRINT, a user application on MyClient calls **AddPrinterConnection** as follows:

```
AddPrinterConnection("\\NTPRINT\HpColor")
```

On the server, the spooler loads Mscms.dll and calls [**GenerateCopyFilePaths**](https://msdn.microsoft.com/library/windows/hardware/ff549896) as follows:

```
GenerateCopyFilePaths(
    "HpColor",
    "Color",
    &SplclientInfo1,
    1,
    \\NTPRINT\PRINT$\Color,
    &dwSourceDirSize,
    "Color",
    &dwDestDirSize,
    COPYFILE_FLAG_SERVER_SPOOLER)
```

Microsoft ICM's Mscms.dll module does not modify the source or destination paths, so it just returns ERROR\_SUCCESS.

The server spooler returns the following keys to MyClient:

```
SourceDir: \\NTPRINT\PRINT$\Color
TargetDir: "Color"
```

On the client, the value for **TargetDir** expands to C:\\Winnt\\System32\\Spool\\Drivers\\Color.

The spooler on MyClient performs the following operations:

-   Downloads Mscms.dll and calls [**GenerateCopyFilePaths**](https://msdn.microsoft.com/library/windows/hardware/ff549896) as follows:

    ```
    GenerateCopyFilePaths(
        "\\NTPRINT\HpColor",
        "Color",
        &SplclientInfo1,
        1,
        \\NTPRINT\PRINT$\Color,
        &dwSourceDirSize,
        "C:\Winnt\System32\Spool\Drivers\Color",
        &dwDestDirSize,
        COPYFILE_FLAG_CLIENT_SPOOLER)
    ```

    Microsoft ICM's Mscms.dll module does not modify the source or destination paths, so it just returns ERROR\_SUCCESS.

-   Downloads Hpclrlsr.icm to C:\\Winnt\\System32\\Spool\\Drivers\\Color.

-   Logs an event, indicating Point and Print files were downloaded.

-   Calls the [**SpoolerCopyFileEvent**](https://msdn.microsoft.com/library/windows/hardware/ff562681) function in Mscms.dll, specifying a COPYFILE\_EVENT\_FILES\_CHANGED event.

-   Calls the printer driver's [**DrvPrinterEvent**](https://msdn.microsoft.com/library/windows/hardware/ff548564) function, specifying a PRINTER\_EVENT\_CACHE\_REFRESH event.

-   Calls the printer driver's [**DrvPrinterEvent**](https://msdn.microsoft.com/library/windows/hardware/ff548564) function again, specifying a PRINTER\_EVENT\_ADD\_CONNECTION event.

-   Calls the [**SpoolerCopyFileEvent**](https://msdn.microsoft.com/library/windows/hardware/ff562681) function in Mscms.dll, specifying a COPYFILE\_EVENT\_ADD\_PRINTER\_CONNECTION event.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Downloading%20Queue-Specific%20Files%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


