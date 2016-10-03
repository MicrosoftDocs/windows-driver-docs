---
title: Constraints between Selections and Installations
author: windows-driver-content
description: Constraints between Selections and Installations
MS-HAID:
- 'nt5gpd\_6e2ba20e-bc6b-4086-b415-b2739b75aed0.xml'
- 'print.constraints\_between\_selections\_and\_installations'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: abb6004f-daae-4f28-b36c-102d0b8c9f55
keywords: ["installation constraints WDK Unidrv", "selection constraints WDK Unidrv"]
---

# Constraints between Selections and Installations


## <a href="" id="ddk-constraints-between-selections-and-installations-gg"></a>


Sometimes it is necessary to specify that a certain option cannot be selected if some other option is installed, or that a certain option cannot be selected if some other option is not installed. For example, a user should not be able to select tabloid paper if a printer's large format paper tray is not installed.

To specify relationships between the selection of certain options with the installation state of other options, use \***InstalledConstraints** and \***NotInstalledConstraints** entries. Their format is:

<table>
<colgroup>
<col width="100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>*InstalledConstraints : <em>FeatureName</em> . <em>OptionName</em></p></td>
</tr>
<tr class="even">
<td><p>*NotInstalledConstraints : <em>FeatureName</em> . <em>OptionName</em></p></td>
</tr>
</tbody>
</table>

 

where *FeatureName* is the name of a feature and *OptionName* is the name of an option associated with the feature. If the argument is a feature, the period and *OptionName* are not included.

An \***InstalledConstraints** or \***NotInstalledConstraints** entry must be placed inside a \*Feature or \*Option entry. For example, to indicate that a user should not be able to select tabloid paper if a printer's large format paper tray is not installed, the following entries can be used:

```
*Feature: InputBin
{
    *Option: LARGEFMT
    {
        Installable?: TRUE
        NotInstalledConstraints: PaperSize.TABLOID
    }
}
```

If a feature or option includes an \***InstalledConstraints** or \***NotInstalledConstraints** entry, the feature or option's \*Installable? attribute must be set to **TRUE**.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Constraints%20between%20Selections%20and%20Installations%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


