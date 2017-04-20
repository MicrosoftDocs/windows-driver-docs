---
title: Bidi Extension Example for WSD Port Monitor
author: windows-driver-content
description: Bidi Extension Example for WSD Port Monitor
ms.assetid: a04f16d5-ae99-4df5-bb55-aef95bd03588
keywords:
- bidi extension files WDK printer autoconfig
- in-box autoconfiguration support WDK printer , bidi extension files
- WSD schema extensions WDK printer
- schema extensions WDK WSD
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Bidi Extension Example for WSD Port Monitor


The following code example is a sample XML file that extends the bidi communications schema for the Web Services for Devices (WSD) port monitor:

```
<?xml version=&#39;1.0&#39;?>
<bidi:Definition xmlns:bidi=&#39;http://schemas.microsoft.com/windows/2005/03/printing/bidi&#39;>

  <Schema xmlns:nprt=&#39;http://schemas.microsoft.com/windows/2006/08/wdp/print&#39;>
    <Property name=&#39;Printer&#39;>
      <Property name=&#39;DeviceInfo&#39;>
        <Value name=&#39;FriendlyName&#39; query=&#39;nprt:PrinterDescription&#39; filter=&#39;nprt:PrinterDescription/nprt:PrinterName&#39; type=&#39;BIDI_STRING&#39; xmllang=&#39;true&#39;/>
        <Value name=&#39;Location&#39; query=&#39;nprt:PrinterDescription&#39; filter=&#39;nprt:PrinterDescription/nprt:PrinterLocation&#39; type=&#39;BIDI_STRING&#39; xmllang=&#39;true&#39;/>
        <Value name=&#39;Comment&#39; query=&#39;nprt:PrinterDescription&#39; filter=&#39;nprt:PrinterDescription/nprt:PrinterInfo&#39; type=&#39;BIDI_STRING&#39; xmllang=&#39;true&#39;/>
        <Value name=&#39;IEEE1284DeviceId&#39; query=&#39;nprt:PrinterDescription&#39; filter=&#39;nprt:PrinterDescription/nprt:DeviceId&#39; type=&#39;BIDI_STRING&#39;/>
      </Property>
      <Property name=&#39;Configuration&#39;>
        <Property name=&#39;Memory&#39;>
          <Value name=&#39;Size&#39; query=&#39;nprt:PrinterConfiguration&#39; filter=&#39;nprt:PrinterConfiguration/nprt:Storage/nprt:StorageEntry[nprt:Type="RAM"]/nprt:Size&#39; type=&#39;BIDI_INT&#39; drvPrinterEvent=&#39;true&#39;/>
          <Value name=&#39;PS&#39; query=&#39;nprt:PrinterConfiguration&#39; filter=&#39;nprt:PrinterConfiguration/nprt:Storage/nprt:StorageEntry[nprt:Type="PSMemory"]/nprt:Size&#39; type=&#39;BIDI_INT&#39; drvPrinterEvent=&#39;true&#39;/>
        </Property>
        <Property name=&#39;HardDisk&#39;>
          <Installed name=&#39;Installed&#39; query=&#39;nprt:PrinterConfiguration&#39; filter=&#39;nprt:PrinterConfiguration/nprt:Storage/nprt:StorageEntry[nprt:Type="HardDisk"]&#39; drvPrinterEvent=&#39;true&#39;/>
          <Value name=&#39;Capacity&#39; query=&#39;nprt:PrinterConfiguration&#39; filter=&#39;nprt:PrinterConfiguration/nprt:Storage/nprt:StorageEntry[nprt:Type="HardDisk"]/nprt:Size&#39; type=&#39;BIDI_INT&#39; drvPrinterEvent=&#39;true&#39;/>
          <Value name=&#39;FreeSpace&#39; query=&#39;nprt:PrinterConfiguration&#39; filter=&#39;nprt:PrinterConfiguration/nprt:Storage/nprt:StorageEntry[nprt:Type="HardDisk"]/nprt:Free&#39; type=&#39;BIDI_INT&#39; drvPrinterEvent=&#39;true&#39;/>
        </Property>
        <Property name=&#39;DuplexUnit&#39;>
          <Value name=&#39;Installed&#39; query=&#39;nprt:PrinterConfiguration&#39; filter=&#39;nprt:PrinterConfiguration/nprt:Finishings/nprt:DuplexerInstalled&#39; type=&#39;BIDI_BOOL&#39; optional=&#39;true&#39; drvPrinterEvent=&#39;true&#39;>false</Value>
        </Property>
      </Property>
      <Property name=&#39;Consumables&#39;>
        <Parameter name=&#39;$Name$&#39; parameter=&#39;Name&#39; query=&#39;nprt:PrinterConfiguration&#39; filter=&#39;nprt:PrinterConfiguration/nprt:Consumables/nprt:ConsumableEntry/@nprt:Name&#39;>
          <Installed name=&#39;Installed&#39; query=&#39;nprt:PrinterConfiguration&#39; filter=&#39;nprt:PrinterConfiguration/nprt:Consumables/nprt:ConsumableEntry[@nprt:Name="$Name$"]&#39; drvPrinterEvent=&#39;true&#39;/>
          <Value name=&#39;Type&#39; query=&#39;nprt:PrinterConfiguration&#39; filter=&#39;nprt:PrinterConfiguration/nprt:Consumables/nprt:ConsumableEntry[@nprt:Name="$Name$"]/nprt:Type&#39; type=&#39;BIDI_STRING&#39; drvPrinterEvent=&#39;true&#39;/>
          <Value name=&#39;Color&#39; query=&#39;nprt:PrinterConfiguration&#39; filter=&#39;nprt:PrinterConfiguration/nprt:Consumables/nprt:ConsumableEntry[@nprt:Name="$Name$"]/nprt:Color&#39; type=&#39;BIDI_STRING&#39; drvPrinterEvent=&#39;true&#39;/>
          <Value name=&#39;Level&#39; query=&#39;nprt:PrinterConfiguration&#39; filter=&#39;nprt:PrinterConfiguration/nprt:Consumables/nprt:ConsumableEntry[@nprt:Name="$Name$"]/nprt:Level&#39; type=&#39;BIDI_INT&#39; drvPrinterEvent=&#39;true&#39;/>
          <Value name=&#39;Model&#39; query=&#39;nprt:PrinterConfiguration&#39; filter=&#39;nprt:PrinterConfiguration/nprt:Consumables/nprt:ConsumableEntry[@nprt:Name="$Name$"]/nprt:Model&#39; type=&#39;BIDI_STRING&#39; drvPrinterEvent=&#39;true&#39;/>
        </Parameter>
      </Property>
      <Property name=&#39;Layout&#39;>
        <Property name=&#39;NumberUp&#39;>
          <Property name=&#39;PagesPerSheet&#39;>
            <Value name=&#39;CurrentValue&#39; query=&#39;nprt:DefaultPrintTicket&#39; filter=&#39;nprt:DefaultPrintTicket/nprt:DocumentProcessing/nprt:NumberUp/nprt:PagesPerSheet&#39; type=&#39;BIDI_INT&#39; drvPrinterEvent=&#39;true&#39;/>
            <List name=&#39;Supported&#39; query=&#39;nprt:PrinterCapabilities&#39; filter=&#39;nprt:PrinterCapabilities/nprt:JobValues/nprt:DocumentProcessing/nprt:NumberUp/nprt:PagesPerSheet/nprt:AllowedValue&#39; drvPrinterEvent=&#39;true&#39;/>
          </Property>
          <Property name=&#39;Direction&#39;>
            <Value name=&#39;CurrentValue&#39; query=&#39;nprt:DefaultPrintTicket&#39; filter=&#39;nprt:DefaultPrintTicket/nprt:DocumentProcessing/nprt:NumberUp/nprt:Direction&#39; type=&#39;BIDI_STRING&#39; drvPrinterEvent=&#39;true&#39;/>
            <List name=&#39;Supported&#39; query=&#39;nprt:PrinterCapabilities&#39; filter=&#39;nprt:PrinterCapabilities/nprt:JobValues/nprt:DocumentProcessing/nprt:NumberUp/nprt:Direction/nprt:AllowedValue&#39; drvPrinterEvent=&#39;true&#39;/>
          </Property>
        </Property>
        <Property name=&#39;Orientation&#39;>
          <Value name=&#39;CurrentValue&#39; query=&#39;nprt:DefaultPrintTicket&#39; filter=&#39;nprt:DefaultPrintTicket/nprt:DocumentProcessing/nprt:Orientation&#39; type=&#39;BIDI_STRING&#39; drvPrinterEvent=&#39;true&#39;/>
          <List name=&#39;Supported&#39; query=&#39;nprt:PrinterCapabilities&#39; filter=&#39;nprt:PrinterCapabilities/nprt:JobValues/nprt:DocumentProcessing/nprt:Orientation/nprt:AllowedValue&#39; drvPrinterEvent=&#39;true&#39;/>
        </Property>
        <Property name=&#39;InputBins&#39;>
          <Parameter name=&#39;$TrayName$&#39; parameter=&#39;TrayName&#39; query=&#39;nprt:PrinterConfiguration&#39; filter=&#39;nprt:PrinterConfiguration/nprt:InputBins/nprt:InputBinEntry/@nprt:Name&#39;>
            <Installed name=&#39;Installed&#39; query=&#39;nprt:PrinterConfiguration&#39; filter=&#39;nprt:PrinterConfiguration/nprt:InputBins/nprt:InputBinEntry[@nprt:Name="$TrayName$"]&#39; drvPrinterEvent=&#39;true&#39;/>
            <Value name=&#39;MediaSize&#39; query=&#39;nprt:PrinterConfiguration&#39; filter=&#39;nprt:PrinterConfiguration/nprt:InputBins/nprt:InputBinEntry[@nprt:Name="$TrayName$"]/nprt:MediaSize&#39; type=&#39;BIDI_STRING&#39; drvPrinterEvent=&#39;true&#39;/>
            <Value name=&#39;MediaType&#39; query=&#39;nprt:PrinterConfiguration&#39; filter=&#39;nprt:PrinterConfiguration/nprt:InputBins/nprt:InputBinEntry[@nprt:Name="$TrayName$"]/nprt:MediaType&#39; type=&#39;BIDI_STRING&#39; drvPrinterEvent=&#39;true&#39;/>
            <Value name=&#39;MediaColor&#39; query=&#39;nprt:PrinterConfiguration&#39; filter=&#39;nprt:PrinterConfiguration/nprt:InputBins/nprt:InputBinEntry[@nprt:Name="$TrayName$"]/nprt:MediaColor&#39; type=&#39;BIDI_STRING&#39; drvPrinterEvent=&#39;true&#39;/>
            <Value name=&#39;FeedDirection&#39; query=&#39;nprt:PrinterConfiguration&#39; filter=&#39;nprt:PrinterConfiguration/nprt:InputBins/nprt:InputBinEntry[@nprt:Name="$TrayName$"]/nprt:FeedDirection&#39; type=&#39;BIDI_STRING&#39; drvPrinterEvent=&#39;true&#39;/>
            <Value name=&#39;Capacity&#39; query=&#39;nprt:PrinterConfiguration&#39; filter=&#39;nprt:PrinterConfiguration/nprt:InputBins/nprt:InputBinEntry[@nprt:Name="$TrayName$"]/nprt:Capacity&#39; type=&#39;BIDI_INT&#39; drvPrinterEvent=&#39;true&#39;/>
            <Value name=&#39;Level&#39; query=&#39;nprt:PrinterConfiguration&#39; filter=&#39;nprt:PrinterConfiguration/nprt:InputBins/nprt:InputBinEntry[@nprt:Name="$TrayName$"]/nprt:Level&#39; type=&#39;BIDI_INT&#39; drvPrinterEvent=&#39;true&#39;/>
          </Parameter>
        </Property>
      </Property>
      <Property name=&#39;Finishing&#39;>
        <Value name=&#39;CollationSupported&#39; query=&#39;nprt:PrinterConfiguration&#39; filter=&#39;nprt:PrinterConfiguration/nprt:Finishings/nprt:CollationSupported&#39; type=&#39;BIDI_BOOL&#39; optional=&#39;true&#39; drvPrinterEvent=&#39;true&#39;>false</Value>
        <Value name=&#39;JogOffsetSupported&#39; query=&#39;nprt:PrinterConfiguration&#39; filter=&#39;nprt:PrinterConfiguration/nprt:Finishings/nprt:JogOffsetSupported&#39; type=&#39;BIDI_BOOL&#39; optional=&#39;true&#39; drvPrinterEvent=&#39;true&#39;>false</Value>
        <Property name=&#39;Staple&#39;>
          <Value name=&#39;Installed&#39; query=&#39;nprt:PrinterConfiguration&#39; filter=&#39;nprt:PrinterConfiguration/nprt:Finishings/nprt:StaplerInstalled&#39; type=&#39;BIDI_BOOL&#39; optional=&#39;true&#39; drvPrinterEvent=&#39;true&#39;>false</Value>
          <Property name=&#39;Location&#39;>
            <Value name=&#39;CurrentValue&#39; query=&#39;nprt:DefaultPrintTicket&#39; filter=&#39;nprt:DefaultPrintTicket/nprt:JobProcessing/nprt:JobFinishings/nprt:Staple/nprt:Location&#39; type=&#39;BIDI_STRING&#39; drvPrinterEvent=&#39;true&#39;/>
            <List name=&#39;Supported&#39; query=&#39;nprt:PrinterCapabilities&#39; filter=&#39;nprt:PrinterCapabilities/nprt:JobValues/nprt:JobProcessing/nprt:JobFinishings/nprt:Staple/nprt:Location/nprt:AllowedValue&#39; drvPrinterEvent=&#39;true&#39;/>
          </Property>
          <Property name=&#39;Angle&#39;>
            <Value name=&#39;CurrentValue&#39; query=&#39;nprt:DefaultPrintTicket&#39; filter=&#39;nprt:DefaultPrintTicket/nprt:JobProcessing/nprt:JobFinishings/nprt:Staple/nprt:Angle&#39; type=&#39;BIDI_STRING&#39; drvPrinterEvent=&#39;true&#39;/>
            <List name=&#39;Supported&#39; query=&#39;nprt:PrinterCapabilities&#39; filter=&#39;nprt:PrinterCapabilities/nprt:JobValues/nprt:JobProcessing/nprt:JobFinishings/nprt:Staple/nprt:Angle/nprt:AllowedValue&#39; drvPrinterEvent=&#39;true&#39;/>
          </Property>
        </Property>
        <Property name=&#39;HolePunch&#39;>
          <Value name=&#39;Installed&#39; query=&#39;nprt:PrinterConfiguration&#39; filter=&#39;nprt:PrinterConfiguration/nprt:Finishings/nprt:HolePunch/nprt:HolePunchInstalled&#39; type=&#39;BIDI_BOOL&#39; optional=&#39;true&#39; drvPrinterEvent=&#39;true&#39;>false</Value>
          <Property name=&#39;Pattern&#39;>
            <Value name=&#39;CurrentValue&#39; query=&#39;nprt:DefaultPrintTicket&#39; filter=&#39;nprt:DefaultPrintTicket/nprt:JobProcessing/nprt:JobFinishings/nprt:HolePunch/nprt:Pattern&#39; type=&#39;BIDI_STRING&#39; drvPrinterEvent=&#39;true&#39;/>
            <List name=&#39;Supported&#39; query=&#39;nprt:PrinterCapabilities&#39; filter=&#39;nprt:PrinterCapabilities/nprt:JobValues/nprt:JobProcessing/nprt:JobFinishings/nprt:HolePunch/nprt:Pattern/nprt:AllowedValue&#39; drvPrinterEvent=&#39;true&#39;/>
          </Property>
          <Property name=&#39;Location&#39;>
            <Value name=&#39;CurrentValue&#39; query=&#39;nprt:DefaultPrintTicket&#39; filter=&#39;nprt:DefaultPrintTicket/nprt:JobProcessing/nprt:JobFinishings/nprt:HolePunch/nprt:Edge&#39; type=&#39;BIDI_STRING&#39; drvPrinterEvent=&#39;true&#39;/>
            <List name=&#39;Supported&#39; query=&#39;nprt:PrinterCapabilities&#39; filter=&#39;nprt:PrinterCapabilities/nprt:JobValues/nprt:JobProcessing/nprt:JobFinishings/nprt:HolePunch/nprt:Edge/nprt:AllowedValue&#39; drvPrinterEvent=&#39;true&#39;/>
          </Property>
        </Property>
        <Property name=&#39;OutputBins&#39;>
          <Parameter name=&#39;$TrayName$&#39; parameter=&#39;TrayName&#39; query=&#39;nprt:PrinterConfiguration&#39; filter=&#39;nprt:PrinterConfiguration/nprt:OutputBins/nprt:OutputBinEntry/@nprt:Name&#39;>
            <Installed name=&#39;Installed&#39; query=&#39;nprt:PrinterConfiguration&#39; filter=&#39;nprt:PrinterConfiguration/nprt:OutputBins/nprt:OutputBinEntry[@nprt:Name="$TrayName$"]&#39; drvPrinterEvent=&#39;true&#39;/>
            <Value name=&#39;Capacity&#39; query=&#39;nprt:PrinterConfiguration&#39; filter=&#39;nprt:PrinterConfiguration/nprt:OutputBins/nprt:OutputBinEntry[@nprt:Name="$TrayName$"]/nprt:Capacity&#39; type=&#39;BIDI_INT&#39; drvPrinterEvent=&#39;true&#39;/>
            <Value name=&#39;Level&#39; query=&#39;nprt:PrinterConfiguration&#39; filter=&#39;nprt:PrinterConfiguration/nprt:OutputBins/nprt:OutputBinEntry[@nprt:Name="$TrayName$"]/nprt:Level&#39; type=&#39;BIDI_INT&#39; drvPrinterEvent=&#39;true&#39;/>
          </Parameter>
        </Property>
      </Property>
      <Property name=&#39;Status&#39;>
        <Property name=&#39;Summary&#39;>
          <Value name=&#39;State&#39; query=&#39;nprt:PrinterStatus&#39; filter=&#39;nprt:PrinterStatus/nprt:PrinterState&#39; type=&#39;BIDI_STRING&#39;/>
          <Value name=&#39;StateReason&#39; query=&#39;nprt:PrinterStatus&#39; filter=&#39;nprt:PrinterStatus/nprt:PrinterPrimaryStateReason&#39; type=&#39;BIDI_STRING&#39;/>
        </Property>
        <Property name=&#39;Detailed&#39;>
          <Parameter name=&#39;Event$EventIndex$&#39; parameter=&#39;EventIndex&#39; query=&#39;nprt:PrinterStatus&#39; filter=&#39;nprt:PrinterStatus/nprt:ActiveCondition/nprt:DeviceCondition/@nprt:Id&#39;>
            <Value name=&#39;Name&#39; query=&#39;nprt:PrinterStatus&#39; filter=&#39;nprt:PrinterStatus/nprt:ActiveCondition/nprt:DeviceCondition[@nprt:Id="$EventIndex$"]/nprt:Name&#39; type=&#39;BIDI_STRING&#39;/>
            <Value name=&#39;Severity&#39; query=&#39;nprt:PrinterStatus&#39; filter=&#39;nprt:PrinterStatus/nprt:ActiveCondition/nprt:DeviceCondition[@nprt:Id="$EventIndex$"]/nprt:Severity&#39; type=&#39;BIDI_STRING&#39;/>
            <Property name=&#39;Component&#39;>
              <Value name=&#39;Group&#39; query=&#39;nprt:PrinterStatus&#39; filter=&#39;nprt:PrinterStatus/nprt:ActiveCondition/nprt:DeviceCondition[@nprt:Id="$EventIndex$"]/nprt:Component/nprt:Group&#39; type=&#39;BIDI_STRING&#39;/>
              <Value name=&#39;Name&#39; query=&#39;nprt:PrinterStatus&#39; filter=&#39;nprt:PrinterStatus/nprt:ActiveCondition/nprt:DeviceCondition[@nprt:Id="$EventIndex$"]/nprt:Component/nprt:Name&#39; type=&#39;BIDI_STRING&#39;/>
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

```
<Definition>
  <Schema>...</Schema>
  <PortStatus>...</PortStatus>
