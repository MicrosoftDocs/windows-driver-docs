---
title: Using Multiple GPD Files in a Minidriver
author: windows-driver-content
description: Using Multiple GPD Files in a Minidriver
MS-HAID:
- 'nt5gpd\_319226d9-78d3-4e72-8d69-5739692ebe9d.xml'
- 'print.using\_multiple\_gpd\_files\_in\_a\_minidriver'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 2ec08b46-a286-4af8-a5d4-e0306f731b3f
keywords: ["GPD files WDK Unidrv , multiple", "multiple GPD files WDK Unidrv"]
---

# Using Multiple GPD Files in a Minidriver


## <a href="" id="ddk-using-multiple-gpd-files-in-a-minidriver-gg"></a>


Unidrv minidrivers can consist of more than one GPD file. This allows you to place characteristics that are common to more than one printer in one or more GPD files, and then to include these common GPD files in a particular printer's individual GPD file.

To include additional GPD files, you use \*Include directives, which are described in [Preprocessor Directives](preprocessor-directives.md). You can use multiple \*Include directives, as shown in the following example:

```
*Include: "common1.gpd"
*Include: "common2.gpd"
*Include: "common3.gpd"
```

The \*Include directive's filename parameter cannot be a macro reference, and it cannot include a path specification.

Each included file must end with a complete GPD file entry, and the file must contain equal numbers of left and right braces. Included files can also contain \*Include directives.

The GPD parser treats the top-level GPD file and all included files as if they were one long file. Therefore, macros defined in one file can be referenced in subsequently included files. If a GPD file entry is duplicated, the most recently parsed entry replaces previous ones. Entries not duplicated are added to Unidrv's database.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Using%20Multiple%20GPD%20Files%20in%20a%20Minidriver%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


