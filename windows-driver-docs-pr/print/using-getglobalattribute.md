---
title: Using GetGlobalAttribute
description: Using GetGlobalAttribute
keywords:
- GetGlobalAttribute
ms.date: 02/20/2024
---

# Using GetGlobalAttribute

[!include[Print Support Apps](../includes/print-support-apps.md)]

All of the global attribute names are the same as the keyword names defined in *PostScript Printer Description File Format Specification, v4.3*. Refer to this specification for their semantics. (This resource may not be available in some languages and countries.)

In the following table, the *pdwDataType* parameter takes values of the [**EATTRIBUTE_DATATYPE**](/windows-hardware/drivers/ddi/printoem/ne-printoem-_eattribute_datatype) enumerated type.

| Global attribute | Output parameters |
|--|--|
| **CenterRegistered** | *pdwDataType*: kADT_BOOL<br><br>*pbData*: **TRUE** or **FALSE**<br><br>*pcbNeeded*: sizeof(BOOL) |
| **ColorDevice** | *pdwDataType*: kADT_BOOL<br><br>*pbData*: **TRUE** or **FALSE**<br><br>*pcbNeeded*: sizeof(BOOL) |
| **Extensions** | *pdwDataType*: kADT_ASCII<br><br>*pbData*: ASCII string (in MULTI_SZ format) containing registered values of extensionOption the printer supports.<br><br>*pcbNeeded*: byte count of the ASCII string pointed to by pbData (including the last null character).<br><br>"FileSystem: True" is treated as if **Extensions** had the "FileSystem" option. "FileSystem: False" is treated as if Extensions didn't have the "FileSystem" option. |
| **FileVersion** | *pdwDataType*: kADT_DWORD<br><br>*pbData*: a DWORD whose high-order word contains the major version number, and whose low-order word contains the minor version number.<br><br>*pcbNeeded*: sizeof(DWORD) |
| **FreeVM** | *pdwDataType*: kADT_DWORD<br><br>*pbData*: value of FreeVM<br><br>*pcbNeeded*: sizeof(DWORD) |
| **LandscapeOrientation** | *pdwDataType*: kADT_ASCII<br><br>*pbData*: NULL-terminated ASCII string of either "Plus90" or "Minus90".<br><br>*pcbNeeded*: byte count of the ASCII string pointed to by pbData (including the last null character).<br><br>"Minus90" is returned only when the PPD contains "LandscapeOrientation: Minus90". In all other cases, "Plus90" is returned. |
| **LanguageEncoding** | *pdwDataType*: kADT_ASCII<br><br>*pbData*: NULL-terminated ASCII string containing one of the following encodingOption values:<br><br>"ISOLatin1"<br><br>"Unicode"<br><br>"JIS83-RKSJ"<br><br>"None"<br><br>*pcbNeeded*: byte count of the ASCII string pointed to by pbData (including the last null character).<br><br>"WindowsANSI" is treated the same as "ISOLatin1". Other encodingOption values aren't supported.<br><br>If LanguageEncoding is absent, LanguageVersion is used to deduce the return value. |
| **LanguageLevel** | *pdwDataType*: kADT_DWORD<br><br>*pbData*: PostScript language level supported by the printer<br><br>*pcbNeeded*: sizeof(DWORD) |
| **NickName** | *pdwDataType*: kADT_UNICODE<br><br>*pbData*: NULL-terminated Unicode string of the PPD's ShortNickName value if ShortNickName is present, or NickName value if ShortNickName is absent.<br><br>*pcbNeeded*: byte count of the Unicode string pointed to by pbData (including the last null character) |
| **PPD-Adobe** | *pdwDataType*: kADT_DWORD<br><br>*pbData*: a DWORD whose high-order word contains the major version number, and whose low-order word contains the minor version number.<br><br>*pcbNeeded*: sizeof(DWORD) |
| **PrintPSErrors** | *pdwDataType*: kADT_BOOL<br><br>*pbData*: **TRUE** or **FALSE**<br><br>*pcbNeeded*: sizeof(BOOL)<br><br>If PrintPSErrors is absent, it's assumed to be **TRUE**. |
| **Product** | *pdwDataType*: kADT_BINARY<br><br>*pbData*: the Product value<br><br>*pcbNeeded*: byte count of output binary data<br><br>Only the first Product entry is returned. |
| **Protocols** | *pdwDataType*: kADT_ASCII<br><br>*pbData*: ASCII string (in MULTI_SZ format) containing registered values of protocolOption the printer supports.<br><br>*pcbNeeded*: byte count of the ASCII string pointed to by pbData (including the last null character) |
| **PSVersion** | *pdwDataType*: kADT_BINARY<br><br>*pbData*: the PSVersion value<br><br>*pcbNeeded*: byte count of output binary data<br><br>Only the first PSVersion entry is returned. |
| **SuggestedJobTimeout** | *pdwDataType*: kADT_DWORD<br><br>*pbData*: the SuggestedJobTimeout value. If it's absent from the PPD, returns 0 by default.<br><br>*pcbNeeded*: sizeof(DWORD) |
| **SuggestedWaitTimeout** | *pdwDataType*: kADT_DWORD<br><br>*pbData*: the SuggestedWaitTimeout value. If it isn't present in the PPD, returns 300 by default.<br><br>*pcbNeeded*: sizeof(DWORD) |
| **Throughput** | *pdwDataType*: kADT_DWORD<br><br>*pbData*: the Throughput value. If it isn't present in the PPD, returns 0 by default.<br><br>*pcbNeeded*: sizeof(DWORD) |
| **TTRasterizer** | *pdwDataType*: kADT_ASCII<br><br>*pbData*: a NULL-terminated ASCII string containing one of following rasterizerOption values:<br><br>"None"<br><br>"Accept68K"<br><br>"Type42"<br><br>"TrueImage"<br><br>*pcbNeeded*: byte count of the ASCII string pointed to by pbData (including the last null character).<br><br>If the*TTRasterizer entry is absent, "None" is returned. |
