---
title: Installing a PCL XL Minidriver
description: Installing a PCL XL Minidriver
keywords:
- PCL XL vector graphics WDK Unidrv , installing minidrivers
- minidrivers WDK PCL XL
ms.date: 01/27/2023
---

# Installing a PCL XL Minidriver

[!include[Print Support Apps](../includes/print-support-apps.md)]

In Windows XP and later, ntprint.inf has the following \[PCLXL.OEM\] section:

```inf
[PCLXL.OEM]
CopyFiles=PCLXL,@PCL5ERES.DLL
```

The [**INF CopyFiles directive**](../install/inf-copyfiles-directive.md) copies all of the files listed in the \[PCLXL\] section, as well as pcl5eres.dll, to the default destination directory. The \[PCLXL\] section also appears in ntprint.inf and lists the files to be copied.

```inf
[PCLXL]
PCLXL.DLL
PCLXL.GPD
P6FONT.GPD
PJL.GPD
P6DISP.GPD
```

Pclxl.dll contains the PCL XL *UFMs* and various resource strings. The other GPDs listed in this section are the PCL XL (PCL-6) support files.

To install a PCL XL printer minidriver, an OEM should add a section similar to the following in the printer-specific INF. This INF loads before ntprint.inf does.

```cinf
[P6SAMPLE.GPD]
CopyFiles=@P6SAMPLE.GPD
DataSection=UNIDRV_DATA
DataFile=P6SAMPLE.GPD
Include=NTPRINT.INF
Needs=UNIDRV.OEM,TTFSUB.OEM,PCLXL.OEM
```

In the preceding section, the **CopyFiles** directive in the first line copies the OEM's GPD file (called p6sample.gpd in this example). The entry associated with the **DataSection** directive in the second line (see [Printer INF File Data Sections](printer-inf-file-data-sections.md) and [Printer INF File Install Sections](printer-inf-file-install-sections.md)) refers to the \[UNIDRV\_DATA\] section in ntprint.inf. The **DataFile** directive in the third line specifies that p6sample.gpd is the data file associated with this printer minidriver. The fourth line causes ntprint.inf to be included. The three entries in the **Needs** directive of the fifth line refer to the identically-named sections in ntprint.inf. This enables the INF file to gain access to the files that it loads in driver.cab.

For additional information about using the **CopyFiles** directive for printer installations, see [Printer INF File CopyFiles Sections](printer-inf-file-copyfiles-sections.md).