</Definition>
```

Each bidi query from this extension file includes:

-   The algorithm that describes how to compose bidi data from the WSD data; algorithms can be defined with the four constructs [Const](const.md), [Installed](installed.md), [List](list.md), and [Value](value.md).

-   The WSD query parameter that describes how to get WSD data.

-   The XPath filter that filters the specific XML elements from the WSD schema that will be used to compose the bidi result.

### <a href="" id="parameter-construct"></a> Parameter Construct

The &lt;Parameter&gt; element used in the preceding example bidi extension file defines a variable property that can take different values (for example, TopBin or BottomBin), such that queries of the following form are possible:

-   <span codelanguage=""></span>
    <table>
    <colgroup>
    <col width="100%" />
    </colgroup>
    <tbody>
    <tr class="odd">
    <td><pre><code>\Printer.Layout.InputBins.TopBin:Installed</code></pre></td>
    </tr>
    </tbody>
    </table>

-   <span codelanguage=""></span>
    <table>
    <colgroup>
    <col width="100%" />
    </colgroup>
    <tbody>
    <tr class="odd">
    <td><pre><code>\Printer.Layout.InputBins.BottomBin:Installed</code></pre></td>
    </tr>
    </tbody>
    </table>

The following example query illustrates the use of custom attributes defined in the preceding bidi extension:

```
<Property name=&#39;Printer&#39;>
  <Property name=&#39;Layout&#39;>
    <Property name=&#39;InputBins&#39;>
      <Parameter name=&#39;$TrayName$&#39;
        parameter=&#39;TrayName&#39;
        query=&#39;wprt:PrinterConfiguration&#39;
        filter=&#39;wprt:PrinterConfiguration/wprt:InputBins/wprt:InputBinEntry/wprt:Name&#39;>
        <Installed
          name=&#39;Installed&#39;
          query=&#39;wprt:PrinterConfiguration&#39;
          filter=&#39;wprt:PrinterConfiguration/wprt:InputBins/wprt:InputBinEntry[wprt:Name="$TrayName$"]&#39;/>
      </Parameter>
    </Property>
  </Property>
</Property>
```

The preceding example results in the following query:

```
\Printer.Layout.InputBins.[TrayName]:Installed
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Bidi%20Extension%20Example%20for%20WSD%20Port%20Monitor%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


