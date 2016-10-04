---
title: Installing a Unidrv Minidriver
author: windows-driver-content
description: Installing a Unidrv Minidriver
MS-HAID:
- 'nt5gpd\_cb0ec936-be92-4345-8c02-19bb863206a6.xml'
- 'print.installing\_a\_unidrv\_minidriver'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 0efead8f-c413-4ec1-b940-89b57f95345e
keywords: ["Unidrv, minidrivers", "minidrivers WDK Unidrv", "INF files WDK print , Unidrv minidrivers", "Unidrv WDK print"]
---

# Installing a Unidrv Minidriver


## <a href="" id="ddk-installing-a-unidrv-minidriver-gg"></a>


Installation of a Unidrv minidriver requires a [printer INF file](printer-inf-files.md) that identifies the minidriver's files. If a printer model is not supported by Microsoft's printer INF file, ntprint.inf, a vendor-supplied INF file is required. The INF file should reference [printer INF file data sections](printer-inf-file-data-sections.md) and [printer INF file install sections](printer-inf-file-install-sections.md), which are defined in ntprint.inf. For a minidriver named abc100, the following INF file entries are typically needed, if the printer is bidirectional, supports TrueType font substitution, and uses a single resource DLL:

```
[Manufacturer]
"ABC Printers"
 
[ABC Printers]
"ABC Printer 100" = ABC100.GPD, ABC_Printer_100
 
[ABC100.GPD]
CopyFiles=@ABCres.dll,@ABC100.gpd  ;Resource DLL and GPD file
DataSection=UNIDRV_BIDI_DATA       ;Unidrv Data Section
DataFile=ABC100.gpd
Include=NTPRINT.INF                ;Include NTPRINT.INF.
Needs=TTFSUB.OEM,UNIDRV_BIDI.OEM   ;Install TrueType subs, Unidrv,
  ;    and PJL language monitor.
```

If you are providing a [user interface plug-in](user-interface-plug-ins.md) or a [rendering plug-in](rendering-plug-ins.md), you need to include the names of these components within your INF file. For information about installing customized code, see [Installing Customized Driver Components](installing-customized-driver-components.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Installing%20a%20Unidrv%20Minidriver%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


