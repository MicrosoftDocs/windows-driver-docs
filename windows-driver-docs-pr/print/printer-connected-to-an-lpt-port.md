---
title: Printer Connected to an LPT Port
author: windows-driver-content
description: Printer Connected to an LPT Port
ms.assetid: fbc71ae8-9b63-4667-b9d6-fdff9100d70b
keywords:
- LPT enumerator WDK printer
- parallel ports WDK , printer connections
- parallel enumerators WDk printer
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Printer Connected to an LPT Port


## <a href="" id="ddk-printer-connected-to-an-lpt-port-gg"></a>


The LPT enumerator is an example of a [bus driver](https://msdn.microsoft.com/library/windows/hardware/ff540704). The LPT enumerator is capable of obtaining identification information from LPT port hardware that conforms to the *IEEE 1284 Extended Capabilities Port Protocol and ISA Interface Standard*.

When a Windows 2000 or later system starts, the configuration manager calls the LPT enumerator to enumerate the IEEE 1284-compatible devices connected to LPT ports. For each device found, the configuration manager calls the printer class installer. The printer class installer calls **SetupDi**-prefixed [device installation functions](https://msdn.microsoft.com/library/windows/hardware/ff541299), which obtain information from [printer INF files](printer-inf-files.md).

For a parallel-connected printer, the parallel enumerator creates a [*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode) with a unique [*hardware ID*](https://msdn.microsoft.com/library/windows/hardware/ff556288#wdkgloss-hardware-id) generated from the 1284 string it receives from the printer.

An example 1284 string is:

```
"MANUFACTURER:Hewlett-Packard;COMMAND SET:PJL,MLC,PCL,POSTSCRIPT;MODEL:HP Color LaserJet 550;CLASS:PRINTER;COMMENT:HP LaserJet;"
```

From this 1284 string the parallel enumerator produces the following hardware ID:

```
LPTENUM\Hewlett-PackardHP_Co3115
```

The hardware ID is made up of the enumerator prefix, followed by the Manufacturer Name, the Model name, and a cyclic redundancy check (CRC) code. The CRC code, which is the last four digits of the hardware ID, is generated from the manufacturer and model strings. Spaces in the string are replaced with underscores.

To read the 1284 ID string from the device, send [**IOCTL\_PAR\_QUERY\_DEVICE\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff544076). Note that the spooler redirects the LPT*x* symbolic link (where *x* is the LPT number 1, 2, or 3) to the spooler's named pipe, which means that if the spooler is running, then parport never sees the IOCTLs sent to LPTx.

The devnode for a parallel-connected Plug and Play printer is placed under **HKLM\\SYSTEM\\CurrentControlSet\\Enum\\LPTENUM** and has a single hardware ID of the form:

```
LPTENUM\Company_NameModelNam1234
```

The driver stack appears in the figure following the next code sample.

The INF code that will correctly "plug and play" a hardware ID of the form LPTENUM\\*Company\_NameModelNam1234* is shown in the following example. Notice that the "Model Name XYZ" device description appears twice in the [**INF Manufacturer section**](https://msdn.microsoft.com/library/windows/hardware/ff547454). The hardware ID in the first line includes the bus enumerator, while the hardware ID in the second line does not. The two lines guarantee a rank-0 hardware ID match regardless of the type of bus on which the printer is installed. See [Installing a Custom Plug and Play Printer Driver](installing-a-custom-plug-and-play-printer-driver.md) for more information.

```
[Manufacturer]
%Company_Name%=Company_Name

; Section name for all drivers for Company_Name
[Company_Name]
"Model Name XYZ" = Install_Section_XYZ, LPTENUM\Company_NameModelNam1234 ; plus any compatible IDs
"Model Name XYZ" = Install_Section_XYZ, Company_NameModelNam1234 ; plus any compatible IDs

; The install section for the XYZ model
[Install_Section_XYZ]

[Strings]
Company_Name="Company Name"
```

![plug and play for parallel port printers](images/pnppar01.png)

For a printer that shares its [*device ID*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-id) with other models, the INF file should be similar to the following:

```
[Manufacturer]
%Company_Name%=Company_Name

; The section for all drivers for Company_Name
[Company_Name]
"Model Name XYA" = Install_Section_XYA, LPTENUM\Company_NameModelNam1234, Company_NameModelNam1234 ; plus any other compatible IDs
"Model Name XYA" = Install_Section_XYA, Company_NameModelNam1234, Company_NameModelNam1234 ; plus any other compatible IDs
"Model Name XYB" = Install_Section_XYB, LPTENUM\Company_NameModelNam1234, Company_NameModelNam1234; plus any other compatible IDs
"Model Name XYB" = Install_Section_XYB, Company_NameModelNam1234, Company_NameModelNam1234 ; plus any other compatible IDs

; The install sections
[Install_Section_XYA]

[Install_Section_XYB]

[ControlFlags]
InteractiveInstall = LPTENUM\Company_NameModelNam1234, Company_NameModelNam1234

[Strings]
Company_Name = "Company Name"
```

Just as in the previous example, each model in the [**INF Manufacturer section**](https://msdn.microsoft.com/library/windows/hardware/ff547454) is represented by a pair of nearly identical lines. For a given model, one line in the pair includes the bus enumerator; the other does not. The two lines guarantee a rank-0 hardware ID match regardless of the type of bus on which the printer is installed. See [Installing a Custom Plug and Play Printer Driver](installing-a-custom-plug-and-play-printer-driver.md) for more information.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Printer%20Connected%20to%20an%20LPT%20Port%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


