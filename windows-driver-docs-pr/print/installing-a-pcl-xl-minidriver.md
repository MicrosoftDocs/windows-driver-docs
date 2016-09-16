---
title: Installing a PCL XL Minidriver
author: windows-driver-content
description: Installing a PCL XL Minidriver
MS-HAID:
- 'nt5gpd\_8da523d9-26e6-43a7-8f56-9dde03ab995d.xml'
- 'print.installing\_a\_pcl\_xl\_minidriver'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 88e4e1a0-8adb-4f40-abeb-a4da761ca4ee
keywords: ["PCL XL vector graphics WDK Unidrv , installing minidrivers", "minidrivers WDK PCL XL"]
---

# Installing a PCL XL Minidriver


## <a href="" id="ddk-installing-a-pcl-xl-minidriver-gg"></a>


In Windows XP and later, ntprint.inf has the following \[PCLXL.OEM\] section:

```
[PCLXL.OEM]
CopyFiles=PCLXL,@PCL5ERES.DLL
```

The [**INF CopyFiles directive**](https://msdn.microsoft.com/library/windows/hardware/ff546346) copies all of the files listed in the \[PCLXL\] section, as well as pcl5eres.dll, to the default destination directory. The \[PCLXL\] section also appears in ntprint.inf and lists the files to be copied.

```
[PCLXL]
PCLXL.DLL
PCLXL.GPD
P6FONT.GPD
PJL.GPD
P6DISP.GPD
```

Pclxl.dll contains the PCL XL [*UFMs*](https://msdn.microsoft.com/library/windows/hardware/ff556343#wdkgloss-unidrv-font-metrics--ufm-) and various resource strings. The other GPDs listed in this section are the PCL XL (PCL-6) support files.

To install a PCL XL printer minidriver, an OEM should add a section similar to the following in the printer-specific INF. This INF loads before ntprint.inf does.

```
[P6SAMPLE.GPD]
CopyFiles=@P6SAMPLE.GPD
DataSection=UNIDRV_DATA
DataFile=P6SAMPLE.GPD
Include=NTPRINT.INF
Needs=UNIDRV.OEM,TTFSUB.OEM,PCLXL.OEM
```

In the preceding section, the **CopyFiles** directive in the first line copies the OEM's GPD file (called p6sample.gpd in this example). The entry associated with the **DataSection** directive in the second line (see [Printer INF File Data Sections](printer-inf-file-data-sections.md) and [Printer INF File Install Sections](printer-inf-file-install-sections.md)) refers to the \[UNIDRV\_DATA\] section in ntprint.inf. The **DataFile** directive in the third line specifies that p6sample.gpd is the data file associated with this printer minidriver. The fourth line causes ntprint.inf to be included. The three entries in the **Needs** directive of the fifth line refer to the identically-named sections in ntprint.inf. This enables the INF file to gain access to the files that it loads in driver.cab.

For additional information about using the **CopyFiles** directive for printer installations, see [Printer INF File CopyFiles Sections](printer-inf-file-copyfiles-sections.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Installing%20a%20PCL%20XL%20Minidriver%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


