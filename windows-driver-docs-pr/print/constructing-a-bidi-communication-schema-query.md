---
title: Constructing a Bidi Communication Schema Query
author: windows-driver-content
description: Constructing a Bidi Communication Schema Query
MS-HAID:
- 'autocfg\_91accda0-abad-498c-a9c5-33a400404ab7.xml'
- 'print.constructing\_a\_bidi\_communication\_schema\_query'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: b18fc69a-652c-4e36-83b3-fc4715b03c0f
keywords: ["bidirectional communication schema WDK print", "bidi communication schema WDK print"]
---

# Constructing a Bidi Communication Schema Query


There are three points to remember when you construct a bidi communications schema query:

1.  The query must start with the `Printer` property, which must be preceded by a backslash character (`\`).

2.  Any properties in the query must be separated by a period character (`.`).

3.  If the query includes a value, the value must be separated from its parent property by a colon (`:`).

### <a href="" id="example-request-and-response"></a> Example Request and Response

The following are examples of the XML query and response format that is required by the [bidi communication interfaces](https://msdn.microsoft.com/library/windows/hardware/ff545163), and specifically by the IBidiSpl2 COM interface. The first example is a request that contains two schemas. The first schema determines whether a duplex unit is installed. The second schema determines the values associated with the hard disk.

```
<bidi:Get xmlns:bidi="http://schemas.microsoft.com/windows/2005/03/printing/bidi">
  <Query schema="\Printer.Configuration.DuplexUnit:Installed"/>
  <Query schema="\Printer.Configuration.HardDisk"/>
</bidi:Get>
```

The next example is a set of typical responses from the schemas in the first example. The first response indicates that the duplex unit is installed. The remaining responses indicate that a hard disk is installed and that its capacity is 20 MB, of which there is 10 MB unused.

```
<bidi:Get xmlns:bidi="http://schemas.microsoft.com/windows/2005/03/printing/bidi">
  <Query schema="\Printer.Configuration.DuplexUnit:Installed">
    <Schema name="\Printer.Configuration.DuplexUnit:Installed">
      <BIDI_BOOL>true</BIDI_BOOL>
    </Schema>
  </Query>
  <Query schema="\Printer.Configuration.HardDisk">
    <Schema name="\Printer.Configuration.HardDisk:Installed">
      <BIDI_BOOL>true</BIDI_BOOL>
    </Schema>
    <Schema name="\Printer.Configuration.HardDisk:Capacity">
      <BIDI_INT>20</BIDI_INT>
    </Schema>
    <Schema name="\Printer.Configuration.HardDisk:FreeSpace">
      <BIDI_INT>10</BIDI_INT>
    </Schema>
  </Query>
</bidi:Get>
```

### <a href="" id="additional-query-examples"></a> Additional Query Examples

The following is a list of typical tasks and associated queries:

<a href="" id="determine-whether-a-duplex-unit-is-installed-"></a>Determine whether a duplex unit is installed.  
```
\Printer.Configuration.DuplexUnit:Installed
```

<a href="" id="determine-which-input-bins-are-present-"></a>Determine which input bins are present.  
```
\Printer.Layout.InputBins
```

<a href="" id="determine-all-information-about-the-tray1-input-bin-"></a>Determine all information about the Tray1 input bin.  
```
\Printer.Layout.InputBins.Tray1
```

<a href="" id="determine-whether-the-tray1-input-bin-is-installed-"></a>Determine whether the Tray1 input bin is installed.  
```
\Printer.Layout.InputBins.Tray1:Installed
```

<a href="" id="determine-the-level-of-black-toner-identified-by--name--blk3e-"></a>Determine the level of black toner identified by \[Name\] Blk3E.  
```
\Printer.Consumables.Blk3E:Level
```

<a href="" id="determine-the-level-of-fuser-oil-"></a>Determine the level of fuser oil.  
```
\Printer.Consumables.FuserOil:Level
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Constructing%20a%20Bidi%20Communication%20Schema%20Query%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


