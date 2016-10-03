---
title: Printer INF File Data Sections
author: windows-driver-content
description: Printer INF File Data Sections
MS-HAID:
- 'prtinst\_5a6b18f4-dcee-4e41-9615-8b8ce69f5b4e.xml'
- 'print.printer\_inf\_file\_data\_sections'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: d060716c-7c26-41a8-afbc-6fe83829d46a
keywords: ["INF files WDK print , data sections", "data sections WDK printer", "Previous Names data section WDK printer", "sections WDK printer"]
---

# Printer INF File Data Sections


## <a href="" id="ddk-printer-inf-file-data-sections-gg"></a>


The default Windows 2000 and later printer class installer, Ntprint.dll, allows printer INF files to contain data sections. Data sections are specified using the following format:

**DataSection**= *SectionName*

where *SectionName* is an INF file section name.

Data sections are used for specifying sets of [printer INF file entries](printer-inf-file-entries.md) that are common to multiple printers. By grouping the common entries in a list under the named section, and then referencing that section with a **DataSection** statement for each printer that uses the entries, the entry list has to be included only once in the INF file.

Microsoft's printer INF file, Ntprint.inf, defines the following data sections:

-   \[PSCRIPT\_DATA\]

    Assigns values to the **DriverFile**, **ConfigFile**, and **HelpFile** entries for the Microsoft PostScript Printer Driver.

-   \[UNIDRV\_DATA\]

    Assigns values to the **DriverFile**, **ConfigFile**, and **HelpFile** entries for the Microsoft Universal Printer Driver.

-   \[UNIDRV\_BIDI\_DATA\]

    Assigns values to the **DriverFile**, **ConfigFile**, **HelpFile**, and **LanguageMonitor** entries for the Microsoft Universal Printer Driver, for bidirectional printers.

These data sections should be referenced from within vendor-supplied INF files. For examples, see [Installing a Unidrv Minidriver](installing-a-unidrv-minidriver.md) and [Installing a Pscript Minidriver](installing-a-pscript-minidriver.md).

**Note**   An IHV printer INF file that has either a **Needs** entry or an **Include** entry that refers to Ntprint.inf must not contain data section names that are the same as any INF section name present in Ntprint.inf. Before naming a data section in a vendor-supplied printer INF file, search %windir%/inf/Ntprint.inf to be sure that your section name does not already exist as a section name (of any type) within Ntprint.inf.

 

### <a href="" id="ddk--previous-names-section-gg"></a>"Previous Names" Section

The Windows 2000 and later printer class installer recognizes a special data section called "Previous Names". One of these sections is permitted in each INF file. Entries in the section identify drivers for which the printer name is different for Windows 2000 and later than it is for Windows 95/98/Me. Specifying such name differences allows Point and Print to be supported for Windows 95/98/Me clients connecting to Windows 2000 and later servers.

The format for each entry in this section is:

"*Windows 2000 or later Printer Name*" = "*Windows 95/98/Me Printer Name*"

The following are sample entries:

```
[Previous Names]
"HP Color LaserJet" = "HP Color LaserJet (MS)"
"HP DeskJet 1200C" = "HP DeskJet 1200C (MS)"
"HP DeskJet 310" = "HP DeskJet 310 Printer"
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Printer%20INF%20File%20Data%20Sections%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


