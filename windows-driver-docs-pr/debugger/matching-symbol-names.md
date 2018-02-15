---
title: Matching Symbol Names
description: Matching Symbol Names
ms.assetid: 34e2401e-9074-4adc-9644-48ad768c7c2f
ms.author: domars
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Matching Symbol Names


In certain situations, the actual name of a symbol is replaced with an alternative form which can then result in symbol matching problems. This most commonly happens when changing between public and private symbols or when using MS-DOS compatibility 8.3 short names for files.

### <span id="public_vs__private_symbol_matching"></span><span id="PUBLIC_VS__PRIVATE_SYMBOL_MATCHING"></span>Public vs. Private Symbol Matching

Switching between public symbols and private symbols can sometimes cause symbol matching problems. Typically, a public symbol and the corresponding private symbol have the same name with different symbol decorations. But in some cases, they may have entirely different names. In such cases, you might have to explicitly reference both names. For example, you could set up two breakpoints: one on the public symbol, and a second one on the private symbol. For more details, see [Public and Private Symbols](public-and-private-symbols.md).

### <span id="ms_dos_compatability_8_3_short_name_symbol_matching"></span><span id="MS_DOS_COMPATABILITY_8_3_SHORT_NAME_SYMBOL_MATCHING"></span>MS-DOS Compatibility 8.3 Short Name Symbol Matching

Files that have very long names are sometimes given auto-generated MS-DOS compatibility 8.3 short names. Depending on the tools and options used for creating symbol files and for debugging, the file name stored in the image's debug record can be either the long name or one of these short names. If the short names is used, this can cause symbol matching problems because the short name assigned is system dependent.

For example, suppose there are two files, Longfilename1.pdb and Longfilename2.pdb. If they are put in the same directory one will have an MS-DOS compatibility 8.3 name of Longfi~1.pdb and the other will be Longfi~2.pdb. If they are not put in the same directory they will both be Longfi~1.pdb. Thus, if the associated .pdb files are copied carelessly, the short filenames can change, causing symbol matching problems. For more details, see [File System References and Symbol Files](file-system-references-and-symbol-files.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Matching%20Symbol%20Names%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




