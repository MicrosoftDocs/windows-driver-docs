---
title: Printer INF File Install Sections
author: windows-driver-content
description: Printer INF File Install Sections
ms.assetid: fb544271-1f0f-4bbd-b0a7-88dc89cc8186
keywords:
- INF files WDK print , install sections
- install sections WDK printer
- sections WDK printer
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Printer INF File Install Sections


## <a href="" id="ddk-printer-inf-file-install-sections-gg"></a>


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

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Printer%20INF%20File%20Install%20Sections%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


