---
title: Specifying New Device Fonts in PCL XL Minidrivers
author: windows-driver-content
description: Specifying New Device Fonts in PCL XL Minidrivers
ms.assetid: 395b9200-4514-4b05-b417-15d4896914f4
keywords:
- PCL XL vector graphics WDK Unidrv , device fonts
- device fonts WDK PCL XL
- fonts WDK PCL XL
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Specifying New Device Fonts in PCL XL Minidrivers


## <a href="" id="ddk-specifying-new-device-fonts-in-pcl-xl-minidrivers-gg"></a>


If you want to support new device fonts in a PCL XL minidriver, you must create [*Unidrv font metrics (UFM)*](https://msdn.microsoft.com/library/windows/hardware/ff556343#wdkgloss-unidrv-font-metrics--ufm-) files for those device fonts.

A UFM file has the following format:

A [**UNIFM\_HDR**](https://msdn.microsoft.com/library/windows/hardware/ff563587) structure, which serves as a header for the UFM file

A [**UNIDRVINFO**](https://msdn.microsoft.com/library/windows/hardware/ff562872) structure

An [**IFIMETRICS**](https://msdn.microsoft.com/library/windows/hardware/ff567418) structure

An [**EXTTEXTMETRIC**](https://msdn.microsoft.com/library/windows/hardware/ff548801) structure

A character width table

A correctly formatted font selection command must be placed in the correct location in the UFM file. The font selection command consists of 16 bytes for the font selection, one byte for a space character, and as many bytes as are needed to hold the digits of the symbol set number.

Following is an example of how a font selection command would appear in a UFM file. (The numbers in the second line show the position of each character in the font selection command.)

```
CG Omega    BdIt 629
12345678901234567890
```

The font name and style, CG Omega BdIt (bold/italic) take up the first 16 bytes. After that, there is a single space character, which separates the font name from the symbol set number. The symbol set number, 629, takes up the last three bytes. Unidrv parses the font selection command in the UFM file and sends the font selection command and symbol set number separately.

The font name and symbol set number discussed in the previous example are two of the three attributes required for the **SetFont** operator, which would appear in the output data from the driver. In the following example, the **FontName** and **SymbolSet** attributes of this operator are set to the same values as in the preceding example. The third attribute, **CharSize**, is set to the value 100.

```
ubyte_array (CG Omega    BdIt) FontName
real32 100 CharSize
uint16 629 SymbolSet
SetFont
```

For more information about the **SetFont** font selection command, see the *PCL XL Feature Reference Protocol Class 2.0* documentation. (This resource may not be available in some languages and countries.)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Specifying%20New%20Device%20Fonts%20in%20PCL%20XL%20Minidrivers%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


