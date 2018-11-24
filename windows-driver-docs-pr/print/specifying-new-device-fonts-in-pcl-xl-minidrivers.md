---
title: Specifying New Device Fonts in PCL XL Minidrivers
description: Specifying New Device Fonts in PCL XL Minidrivers
ms.assetid: 395b9200-4514-4b05-b417-15d4896914f4
keywords:
- PCL XL vector graphics WDK Unidrv , device fonts
- device fonts WDK PCL XL
- fonts WDK PCL XL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Specifying New Device Fonts in PCL XL Minidrivers





If you want to support new device fonts in a PCL XL minidriver, you must create [*Unidrv font metrics (UFM)*](https://msdn.microsoft.com/library/windows/hardware/ff556343#wdkgloss-unidrv-font-metrics--ufm-) files for those device fonts.

A UFM file has the following format:

A [**UNIFM\_HDR**](https://msdn.microsoft.com/library/windows/hardware/ff563587) structure, which serves as a header for the UFM file

A [**UNIDRVINFO**](https://msdn.microsoft.com/library/windows/hardware/ff562872) structure

An [**IFIMETRICS**](https://msdn.microsoft.com/library/windows/hardware/ff567418) structure

An [**EXTTEXTMETRIC**](https://msdn.microsoft.com/library/windows/hardware/ff548801) structure

A character width table

A correctly formatted font selection command must be placed in the correct location in the UFM file. The font selection command consists of 16 bytes for the font selection, one byte for a space character, and as many bytes as are needed to hold the digits of the symbol set number.

Following is an example of how a font selection command would appear in a UFM file. (The numbers in the second line show the position of each character in the font selection command.)

```cpp
CG Omega    BdIt 629
12345678901234567890
```

The font name and style, CG Omega BdIt (bold/italic) take up the first 16 bytes. After that, there is a single space character, which separates the font name from the symbol set number. The symbol set number, 629, takes up the last three bytes. Unidrv parses the font selection command in the UFM file and sends the font selection command and symbol set number separately.

The font name and symbol set number discussed in the previous example are two of the three attributes required for the **SetFont** operator, which would appear in the output data from the driver. In the following example, the **FontName** and **SymbolSet** attributes of this operator are set to the same values as in the preceding example. The third attribute, **CharSize**, is set to the value 100.

```cpp
ubyte_array (CG Omega    BdIt) FontName
real32 100 CharSize
uint16 629 SymbolSet
SetFont
```

For more information about the **SetFont** font selection command, see the *PCL XL Feature Reference Protocol Class 2.0* documentation. (This resource may not be available in some languages and countries.)

 

 




