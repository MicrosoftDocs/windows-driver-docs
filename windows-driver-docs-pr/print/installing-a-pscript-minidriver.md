---
title: Installing a Pscript Minidriver
author: windows-driver-content
description: Installing a Pscript Minidriver
ms.assetid: 9c48b2b0-c293-4606-bbaa-3fcaca01c300
keywords: ["minidrivers WDK Pscript , installing", "INF files WDK print , Pscript"]
---

# Installing a Pscript Minidriver


## <a href="" id="ddk-installing-a-pscript-minidriver-gg"></a>


Installation of a Pscript minidriver requires a [printer INF file](printer-inf-files.md) that identifies the minidriver's files. If a printer model is not supported by Microsoft's printer INF file, ntprint.inf, a vendor-supplied INF file is required. The INF file should reference [printer INF file data sections](printer-inf-file-data-sections.md) and [printer INF file install sections](printer-inf-file-install-sections.md), which are defined in ntprint.inf. For a minidriver named abc100, the following INF file entries are typically needed:

```
[Manufacturer]
"ABC Printers"
 
[ABC Printers]
"ABC Printer 100 PS" = ABC100.PPD, ABC_Printer_100_PS
 
[ABC100.PPD]
CopyFiles=@ABC100.ppd       ; PPD file.
DataSection=PSCRIPT_DATA    ; PSCRIPT Data Section
DataFile=ABC100.ppd
Include=NTPRINT.INF         ; Include NTPRINT.INF.
Needs=PSCRIPT.OEM           ; Install PSCRIPT.
```

If you are providing a [user interface plug-in](user-interface-plug-ins.md) or a [rendering plug-in](rendering-plug-ins.md), you need to include the names of these components within your INF file. For information about installing customized code, see [Installing Customized Driver Components](installing-customized-driver-components.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Installing%20a%20Pscript%20Minidriver%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


