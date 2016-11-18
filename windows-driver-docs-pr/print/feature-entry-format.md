---
title: Feature Entry Format
author: windows-driver-content
description: Feature Entry Format
MS-HAID:
- 'nt5gpd\_2d17dfc1-0692-4ce3-a193-dc758be2ad3c.xml'
- 'print.feature\_entry\_format'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: f4e91611-aa68-4426-82ef-9ad3f09d62f2
keywords: ["printer features WDK Unidrv , entry format", "formats WDK printer features"]
---

# Feature Entry Format


## <a href="" id="ddk-feature-entry-format-gg"></a>


To specify a printer feature entry in a GPD file, use the following format:

<table>
<colgroup>
<col width="100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>*Feature: <em>FeatureName</em> {<em>FeatureAttributes</em>}</p></td>
</tr>
</tbody>
</table>

 

where *FeatureName* is the name of either one of the predefined [standard features](standard-features.md) or a customized feature name, and *FeatureAttributes* is a set of [feature attributes](feature-attributes.md).

For example, a GPD file might contain the following specification of the standard InputBin feature.

```
*Feature: InputBin
{
    *Name: "Paper Bin"
    *DefaultOption: Upper
    *Option: Upper
    {
        *Name: "Upper Tray"
        *Command: CmdSelect
        {
            *Order: DOC_SETUP.10
            *Cmd: "<1B>&l1H"
        }
        *Constraints: PaperSize.Env10
    }
    *Option: Manual
    {
        *Name: "Manual Feed"
        *Command: CmdSelect
        {
            *Order: DOC_SETUP.10
            *Cmd: "<1B>&l2H"
        }
        *Installable?: TRUE
    }
}
```

If you repeat a feature specification by, for example, including two or more InputBin feature entries, then the following rules apply:

-   Attributes and options that are not duplicated are added to Unidrv's database.

-   Attributes and options that are duplicated are overwritten, and Unidrv retains only the last specification.

You can control the order in which features are displayed to the user. See [Specifying Feature and Option Display Order](specifying-feature-and-option-display-order.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Feature%20Entry%20Format%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


