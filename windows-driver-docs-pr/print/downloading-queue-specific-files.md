---
title: Downloading Queue-Specific Files
description: Downloading Queue-Specific Files
ms.assetid: b6aad46a-2934-461a-ad11-6ad699687fc1
keywords:
- downloading queue-specific printer files
- Point and Print WDK , queue-specific files
- queue-specific files WDK printer
- print queues WDK , Point and Print
- queues WDK printer , Point and Print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Downloading Queue-Specific Files





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

```cpp
AddPrinterConnection("\\NTPRINT\HpColor")
```

On the server, the spooler loads Mscms.dll and calls [**GenerateCopyFilePaths**](https://msdn.microsoft.com/library/windows/hardware/ff549896) as follows:

```cpp
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

```cpp
SourceDir: \\NTPRINT\PRINT$\Color
TargetDir: "Color"
```

On the client, the value for **TargetDir** expands to C:\\Winnt\\System32\\Spool\\Drivers\\Color.

The spooler on MyClient performs the following operations:

-   Downloads Mscms.dll and calls [**GenerateCopyFilePaths**](https://msdn.microsoft.com/library/windows/hardware/ff549896) as follows:

    ```cpp
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

 

 




