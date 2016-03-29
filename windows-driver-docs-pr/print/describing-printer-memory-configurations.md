---
title: Describing Printer Memory Configurations
description: Describing Printer Memory Configurations
ms.assetid: 4a85788a-9713-42fb-a788-4d45f9aaabac
keywords: ["Unidrv, printer memory configurations", "GPD files WDK Unidrv , printer memory configurations", "printer memory configurations WDK Unidrv", "memory configurations WDK Unidrv", "Unidrv WDK print"]
---

# Describing Printer Memory Configurations


## <a href="" id="ddk-describing-printer-memory-configurations-gg"></a>


A Unidrv minidriver can contain descriptions of a printer's possible and default memory configurations, so that Unidrv can attempt to keep track of printer memory usage. Each memory configuration description includes values for both the total memory and available memory. Available memory can be used for downloading fonts, protecting pages, and other operations controlled by Unidrv.

Within a GPD file, you can use two methods to describe a printer's possible memory configurations. Both methods involve specifying attributes within a \*Feature entry for the Memory feature, which is one of the [standard features](standard-features.md). The two methods are as follows:

1.  You can specify every possible configuration in a separate \*Option entry within the \*Feature entry. Each \*Option entry must contain a \*MemoryConfigKB attribute, which is described in [Option Attributes for the Memory Feature](option-attributes-for-the-memory-feature.md).

    For example, to specify that a printer can have two memory configurations, a 1-megabyte configuration with 450 kilobytes available and a 2-megabyte configuration with 1350 kilobytes available, you can use the following GPD entries:

    <span codelanguage=""></span>
    <table>
    <colgroup>
    <col width="100%" />
    </colgroup>
    <tbody>
    <tr class="odd">
    <td align="left"><pre><code>*Feature: Memory
    {
        *Name: &quot;Printer Memory&quot;
        *DefaultOption: 1MB
        *Option: 1MB
        {
            *Name: &quot;Standard 1MB&quot;
            *MemoryConfigKB: PAIR(1024, 450)
        }
        *Option: 2MB 
        {
            *Name: &quot;Add-On 2MB&quot;
            *MemoryConfigKB: PAIR(2048,1350)
        }
    }
     </code></pre></td>
    </tr>
    </tbody>
    </table>

2.  Alternatively, the \*Feature entry can contain one or more \*MemConfigKB or \*MemConfigMB attributes instead of \*Option entries. This is simply a way to specify memory options without including a set of \*Option entries. Each \*MemConfigKB or \*MemConfigMB attribute represents a memory option.

    For example, to specify the same two configurations, a 1-megabyte configuration with 450 kilobytes available and a 2-megabyte configuration with 1350 kilobytes available, you can use the following GPD entries:

    <span codelanguage=""></span>
    <table>
    <colgroup>
    <col width="100%" />
    </colgroup>
    <tbody>
    <tr class="odd">
    <td align="left"><pre><code>*Feature: Memory
    {
        *Name: &quot;Printer Memory&quot;
        *DefaultOption: 1024KB
        *MemConfigKB: PAIR(1024, 450)
        *MemConfigKB: PAIR(2048, 1350)
    }
     </code></pre></td>
    </tr>
    </tbody>
    </table>

    The GPD parser creates a displayable option name for each configuration, based on the first entry in the PAIR statement. In the example, option names would be "1024KB" and "2048KB". The argument to the \*DefaultOption attribute must match one of these names.

Both method 1 and method 2 can be used within a single \*Feature entry.

If parser-generated option names are incompatible with localization requirements, use method 1 instead of method 2.

Whichever method you use, the [Unidrv user interface](unidrv-user-interface.md) displays the memory feature options in the device's printer property sheet.

If your minidriver specifies memory configurations, it can also specify the types of data that can be stored in printer memory and use up its available space. The \*MemoryUsage attribute is one of the [printer capability attributes](printer-capability-attributes.md), and you can use it to indicate to Unidrv whether font, raster, or vector data, or a combination of the three, are stored within printer memory. For each type specified, Unidrv attempts to keep track of how much printer memory is in use.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Describing%20Printer%20Memory%20Configurations%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




