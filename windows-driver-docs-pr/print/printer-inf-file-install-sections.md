---
title: Printer INF File Install Sections
description: Printer INF File Install Sections
ms.assetid: fb544271-1f0f-4bbd-b0a7-88dc89cc8186
keywords:
- INF files WDK print , install sections
- install sections WDK printer
- sections WDK printer
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Printer INF File Install Sections





For Windows NT 4.0 and previous, vendors who supplied minidrivers to customers also supplied the customer with a copy of the appropriate Microsoft printer driver, obtained from Microsoft.

Typically, for Windows 2000 and later, vendors do not distribute Microsoft's printer drivers along with their minidrivers. Instead, each vendor supplies an INF file that installs the vendor's files and then invokes Microsoft's printer INF file, Ntprint.inf, which in turn installs the appropriate printer driver components.

**Note**   Microsoft periodically releases updated versions of its printer drivers.Minidrivers that require features available only in the updated versions might require additional steps. For more information, see [Using Updated Core Print Drivers](using-updated-core-print-drivers.md).

 

Microsoft's printer INF file, Ntprint.inf, contains the following [**INF DDInstall sections**](https://msdn.microsoft.com/library/windows/hardware/ff547344) that can be referenced by vendor INF files:

-   \[PSCRIPT.OEM\]

    Installs the Microsoft Postscript Printer Driver (Pscript).

-   \[UNIDRV.OEM\]

    Installs the Microsoft Universal Printer Driver (Unidrv).

-   \[UNIDRV\_BIDI.OEM\]

    Installs the Microsoft Universal Printer Driver and Pjlmon.dll, the [*language monitor*](https://msdn.microsoft.com/library/windows/hardware/ff556305#wdkgloss-language-monitor) that supports Printer Job Language (PJL) and provides bidirectional communication for PJL printers.

-   \[TTFSUB.OEM\]

    Installs Ttfsub.gpd, which is included with the Windows Driver Kit (WDK) and contains a set of \*TTFS entries for common TrueType font substitutions that can be used with Unidrv-supported printers.

-   \[sRGBPROFILE.OEM\]

    Installs the system's sRGB color profile.

-   \[LOCALE.OEM\]

    Installs Locale.gpd, which contains locale identifiers. (See [Referencing Locales](referencing-locales.md).)

To reference these Install sections from your INF file, the file must use the Include and Needs directives, as illustrated in the following example:

```cpp
[Manufacturer]
"ABC Printers"
 
[ABC Printers]
"ABC Printer 100ex" = ABC100EX.GPD, ABC_Printer_100ex
 
[ABC100EX.GPD]
CopyFiles=@ABCres.dll,@ABC100EX.gpd
DataSection=UNIDRV_BIDI_DATA      ; Unidrv Bidirectional Data Section
DataFile=ABC100EX.gpd
Include=NTPRINT.INF               ; Include NTPRINT.INF.
Needs=TTFSUB.OEM,UNIDRV_BIDI.OEM  ; Install Unidrv, TrueType subs,
 ;    and PJL language monitor.
```

 

 




