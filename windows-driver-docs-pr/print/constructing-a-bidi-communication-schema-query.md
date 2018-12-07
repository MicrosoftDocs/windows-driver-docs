---
title: Constructing a Bidi Communication Schema Query
description: Constructing a Bidi Communication Schema Query
ms.assetid: b18fc69a-652c-4e36-83b3-fc4715b03c0f
keywords:
- bidirectional communication schema WDK print
- bidi communication schema WDK print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Constructing a Bidi Communication Schema Query


There are three points to remember when you construct a bidi communications schema query:

1.  The query must start with the `Printer` property, which must be preceded by a backslash character (`\`).

2.  Any properties in the query must be separated by a period character (`.`).

3.  If the query includes a value, the value must be separated from its parent property by a colon (`:`).

### <a href="" id="example-request-and-response"></a> Example Request and Response

The following are examples of the XML query and response format that is required by the [bidi communication interfaces](https://msdn.microsoft.com/library/windows/hardware/ff545163), and specifically by the IBidiSpl2 COM interface. The first example is a request that contains two schemas. The first schema determines whether a duplex unit is installed. The second schema determines the values associated with the hard disk.

```cpp
<bidi:Get xmlns:bidi="http://schemas.microsoft.com/windows/2005/03/printing/bidi">
  <Query schema="\Printer.Configuration.DuplexUnit:Installed"/>
  <Query schema="\Printer.Configuration.HardDisk"/>
</bidi:Get>
```

The next example is a set of typical responses from the schemas in the first example. The first response indicates that the duplex unit is installed. The remaining responses indicate that a hard disk is installed and that its capacity is 20 MB, of which there is 10 MB unused.

```cpp
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
```cpp
\Printer.Configuration.DuplexUnit:Installed
```

<a href="" id="determine-which-input-bins-are-present-"></a>Determine which input bins are present.  
```cpp
\Printer.Layout.InputBins
```

<a href="" id="determine-all-information-about-the-tray1-input-bin-"></a>Determine all information about the Tray1 input bin.  
```cpp
\Printer.Layout.InputBins.Tray1
```

<a href="" id="determine-whether-the-tray1-input-bin-is-installed-"></a>Determine whether the Tray1 input bin is installed.  
```cpp
\Printer.Layout.InputBins.Tray1:Installed
```

<a href="" id="determine-the-level-of-black-toner-identified-by--name--blk3e-"></a>Determine the level of black toner identified by \[Name\] Blk3E.  
```cpp
\Printer.Consumables.Blk3E:Level
```

<a href="" id="determine-the-level-of-fuser-oil-"></a>Determine the level of fuser oil.  
```cpp
\Printer.Consumables.FuserOil:Level
```

 

 




