---
title: Bidi Extension Example for WSD Port Monitor
description: Bidi Extension Example for WSD Port Monitor
ms.assetid: a04f16d5-ae99-4df5-bb55-aef95bd03588
keywords:
- bidi extension files WDK printer autoconfig
- in-box autoconfiguration support WDK printer , bidi extension files
- WSD schema extensions WDK printer
- schema extensions WDK WSD
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Bidi Extension Example for WSD Port Monitor

The following code example is a sample XML file that extends the bidi communications schema for the Web Services for Devices (WSD) port monitor:

```xml
<?xml version='1.0'?>
<bidi:Definition xmlns:bidi='http://schemas.microsoft.com/windows/2005/03/printing/bidi'>

  <Schema xmlns:nprt='http://schemas.microsoft.com/windows/2006/08/wdp/print'>
    <Property name='Printer'>
      <Property name='DeviceInfo'>
        <Value name='FriendlyName' query='nprt:PrinterDescription' filter='nprt:PrinterDescription/nprt:PrinterName' type='BIDI_STRING' xmllang='true'/>
        <Value name='Location' query='nprt:PrinterDescription' filter='nprt:PrinterDescription/nprt:PrinterLocation' type='BIDI_STRING' xmllang='true'/>
        <Value name='Comment' query='nprt:PrinterDescription' filter='nprt:PrinterDescription/nprt:PrinterInfo' type='BIDI_STRING' xmllang='true'/>
        <Value name='IEEE1284DeviceId' query='nprt:PrinterDescription' filter='nprt:PrinterDescription/nprt:DeviceId' type='BIDI_STRING'/>
      </Property>
      <Property name='Configuration'>
        <Property name='Memory'>
          <Value name='Size' query='nprt:PrinterConfiguration' filter='nprt:PrinterConfiguration/nprt:Storage/nprt:StorageEntry[nprt:Type="RAM"]/nprt:Size' type='BIDI_INT' drvPrinterEvent='true'/>
          <Value name='PS' query='nprt:PrinterConfiguration' filter='nprt:PrinterConfiguration/nprt:Storage/nprt:StorageEntry[nprt:Type="PSMemory"]/nprt:Size' type='BIDI_INT' drvPrinterEvent='true'/>
        </Property>
        <Property name='HardDisk'>
          <Installed name='Installed' query='nprt:PrinterConfiguration' filter='nprt:PrinterConfiguration/nprt:Storage/nprt:StorageEntry[nprt:Type="HardDisk"]' drvPrinterEvent='true'/>
          <Value name='Capacity' query='nprt:PrinterConfiguration' filter='nprt:PrinterConfiguration/nprt:Storage/nprt:StorageEntry[nprt:Type="HardDisk"]/nprt:Size' type='BIDI_INT' drvPrinterEvent='true'/>
          <Value name='FreeSpace' query='nprt:PrinterConfiguration' filter='nprt:PrinterConfiguration/nprt:Storage/nprt:StorageEntry[nprt:Type="HardDisk"]/nprt:Free' type='BIDI_INT' drvPrinterEvent='true'/>
        </Property>
        <Property name='DuplexUnit'>
          <Value name='Installed' query='nprt:PrinterConfiguration' filter='nprt:PrinterConfiguration/nprt:Finishings/nprt:DuplexerInstalled' type='BIDI_BOOL' optional='true' drvPrinterEvent='true'>false</Value>
        </Property>
      </Property>
      <Property name='Consumables'>
        <Parameter name='$Name$' parameter='Name' query='nprt:PrinterConfiguration' filter='nprt:PrinterConfiguration/nprt:Consumables/nprt:ConsumableEntry/@nprt:Name'>
          <Installed name='Installed' query='nprt:PrinterConfiguration' filter='nprt:PrinterConfiguration/nprt:Consumables/nprt:ConsumableEntry[@nprt:Name="$Name$"]' drvPrinterEvent='true'/>
          <Value name='Type' query='nprt:PrinterConfiguration' filter='nprt:PrinterConfiguration/nprt:Consumables/nprt:ConsumableEntry[@nprt:Name="$Name$"]/nprt:Type' type='BIDI_STRING' drvPrinterEvent='true'/>
          <Value name='Color' query='nprt:PrinterConfiguration' filter='nprt:PrinterConfiguration/nprt:Consumables/nprt:ConsumableEntry[@nprt:Name="$Name$"]/nprt:Color' type='BIDI_STRING' drvPrinterEvent='true'/>
          <Value name='Level' query='nprt:PrinterConfiguration' filter='nprt:PrinterConfiguration/nprt:Consumables/nprt:ConsumableEntry[@nprt:Name="$Name$"]/nprt:Level' type='BIDI_INT' drvPrinterEvent='true'/>
          <Value name='Model' query='nprt:PrinterConfiguration' filter='nprt:PrinterConfiguration/nprt:Consumables/nprt:ConsumableEntry[@nprt:Name="$Name$"]/nprt:Model' type='BIDI_STRING' drvPrinterEvent='true'/>
        </Parameter>
      </Property>
      <Property name='Layout'>
        <Property name='NumberUp'>
          <Property name='PagesPerSheet'>
            <Value name='CurrentValue' query='nprt:DefaultPrintTicket' filter='nprt:DefaultPrintTicket/nprt:DocumentProcessing/nprt:NumberUp/nprt:PagesPerSheet' type='BIDI_INT' drvPrinterEvent='true'/>
            <List name='Supported' query='nprt:PrinterCapabilities' filter='nprt:PrinterCapabilities/nprt:JobValues/nprt:DocumentProcessing/nprt:NumberUp/nprt:PagesPerSheet/nprt:AllowedValue' drvPrinterEvent='true'/>
          </Property>
          <Property name='Direction'>
            <Value name='CurrentValue' query='nprt:DefaultPrintTicket' filter='nprt:DefaultPrintTicket/nprt:DocumentProcessing/nprt:NumberUp/nprt:Direction' type='BIDI_STRING' drvPrinterEvent='true'/>
            <List name='Supported' query='nprt:PrinterCapabilities' filter='nprt:PrinterCapabilities/nprt:JobValues/nprt:DocumentProcessing/nprt:NumberUp/nprt:Direction/nprt:AllowedValue' drvPrinterEvent='true'/>
          </Property>
        </Property>
        <Property name='Orientation'>
          <Value name='CurrentValue' query='nprt:DefaultPrintTicket' filter='nprt:DefaultPrintTicket/nprt:DocumentProcessing/nprt:Orientation' type='BIDI_STRING' drvPrinterEvent='true'/>
          <List name='Supported' query='nprt:PrinterCapabilities' filter='nprt:PrinterCapabilities/nprt:JobValues/nprt:DocumentProcessing/nprt:Orientation/nprt:AllowedValue' drvPrinterEvent='true'/>
        </Property>
        <Property name='InputBins'>
          <Parameter name='$TrayName$' parameter='TrayName' query='nprt:PrinterConfiguration' filter='nprt:PrinterConfiguration/nprt:InputBins/nprt:InputBinEntry/@nprt:Name'>
            <Installed name='Installed' query='nprt:PrinterConfiguration' filter='nprt:PrinterConfiguration/nprt:InputBins/nprt:InputBinEntry[@nprt:Name="$TrayName$"]' drvPrinterEvent='true'/>
            <Value name='MediaSize' query='nprt:PrinterConfiguration' filter='nprt:PrinterConfiguration/nprt:InputBins/nprt:InputBinEntry[@nprt:Name="$TrayName$"]/nprt:MediaSize' type='BIDI_STRING' drvPrinterEvent='true'/>
            <Value name='MediaType' query='nprt:PrinterConfiguration' filter='nprt:PrinterConfiguration/nprt:InputBins/nprt:InputBinEntry[@nprt:Name="$TrayName$"]/nprt:MediaType' type='BIDI_STRING' drvPrinterEvent='true'/>
            <Value name='MediaColor' query='nprt:PrinterConfiguration' filter='nprt:PrinterConfiguration/nprt:InputBins/nprt:InputBinEntry[@nprt:Name="$TrayName$"]/nprt:MediaColor' type='BIDI_STRING' drvPrinterEvent='true'/>
            <Value name='FeedDirection' query='nprt:PrinterConfiguration' filter='nprt:PrinterConfiguration/nprt:InputBins/nprt:InputBinEntry[@nprt:Name="$TrayName$"]/nprt:FeedDirection' type='BIDI_STRING' drvPrinterEvent='true'/>
            <Value name='Capacity' query='nprt:PrinterConfiguration' filter='nprt:PrinterConfiguration/nprt:InputBins/nprt:InputBinEntry[@nprt:Name="$TrayName$"]/nprt:Capacity' type='BIDI_INT' drvPrinterEvent='true'/>
            <Value name='Level' query='nprt:PrinterConfiguration' filter='nprt:PrinterConfiguration/nprt:InputBins/nprt:InputBinEntry[@nprt:Name="$TrayName$"]/nprt:Level' type='BIDI_INT' drvPrinterEvent='true'/>
          </Parameter>
        </Property>
      </Property>
      <Property name='Finishing'>
        <Value name='CollationSupported' query='nprt:PrinterConfiguration' filter='nprt:PrinterConfiguration/nprt:Finishings/nprt:CollationSupported' type='BIDI_BOOL' optional='true' drvPrinterEvent='true'>false</Value>
        <Value name='JogOffsetSupported' query='nprt:PrinterConfiguration' filter='nprt:PrinterConfiguration/nprt:Finishings/nprt:JogOffsetSupported' type='BIDI_BOOL' optional='true' drvPrinterEvent='true'>false</Value>
        <Property name='Staple'>
          <Value name='Installed' query='nprt:PrinterConfiguration' filter='nprt:PrinterConfiguration/nprt:Finishings/nprt:StaplerInstalled' type='BIDI_BOOL' optional='true' drvPrinterEvent='true'>false</Value>
          <Property name='Location'>
            <Value name='CurrentValue' query='nprt:DefaultPrintTicket' filter='nprt:DefaultPrintTicket/nprt:JobProcessing/nprt:JobFinishings/nprt:Staple/nprt:Location' type='BIDI_STRING' drvPrinterEvent='true'/>
            <List name='Supported' query='nprt:PrinterCapabilities' filter='nprt:PrinterCapabilities/nprt:JobValues/nprt:JobProcessing/nprt:JobFinishings/nprt:Staple/nprt:Location/nprt:AllowedValue' drvPrinterEvent='true'/>
          </Property>
          <Property name='Angle'>
            <Value name='CurrentValue' query='nprt:DefaultPrintTicket' filter='nprt:DefaultPrintTicket/nprt:JobProcessing/nprt:JobFinishings/nprt:Staple/nprt:Angle' type='BIDI_STRING' drvPrinterEvent='true'/>
            <List name='Supported' query='nprt:PrinterCapabilities' filter='nprt:PrinterCapabilities/nprt:JobValues/nprt:JobProcessing/nprt:JobFinishings/nprt:Staple/nprt:Angle/nprt:AllowedValue' drvPrinterEvent='true'/>
          </Property>
        </Property>
        <Property name='HolePunch'>
          <Value name='Installed' query='nprt:PrinterConfiguration' filter='nprt:PrinterConfiguration/nprt:Finishings/nprt:HolePunch/nprt:HolePunchInstalled' type='BIDI_BOOL' optional='true' drvPrinterEvent='true'>false</Value>
          <Property name='Pattern'>
            <Value name='CurrentValue' query='nprt:DefaultPrintTicket' filter='nprt:DefaultPrintTicket/nprt:JobProcessing/nprt:JobFinishings/nprt:HolePunch/nprt:Pattern' type='BIDI_STRING' drvPrinterEvent='true'/>
            <List name='Supported' query='nprt:PrinterCapabilities' filter='nprt:PrinterCapabilities/nprt:JobValues/nprt:JobProcessing/nprt:JobFinishings/nprt:HolePunch/nprt:Pattern/nprt:AllowedValue' drvPrinterEvent='true'/>
          </Property>
          <Property name='Location'>
            <Value name='CurrentValue' query='nprt:DefaultPrintTicket' filter='nprt:DefaultPrintTicket/nprt:JobProcessing/nprt:JobFinishings/nprt:HolePunch/nprt:Edge' type='BIDI_STRING' drvPrinterEvent='true'/>
            <List name='Supported' query='nprt:PrinterCapabilities' filter='nprt:PrinterCapabilities/nprt:JobValues/nprt:JobProcessing/nprt:JobFinishings/nprt:HolePunch/nprt:Edge/nprt:AllowedValue' drvPrinterEvent='true'/>
          </Property>
        </Property>
        <Property name='OutputBins'>
          <Parameter name='$TrayName$' parameter='TrayName' query='nprt:PrinterConfiguration' filter='nprt:PrinterConfiguration/nprt:OutputBins/nprt:OutputBinEntry/@nprt:Name'>
            <Installed name='Installed' query='nprt:PrinterConfiguration' filter='nprt:PrinterConfiguration/nprt:OutputBins/nprt:OutputBinEntry[@nprt:Name="$TrayName$"]' drvPrinterEvent='true'/>
            <Value name='Capacity' query='nprt:PrinterConfiguration' filter='nprt:PrinterConfiguration/nprt:OutputBins/nprt:OutputBinEntry[@nprt:Name="$TrayName$"]/nprt:Capacity' type='BIDI_INT' drvPrinterEvent='true'/>
            <Value name='Level' query='nprt:PrinterConfiguration' filter='nprt:PrinterConfiguration/nprt:OutputBins/nprt:OutputBinEntry[@nprt:Name="$TrayName$"]/nprt:Level' type='BIDI_INT' drvPrinterEvent='true'/>
          </Parameter>
        </Property>
      </Property>
      <Property name='Status'>
        <Property name='Summary'>
          <Value name='State' query='nprt:PrinterStatus' filter='nprt:PrinterStatus/nprt:PrinterState' type='BIDI_STRING'/>
          <Value name='StateReason' query='nprt:PrinterStatus' filter='nprt:PrinterStatus/nprt:PrinterPrimaryStateReason' type='BIDI_STRING'/>
        </Property>
        <Property name='Detailed'>
          <Parameter name='Event$EventIndex$' parameter='EventIndex' query='nprt:PrinterStatus' filter='nprt:PrinterStatus/nprt:ActiveCondition/nprt:DeviceCondition/@nprt:Id'>
            <Value name='Name' query='nprt:PrinterStatus' filter='nprt:PrinterStatus/nprt:ActiveCondition/nprt:DeviceCondition[@nprt:Id="$EventIndex$"]/nprt:Name' type='BIDI_STRING'/>
            <Value name='Severity' query='nprt:PrinterStatus' filter='nprt:PrinterStatus/nprt:ActiveCondition/nprt:DeviceCondition[@nprt:Id="$EventIndex$"]/nprt:Severity' type='BIDI_STRING'/>
            <Property name='Component'>
              <Value name='Group' query='nprt:PrinterStatus' filter='nprt:PrinterStatus/nprt:ActiveCondition/nprt:DeviceCondition[@nprt:Id="$EventIndex$"]/nprt:Component/nprt:Group' type='BIDI_STRING'/>
              <Value name='Name' query='nprt:PrinterStatus' filter='nprt:PrinterStatus/nprt:ActiveCondition/nprt:DeviceCondition[@nprt:Id="$EventIndex$"]/nprt:Component/nprt:Name' type='BIDI_STRING'/>
            </Property>
          </Parameter>
        </Property>
      </Property>
    </Property>
  </Schema>
  <PortStatus>
    <Status>
      <Keyword>None</Keyword>
      <Code>0</Code>
      <Severity>0</Severity>
    </Status>
    <Status>
      <Keyword>AttentionRequired</Keyword>
      <Code>8</Code>
      <Severity>1</Severity>
    </Status>
    <Status>
      <Keyword>DoorOpen</Keyword>
      <Code>7</Code>
      <Severity>1</Severity>
    </Status>
    <Status>
      <Keyword>MarkerFailure</Keyword>
      <ResourceIdOffset>0</ResourceIdOffset>
      <Severity>1</Severity>
    </Status>
    <Status>
      <Keyword>MarkerSupplyLow</Keyword>
      <Code>10</Code>
      <Severity>2</Severity>
    </Status>
    <Status>
      <Keyword>MarkerSupplyEmpty</Keyword>
      <Code>6</Code>
      <Severity>1</Severity>
    </Status>
    <Status>
      <Keyword>MediaEmpty</Keyword>
      <Code>3</Code>
      <Severity>1</Severity>
    </Status>
    <Status>
      <Keyword>MediaJam</Keyword>
      <Code>2</Code>
      <Severity>1</Severity>
    </Status>
    <Status>
      <Keyword>MediaLow</Keyword>
      <ResourceIdOffset>1</ResourceIdOffset>
      <Severity>2</Severity>
    </Status>
    <Status>
      <Keyword>MediaNeeded</Keyword>
      <Code>5</Code>
      <Severity>1</Severity>
    </Status>
    <Status>
      <Keyword>OutputAreaAlmostFull</Keyword>
      <ResourceIdOffset>2</ResourceIdOffset>
      <Severity>2</Severity>
    </Status>
    <Status>
      <Keyword>OutputAreaFull</Keyword>
      <Code>4</Code>
      <Severity>1</Severity>
    </Status>
    <Status>
      <Keyword>Paused</Keyword>
      <ResourceIdOffset>3</ResourceIdOffset>
      <Severity>3</Severity>
    </Status>
  </PortStatus>
</bidi:Definition>
```

### Description of Schema Extension

The preceding example bidi extension file contains the root element &lt;Definition&gt;, with two major sections: &lt;Schema&gt;, where the bidi schema extension is placed, and &lt;PortStatus&gt;, where the driver maps the WSD status into the PORT\_INFO\_3 port status structure (described in the Windows SDK documentation).

Any namespaces that are used in schema extensions must be defined in the Schema element. The extension processing will not recognize a namespace that is defined in a lower-level element. Defining a namespace in a lower-level element will cause the extension file to fail validation.

```xml
<Definition>
  <Schema>...</Schema>
  <PortStatus>...</PortStatus>
</Definition>
```

Each bidi query from this extension file includes:

-   The algorithm that describes how to compose bidi data from the WSD data; algorithms can be defined with the four constructs [Const](const.md), [Installed](installed.md), [List](list.md), and [Value](value.md).

-   The WSD query parameter that describes how to get WSD data.

-   The XPath filter that filters the specific XML elements from the WSD schema that will be used to compose the bidi result.

### Parameter Construct

The &lt;Parameter&gt; element used in the preceding example bidi extension file defines a variable property that can take different values (for example, TopBin or BottomBin), such that queries of the following form are possible:

-   `\Printer.Layout.InputBins.TopBin:Installed`

-   `\Printer.Layout.InputBins.BottomBin:Installed`

The following example query illustrates the use of custom attributes defined in the preceding bidi extension:

```xml
<Property name='Printer'>
  <Property name='Layout'>
    <Property name='InputBins'>
      <Parameter name='$TrayName$'
        parameter='TrayName'
        query='wprt:PrinterConfiguration'
        filter='wprt:PrinterConfiguration/wprt:InputBins/wprt:InputBinEntry/wprt:Name'>
        <Installed
          name='Installed'
          query='wprt:PrinterConfiguration'
          filter='wprt:PrinterConfiguration/wprt:InputBins/wprt:InputBinEntry[wprt:Name="$TrayName$"]'/>
      </Parameter>
    </Property>
  </Property>
</Property>
```

The preceding example results in the following query:

`\Printer.Layout.InputBins.[TrayName]:Installed`
